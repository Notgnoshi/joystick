#include "joy.h"

Joystick::Joystick(std::string filename)
{
    int fd = open(filename.c_str(), O_RDONLY);

    if (fd < 0)
    {
        std::cout << "Failed to open '" << filename << "'." << std::endl;
        exit(1);
    }

    this->file_descriptor = fd;
}

Joystick::~Joystick()
{
    close(this->file_descriptor);
}

void Joystick::Update()
{
    // zero out the previous event
    memset(&event, 0, JS_EVENT_SIZE);
    size_t bytes_read = 0;
    ssize_t tmp = 0;

    // perform a blocking read.
    while (bytes_read < JS_EVENT_SIZE)
    {
        tmp = read(file_descriptor, &event + bytes_read, JS_EVENT_SIZE - bytes_read);

        if (tmp > 0)
        {
            bytes_read += tmp;
        }
    }

    // ignore non-input events
    event.type &= ~EVENT_INIT;

    // update the corresponding axis/button with its new value
    if (event.type == EVENT_AXIS)
    {
        updated_axis = static_cast<AxisId>(event.id);
        is_axis_update = true;
        is_button_update = false;
        axis_values[event.id] = event.value;
    }

    if (event.type == EVENT_BUTTON)
    {
        updated_button = static_cast<ButtonId>(event.id);
        is_axis_update = false;
        is_button_update = true;
        button_values[event.id] = event.value;
    }
}

bool Joystick::hasButtonUpdate()
{
    return is_button_update;
}

bool Joystick::hasAxisUpdate()
{
    return is_axis_update;
}

uint8_t Joystick::getButtonState(ButtonId button_id)
{
    return button_values[(int) button_id];
}

int16_t Joystick::getAxisState(AxisId axis_id)
{
    return axis_values[(int) axis_id];
}

ButtonId Joystick::getUpdatedButton()
{
    return updated_button;
}

AxisId Joystick::getUpdatedAxis()
{
    return updated_axis;
}
