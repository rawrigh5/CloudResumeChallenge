import re

# Regular expression for matching IPv4 addresses
ipv4_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$")

# Function to check the validity of an IP address
def is_valid_ip(ip):
    return bool(ipv4_pattern.match(ip))

# Read IP addresses from the input file
input_file = "./ip_input.txt"

#with open(input_file, "r") as file:
#    ip_addresses = file.read().splitlines()


ip_addresses = ["8.8.8.8","2.2.2.2.2","127.5.6.7","3.3.3.305","0.120.3.5"]    

# Check validity for each IP address
for ip in ip_addresses:
    validity = "yes" if is_valid_ip(ip) else "no - bad format"
    
    print(f"IP address: {ip}")
    print(f"Validity: {validity}")
    print()
