import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is close")
        sock.close()
    except Exception as e:
        print(f"Error occurred: {str(e)}")

host = '127.0.0.1'

for port in range(1, 65536):
    port_scanner(host, port)
