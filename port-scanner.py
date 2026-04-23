"""
Simple TCP Port Scanner
Author: Nilanjan
Description: Scans a target for open TCP ports and identifies common services.
"""

import socket
import argparse

def scan_ports(target, ports):
    print(f"\n[+] Starting scan on {target}\n")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[-] Could not resolve hostname.")
        return

    print(f"[+] Resolved IP: {target_ip}\n")

    common_ports = {
        22: "SSH",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[OPEN] Port {port} ({service})")

        s.close()

    print("\n[+] Scan complete.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")

    parser.add_argument("target", help="Target IP or domain")

    parser.add_argument(
        "-p", "--ports",
        help="Ports (e.g. 21,22,80 or 1-100)",
        required=True
    )

    args = parser.parse_args()

    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        port_list = range(start, end + 1)
    else:
        port_list = list(map(int, args.ports.split(",")))

    scan_ports(args.target, port_list)
