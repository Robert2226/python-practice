import subprocess
import platform

# List of IPs to ping
ip_list = [
    "8.8.8.8",        # Google DNS
    "1.1.1.1",        # Cloudflare DNS
    "192.168.1.1",    # Example local gateway
]

# Determine the ping command based on OS
param = "-n" if platform.system().lower() == "windows" else "-c"

for ip in ip_list:
    print(f"Pinging {ip}...")
    response = subprocess.run(["ping", param, "2", ip], stdout=subprocess.PIPE)

    if response.returncode == 0:
        print(f"{ip} is **UP**")
    else:
        print(f"{ip} is **DOWN**")
