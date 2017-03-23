#pragma once

#define EVENT_BUTTON         0x01    // Button state update
#define EVENT_AXIS           0x02    // Axis state update
#define EVENT_INIT           0x80    // Non-input event, to be ignored

#define MAX_BUTTON_COUNT       18
#define MAX_AXIS_COUNT         27    // 8 for 360, 27 for PS3

#define BUTTON_DOWN 1
#define BUTTON_UP 0

// make the axes less sensitive...
#define DEADZONE 20

// "Axis" definitions. Down (trigger pulled in, stick down) and right are positive values

enum AxisId
{
    AXIS_LEFT_STICK_HORIZONTAL,  // 0
    AXIS_LEFT_STICK_VERTICAL,    // 1
    AXIS_RIGHT_STICK_HORIZONTAL, // 2
    AXIS_RIGHT_STICK_VERTICAL,   // 3
    NA4,
    NA5,
    NA6,
    NA7,
    AXIS_DPAD_UP,                // 8
    AXIS_DPAD_RIGHT,             // 9
    AXIS_DPAD_DOWN,              // 10
    // who knows what the left value should be...
    AXIS_DPAD_LEFT,              // 11
    AXIS_LEFT_TRIGGER,           // 12
    AXIS_RIGHT_TRIGGER,          // 13
    AXIS_LEFT_BUMPER,            // 14
    AXIS_RIGHT_BUMPER,           // 15
    AXIS_TRIANGLE,               // 16
    AXIS_CIRCLE,                 // 17
    AXIS_X,                      // 18
    AXIS_SQUARE,                 // 19
    NA20,
    NA21,
    NA22,
    // X is left/right
    AXIS_ACCEL_X,                // 23 note: left is positive, right is negative
    // Y is front/back
    AXIS_ACCEL_Y,                // 24 note: back is positive, forward is negative
    // Z is up/down
    AXIS_ACCEL_Z,                // 25 note: can't tell what sign is what
};

// if you add or remove items from the above enum, update this value
#define AXIS_COUNT 26

enum ButtonId
{
    BUTTON_SELECT,          //  0
    BUTTON_LEFT_JOYSTICK,   //  1
    BUTTON_RIGHT_JOYSTICK,  //  2
    BUTTON_START,           //  3
    BUTTON_DPAD_UP,         //  4
    BUTTON_DPAD_RIGHT,      //  5
    BUTTON_DPAD_DOWN,       //  6
    BUTTON_DPAD_LEFT,       //  7
    BUTTON_LEFT_TRIGGER,    //  8
    BUTTON_RIGHT_TRIGGER,   //  9
    BUTTON_LEFT_BUMPER,     // 10
    BUTTON_RIGHT_BUMPER,    // 11
    BUTTON_TRIANGLE,        // 12
    BUTTON_CIRCLE,          // 13
    BUTTON_X,               // 14
    BUTTON_SQUARE,          // 15
    BUTTON_PS3,             // 16
};

// if you add or remove items from the above enum, update this value
#define BUTTON_COUNT 17
