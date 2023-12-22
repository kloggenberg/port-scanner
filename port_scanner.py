import socket
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
    sock.settimeout(1)
    
    try:
        sock.connect((target,port))
        print(f"Port {port} is OPEN")
    except:
        print(f"Port {port} is Closed")
    finally:
        sock.close()


if __name__ == "__main__":
    print_banner()