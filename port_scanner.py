import re
import socket
import sys
import threading
from pyfiglet import Figlet

def print_banner():
    TEXT = "Port Scanner 9000"
    # Create a Figlet object
    fig = Figlet()

    # Use the Figlet object to convert text to ASCII art
    ascii_art = fig.renderText(TEXT)

    # Print the ASCII art
    print("-" * 100)
    print(ascii_art)
    print("-" * 100)

def scan_port(target, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((target, port))
        results.append((port, "OPEN"))
    except:
        results.append((port, "CLOSED"))
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

def thread_scan(target, start_port, end_port):
    threads = []
    results = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    results.sort()
    for port, status in results:
        print(f"Port {port} is {status}")

if __name__ == "__main__":
    try:
        # Check for command line arguments
        if len(sys.argv) < 2:
            raise IndexError

        target = sys.argv[1]
        if not is_valid_ip(target):
            raise ValueError("Invalid IP address format")

        # Prompt the user for port range
        port_range = input("Enter port range to scan (e.g., 20-80): ")

        # Extract start and end ports
        try:
            start_port, end_port = map(int, port_range.split('-'))
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                raise ValueError("Invalid port range")
        except ValueError:
            raise ValueError("Invalid port range format")

        print_banner()
        print(f"Scanning target: {target}")
        print(f"Scanning ports {start_port} to {end_port}...\n")

        thread_scan(target, start_port, end_port)

    except IndexError:
        print("Usage: python port_scanner.py <target_ip>")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")
