How to use these instructions:

#### Step 1:

Make sure the pre-requisites are installed onto your system. These instructions are for after your environment has been setup already so you can follow the instructions for repeated use. See Chris' and Yiming's notes on how to download the dependencies.

Pre-requisites:
- ROS2 Environment, Visual Studio
- Docker
- Docker Compose
- sim_ws from F1Tenth_gym_ros repo


Use obsidian (or whatever markdown reader you wish to view the  .md files).
##### Step 2:

Start with the 'Starting the simulator.md'
- This will get the python files and setup before interacting with the car ready.

For Step 2 in this file. Copy and paste the following files into the src>user_test folder;

- Opt_test_moving_forward.py
- test_moving_forward.py
Copy the array contents from console scripts in the setup.py. Do not copy the setup.py to your package.

This will provide a "barebones" template for implementing instructions to the F1Tenth car. It will simply drive the wheels at 2 m/s.

##### Step 3:

Next do the 'Driving the Car.md' after your simulation in Ros works as intended.

At the end of this, the car should start moving the wheels at 2 m/s.

By the end of this you should have a template for implementing your own software onto the F1Tenth car.