from scapy.all import *
import random
import ipaddress

def tcp_port_scan(target_ip, port_range):
    # Existing TCP Port Scan code here
    # ...

def icmp_ping_sweep(network):
    online_hosts = 0
    network = ipaddress.ip_network(network)
    for host in network.hosts():
        # ICMP packet
        icmp_pkt = IP(dst=str(host))/ICMP()
        resp = sr1(icmp_pkt, timeout=1, verbose=0)
        
        if resp is None:
            print(f"{host} is down or unresponsive.")
        elif int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
            print(f"{host} is actively blocking ICMP traffic.")
        else:
            print(f"{host} is responding.")
            online_hosts += 1

    print(f"Total hosts online: {online_hosts}")

def main():
    choice = input("Choose mode (1-TCP Port Range Scanner, 2-ICMP Ping Sweep): ")
    if choice == '1':
        target_ip = input("Enter target IP: ")
        port_range = range(20, 1025)  # or prompt user for custom range
        tcp_port_scan(target_ip, port_range)
    elif choice == '2':
        network = input("Enter network address with CIDR (e.g., 192.168.1.0/24): ")
        icmp_ping_sweep(network)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
