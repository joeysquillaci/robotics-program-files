from picarx import Picarx
from time import sleep

#Define initial variables
px = Picarx()
px.set_grayscale_reference(1600)
last_state = None
current_state = None
px_power = 0.25 #Define how fast we want the robot to move
offset = 20
alpha = 0.000332 #Alpha we selected based on testing
distance = 0

def outHandle():
    global last_state, current_state
    if last_state == 'left':	    #Straighten wheels if we just turned left
        px.set_dir_servo_angle(-12)
        px.backward(5)
    elif last_state == 'right': #Straighten wheels if we just turned left
        px.set_dir_servo_angle(12)
        px.backward(5)
    while True:
        gm_val_list = px.get_grayscale_data() #Logic for following based on grayscale data
        gm_state = px.get_line_status(gm_val_list)
        print("outHandle gm_val_list: Grayscale Data:%s, Line Status:%s" %
              (gm_val_list, gm_state))
        currentSta = gm_state
        if currentSta != last_state:
            break
    sleep(0.001)


if __name__ == '__main__':
    try:
        while True:
#Get grayscale data and to determine how we will follow the line
            gm_val_list = px.get_grayscale_data()
            gm_state = px.get_line_status(gm_val_list)
            print("gm_val_list: Grayscale Data:%s, Line Status:%s" %
                  (gm_val_list, gm_state))

            if gm_state != "stop":
                last_state = gm_state

            if distance/0.0205 < 2:	#Converts distance and makes computations based on if its less than 2 meters

                distance = (alpha*px_power+distance)

            if distance > 0.04:	#Stop robot if distance is greater than 2m (This is without conversion like in last ‘if’ statement)

                px.stop()

	#Logic for moving robot
            elif gm_state == 'forward':
                px.set_dir_servo_angle(0)
                px.forward(px_power)
            elif gm_state == 'left':
                px.set_dir_servo_angle(offset)
                px.forward(px_power)
            elif gm_state == 'right':
                px.set_dir_servo_angle(-offset)
                px.forward(px_power)
            else:
                outHandle()

          #Print distance with conversion
            print('distance: ' + str(distance/0.0205))
    finally:
        px.stop()

