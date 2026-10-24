devices = [
 {"name":"Router","ip":"192.168.1.1"},
 {"name":"Switch","ip":"192.168.1.2"},
 {"name":"Firewall","ip":"192.168.1.3"},
]

for device in devices:
 print("Device Name:",device["name"])
 print("Device IP:",device["ip"])
 print("--------------------")