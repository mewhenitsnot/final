import datetime

# ANSI escape codes for terminal colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Business Information
business_name = "Goat Milk Stuff"
description = (
    "Goat Milk Stuff is a family-owned business based in Scottsburg, Indiana, specializing "
    "in creating natural goat milk products. Their mission is to provide high-quality, sustainable, "
    "and healthy alternatives to traditional skincare and consumables, using milk sourced from their own goats."
)
contact_info = {
    "Address": "76 S Lake Rd N, Scottsburg, IN 47170, USA",
    "Phone": "(812) 752-0622",
    "Email": "pj@goatmilkstuff.com",
    "Website": "https://goatmilkstuff.com",
}
services = [
    "Handcrafted goat milk soaps",
    "Lotions and creams made with goat milk",
    "Natural deodorants and lip balms",
    "Goat milk food products (cheese, caramel, fudge)",
    "Farm tours and educational experiences",
    "Custom gift baskets and sets",
]

# Print formatted documentation with colors
def print_documentation():
    print(f"{Colors.HEADER}{Colors.BOLD}# {business_name}{Colors.RESET}\n")
    print(f"{Colors.BLUE}{Colors.BOLD}### Description{Colors.RESET}")
    print(f"{Colors.GREEN}{description}{Colors.RESET}\n")
    print(f"{Colors.BLUE}{Colors.BOLD}### Contact Information{Colors.RESET}")
    for key, value in contact_info.items():
        print(f"{Colors.YELLOW}- {key}: {Colors.RESET}{value}")
    print(f"\n{Colors.BLUE}{Colors.BOLD}### Services Offered{Colors.RESET}")
    for service in services:
        print(f"{Colors.GREEN}- {service}{Colors.RESET}")
    print(f"\n{Colors.BLUE}{Colors.BOLD}### Generated On{Colors.RESET}")
    print(f"{Colors.RED}- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}\n")

# Execute the function
print_documentation()

