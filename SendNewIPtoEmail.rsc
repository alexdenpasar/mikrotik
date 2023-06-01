# Check ip and send to e-mail if changed
#---------- Config below this line ----------

# set WAN interface name
:local WAN "bridge-local";
# set e-mail smtp server name
:local smtpserv "192.168.254.9";
# set e-mail mikrotik@komplex-group.ru
:local Eaccount "mikrotik@komplex-group.ru";
# set e-mail 12345678
:local Epassword "DataCenter2!";
# set e-mail main recipient
:local Etomail "alert@komplex-group.ru";

#---------- Config above this line ----------

:global StoredIP
:local sysname [/system identity get name];
:local sysver [/system package get system version];
:local CurrIP
:log info "Get WAN interface IP address (New IP to e-mail script)"

# Get WAN interface IP address
:set CurrIP [/ip address get [/ip address find interface=$WAN] address]
:set CurrIP [:pick [:tostr $CurrIP] 0 [:find [:tostr $CurrIP] "/"]]

:if ([:len $CurrIP] = 0) do={
:log error ("Could not get IP for interface " . $WAN)
:error ("Could not get IP for interface " . $WAN)
} else={:log info "IP from $WAN get. (New IP to e-mail script)"}
:log info "Checking & sending IP if needed."

# Check IP address & send if needed

:if ($StoredIP != $CurrIP) do={
/tool e-mail send from=$Eaccount to=$Etomail \
server=$smtpserv port=587 user=$Eaccount password=$Epassword \
subject=("Mikrotik $sysname IP changed (" . [/system clock get date] . \
")") body=("New $sysname IP: $CurrIP.\nRouterOS \
version: $sysver\nTime and Date stamp: " . [/system clock get time] . " \
" . [/system clock get date]);
:log info "Send new IP to e-mail complete"
:set StoredIP "$CurrIP"
:log info "Stored IP Updated"
} else={:log info "IP not changed"}