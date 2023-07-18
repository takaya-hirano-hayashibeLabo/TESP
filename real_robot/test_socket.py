from socket import socket,AF_INET,SOCK_DGRAM
import time
import keyboard
from math import pi

PORT=5000
CLIENT="192.168.0.112"


def main():
    sock=socket(AF_INET,SOCK_DGRAM)

    while True:

        try:
            if keyboard.read_key()=="d":
                msg=f"{pi/9.2},0,0,0,0,0,0,0,0,0,0,0" #'msg' is each servo motor's radian. Maximum value is |pi/9.2|.
            elif keyboard.read_key()=="a":
                msg=f"{-pi/9.2},0,0,0,0,0,0,0,0,0,0,0"
            else:
                msg="0,0,0,0,0,0,0,0,0,0,0,0"
                 
            sock.sendto(msg.encode("utf-8"),(CLIENT,PORT))

        except KeyboardInterrupt:
            break

        print("your message : ",msg)
        time.sleep(0.1)


if __name__=="__main__":
    main()

