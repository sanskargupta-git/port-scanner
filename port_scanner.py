import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
    except:
        pass  # Silently ignore closed ports
    finally:
        sock.close()

# Main program
def main():
    target_ip = input("Enter target IP: ")

    print(f"\nScanning {target_ip} from port 1 to 1024...\n")

    # Loop through ports 1 to 1024
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        t.start()

if __name__ == "__main__":
    main()
