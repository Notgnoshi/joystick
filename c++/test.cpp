#include "joy.h"
#include "updates.h"

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s <device>\n", argv[0]);
        fprintf(stderr, "Example: %s /dev/input/js0\n", argv[0]);
        exit(0);
    }

    Joystick* joy = new Joystick(argv[1]);

    while (true)
    {
        usleep(1000);
        joy->Update();

        if (joy->hasButtonUpdate())
        {
            update_buttons(joy);
        }

        if (joy->hasAxisUpdate())
        {
            update_axes(joy);
        }
    }

    return 0;
}
