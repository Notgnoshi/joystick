from joystick import Joystick, JSEvent


class JoystickController(Joystick):
    """An implementation specific controller that inherits a basic Joystick. Adds the capability to
    check for specific updates that you care about and then do something based on that.
    """
    def __init__(self, js_file='/dev/input/js0'):
        Joystick.__init__(self, js_file)

    def hasUpdate(self):
        return self.ButtonUpdate or self.AxisUpdate

    def performUpdates(self):
        care_about_buttons = [
            JSEvent.BUTTON_SELECT,
            JSEvent.BUTTON_LEFT_JOYSTICK,
            JSEvent.BUTTON_RIGHT_JOYSTICK,
            JSEvent.BUTTON_START,
            JSEvent.BUTTON_DPAD_UP,
            JSEvent.BUTTON_DPAD_RIGHT,
            JSEvent.BUTTON_DPAD_DOWN,
            JSEvent.BUTTON_DPAD_LEFT,
            JSEvent.BUTTON_LEFT_TRIGGER,
            JSEvent.BUTTON_RIGHT_TRIGGER,
            JSEvent.BUTTON_LEFT_BUMPER,
            JSEvent.BUTTON_RIGHT_BUMPER,
            JSEvent.BUTTON_TRIANGLE,
            JSEvent.BUTTON_CIRCLE,
            JSEvent.BUTTON_X,
            JSEvent.BUTTON_SQUARE,
            JSEvent.BUTTON_PS3,
        ]
        care_about_axes = [
            JSEvent.AXIS_DPAD_LEFT,
            JSEvent.AXIS_LEFT_STICK_HORIZONTAL,
            JSEvent.AXIS_LEFT_STICK_VERTICAL,
            JSEvent.AXIS_RIGHT_STICK_HORIZONTAL,
            JSEvent.AXIS_RIGHT_STICK_VERTICAL,
            JSEvent.AXIS_DPAD_UP,
            JSEvent.AXIS_DPAD_LEFT,
            JSEvent.AXIS_DPAD_RIGHT,
            JSEvent.AXIS_DPAD_DOWN,
            JSEvent.AXIS_LEFT_TRIGGER,
            JSEvent.AXIS_RIGHT_TRIGGER,
            JSEvent.AXIS_LEFT_BUMPER,
            JSEvent.AXIS_RIGHT_BUMPER,
            JSEvent.AXIS_TRIANGLE,
            JSEvent.AXIS_CIRCLE,
            JSEvent.AXIS_X,
            JSEvent.AXIS_SQUARE,
            # JSEvent.AXIS_ACCEL_X,
            # JSEvent.AXIS_ACCEL_Y,
            # JSEvent.AXIS_ACCEL_Z,
        ]

        if self.ButtonUpdate and self.update_id in care_about_buttons:
            self.__button_update()

        if self.AxisUpdate and self.update_id in care_about_axes:
            self.__axis_update()

    def __button_update(self):
        print('button: {} \tvalue: {}'.format(self.update_id, self.getButtonState(self.update_id)))

    def __axis_update(self):
        # TODO: turn axis update information into a direction vector
        print('axis: {} \tvalue: {}'.format(self.update_id, self.getAxisState(self.update_id)))
