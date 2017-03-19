#pragma once

#include "joy.h"
#include <iostream>
#include <climits>

void update_buttons(Joystick* joy);
void update_axes(Joystick* joy);

short bound_short(int num);
short map(long x, long in_min, long in_max, long out_min, long out_max);
short short_map(long x);
