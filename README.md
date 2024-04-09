# Mikrotik
	A set of scripts for automating the operation of Mikrotik devices.
	The script uses an ssh connection (port 22 must be open)
	
## CreateRadiusAuth.py
	Activation of authorization on the device through the radius server.
## PassChange.py
	Script to change password.
## BackupConf.rsc
	Script to create an encrypted backup of the RouterOS configuration.
## BackupConfNoEncrypt.rsc
	Script to create an unencrypted RouterOS configuration backup.
## Drop_brute_force_password.rsc
	Script for blocking IPs from which brute-force password guessing attacks are conducted. Replace with your values for incoming interface, protocol, and port.