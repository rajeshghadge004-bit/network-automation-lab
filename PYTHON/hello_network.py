# Enterprise Network Device Inventory

devices = [
    {
        "hostname": "CORE1",
        "device_type": "Core Switch",
        "vendor": "Cisco",
        "model": "3650-24PS",
        "management_ip": "10.10.99.2",
        "location": "HQ",
        "status": "Active"
    },
    {
        "hostname": "CORE2",
        "device_type": "Core Switch",
        "vendor": "Cisco",
        "model": "3650-24PS",
        "management_ip": "10.10.99.3",
        "location": "HQ",
        "status": "Standby"
    },
    {
        "hostname": "ACCESS-SW1",
        "device_type": "Access Switch",
        "vendor": "Cisco",
        "model": "2960",
        "management_ip": "10.10.99.11",
        "location": "HQ Floor 1",
        "status": "Active"
    },
    {
        "hostname": "EDGE-R1",
        "device_type": "Router",
        "vendor": "Cisco",
        "model": "ISR4331",
        "management_ip": "10.10.99.21",
        "location": "HQ",
        "status": "Active"
    },
    {
        "hostname": "FW1",
        "device_type": "Firewall",
        "vendor": "Cisco",
        "model": "Firewall Appliance",
        "management_ip": "10.10.99.31",
        "location": "HQ",
        "status": "Active"
    },
    {
        "hostname": "DNS-DHCP-SRV",
        "device_type": "Server",
        "vendor": "Cisco Packet Tracer",
        "model": "Server",
        "management_ip": "10.10.20.10",
        "location": "HQ Server Farm",
        "status": "Active"
    },
    {
        "hostname": "WEB-SRV",
        "device_type": "Server",
        "vendor": "Cisco Packet Tracer",
        "model": "Server",
        "management_ip": "10.10.20.20",
        "location": "HQ Server Farm",
        "status": "Active"
    }
]


def display_devices():
    print("\n===== ENTERPRISE NETWORK DEVICE INVENTORY =====\n")

    for device in devices:
        print(f"Hostname      : {device['hostname']}")
        print(f"Device Type   : {device['device_type']}")
        print(f"Vendor        : {device['vendor']}")
        print(f"Model         : {device['model']}")
        print(f"Management IP : {device['management_ip']}")
        print(f"Location      : {device['location']}")
        print(f"Status        : {device['status']}")
        print("-" * 45)


if __name__ == "__main__":
    display_devices()