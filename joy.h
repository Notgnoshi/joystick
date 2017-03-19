#pragma once
// #pragma pack (1)

#include <iostream>
#include <vector>
#include <unistd.h>
#include <fcntl.h>
#include <cstring>

#include "ps3_mappings.h"

struct js_event_t
{
    uint32_t time;     /* event timestamp in milliseconds */
    int16_t value;     /* value */
    uint8_t type;      /* event type */
    uint8_t id;        /* axis/button number */
};

const size_t JS_EVENT_SIZE = sizeof(js_event_t);

class Joystick
{
public:
    Joystick(std::string filename="/dev/input/js0");
    ~Joystick();

    // reads in the next available joystick update. Blocks until it receives an update.
    void Update();

    // Checks if the most recent call to this->Update() was a Button or an Axis
    bool hasButtonUpdate();
    bool hasAxisUpdate();

    // Get the ID of the updated button or axis
    ButtonId getUpdatedButton();
    AxisId getUpdatedAxis();

    // get the state of a particular button or axis
    uint8_t getButtonState(ButtonId button_id);
    int16_t getAxisState(AxisId axis_id);

private:
    int file_descriptor;
    js_event_t event;

    ButtonId updated_button;
    AxisId updated_axis;

    bool is_axis_update;
    bool is_button_update;

    uint8_t button_values[MAX_BUTTON_COUNT] = {0};
    int16_t axis_values[MAX_AXIS_COUNT] = {0};
};
