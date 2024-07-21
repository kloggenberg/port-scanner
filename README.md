# Port Scanner 9000

Port Scanner 9000 is a simple multi-threaded port scanner that scans a specified range of ports on a target IP address. The scanner outputs whether each port is open or closed.

## Features

- Multi-threaded scanning for faster performance
- User-friendly ASCII art banner
- Validates IP addresses and port ranges
- Scans ports in a specified range and outputs results in numerical order

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

2. When prompted, enter the range of ports to be scanned in the format `start-end`:

    ```sh
    Enter port range to scan (e.g., 20-80): 630-640
    ```

3. The script will scan the specified range of ports and output the results in numerical order.

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
Scanning ports 630 to 640...

Port 630 is CLOSED
Port 631 is CLOSED
Port 632 is CLOSED
Port 633 is CLOSED
