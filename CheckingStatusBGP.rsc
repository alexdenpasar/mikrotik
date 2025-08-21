# BGP system based on RouterOS 6.49.13
:local sysname [/system identity get name]

:foreach peer in=[/routing bgp peer find] do={
    :local name [/routing bgp peer get $peer name]
    :local disabled [/routing bgp peer get $peer disabled]
    :local state [/routing bgp peer get $peer state]  
    
    :if ($disabled != true) do={
            /log info ("$sysname: Peer $name BGP state is $state")
    }
}