import json
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

# Load rules from JSON file
with open("rules.json", "r") as file:
    rules = json.load(file)

def log_packet(packet, reason):
    with open("firewall_log.txt", "a") as log:
        log.write(f"[{datetime.now()}] [{reason}] {packet.summary()}\n")
    print(f"[LOGGED] {reason}: {packet.summary()}")

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        if ip_layer.src in rules["block_ips"] or ip_layer.dst in rules["block_ips"]:
            log_packet(packet, "Blocked IP")
            return

    if TCP in packet or UDP in packet:
        layer = packet[TCP] if TCP in packet else packet[UDP]
        if layer.sport in rules["block_ports"] or layer.dport in rules["block_ports"]:
            log_packet(packet, "Blocked Port")
            return

    if ICMP in packet and "ICMP" in rules["block_protocols"]:
        log_packet(packet, "Blocked Protocol")
        return

    print(f"[ALLOWED] {packet.summary()}")

print("[INFO] Firewall is running...")
sniff(prn=packet_callback, store=0)

