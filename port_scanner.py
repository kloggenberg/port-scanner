import re
import socket
import sys
from pyfiglet import Figlet

def print_banner():
    TEXT = "Port Scanner 9000"
    # Create a Figlet object
    fig = Figlet()

    # Use the Figlet object to convert text to ASCII art
    ascii_art = fig.renderText(TEXT)

    # Print the ASCII art
    print("-"*100)
    print(ascii_art)
    print("-"*100)
    
    
def scan_port(target,port):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    
    try:
        sock.connect((target,port))
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is Closed")
    finally:
        sock.close()


def is_valid_ip(ip_str):
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

    if ip_pattern.match(ip_str):
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        target = "120.0.0.1"
        # target = sys.argv[1]
        print_banner()
        if target != "":
            for port in range(630,641):
                scan_port(target,port)
        else:
            print("Please enter a target IP address")
    except IndexError:
        print("No target IP address given")