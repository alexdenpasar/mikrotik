:local nameinterface "ether2"
:local host1 "192.168.1.1"
:local host2 "192.168.2.2"

:local checkip1 [/ping $host1 count=4]

:if (checkip1 = 0) do={ 
/log error "Server $host1 is not available. Server check $host2...."
:local checkip2 [/ping $host2 count=4]

:if (checkip2 = 0) do={ 
/interface ethernet disable $nameinterface
/log error ("Interface $nameinterface disable")
}
} else {
/log warning ("Server $host1 is available.")
/interface ethernet enable $nameinterface
/log warning ("Interface $nameinterface enable")
}


