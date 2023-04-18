# robotics-program-files
A collection of python files used to program the SunFounder Raspberry Pi Robot Car. This kit was used in the Robotics &amp; Algorithms Control class, also known as ECE 452 at UIC.

Each project has three tasks, all listed briefly below:

Project 1 -

- Line Tracking.py: Utilizes the line-tracking module to read grayscale values to follow a line.
- Obstacle Avoidance.py: Utilizes the ultrasonic sensors to avoid oncoming obstacles.
- PiCar-X Move.py: Basic program to control movement of the robot.

Project 2 -

- Line Tracking Until 2m.py: Follows a line using the line tracking module to read grayscale values. Constantly outputs distance traveled until it reach 2 meters, where the robot stops.
- Obstacle Avoidance and Path Continuance.py: Placing the robot ~20cm away from the obstacle, this program allows the robot to manuever around the obstacle using the ultrasonic sensor and a counter.
- Velocity Change Based on Distance.py: The further the robot is from an obstacle, the faster it will move. The velocity is capped at a predetermined speed. Once it detects an object within range, the robot moves slower as it approaches the object. Comes to a stop once it is close enough and has a light indicator when the object is identified. 
