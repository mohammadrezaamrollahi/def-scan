import socket

ip_server = "....."
ip_mint = "......"
port_ftp = 21
port_webserver = 80
def pscan(ip,port):
    try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(f "port {port} is open in ip {ip}")
    except:
        print(f "port {port} is  not open in ip {ip}")
pscan(ip_server,port_ftp)
pscan(ip_server,port_webserver)
pscan(ip_mint,port_webserver)
