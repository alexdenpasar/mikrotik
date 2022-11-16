import time
from netmiko import ConnectHandler
import sys
import getpass

# Entering data to connect.
ipAddr = input("Enter ip address Mikrotik: ")
loginMik = input("Enter login Mikrotik: ")
passMik = getpass.getpass("Enter password Mikrotik: ")

mikrotik_router_1 = {
'device_type': 'mikrotik_routeros',
'host': ipAddr,
'port': '22',
'username': loginMik,
'password': passMik
}

# Opening ssh connection.
sshCli = ConnectHandler(**mikrotik_router_1)

addressRadiusServer = input("Enter ip address Radius Server: ")
secretRadius = input("Enter secret Radius Server: ")

# Enable AAA authorization and reset server radius settings.
enableUseRadius = "/user aaa set use-radius=yes"
addRadiusAuth = f"/radius add service=login address={addressRadiusServer} secret={secretRadius}"
showComOne = "/radius print detail"
showComTwo = "/user aaa print" 
comdOne = sshCli.send_command(enableUseRadius)
comTwo = sshCli.send_command(addRadiusAuth)
time.sleep(1)
print(sshCli.send_command(showComOne))
time.sleep(1)
print(sshCli.send_command(showComTwo))
# Closing the ssh connection.
sshCli.disconnect()
print(" ")
print("Successfully!")
# Wait 10 seconds and close the console.
time.sleep(10)
sys.exit