### Setting up a New Workspace

Once everything is set up. Create a workspace on the linux machine (change the path on the .bashrc file to the new workspace - `gedit ~/.bashrc`). 

`colcon build`

Create a src folder.

Go into the src folder and create a package.

`ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy`
`cd ..`
`colcon build`

Push the package to a git repo so that the mac can use the stuff too, and everything can be connected.

`git init`
`git add .`
`git commit -m "COMMIT NO"`
`git branch -M main`
`git remote add origin <URL>`
`git push -u origin main`

May have to use a password

Now the repo should be available for the mac to clone and use. Disconnect the keyboard from the desktop, and connect it to the mac.

Go to the memory stick

`cd ..`
`cd ../Volumes/'DRIVE NAME'`
`mkdir <worskspace>`
`cd <workspace>`
`mkdir src`
`git clone <URL>`

You may have to enter the password


### Updating Git Once the Environment is Ready

The code can be edited on either computer using VS code. Once the code is edited from the mac, it can be pushed to github. Once in the src folder:

`git push -u origin main`

The linux computer can then pull the files when going back to the src folder

`git pull`
