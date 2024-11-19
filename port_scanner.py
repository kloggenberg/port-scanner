import re
import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pyfiglet import Figlet
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()

def print_banner():
    TEXT = "Port Scanner 9000"
    fig = Figlet()
    ascii_art = fig.renderText(TEXT)
    print("-" * 100)
    print(ascii_art)
    print("-" * 100)

def grab_banner(sock):
    try:
        sock.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = sock.recv(1024).decode('utf-8').strip()
        return banner if banner else "No banner"
    except Exception as e:
        return f"Error grabbing banner: {e}"

def scan_port(target, port, timeout, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((target, port))
        status = "OPEN"
        banner = grab_banner(sock)
        results.append((port, status, banner))
    except Exception:
        results.append((port, "CLOSED", None))
    finally:
        sock.close()

def is_valid_ip(ip_str):
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    if ip_pattern.match(ip_str):
        octets = ip_str.split('.')
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    return False

def thread_scan(target, start_port, end_port, timeout):
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port, timeout, results)
    results.sort()
    for port, status, banner in results:
        if status == "OPEN":
            logger.info(f"Port {port} is {status}. Banner: {banner}")
        else:
            logger.info(f"Port {port} is {status}")

def parse_args():
    parser = argparse.ArgumentParser(description='Port Scanner 9000')
    parser.add_argument('target', help='Target IP address')
    parser.add_argument('-p', '--ports', default='20-80', help='Port range to scan (e.g., 20-80)')
    parser.add_argument('-t', '--timeout', type=float, default=0.5, help='Timeout for each port scan')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    target = args.target

    if not is_valid_ip(target):
        logger.error("Invalid IP address format")
        sys.exit(1)

    try:
        start_port, end_port = map(int, args.ports.split('-'))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError("Invalid port range")
    except ValueError:
        logger.error("Invalid port range format")
        sys.exit(1)

    print_banner()
    logger.info(f"Scanning target: {target}")
    logger.info(f"Scanning ports {start_port} to {end_port}...\n")

    thread_scan(target, start_port, end_port, args.timeout)
