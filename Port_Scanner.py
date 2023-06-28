import socket as socket #socket library to use the ports 
from IPy import IP #to convert the domain name into IP we required this library 

class PortScan:
    banners = []
    open_ports = []
    def __init__(self,target,port_num):
        self.target = target
        self.port_num = port_num

    
    def scan(self):
        for port in range(1,1000):
            self.port_scan(port)
    
    
    def check_ip(self): #function to convert Domain into the IP address 
        try:
            IP(self.target)
            return self.target # simple , if use input the IP then only IP will scan 
        except ValueError:
            return socket.gethostbyname(self.target) #otherwise the this parameter will convert the IP into IP



    def port_scan(self,port): #here we define function to scan a port
        try:
            converted_ip - self.check_ip()
            sock = socket.socket() # socket will fucntion from library will run here
            sock.settimeout(0.5)
            sock.connect(converted_ip , port)
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass # here if port is closed then simply it will pass 


