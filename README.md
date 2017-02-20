# head_driver

install raspbian 

this package need : 

                    ROS Groovy 
                                       
Installation:

  ROS:
  
    install ROS Grovvy http://wiki.ros.org/groovy/Installation/Raspbian
 

  now use git clone to download the package:

      $ cd catkin_ws/src

      $ git clone https://github.com/mekhtiche/head_driver.git

      $ cd ..

      $ catkin_make
  
  source the work space
  
      $ sudo nano .bashrc
    
    in the end of the file add "source ~/catkin_ws/devel/setup.bash"
    
    
  To launch the robot:

      $ roslaunch head_driver face.launch
   
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

