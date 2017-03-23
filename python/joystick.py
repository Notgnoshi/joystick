from struct import Struct


class JSEvent(object):
    """A joystick even class (struct)

        struct js_event_t
        {
            uint32_t time;
            int16_t value;
            uint8_t type;
            uint8_t id;
        };

    Takes in raw bytes from a file.read(JS_EVENT_SIZE) call.

    Also defines AXIS and BUTTON ids
    """
    JS_EVENT_SIZE = 8  # 64 bits is 8 bytes
    EVENT_BUTTON = 0x01
    EVENT_AXIS = 0x02
    EVENT_INIT = 0x80
    MAX_AXIS_COUNT = 27
    MAX_BUTTON_COUNT = 18
    AXIS_COUNT = 26
    BUTTON_COUNT = 17

    AXIS_LEFT_STICK_HORIZONTAL = 0
    AXIS_LEFT_STICK_VERTICAL = 1
    AXIS_RIGHT_STICK_HORIZONTAL = 2
    AXIS_RIGHT_STICK_VERTICAL = 3
    AXIS_DPAD_UP = 8
    AXIS_DPAD_RIGHT = 9
    AXIS_DPAD_DOWN = 10
    AXIS_DPAD_LEFT = 11  # who knows what the left value should actually be...
    AXIS_LEFT_TRIGGER = 12
    AXIS_RIGHT_TRIGGER = 13
    AXIS_LEFT_BUMPER = 14
    AXIS_RIGHT_BUMPER = 15
    AXIS_TRIANGLE = 16
    AXIS_CIRCLE = 17
    AXIS_X = 18
    AXIS_SQUARE = 19
    AXIS_ACCEL_X = 23  # note: left is positive, right is negative
    AXIS_ACCEL_Y = 24  # note: back is positive, forward is negative
    AXIS_ACCEL_Z = 25  # note: can't tell what sign is what

    BUTTON_SELECT = 0
    BUTTON_LEFT_JOYSTICK = 1
    BUTTON_RIGHT_JOYSTICK = 2
    BUTTON_START = 3
    BUTTON_DPAD_UP = 4
    BUTTON_DPAD_RIGHT = 5
    BUTTON_DPAD_DOWN = 6
    BUTTON_DPAD_LEFT = 7
    BUTTON_LEFT_TRIGGER = 8
    BUTTON_RIGHT_TRIGGER = 9
    BUTTON_LEFT_BUMPER = 10
    BUTTON_RIGHT_BUMPER = 11
    BUTTON_TRIANGLE = 12
    BUTTON_CIRCLE = 13
    BUTTON_X = 14
    BUTTON_SQUARE = 15
    BUTTON_PS3 = 16

    def __init__(self, event_struct):
        # c.f. https://docs.python.org/3/library/struct.html#format-characters
        s = Struct('< I h B B')
        self.time, self.value, self.type, self.id = s.unpack(event_struct)
        # also c.f. Struct.pack()

        # ignore non-input events
        self.type = self.type & ~self.EVENT_INIT

    def __repr__(self):
        struct = 'struct js_event_t\n{'
        # struct += '\n\tuint32_t time : {}'.format(self.time)
        struct += '\n\tint16_t value : {}'.format(self.value)
        struct += '\n\tuint8_t type  : {}'.format(hex(self.type))
        struct += '\n\tuint8_t id    : {}'.format(self.id)
        struct += '\n};\n'
        return struct


class Joystick(object):
    def __init__(self, js_file='/dev/input/js1'):
        # note names beginning with `__` are enforced as private
        self.file = open(js_file, 'rb')
        # since we're using ID's as indices, account for 0 based indices
        self.__axis_values = [0] * (JSEvent.MAX_AXIS_COUNT + 1)
        # since we're using ID's as indices, account for 0 based indices
        self.__button_values = [0] * (JSEvent.MAX_BUTTON_COUNT + 1)

        # TODO: think about adding in previous value lists
        self.update_id = -1
        self.AxisUpdate = False
        self.ButtonUpdate = False
        self.event = None

    def __del__(self):
        self.file.close()

    def __enter__(self):
        return self

    # __enter__ and __exit__ allow the context manager syntax
    # with Joystick() as js:
    # ...
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def Update(self):
        self.event = JSEvent(self.file.read(JSEvent.JS_EVENT_SIZE))

        if self.event.type == JSEvent.EVENT_AXIS:
            self.update_id = self.event.id
            self.AxisUpdate = True
            self.ButtonUpdate = False
            self.__axis_values[self.event.id] = self.event.value

        if self.event.type == JSEvent.EVENT_BUTTON:
            self.update_id = self.event.id
            self.AxisUpdate = False
            self.ButtonUpdate = True
            self.__button_values[self.event.id] = self.event.value

    def getButtonState(self, button_id):
        return self.__button_values[button_id]

    def getAxisState(self, axis_id):
        return self.__axis_values[axis_id]
