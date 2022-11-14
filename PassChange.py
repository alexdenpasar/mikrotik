from netmiko import ConnectHandler

print("########################################")
print("####  User password change script.  ####")
print("########################################")
print(" ")

# Entering data to connect
ipAddr = input("Enter ip address Mikrotik: ")
loginMik = input("Enter login Mikrotik: ")
passMik = input("Enter password Mikrotik: ")

mikrotik_router_1 = {
'device_type': 'mikrotik_routeros',
'host': ipAddr,
'port': '22',
'username': loginMik,
'password': passMik
}

# Opening ssh connection.
sshCli = ConnectHandler(**mikrotik_router_1)

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

# Changing the password.
loginMikChange = input("Enter the username for which you want to change the password: ")    
newPassMikChange = input(f"Enter a new password for the user {loginMikChange}: ")
confirmNewPassMikChange = input(f"Confirm new password for user {loginMikChange}: ")

# Checking the correctness of the password entered and, if correct, then change.
if newPassMikChange == confirmNewPassMikChange:
    sshCli.send_command(f"user set password={newPassMikChange} {loginMikChange}")
    print("Password changed successfully!")
else:
    print("Wrong login or password!")

# Closing the ssh connection.
sshCli.disconnect()