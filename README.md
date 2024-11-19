# Port Scanner 9000

Port Scanner 9000 is a simple multi-threaded port scanner that scans a specified range of ports on a target IP address. It identifies whether each port is open or closed and attempts to grab banners from open ports to provide additional information about running services.

## Features

- Multi-threaded scanning for faster performance
- User-friendly ASCII art banner
- Validates IP addresses and port ranges
- Scans ports in a specified range and outputs results in numerical order
- **NEW:** Banner grabbing for open ports to identify running services

## Requirements

- Python 3.x
- `pyfiglet` module

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/port-scanner-9000.git
    ```

2. Change to the project directory:

    ```sh
    cd port-scanner-9000
    ```

3. Install the required module:

    ```sh
    pip install pyfiglet
    ```

## Usage

1. Run the script with the target IP as an argument:

    ```sh
    python port_scanner.py <target_ip>
    ```

    Example:

    ```sh
    python port_scanner.py 192.168.1.1
    ```

2. Optionally, specify the port range and timeout:

    ```sh
    python port_scanner.py 192.168.1.1 -p 20-100 -t 1
    ```

3. The script will scan the specified range of ports, output the results in numerical order, and display any retrieved banners for open ports.

## Example Output

```sh
----------------------------------------------------------------------------------------------------
  ____             _     ____                                
 |  _ \ ___   ___ | |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_) / _ \ / _ \| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 |  __/ (_) | (_) | |_   ___) | (_| (_| | | | | | | |  __/ |   
 |_|   \___/ \___/ \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                        
----------------------------------------------------------------------------------------------------
Scanning target: 192.168.1.1
Scanning ports 20 to 25...

Port 20 is CLOSED
Port 21 is OPEN. Banner: 220 FTP Server ready.
Port 22 is OPEN. Banner: SSH-2.0-OpenSSH_7.9
Port 23 is CLOSED
Port 24 is CLOSED
Port 25 is OPEN. Banner: 220 smtp.example.com ESMTP Postfix
