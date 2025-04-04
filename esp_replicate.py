import socket
import time
import random

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_fake_data():
    ax = round(random.uniform(-1.0, 1.0),2)
    ay = round(random.uniform(-1.0, 1.0),2)
    az = round(random.uniform(-9.8, 9.6),2)
    gx = round(random.uniform(-5.0, 5.0),2)
    gy = round(random.uniform(-5.0, 5.0),2)
    gz = round(random.uniform(-5.0, 5.0),2)
    return f"{ax},{ay},{az},{gx},{gy},{gz}"

while True:
    data = get_fake_data()
    print(f"Sending: {data}")
    sock.sendto(data.encode(), (UDP_IP,UDP_PORT))
    time.sleep(0.05)