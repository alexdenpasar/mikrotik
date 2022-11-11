import time
from netmiko import ConnectHandler
import sys

ipAddr = input("Enter ip address: ")
loginMik = input("Enter login mikrotik: ")
passMik = input("Enter password mikrotik: ")

mikrotik_router_1 = {
'device_type': 'mikrotik_routeros',
'host': ipAddr,
'port': '22',
'username': loginMik,
'password': passMik
}

sshCli = ConnectHandler(**mikrotik_router_1)

enableUseRadius = "/user aaa set use-radius=yes"
addRadiusAuth = "/radius add service=login address=192.168.254.7 secret=komplexhost"
showComOne = "/radius print detail"
showComTwo = "/user aaa print" 
comdOne = sshCli.send_command(enableUseRadius)
comTwo = sshCli.send_command(addRadiusAuth)
time.sleep(1)
print(sshCli.send_command(showComOne))
time.sleep(1)
print(sshCli.send_command(showComTwo))
sshCli.disconnect()
print(" ")
print("Successfully!")
time.sleep(10)
sys.exit