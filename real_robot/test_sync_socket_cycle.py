from socket import socket,AF_INET,SOCK_DGRAM
import time
import keyboard
from math import pi,sin

PORT=5000
CLIENT="192.168.0.111"
# CLIENT="192.168.0.112"


def main():
    sock=socket(AF_INET,SOCK_DGRAM)


    t_interval=0.12 #[s] socket connection cycle
    t_now=time.perf_counter()
    t_prev=t_now

    while True:

        ##For Synchronization
        ##skip process until 0.12 seconds have elapsed.
        t_now=time.perf_counter()
        if t_now-t_prev<t_interval:
            continue
        t_prev=t_now #update 't_prev'
        ##

        try:
            head_radian=pi/9.2*sin(t_now)
            msg=f"{head_radian},0,0,0,0,0,0,0,0,0,0,0"
            sock.sendto(msg.encode("utf-8"),(CLIENT,PORT))

        except KeyboardInterrupt:
            break

        print("your message : ",msg,"elapsed_time : ",time.perf_counter())


if __name__=="__main__":
    main()

