# head_driver

install raspbian 

this package need : 

                    ROS Groovy 
                                       
Installation:

  ROS:
  
    install ROS Grovvy http://wiki.ros.org/groovy/Installation/Raspbian
 

  now use git clone to download the package:

      $ cd catkin_ws/src

      $ git clone https://github.com/mekhtiche/head_driver_pkg.git

      $ cd ..

      $ catkin_make
  
  source the work space
  
      $ sudo nano .bashrc
    
    in the end of the file add "source ~/catkin_ws/devel/setup.bash"
    
    
  To launch the head package:

      $ roslaunch head_driver_pkg face.launch
      
  Network configuration:
  
    First in raspberrypi configuration change the hostname of raspberrypi to "head" and password to "headdriver" and in interface panel enabel the SSH 
  
    Change the configuration in hosts file:
      
      $ sudo nano /etc/hosts
      
      comment the line of head ip address and add two new lines:
      
        #127.0.0.1  head
        10.42.0.1   odroid
        10.42.0.25  head
        
      save it.
      
      Make sure that the raspberrypi always conect to ROBOT Wi_Fi.
   
  To use remote launch with robot_body you should add source command of your work space in the end of file: /opt/ros/groovy/env.sh
  it should look like this:
  
      #!/usr/bin/env sh
      # generated from catkin/cmake/templates/env.sh.in

      if [ $# -eq 0 ] ; then
        /bin/echo "Usage: env.sh COMMANDS"
        /bin/echo "Calling env.sh without arguments is not supported anymore. Instead$
        exit 1
      else
        . "/opt/ros/groovy/setup.sh"
        . "/home/pi/catkin_ws/devel/setup.sh"
        exec "$@"
      fi

  If the package has grafic interface the remote launch will not work like this package, the solution is to use the autostart with option of waitiong for master to start:
  
  First in home folder create file launch.sh and type in it :
      
      #!/bin/sh
      export ROS_MASTER_URI=http://odroid:11311
      . "/opt/ros/groovy/setup.sh"
      . "/home/pi/catkin_ws/devel/setup.sh"
      roslaunch --wait head_driver_pkg face.launch
        
  save it.
    
  in /usr/shar/applications create file "autolaunch.desktop" and put on it: >>>>> use "sudo"
    
      [Desktop Entry]
      Name=autolanch
      Exec=/home/pi/launch.sh
      Type=Application
      Terminal=false
        
  save it. REF https://askubuntu.com/questions/166777/how-can-you-make-a-sh-file-come-on-at-startup-in-lubuntu-12-04

  now copy and paste the file "autolaunch.desktop" to /etc/xdg/autostart/

  reboot the system.
  
  In this method the system will start automaticly when the raspberrypi boot and still waiting for the master to start in the odroid bord.
  
  
To configure the VU5 HDMI screen commant all lines in /boot/config.txt and in the end of the file add:
      
      hdmi_cvt=800 480 54
      hdmi_group=0
      hdmi_mode=87
      hdmi_drive=1
      
      
