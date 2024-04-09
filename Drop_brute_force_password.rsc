:local InInterface "ether1"
:local protocol "tcp"
:local port "8291"
:local timeoutBlacklist "1d 00:00:00"

/ip firewall filter add action=drop src-address-list=blacklist chain=input
/ip firewall filter add action=add-src-to-address-list address-list=blacklist address-list-timeout=$timeoutBlacklist src-address-list=blacklist_2 chain=input in-interface=$InInterface connection-state=new protocol=$protocol dst-port=$port
/ip firewall filter add action=add-src-to-address-list address-list=blacklist_2 address-list-timeout=00:05:00 src-address-list=blacklist_1 chain=input in-interface=$InInterface connection-state=new protocol=$protocol dst-port=$port
/ip firewall filter add action=add-src-to-address-list address-list=blacklist_1 address-list-timeout=00:05:00 chain=input in-interface=$InInterface connection-state=new protocol=$protocol dst-port=$port