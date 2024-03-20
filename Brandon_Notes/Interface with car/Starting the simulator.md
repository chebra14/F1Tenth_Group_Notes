
Pre-requisites:
- ROS2 Environment, Visual Studio
- Docker
- Docker Compose
- sim_ws from F1Tenth_gym_ros repo
##### Step 1: Create a ROS2 workspace:
```bash
mkdir ros2_ws
cd ros2_ws
mkdir src
cd src
ros2 pkg create user_test --build-type ament_python --dependencies rclpy
cd user_test/
code .
```

##### Step 2: Create the Python Files
Add python files (one for the simulator, and one for the actual car) depending on what you want to do. (Usual Ros setup).
- Python Files:
	- ros2_ws > src > user_test
	- 2 Python files for example
	- Add one .py for simulator and one .py for the car
- Console scripts array in setup.py 
	- e.g.
```
"Moving_forward = breandon.test_moving_forward:main",
"Opt_Moving_forward = breandon.Opt_test_moving_forward:main"
```

- For the example. Copy the 2 .py files, but only copy the Console Scripts array from the setup.py into your own package

(See moving Forward example)

##### Step 3: Build the workspace
Go to ros_ws/
(From currently open terminal)
```bash
cd ..
cd ..
colcon build --symlink-install
```

##### Now the software should be setup completely

##### Step 4: Run the ROS Simulator
Start the terminal environment (Ctrl + Alt + T)

Open 3 windows on the left, and one on the right:
Ctrl + Shift + E
Click the first window
Ctrl + Shift + O
Ctrl + Shift + O

Enter the following terminal code for each window:

(Labeled Up to Down, Left to Right)
###### Terminal 1:
```bash
cd sim_ws/src/f1tenth_gym_ros/
sudo docker-compose up
```
###### Terminal 2:
```bash
sudo docker exec -it f1tenth_gym_ros-sim-1 /bin/bash
#For some computers it will be f1tenth_gym_ros_sim_1, if error
#Then enter these into the new terminal line made: root@9fa42de446d2:/sim_ws#
source /opt/ros/foxy/setup.bash
source install/local_setup.bash
ros2 launch f1tenth_gym_ros gym_bridge_launch.py
```

If you get an error similar to 'Can't find map', follow these instructions:
Home -> sim_ws -> src -> f1then_gym_ros -> config -> sim.yaml
change the map path on line 45 to:
'/sim_ws/src/f1tenth_gym_ros/maps/levine'
The install instructions for the sim_ws asked to change this to your directory, but this will fix the problem
###### Terminal 3:
```bash
cd ros2_ws/src/user_test/user_test/
ros2 run rviz2 rviz2
```
Once Rviz is open:
File -> Open Config -> 
Home -> sim_ws -> src -> f1tenth_gym_ros -> launch 
Click on gym_bridge.rviz and open
(Close without saving)
###### Terminal 4:
```bash
cd ros2_ws/src/
ros2 run user_test Moving_forward
```

The car should then move (if Moving_forward), or execute whatever code you wrote.

To restart:
Ctrl+C in Terminal 4
Ctrl+C Terminal2

Redo Term 2
Redo Term 4
