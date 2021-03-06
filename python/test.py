#!/usr/bin/python3
from controller import JoystickController
from time import sleep


def main():

    # TODO: Think about some kind of async controller.Run() that performs this stuff in the background?
    with JoystickController('/dev/input/js1') as controller:
        while True:
            try:
                controller.Update()
                sleep(0.0001)

                if controller.hasUpdate():
                    controller.performUpdates()
            except KeyboardInterrupt:
                exit()


if __name__ == '__main__':
    main()
