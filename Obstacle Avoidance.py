from picarx import Picarx


def main():
    try:
        px = Picarx()
        # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
        px.forward(30) #Move forward
        while True:
            distance = px.ultrasonic.read() #Read distance from sensor
            print("distance: ",distance)
            if distance > 0 and distance < 300: #Logic to change servo angle within certain distance
                if distance < 25:
                    px.set_dir_servo_angle(-35)
                else:
                    px.set_dir_servo_angle(0)
    finally:
        px.forward(0)


if __name__ == "__main__":
    main()
