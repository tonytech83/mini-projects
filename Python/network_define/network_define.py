import ipaddress

# ANSI escape code for red text
RED = "\033[91m"
RC = "\033[0m"

def check_net_ip(net_ip):
    """Check if the provided net_ip is a valid IPv4 address."""
    try:
        ipaddress.IPv4Address(net_ip)
        return True
    except ValueError:
        print(f"{RED}WARNING{RC} You entered an invalid IP address!")
        return False

def check_net_range(net_range):
    """Check if the provided net_range is a valid CIDR range (0-30)."""
    try:
        net_range = int(net_range)
        if 0 <= net_range <= 30:
            return True
        else:
            print(f"{RED}WARNING{RC} Network range must be between 0 and 30!")
            return False
    except ValueError:
        print(f"{RED}WARNING{RC} Network range must be an integer between 0 and 30!")
        return False


while True:
    net_ip = input("Enter network IP address: ")
    if check_net_ip(net_ip):
        break
    else:
        print("Please enter a valid IPv4 address.")

while True:
    net_range = input("Enter network range (CIDR notation): ")
    if check_net_range(net_range):
        break
    else:
        print("Please enter a valid CIDR range (0-30).")

network = F"{net_ip}/{net_range}"
network_obj = ipaddress.IPv4Network(network, strict=False)
usable_ips = list(network_obj.hosts())

print("=" * 40)
print(f"The input network is: {network}")
print(f"The range starts with {usable_ips[0]} and ends with {usable_ips[-1]}")
print(f"The count of usable ip address is: {len(usable_ips)}")
print("The usable IP addresses are:")
for idx, ip in enumerate(usable_ips, start=1):
    print(f"{idx} - {ip}")
