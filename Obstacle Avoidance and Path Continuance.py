#Define initial variables
from picarx import Picarx
import time
from robot_hat import Pin
pin = Pin('LED')
pin.value(0)
theta = 30


def main():
    try:
	  #Define initial variables
        right = False
        counter = 0
        px = Picarx()
        px.set_dir_servo_angle(0)
	
#Get distance with ultrasonic sensors, distance will be tested for first turn around object 
        while(True):      
            distance = (px.ultrasonic.read())
            print(distance)
            print(counter)
            time.sleep(0.1)
        
            counter += 1
            
            px.forward(0.1)
#Logic for first turn around object
            if(distance < 30 and right == False):
                px.set_dir_servo_angle(theta)
                px.forward(1)
                pin.value(1)
                time.sleep(0.5)
                right = True
                
#Logic using a counter to turn the robot to the left and head towards the initial path
            elif(counter > 15 and counter < 25 and right == True):
                px.set_dir_servo_angle(-theta)
                px.forward(1)
                pin.value(0)
                
#Logic using a counter to turn the robot to the right to continue on initial path
            elif(counter > 28 and counter < 34 and right == True):
                px.set_dir_servo_angle(theta)
                px.forward(1)
                pin.value(0)
            
                
            else:
                px.set_dir_servo_angle(0)
                
    finally:
        px.stop()


if __name__ == "__main__":
    main()

