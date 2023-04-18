from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        px = Picarx()
        px.forward(30) #Move forward
        time.sleep(0.5) #Pause
        for angle in range(0,35):
            px.set_dir_servo_angle(angle) #Set angle of the servo
            time.sleep(0.01)
        for angle in range(35,-35,-1): #Change angle of servo
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0): #Change angle of servo
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(1)

        for angle in range(0,35): #Change angle of camera servo
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1): #Change angle of camera servo
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0): #Change angle of camera servo
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0,35): #Change angle of camera servo
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35,-35,-1): #Change angle of camera servo
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(-35,0): #Change angle of camera servo
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)

    finally:
        px.forward(0)
