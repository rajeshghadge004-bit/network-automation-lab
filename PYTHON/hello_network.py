devices = [
 {"name":"Router","ip":"192.168.1.1"},
 {"name":"Switch","ip":"192.168.1.2"},
 {"name":"Firewall","ip":"192.168.1.3"},
 {"name":"Router","ip":"10.0.0.1"}
]

print("Firewall Devices:")

for device in devices:
 if device["name"] == "Firewall":
     print(device["name"],"-",device["ip"])