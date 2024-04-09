import socket

def port_scan(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        s.settimeout(1)
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        # Check if the port is open
        if result == 0:
            print("Port {} is open".format(port))
        # Close the socket
        s.close()
    except socket.error:
        pass

def main():
    host = input("Enter the host IP address or domain name: ")
    # Splitting the input if it's a range of IP addresses
    if '-' in host:
        start, end = host.split('-')
        start = int(start.split('.')[-1])
        end = int(end)
        host = '.'.join(host.split('.')[:-1])
        for i in range(start, end + 1):
            for port in range(1, 1025):
                port_scan(host + '.' + str(i), port)
    else:
        for port in range(1, 1025):
            port_scan(host, port)

if _name_ == "_main_":
    main()