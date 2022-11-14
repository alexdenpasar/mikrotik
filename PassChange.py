import time
from netmiko import ConnectHandler
import sys

print("########################################")
print("####  User password change script.  ####")
print("########################################")
print(" ")

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

listUsers = sshCli.send_command("/user print detail")
strStart = "name="
strEnd = "group"
countStart = -1
count = 0
listStart = 0

resStart = [i for i in range(len(listUsers)) if listUsers.startswith(strStart, i)]
resEnd = [i for i in range(len(listUsers)) if listUsers.startswith(strEnd, i)]
resFull = resStart + resEnd

while count < len(listUsers):
    countStart = listUsers.find(strStart, countStart+1)
    if countStart == -1:
        break
    count += 1
print("Number of users:", count)

while listStart < count:
    print(listStart+1,"-", listUsers[resFull[listStart]+5:resFull[listStart+2]])
    listStart += 1

sshCli.disconnect()
