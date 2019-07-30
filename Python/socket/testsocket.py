import socket

sock = socket.socket()

host = "192.168.4.1" #ESP32 IP in local network
port = 80             #ESP32 Server Port

sock.connect((host, port))

message = bytes("#18P2500".encode('utf-8'))

sock.send(message)

data = ""

print(str(data))

sock.close()
