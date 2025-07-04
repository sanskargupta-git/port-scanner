# 🔍 Port Scanner

A simple, fast, multi-threaded port scanner written in Python. This tool scans the most common ports (1–1024) and reports open ones.

## 🚀 Features

- Scans ports 1 to 1024
- Uses multi-threading for high speed
- Built with Python `socket` and `threading`
- Clean, minimal CLI output

## 💡 How It Works

- Creates a socket connection to each port on the target IP
- If the port is open, it reports it
- Uses one thread per port for faster scanning

## 🖥️ Usage

```bash
$ python port_scanner.py
Enter target IP: scanme.nmap.org
[+] Port 22 is OPEN
[+] Port 80 is OPEN
