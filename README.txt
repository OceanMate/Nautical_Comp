Designed to run on a rasberry PI 5. The code purpose is run a underwater ROV including all of its subsystems (motors, claw, sensors).
Instead of doing all of the processing, it talks with a laptop above water via a ethernet cable which handels most processing.

In order to auto install required python Libraries run command below in the directory
pip install -r requirements.txt

To edit ethernet settings of pi use command below and select ethernet
nmtui
then type select wired connection, then ipv4, then change it from manual to automatic
Then add 192.168.1.2/24 to the address


