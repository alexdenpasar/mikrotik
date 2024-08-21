# A set of scripts for automating MikroTik device operations. Some scripts use SSH connection (port 22 should be open).
	
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
## EnableAndDisableInterface.rsc
	The script checks the availability of host $host1. If it is not available, it checks the availability of the second host $host2. If the second host is not available, it disables the specified interface.
## CreateAndSendBackup.rsc
	Script to create an encrypted backup of the RouterOS ver.7 configuration.
## on_login.rsc and SendEmailAuthOnMikrotik.rsc
	Script for notification of user authorization on RouteOS with email notification.
## SendNewIpToEmail.rsc
	The script tracks the receipt of a new public IP address and, if the address changes, sends a notification with the changed IP to the mail. Convenient script, if the IP is dynamic.