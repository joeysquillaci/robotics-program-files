#Define initial variables
from picarx import Picarx
maxVelocity = 100
velocity = 0
import time
from robot_hat import Pin
pin = Pin('LED')
pin.value(0)

def main():
    try:
        
        px = Picarx()
        
#Read distance and compute a velocity
        while(True):
            distance = (px.ultrasonic.read())
            velocity = (0.005*0.005*distance)
            
#Logic for deciding on speed depending on the distance (this one is if it’s too close then it will stop

            if(distance < 20):
                px.stop()
                if(distance > 0 and distance < 20):
                    pin.value(1)
                else:
                    pin.value(0)
                
#Velocity = maxVelocity if far from hand/object
            elif(velocity >= maxVelocity):
                velocity = maxVelocity
                px.forward(velocity)
                
                if(distance > 0 and distance < 20):
                    pin.value(1)
                else:
                    pin.value(0)

#Move at computed velocity if less than maxVelocity
            elif(velocity < maxVelocity):
                
                px.forward(velocity)
                
                if(distance > 0 and distance < 20):
                    pin.value(1)
                else:
                    pin.value(0)
                
                
            else:
                
                px.stop()
            
#Print some important data such as distance and velocity
 time.sleep(0.5)
            print('Distance: ' + str(distance))
            print('Velocity: ' + str(velocity))
                
#If user uses keyboard input such as ctrl + c, then the robot will stop

    except KeyboardInterrupt:
		px.stop()

    finally:
                
        px.stop()
        
if __name__ == '__main__':
    main()
