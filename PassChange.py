# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import getpass
import sys, os

print("########################################")
print("####  User password change script.  ####")
print("########################################")
print(" ")

def authMik():
    global ipAddr
    # Entering data to connect.
    ipAddrAndPort = input("Enter ip address Mikrotik (ip:port): ")
    loginMik = input("Enter login Mikrotik: ")
    passMik = getpass.getpass("Enter password Mikrotik: ")
    if ipAddrAndPort.find(":") > 0:
        ipAddr, Port = ipAddrAndPort.split(':')
    else:
        ipAddr = ipAddrAndPort
        Port = "22"

    mikrotik_router = {
    'device_type': 'mikrotik_routeros',
    'host': ipAddr,
    'port': Port,
    'username': loginMik,
    'password': passMik
    }

    # Opening ssh connection.
    sshCli = ConnectHandler(**mikrotik_router)
    os.system('cls||clear')

    # Menu Sheet
    menuList(ipAddr)
    menuListNumber(sshCli)

def menuList(ipAddr):

    print("########################################")
    print("####  User password change script.  ####")
    print("########################################")
    print(" ")
    print(f"Connected to {ipAddr}")
    print(" ")
    print("1) List of users.")
    print("2) Change user password.")
    print("3) Connect to Microtik.")
    print("4) Exit.")

def menuListNumber(sshCli):
    
    # Menu Sheet
    menuNumber = input("Select the menu number: ")

    if menuNumber == str(1):
        listUsers(sshCli)
    elif menuNumber == str(2):
        changePass(sshCli)
    elif menuNumber == str(3):
        authMik()
    elif menuNumber == str(4):
        sshCli.disconnect()
        sys.exit()

def changePass(sshCli):

    # Changing the password.
    loginMikChange = input("Enter the username for which you want to change the password: ")   
    newPassMikChange = getpass.getpass(f"Enter a new password for the user {loginMikChange}: ")
    confirmNewPassMikChange = getpass.getpass(f"Confirm new password for user {loginMikChange}: ")

    # Checking the correctness of the password entered and, if correct, then change.
    if newPassMikChange == confirmNewPassMikChange:
        sshCli.send_command(f"user set password={newPassMikChange} {loginMikChange}")
        print("Password changed successfully!")
        quesPass = input("Change password for other users?(y/n): ")
        if quesPass == 'y' or quesPass == 'Y':
            changePass(sshCli)
        else:
            os.system('cls||clear')
            menuList(ipAddr)
            menuListNumber(sshCli)
    else:
        print("Wrong login or password! Try again.")
        changePass(sshCli)

def listUsers(sshCli):

    # List of users.
    listUsers = sshCli.send_command("/user print detail")
    strStart = "name="
    strEnd = "group"
    countStart = -1
    count = 0
    listStart = 0

    # Search for a match on the first character or word.
    resStart = [i for i in range(len(listUsers)) if listUsers.startswith(strStart, i)]

    # Search for a match on the last character or word.
    resEnd = [i for i in range(len(listUsers)) if listUsers.startswith(strEnd, i)]

    # Merge lists into one.
    resFull = resStart + resEnd

    # Get the number of matches.
    while count < len(listUsers):
        countStart = listUsers.find(strStart, countStart+1)
        if countStart == -1:
            break
        count += 1
    print("Number of users:", count)

    # Show received matches.
    while listStart < count:
        print(listUsers[resFull[listStart]+5:resFull[listStart+2]])
        listStart += 1
    
    menuListNumber(sshCli)

if __name__ == "__main__":
    authMik()