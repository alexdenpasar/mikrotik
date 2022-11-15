# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import getpass

print("########################################")
print("####  User password change script.  ####")
print("########################################")
print(" ")

def authMik():
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

    # List of users.
    listUsers(sshCli)

    # Changing the password.
    changePass(sshCli)
    sshCli.disconnect()

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
            sshCli.disconnect()
            print("Closed session.")
            print(" ")
            authMik()
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

if __name__ == "__main__":
    authMik()