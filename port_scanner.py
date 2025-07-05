import socket
import threading
import argparse

# Lock for synchronized printing in threads
print_lock = threading.Lock()
open_ports = []

# Scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))
        with print_lock:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
    except:
        pass
    finally:
        sock.close()

# Main function with argument parsing
def main():
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("-o", "--output", help="File to save open ports")

    args = parser.parse_args()

    print(f"\n🔍 Scanning {args.ip} from port {args.start} to {args.end}...\n")

    threads = []
    for port in range(args.start, args.end + 1):
        t = threading.Thread(target=scan_port, args=(args.ip, port))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    if args.output:
        with open(args.output, "w") as f:
            for port in open_ports:
                f.write(f"Port {port} is OPEN\n")
        print(f"\n✅ Results saved to {args.output}")

if __name__ == "__main__":
    main()
