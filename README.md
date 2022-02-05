# Installation

## Install UROS package to `src/uros`

* [Documention](https://micro.ros.org/docs/tutorials/core/teensy_with_arduino/)
* builds `src/uros`

```bash
source /opt/ros/galactic/setup.bash
colcon build
ros2 run micro_ros_setup create_agent_ws.sh
ros2 run micro_ros_setup build_agent.sh
source install/local_setup.bash
```

## Install Udev Rules

Add follwoing rules to `/etc/udev/rules.d/92-scratch.rules`:
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="0483", SYMLINK+="ttyUROS"
# usb port 4 (via hub)
SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{devpath}=="4.*", SYMLINK+="ttyLOG"
# usb port 2 (direct port)
SUBSYSTEMS=="usb", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60" ATTRS{devpath}=="2" SYMLINK+="ttyLIDAR"
```
and run `sudo sh -c "udevadm control --reload-rules && udevadm trigger"`


# Source

```bash
source /opt/ros/galactic/setup.bash
source install/local_setup.bash
```


# Launch

```bash
ros2 launch scratch scratch_init_launch.py
```





