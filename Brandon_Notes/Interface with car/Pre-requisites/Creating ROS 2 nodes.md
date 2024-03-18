**create python package**
-----------------------------------------------------------------------------------------------
```bash
cd ros2_ws/
cd src/
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
#open vs code 
code .   #visual studio code need to be installed for this to work
```
If any files are created make sure to perform `colcon build` one folder before the src file

If you get an error while building the package check the version 

```bash
#if you dont have pip3 installed type
#sudo apt install python3-pip
pip3 list    
pip33 list | grep setuptools
#setuptools                  45.2.0(this was my output and this version works)
pip3 install setuptools==58.2.0
#it should work after this 
```
Install vs code -  `code .` command
-----------------------------------------------------------------------------------------------
First install snap
```bash
sudo apt install snap
```
install code command from VS code
```bash
sudo snap install code --classic
```

Create a python file using terminal
----------------------------------------------------------------------------------------------
First go to the directory you want to create the file in typically for ros its in `<homeDir>/src/folderName/folderName`

Then to create the python file
```bash
touch my_first_node.py                       #creat the python file
chmod +x my_first_node.py                    #making the file as a executable
cd ../..
code .
```

Bare bone essential for a subscriber
-----------------------------------------------------------------------------------------------
```python
#! /usr/bin/env python3

#import necessary classes
import rclpy
from rclpy.node import Node
from topic_name.msg import type_of_message

class NodeName (Node):
	def __init__(self):
		super().__init__("pose_subscriber")
		self.pose_subscriber = self.create_subscription(msg_type, "topic_name", callback, qos_profile)
	
	def callback(self, msg: Pose):
		self.get_logger().info("message you want from the topic")

def main(args = None):

	rclpy.init(args = args)
	node = NodeName()
	rclpy.spin(node)                    #allows the node to always been running 
	rclpy.shutdown()                    #shut dowwn the node
	
```
**NB:** Once you have initialised the node and you want to it to appear in the comand line as a executable you have to add the Node name in the setup.py file under 'consol_script' 

in such format 
```
'console_script':[
	"Node_name = package.Node_name:main"
]

#e.g
"pose_subscriber = my_robot_controller.pose_subcriber:main"
```


To find the what Message type you want to subscribe to
```r
rqt_graph         
```
Find the node that you are interest in e.g Pose of a vehicle

```
ros2 topic echo /topicName/....
```
Check if the output is something you are looking for
```
ros2 topic info /topicName/....
```
In this you will find the type of the topic 
e.g turtlesim/msg/Pose

```r
ros2 interface show turtlesim/msg/Pose
```
This will show the what infomation the topic contains and the type of value and structure 
e.g float32 x 
     float32 linearr_velocity

The import line from earlier `from Node.msg import Something`
then becomes `from turtlesim.msg import Pose`

Once the import is done you need to go to package.xml and include the dependencies as 
`<depend>geometry_msgs</depend>`

Running the Node
-----------------------------------------------------------------------------------------------

Enter command
```r
colcon build --symlink-install            
source ~/.bashrc
```
`--simlink-install` allow you to change the file and save without having to redo `colcon build` in the workspace
`source ~/.bashrc` to "restart" the terminal and redo the .bash files for ROS  