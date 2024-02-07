### Create a Ros2 Workspace

- Create and go into a workspace folder
- Create an src folder in it
`colcon build`

(go to bashrc to change automatic setup if you want a new workspace)
`gedit ~/.bashrc` (change the directory).

### Setup

The three lines (`gedit ~/.bashrc`) creates an organized workspace

You create nodes that talk to one another.

The nodes are stored in a package in the src folder. The package helps organise everything and organise dependencies.

For example
- `ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy`

The package can have many nodes. The "my_robot" can be changed to whatever else is being used, such as f1_tenth

rclpy is for doing ros with python

if the my_robot__controller pkg requires another package add this dependency line:

`<depend>"PACKAGE"</depend>`
The sub folder of the same name is where the ros2 nodes go

Next steps in terminal:
- build:
	- `colcon build`
	- Fix the `SetuptoolsDeprecationWarning` warning
		- `pip3 list | grep setuptools`, downgrade the version
		- `pip3 install setuptools==58.2.0`
		- Check using the list that it downgraded

... At this point:
- workspace configured
- package configured
- Now the nodes can be written

### Writing a node (example)

- Go to the sub package of the same name (where the `__init__.py` lives)
`cd ros2_ws/src/my_robot_controller/my_robot_controller`
- Create the node
`touch my_first_node.py`
- Make it executable
`chmod +x my_first_node.py`
- Open VS Code
`code .`

#### VS Code

- Tell the environment that we're using python
`#!/usr/bin/env python3`
- Import rclpy
`import rclpy`
`from rclpy.node import Node`
	- Enable autocomplete
	- Extensions > search ROS - Microsoft verified > install

`class MyNode(node):`
	`def __init__(self):`
		`super().__init__("first_node")`
		`self.get_logger().info("Hello from ROS2")`

`def main(args=None:`
	`rclpy.init(args=args)`
	`node = MyNode()`
	
	#

	rclpy.shutdown()
- Run the python script from the terminal
`if __name__ == '__main__:`
	`main()`