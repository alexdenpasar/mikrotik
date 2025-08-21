# BGP system based on RouterOS 6.49.13
:foreach peer in=[/routing bgp peer find] do={
    :local name [/routing bgp peer get $peer name]
    :local disabled [/routing bgp peer get $peer disabled]
    :local state [/routing bgp peer get $peer state]
    
    :if ($disabled != true) do={
        :if ($state != "established") do={
            /log error ("RO52: Peer $name BGP state is $state")
        }
    }
}