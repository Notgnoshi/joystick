# joystick
C++ code to handle PS3 joystick events on Linux with the intent of passing them off to a robot eventually.

## TODO:
* figure out what the left dpad axis ID is.
* on initialization, the joystick updates every button and every axis. Handle.
* Provide a copy constructor?
* actually do something with all this

## Usage:
The `Joystick` class exposes the following interface

```c++
class Joystick
{
public:
    Joystick(string filename="/dev/input/js0");
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
};
```

Note that `ButtonId` and `AxisId` are enums defined in `ps3_mappings.h` as follows

```c++
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
```
Axes 4-7 and 20-22 are unimplemented on the PS3 controller as near as I can tell. Further, I am unsure what the value of `AXIS_DPAD_LEFT` should be. Both of the controllers I have tested do not send an Axis update when the left `DPAD` button is pressed - but it does for the other three. Logically, it should be `11` as the numberings start at the top and go clockwise for the shape buttons, and the go clockwise for the DPAD as well.

```c++
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
```

An example of how to use `Joystick` is provided in `test.cpp` - compiled with the given makefile and ran with `./test /dev/input/js1`. Note that the files `updates.h` and `updates.cpp` are *not* a part of the interface, and should be project specific - they are included here only as a quick example of how to use `Joystick`.

Further note that you will run into issues if you pass a `Joystick` object around instead of passing a `Joystick*`.

Both `ps3_mappings.h` and `360_mappings.h` are included. Only the PS3 one has been tested. I've been told it works best for interfacing with a joystick on Linux.

---

There is now a Python version of of `Joystick` that works almost exactly the same. See `python/test.py` for the top level code and `python/controller.py` for project/implementation specific code.
