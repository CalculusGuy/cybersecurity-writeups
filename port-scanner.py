import socket

target = "127.0.0.1"
ports = [21, 22, 53, 80, 443, 8080]

count = 0

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
        count += 1
    else:
        print(f"Port {port}: CLOSED")
    sock.close()

print(f"Total open ports: {count}")
