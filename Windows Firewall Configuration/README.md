# TASK-4:WindowsFirewall
# Windows Firewall Configuration - Basic Security Task
 Task Objective

To configure and test **basic firewall rules** on a Windows system using *Windows Defender Firewall*, demonstrating control over network traffic by blocking and allowing specific ports and services.



#Tools Used


*Windows Defender Firewall with Advanced Security**



#Task Breakdown

1. View Current Firewall Rules

Open Windows Defender Firewall from the Start Menu and check both Inbound and Outbound rules to see the existing configurations.



2. Block Inbound Traffic on Port 23 (Telnet)

Create a new Inbound Rule, set it to block TCP traffic on port 23, and apply it to all profiles. Name the rule appropriately. A screenshot will be included showing this rule.



 3. Test the Rule

Enable the Telnet client and attempt to connect using `telnet 127.0.0.1 23`. A screenshot of the failed connection will confirm the rule is working.



 4. (Optional for Linux) Allow SSH on Port 22

Create an inbound rule to allow TCP traffic on port 22, commonly used for SSH.



 5. Remove Test Rule

Delete the Telnet block rule from the Inbound Rules to restore normal operation.


# Bonus Rules for Security Hardening

1. Block ICMP Echo Requests (Ping)

Use a custom rule to block ICMP Echo Request traffic (Ping). A screenshot will show the rule and a blocked ping attempt.



2. Block RDP Access (Port 3389)

Create a rule that blocks TCP traffic on port 3389 to prevent unauthorized Remote Desktop access. A screenshot will show this rule.



3. Allow File Sharing Only on Local Subnet

Allow ports 137-139 and 445 but restrict access to only the local subnet in the scope settings. A screenshot will show this IP restriction.



# Summary: How Firewalls Filter Traffic

Firewalls inspect data packets based on criteria like IP, port, and protocol. Based on rules, they either **allow** or **block** the traffic. If no rule matches, the default behavior is applied. This ensures unauthorized or unexpected traffic can be filtered.

* **Inbound rules** control incoming traffic.
* **Outbound rules** control outgoing traffic.

Screenshots will be used to demonstrate the rule application and results.



#Screenshots to Include

* Failed Telnet connection

* Firewall interface showing applied rules



# Conclusion

This task highlights how Windows Firewall can be used to manage and secure network traffic through well-defined rules. The configuration steps and bonus rules show basic but effective ways to enhance system security.
