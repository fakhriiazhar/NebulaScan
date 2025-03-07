import socket
import threading
import pyfiglet
import ipaddress
import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

ascii_banner = f"""
{Fore.RED}
███╗   ██╗███████╗██████╗ ██╗   ██╗██╗      █████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██╔════╝██╔══██╗██║   ██║██║     ██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║█████╗  ██████╔╝██║   ██║██║     ███████║    ███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██║     ██╔══██║    ╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║███████╗██████╔╝╚██████╔╝███████╗██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
Code by: fakhriiazhar
                           https://github.com/fakhriiazhar
"""
{Style.RESET_ALL}  
print(ascii_banner)

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        print(f"{Fore.RED}IP address tidak valid.")
        return False

def get_ip_address(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"{Fore.GREEN}IP address dari {hostname} adalah {ip}")
    except socket.gaierror:
        print(f"{Fore.RED}Hostname tidak valid atau tidak ditemukan.")

def scan_port(ip, port, results):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        result = f"{Fore.GREEN}Port {port} is open"
        print(result)
        results.append(result)
    except:
        result = f"{Fore.RED}Port {port} is closed"
        print(result)
        results.append(result)
    finally:
        scanner.close()

def scan_udp_port(ip, port, results):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    scanner.settimeout(1)
    try:
        scanner.sendto(b"Hello", (ip, port))
        scanner.recvfrom(1024)
        result = f"{Fore.GREEN}UDP Port {port} is open"
        print(result)
        results.append(result)
    except:
        result = f"{Fore.RED}UDP Port {port} is closed or filtered"
        print(result)
        results.append(result)
    finally:
        scanner.close()

def port_scanner(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 112, 143, 443, 445, 3306, 8080]
    threads = []
    results = []
    for port in common_ports:
        thread = threading.Thread(target=scan_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()
        time.sleep(0.05)

    for thread in threads:
        thread.join()

    with open("scan_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")
    print(f"{Fore.CYAN}Hasil scan disimpan di scan_results.txt")

def udp_scanner(ip):
    common_ports = [53, 67, 68, 69, 123, 161, 162]
    threads = []
    results = []
    for port in common_ports:
        thread = threading.Thread(target=scan_udp_port, args=(ip, port, results))
        threads.append(thread)
        thread.start()
        time.sleep(0.05)

    for thread in threads:
        thread.join()

    with open("udp_scan_results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")
    print(f"{Fore.CYAN}Hasil scan UDP disimpan di udp_scan_results.txt")

def check_waf(domain):
    try:
        response = requests.get(f"http://{domain}")
        headers = response.headers
        waf_signs = ["cloudflare", "sucuri", "akamai", "incapsula", "modsecurity", "amazon web", "fortiweb", "f5 big-ip", "imperva securesphere", "wallarm", "naxsi", "netsparker", "sqreen", 
                     "varnish", "webknight", "webseal", "yundun", "zenedge", "appwall", "denyall", "distil", "hyperguard", "mission control", "azure web application firewall", "barracuda waf", "binarysec", "bluedon ist", "citrix netscaler", "cloudbric", 
                     "comodo cwatch", "dotdefender", "ibm datapower", "juniper webapp secure", "kona sitedefender", "nsfocus", "pentawaf", "perimeterx", "qihoo 360", "radware appwall", "reblaze", "tencent waf", "trustwave modsecurity", "usp secure entry server", "webarx", "zscaler"]

        detected_waf = [waf for waf in waf_signs if waf in headers.get('Server', '').lower()]

        if detected_waf:
            print(f"{Fore.GREEN}{domain} kemungkinan menggunakan WAF: {', '.join(detected_waf)}")
        else:
            print(f"{Fore.YELLOW}{domain} tidak terdeteksi menggunakan WAF.")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Gagal mengakses {domain}: {e}")

def main():
    while True:
        print("Pilih fitur:")
        print("1. Cari alamat IP dari hostname")
        print("2. Scan port otomatis")
        print("3. Scan UDP port otomatis")
        print("4. Cek apakah domain menggunakan WAF")
        print("5. Keluar")

        choice = input("Masukkan pilihan: ")

        if choice == "1":
            hostname = input("Masukkan hostname: ")
            get_ip_address(hostname)
        elif choice == "2":
            ip = input("Masukkan IP target: ")
            if validate_ip(ip):
                port_scanner(ip)
        elif choice == "3":
            ip = input("Masukkan IP target: ")
            if validate_ip(ip):
                udp_scanner(ip)
        elif choice == "4":
            domain = input("Masukkan domain: ")
            check_waf(domain)
        elif choice == "5":
            print("Keluar dari program.")
            break
        else:
            print(f"{Fore.RED}Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
