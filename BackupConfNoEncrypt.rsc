# automated export backup ftp with simple timeout
# ftp configuration
:local ftphost "192.168.0.1"
:local ftpuser "usrftp"
:local ftppassword "password"
:local ftpport "port"
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

# file name for system export
:local fname1 ("/Mikrotik-".[/system identity get name]."-".$ds."-".$ts.".rsc")

:log info message="System export start (1/1).";
# export the configuration
/export file=$fname1
:delay 5s;
:log info message="System export finished (1/1).";

# upload with timeout and error handling
:log info message="Uploading system export (1/1)."

:do {
    /tool fetch address="$ftphost" port=$ftpport dst-path=("Mikrotik/$ds" . "/$fname1") user="$ftpuser" mode=ftp password="$ftppassword" upload=yes
    :log info message="Upload command executed"
} on-error={
    :log error message="Upload failed or FTP server not accessible"
}

# wait maximum 60 seconds for upload completion
:delay 60s;

# always remove export files regardless of upload success
:log info message="Cleaning up export files..."
:foreach i in=[/file find] do={ 
    :if ([:typeof [:find [/file get $i name] "Mikrotik-"]]!="nil") do={
        :local fileName [/file get $i name]
        /file remove $i
        :log info message="Export file removed: $fileName"
    }
}

:log info message="Configuration export process finished."