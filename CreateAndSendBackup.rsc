# automated backup export ftp
# ftp configuration
:local ftphost "192.168.1.2"
:local ftpuser "ftp-user"
:local ftppassword "ftp-password"
:local ftppath "Mikrotik"
# months array
:local months ("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec");
# get time
:local ts [/system clock get time]
:set ts ([:pick $ts 0 2].[:pick $ts 3 5].[:pick $ts 6 8])
# get Date
:local ds [/system clock get date]
# convert name of month to number
:local month [ :pick $ds 0 3 ];
:local mm ([ :find $months $month -1 ] + 1);
:if ($mm < 10) do={ :set mm ("0" . $mm); }
# set $ds to format YYYY-MM-DD
:set ds ([:pick $ds 7 11] . $mm . [:pick $ds 4 6])
# file name for system backup - file name will be Mikrotik-servername-date-time.backup
:local fname1 ("/Mikrotik-".[/system identity get name]."-".$ds."-".$ts.".backup")
# file name for config export - file name will be Mikrotik-servername-date-time.rsc
:local fname2 ("/Mikrotik-".[/system identity get name]."-".$ds."-".$ts.".rsc")
# backup the data
/system backup save name=$fname1
:log info message="System backup finished (1/2).";
/export compact file=$fname2
:log info message="Config export finished (2/2)."
# upload the user manager backup
:log info message="Uploading system backup (1/2)."
/tool fetch address="$ftphost" src-path=$fname1 user="$ftpuser" mode=ftp password="$ftppassword" dst-path="$ftppath/$fname1" upload=yes
# upload the config export
:log info message="Uploading config export (2/2)."
/tool fetch address="$ftphost" src-path=$fname2 user="$ftpuser" mode=ftp password="$ftppassword" dst-path="$ftppath/$fname2" upload=yes
# delay time to finish the upload - increase it if your backup file is big
:delay 30s;
# find file name start with Mikrotik- then remove
:foreach i in=[/file find] do={ :if ([:typeof [:find [/file get $i name] "Mikrotik-"]]!="nil") do={/file remove $i}; }
:log info message="Configuration backup finished.";

