
##### Step 1: Transport the code on a memory stick
Copy the workspace you made from (Starting the simulator) to usb (NTFS format)

##### Step 2: Connect the battery and accessories to the car
First check the battery charge:
charge to 4.2V/Cell
storage to 3.8V/Cell
not lower than 3.5/Cell

**Using the checker**
- Orientate the checker so the display is facing you
- Orientate the black and red wires from the 4-wire JST cable, so that the black wires are on the left and the red are on the right
- Plug the wires into the battery with these orientation, with the JST connected to the far left 4 pins on the checker
- The checker should beep and display the voltage of each cell and the total voltage

Plug the following accessories to communicate with the car:
- Monitor (HDMI)
- Keyboard (USB)
- Mouse (USB)
- Memory stick with workspace (USB)

Connect the battery, 
- JST: (Orientate the wired, Red to brown)
- Yellow connector (One orientation)

##### Step 3: Starting the system
Flip the on switch, so the 2 toggle switches are in the on position

Once the computer is at the home screem:
- Create a folder in the Home directory with the same name as your ros project (e.g. user_test, but it can be a different name)
- Copy the workspace you made (e.g. ros2_ws) and paste it in the folder you made

Open a terminal and add the source line to the .bashrc
```bash
gedit ~/.bashrc
```
Add the following line:
`source ~/user_test/ros2_ws/install/setup.bash`

- Change 'user_test' to your own folder name

Now in the terminal, build your ROS workspace
```bash
cd user_test/ros2_ws
colcon build --symnlink-install
```
Now close all terminals and start affresh

##### Step 4: Put the code onto the car
Open 5 terminals (4 on the left, 1 big on the right)

Ctrl + Shift + E
Click the first window
Ctrl + Shift + O
Click the first window
Ctrl + Shift + O
Click the bottom window
Ctrl + Shift + O

While the terminals are loading you can connect the PS4 controller
- Turn on the PS4 controller by pressing the PS button, and see connected bluetooth devices.

(Labeled Up to Down, Left to Right)
###### Terminal 1:
```bash
urg
```

###### Terminal 2:

```bash
bringup
```
- You'll notice a line that says 'Connected to Bluetooth Controller' if it is successful
###### Terminal 3:
```bash
pf
```
###### Terminal 4:
```bash
ros2 run rviz2 rviz2
```
###### Terminal 5:

```bash
cd user_test/ros2_ws
ros2 run user_test Opt_Moving_Forward
```

- Press and hold L2 to run the code

##### Step 5: Turn the car off

- Power off the computer
	- Wait for it to finish
- Turn the toggle to 'OFF' (Left) with ports facing you
- Unplug the yellow battery connector
- Unplug the JST battery connector
