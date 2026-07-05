import tkinter as tk
import json

def add_ip():
    ip = ip_entry.get()
    if ip:
        rules["block_ips"].append(ip)
        save_rules()
        log_box.insert(tk.END, f"Added IP to block list: {ip}\n")

def add_port():
    port = port_entry.get()
    if port.isdigit():
        rules["block_ports"].append(int(port))
        save_rules()
        log_box.insert(tk.END, f"Added Port to block list: {port}\n")

def save_rules():
    with open("rules.json", "w") as f:
        json.dump(rules, f, indent=2)

with open("rules.json", "r") as f:
    rules = json.load(f)

root = tk.Tk()
root.title("Firewall Rule Manager")

log_box = tk.Text(root, height=15, width=60)
log_box.pack()

ip_frame = tk.Frame(root)
ip_frame.pack()
ip_label = tk.Label(ip_frame, text="Block IP:")
ip_label.pack(side=tk.LEFT)
ip_entry = tk.Entry(ip_frame)
ip_entry.pack(side=tk.LEFT)
ip_button = tk.Button(ip_frame, text="Add", command=add_ip)
ip_button.pack(side=tk.LEFT)

port_frame = tk.Frame(root)
port_frame.pack()
port_label = tk.Label(port_frame, text="Block Port:")
port_label.pack(side=tk.LEFT)
port_entry = tk.Entry(port_frame)
port_entry.pack(side=tk.LEFT)
port_button = tk.Button(port_frame, text="Add", command=add_port)
port_button.pack(side=tk.LEFT)

root.mainloop()

