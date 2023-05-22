# Division 2 IP Sniffer

This IP sniffer works because Tom Clancy's The Division 2 does not use dedicated servers for VOIP instead opts in to use P2P based communications which of course allows you to gather IP's of clients connecting to you.

## Solution to prevent getting IP Address Taken
- Go to in game settings
- Select audio
- Disable VOIP
#
## How it was so easy to figure out what the VOIP Packet was
- As you can see in the below packet they used a placeholder of 0xCAFEBEEF
- This is also known as the packet "MAGIC" used to identify packets
```
example packet:  
b"\xca\xfe\xbe\xef\x08\x18\x00\x00\x00=3\xdc\xa3\x81\xed\xf6I\x8d0P\xea6\xdc'\xc1H\x00\x00\x00\xd7\xc4\xdb\x01\xff\x9d\xc5T\x05{\xf0.\x03,\x13\x92\x0e[\xee\x91\xd1\x01K\xa8Zh\xe9$\xd4b\xf1\xc9yq\xfeKV\x9fT\x90\x12\xeb\x9f\xa7X\x98%=\x85\x8e\xafC\x98F\xa9\x89\t\x90yV\xc9\xe9\xf4_\xb0\xa0\xc7\xec0\xf7\x89W"
```
#