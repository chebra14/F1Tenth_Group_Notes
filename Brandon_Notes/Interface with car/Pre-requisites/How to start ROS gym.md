Read the following site to install the ROS2 gym
https://github.com/f1tenth/f1tenth_gym_ros

Quick start
---
install the following dependencies specifically for ROS2 foxy
```bash
git clone https://github.com/f1tenth/f1tenth_gym
cd f1tenth_gym && pip3 install -e .
```

Installing the simulation:
- Create a workspace: 
```bash
cd $HOME && mkdir -p sim_ws/src
```
- Clone the repo into the workspace:
```bash 
cd $HOME/sim_ws/src
git clone https://github.com/f1tenth/f1tenth_gym_ros
```
- Update correct parameter for path to map file: Go to `sim.yaml` [https://github.com/f1tenth/f1tenth_gym_ros/blob/main/config/sim.yaml](https://github.com/f1tenth/f1tenth_gym_ros/blob/main/config/sim.yaml) in your cloned repo, change the `map_path` parameter to point to the correct location. It should be ```
```
<your_home_dir>/sim_ws/src/f1tenth_gym_ros/maps/levine
```
- Install dependencies with rosdep:

```bash
source /opt/ros/foxy/setup.bash
cd ..
rosdep install -i --from-path src --rosdistro foxy -y
```
Build the workspace: 
```bash
colcon build
```

Run ROS2 gym
---
you need to first install docker and docker-compose 
https://docs.docker.com/compose/install/

In the terminal, type:
correct the path to your specific path to where the f1tenth_gym_ros is.
```bash
cd sim_ws/src/f1tenth_gym_ros 
sudo docker-compose up
```
then in separate Terminal type:
this will give you access to the docker container
```bash
sudo docker exec -it f1tenth_gym_ros_sim_1 /bin/bash
```
then type in browser of choice navigate to 
http://localhost:8080/vnc.html

Once you have entered the container. Source the following command
run the last command if the gym map is broken and open the config file manually path is not necessary if you don't have files that needs access in that folder.

```bash
cd Documents/Ros2PP/src/my_waypoint_follower/my_waypoint_follower
ros2 run rviz2 rviz2
```
Enter RVis environment with the following command 
```bash
source /opt/ros/foxy/setup.bash
source install/local_setup.bash
ros2 launch f1tenth_gym_ros gym_bridge_launch.py
```

Keyboard Teleop
---
The keyboard teleop node from `teleop_twist_keyboard` is also installed as part of the simulation's dependency. To enable keyboard teleop, set `kb_teleop` to `True` in `sim.yaml`. After launching the simulation, in another terminal, run:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Then, press `i` to move forward, `u` and `o` to move forward and turn, `,` to move backwards, `m` and `.` to move backwards and turn, and `k` to stop in the terminal window running the teleop node.


**more simulations specific stuff is to be continued**
---