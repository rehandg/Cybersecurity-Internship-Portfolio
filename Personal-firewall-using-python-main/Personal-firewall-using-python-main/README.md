# Personal-firewall-using-python
Personal Firewall using Python
Objective
Develop a lightweight personal firewall that filters network traffic based on customizable rules.

Tools Used
Python 3

Scapy (for packet sniffing)

iptables (optional, for system-level blocking)

Tkinter (optional, GUI)

JSON (for rule configuration)

Project Structure
graphql
Copy
Edit
personal_firewall/
├── firewall.py          # Main logic for packet sniffing and blocking
├── gui.py               # Optional Tkinter GUI for managing rules
├── rules.json           # Rule definitions (IPs, ports, protocols)
├── firewall_log.txt     # Log of blocked/suspicious packets
├── README.md            # This file
How to Run
1. Install Requirements
bash
Copy
Edit
pip install scapy
sudo apt install python3-tk  # (Ubuntu/Debian only)
2. Run the Firewall (Needs sudo)
bash
Copy
Edit
sudo python3 firewall.py
3. Run the GUI (Optional)
bash
Copy
Edit
python3 gui.py
The GUI updates the rules.json file dynamically. No need to restart the firewall to apply changes.

Rule Format (rules.json)
json
Copy
Edit
{
  "block_ips": ["192.168.1.100"],
  "block_ports": [23, 445],
  "block_protocols": ["ICMP"]
}
You can manually edit this file or use the GUI to modify it.

Log File
All blocked or suspicious packets are saved in firewall_log.txt with timestamp and reason.

Features
 Sniff incoming/outgoing packets

 Block traffic based on rules (IP, port, protocol)

 Log suspicious packets

 Optional GUI to manage rules

 Optional iptables integration (future)

Author
Built as a mini security tool using Python and Scapy.

Disclaimer
This firewall is for educational use. It should not be used as a substitute for professional firewall software in production environments.
