Designed to run on a rasberry PI 5. The code purpose is run a underwater ROV including all of its subsystems (motors, claw, sensors).
Instead of doing all of the processing, it talks with a laptop above water via a ethernet cable which handels most processing.

In order to auto install required python Libraries run command below in the directory
pip install -r requirements.txt

Required Libraries installs comands
    pip install gpiozero
    pip install adafruit-circuitpython-bno055
    pip install pynput

