import Port_Scanner

target_ip = input('[+] Enter the IP want to scan for vulnerability: ')
port_number = int(input('[+] Enter the Ports amount want to scam: '))
vuln_file = input('[+] Enter the vulnerable file path: ')
print('\n')

target = Port_Scanner.PortScan(target_ip, port_number)
target.scan()

with open(vuln_file ,'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[+] VULNERABLE BANNER:  " ' + banner + ' " ON PORT ' +str(target.open_port[count])  )
    count += 1