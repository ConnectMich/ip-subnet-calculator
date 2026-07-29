import ipaddress


def calc(ip_address, subnet_mask):
    try:
        network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
    except ipaddress.AddressValueError:
        print("Invalid IP address")
        return "IP Error"
    except ipaddress.NetmaskValueError:
        print("Invalid Subnet Mask")
        return "Subnet Error"
    except ValueError:
        print("Invalid Values")
        return "Error"

    usable_hosts = network.num_addresses - 2
    first_host = network.network_address + 1
    last_host = network.broadcast_address - 1

    address_type = ""
    if network.is_private == True:
        address_type = "Private"
    else:
        address_type = "Public"

    ip_class = ""
    first_octet = int(ip_address.split(".")[0])
    if first_octet >= 1 and first_octet <= 126:
        ip_class = "Class A"
    elif first_octet == 127:
        ip_class = "Loopback"
    elif first_octet >= 128 and first_octet <= 191:
        ip_class = "Class B"
    elif first_octet >= 192 and first_octet <= 223:
        ip_class = "Class C"
    elif first_octet >= 224 and first_octet <= 239:
        ip_class = "Class D(Multicast)"
    elif first_octet >= 240 and first_octet <= 255:
        ip_class = "Class E(Experimental/Reserved)"
    else:
        ip_class = "Unknown"

    result = {
        "IP Address": ip_address,
        "Network Address": network.network_address,
        "Broadcast Address": network.broadcast_address,
        "Subnet Mask": network.netmask,
        "CIDR Notation": network.prefixlen,
        "Total Number Of Addresses": network.num_addresses,
        "Usable Hosts": usable_hosts,
        "First Usable Host": first_host,
        "Last Usable Host": last_host,
        "Wildcard Mask": network.hostmask,
        "Type Of Address": address_type,
        "Address Class": ip_class,
    }

    return result
