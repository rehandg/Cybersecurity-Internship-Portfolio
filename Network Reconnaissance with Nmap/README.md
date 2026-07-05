Task-1: Scanning for open Ports
Doing a TCP scan on my own ip address
step-1: First check your system's IP on CMD using (ipconfig)
after that note your IP and check the range
step 2: Now Open Nmap on CMD or Zenmap(GUI) and enter the command nmap -sS 192.168.x.x/24 here make sure you write the range 0/24
step 3: Now scan will start and all the ports of your sytem will be listed 
PORT     STATE  SERVICE
80/tcp   open   http
443/tcp  open   https
1900/tcp open   upnp
2869/tcp closed icslap
7443/tcp open   oracleas-https
8002/tcp closed teradataordbms
8080/tcp open   http-proxy
8200/tcp closed trivnet1
8443/tcp open   https-alt

these were the open/closed ports on my system , you can also check for any malicious activity on you sytem

PART 2(OPTIONAL):WireShark packet Tracing
step-1: Open wireshark , click your network option to do the monitoring WIFI/EHTERNET and then click the BLUE SHARK FIN icon on top left
now the packet tracing has started and now you will get results with TCP (from nmap scanning)
this are some packets i captured:
50852	158.289668	192.168.29.42	192.168.1.39	TCP	58	35631 → 443 [SYN] Seq=0 Win=1024 Len=0 MSS=1460
50853	158.290322	192.168.29.42	192.168.1.51	TCP	58	35629 → 443 [SYN] Seq=0 Win=1024 Len=0 MSS=1460
50862	158.309672	192.168.29.42	192.168.1.56	TCP	58	35629 → 443 [SYN] Seq=0 Win=1024 Len=0 MSS=1460
note:these are the packets of NMAP's scan request.
SCREENSHOTS and TEXTFILES ARE UPLOADED IN REPOSITORY
