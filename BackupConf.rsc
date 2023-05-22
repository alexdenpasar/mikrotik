# automated backup export ftp
# ftp configuration
:local ftphost "ftp-server"
:local ftpuser "ftp-user"
:local ftppassword "ftp-password"
:local ftpport "21"
:local ftppath 
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
:log info message="System backup start (1/1).";
# backup the data
/system backup save name=$fname1 password=PRetendeR1@3
:delay 5s;
:log info message="System backup finished (1/1).";
# upload the user manager backup
:log info message="Uploading system backup (1/1)."
/tool fetch address="$ftphost" port=$ftpport dst-path=("$ds" . "/$fname1") user="$ftpuser" mode=ftp password="$ftppassword" upload=yes
# delay time to finish the upload - increase it if your backup file is big
:delay 10s;
# find file name start with Mikrotik- then remove
:foreach i in=[/file find] do={ :if ([:typeof [:find [/file get $i name] "Mikrotik-"]]!="nil") do={/file remove $i}; }
:log info message="Configuration backup finished.";