from scapy.all import *
import random

def tcp_port_scan(target_ip, port_range):
    for port in port_range:
        source_port = random.randint(1025, 65535)
        pkt = IP(dst=target_ip)/TCP(sport=source_port, dport=port, flags="S")
        resp = sr1(pkt, timeout=2, verbose=0)

        if resp is None:
            print(f"Port {port} is filtered and silently dropped.")
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=target_ip)/TCP(sport=source_port, dport=port, flags="AR"), timeout=1, verbose=0)
                print(f"Port {port} is open.")
            elif resp.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed.")

# Example usage
target_ip = "192.168.1.1"  # Replace with the target IP
port_range = range(20, 1025)  # Define the range of ports to scan
tcp_port_scan(target_ip, port_range)
