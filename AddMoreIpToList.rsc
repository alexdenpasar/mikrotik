:local ipAddresses {
    "192.168.0.1/24";
    "192.168.1.1/24";
    "192.168.2.1/24";
}

:foreach address in=$ipAddresses do={
    /ip firewall address-list add address=$address list=IpList1
}