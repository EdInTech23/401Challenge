import os
import platform
import subprocess
import time
from datetime import datetime

def ping_host(ip):
    """
    Function to send an ICMP packet (ping) to the specified IP address.
    """
    try:
        # Done choose the appropriate ping command based on the operating system
        if platform.system().lower() == "windows":
            result = subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        else:
            result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)

        # Done check if the ping was successful (response code 0)
        if result.returncode == 0:
            return True
        else:
            return False

    except subprocess.TimeoutExpired:
        return False

if __name__ == "__main__":
    # Done specify the IP address to test (replace with your target IP)
    target_ip = "8.8.8.8"

    while True:
        # Done get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Done perform the ping test and get the result
        is_host_up = ping_host(target_ip)

        # Done determine the status based on the ping result
        status = "Network Active" if is_host_up else "Network Inactive"

        # Done print the result along with the timestamp and destination IP
        print(f"{timestamp} {status} to {target_ip}")

        # Done wait for 2 seconds before the next iteration
        time.sleep(2)
