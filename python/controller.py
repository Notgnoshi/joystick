from joystick import Joystick, JSEvent
from math import sqrt, atan2, degrees


class JoystickController(Joystick):
    """An implementation specific controller that inherits a basic Joystick. Adds the capability to
    check for specific updates that you care about and then do something based on that.
    """
    def __init__(self, js_file='/dev/input/js0'):
        Joystick.__init__(self, js_file)
        # direction gives the direction of travel. Defined in terms of r and theta
        self.direction_vector = (0, 0)
        # rotation tells the robot to rotate x degrees
        self.rotation_vector = (0, 0)
        # rotation as direction - rotation
        # self.difference_vector = (0, 0)

    def hasUpdate(self):
        return self.ButtonUpdate or self.AxisUpdate

    def performUpdates(self):
        care_about_buttons = [
            # JSEvent.BUTTON_SELECT,
            # JSEvent.BUTTON_LEFT_JOYSTICK,
            # JSEvent.BUTTON_RIGHT_JOYSTICK,
            # JSEvent.BUTTON_START,
            # JSEvent.BUTTON_DPAD_UP,
            # JSEvent.BUTTON_DPAD_RIGHT,
            # JSEvent.BUTTON_DPAD_DOWN,
            # JSEvent.BUTTON_DPAD_LEFT,
            # JSEvent.BUTTON_LEFT_TRIGGER,
            # JSEvent.BUTTON_RIGHT_TRIGGER,
            # JSEvent.BUTTON_LEFT_BUMPER,
            # JSEvent.BUTTON_RIGHT_BUMPER,
            # JSEvent.BUTTON_TRIANGLE,
            # JSEvent.BUTTON_CIRCLE,
            # JSEvent.BUTTON_X,
            # JSEvent.BUTTON_SQUARE,
            # JSEvent.BUTTON_PS3,
        ]
        care_about_axes = [
            JSEvent.AXIS_LEFT_STICK_HORIZONTAL,
            JSEvent.AXIS_LEFT_STICK_VERTICAL,
            JSEvent.AXIS_RIGHT_STICK_HORIZONTAL,
            JSEvent.AXIS_RIGHT_STICK_VERTICAL,
            # JSEvent.AXIS_DPAD_UP,
            # JSEvent.AXIS_DPAD_LEFT,
            # JSEvent.AXIS_DPAD_RIGHT,
            # JSEvent.AXIS_DPAD_DOWN,
            # JSEvent.AXIS_LEFT_TRIGGER,
            # JSEvent.AXIS_RIGHT_TRIGGER,
            # JSEvent.AXIS_LEFT_BUMPER,
            # JSEvent.AXIS_RIGHT_BUMPER,
            # JSEvent.AXIS_TRIANGLE,
            # JSEvent.AXIS_CIRCLE,
            # JSEvent.AXIS_X,
            # JSEvent.AXIS_SQUARE,
            # JSEvent.AXIS_ACCEL_X,
            # JSEvent.AXIS_ACCEL_Y,
            # JSEvent.AXIS_ACCEL_Z,
        ]

        if self.ButtonUpdate and self.update_id in care_about_buttons:
            self.__button_update

        if self.AxisUpdate and self.update_id in care_about_axes:
            self.__axis_update()

    def __button_update(self):
        print('button: {} \tvalue: {}'.format(self.update_id, self.getButtonState(self.update_id)))

    def __axis_update(self):
        """Uses the left and right joysticks to produce a direction vector and a rotation vector.
        On a traditional mecanum robot, it can locomote in all directions with no rotation. This is
        why they are separate. The vectors are in polar coordinates.
        """
        x = self.getAxisState(JSEvent.AXIS_LEFT_STICK_HORIZONTAL)
        # down and right is positive, so flip y axis
        y = -self.getAxisState(JSEvent.AXIS_LEFT_STICK_VERTICAL)

        # TODO: define SHRT_MAX (32767) as as large as the radius can get, so scale appropriately?
        # interestingly enough, we don't have a circular portion of the plane to work with, we can
        # get the largest vectors in the 45 degree direction. Think about how this will effect
        # scaling the vectors' magnitude

        # TODO: Think about headless - rotation being a difference from the current direction
        # or actually what it would take... This is actually a part of the *robots* locomotion
        # code, not the joystick. Do headless stuff there.
        # by headless I mean - there is no sense of front - the current direction of locomotion is
        # forwards.

        # TODO: Think about what kind of coordinate transformations would be useful...
        d = self.__to_polar(x, y)

        rotate_x = self.getAxisState(JSEvent.AXIS_RIGHT_STICK_HORIZONTAL)
        rotate_y = -self.getAxisState(JSEvent.AXIS_RIGHT_STICK_VERTICAL)
        r = self.__to_polar(rotate_x, rotate_y)

        self.direction_vector = d
        self.rotation_vector = r
        # self.difference_vector = (d[0] - r[0], d[1] - r[1])

        print('direction:  ({0[0]:.2f} {0[1]:.2f})'.format(self.direction_vector))
        print('rotation:   ({0[0]:.2f} {0[1]:.2f})'.format(self.rotation_vector))
        # print('difference: ({0[0]:.2f} {0[1]:.2f})\n'.format(self.difference_vector))

    def __to_polar(self, x, y):
        # since atan2 knows both y and x, it yields the angle in the proper quadrant
        return sqrt(x**2 + y**2), degrees(atan2(y, x))
