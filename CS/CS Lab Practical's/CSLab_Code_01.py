from scapy.all import sniff, Ether, ARP, IP, TCP, UDP

def packet_handler(packet):
    if Ether in packet:
        print("Ethernet Frame:")
        print(f"Source MAC: {packet[Ether].src}, Destination MAC: {packet[Ether].dst}")

    if ARP in packet:
        print("\nARP Packet:")
        print(f"Source MAC: {packet[ARP].hwsrc}, Source IP: {packet[ARP].psrc}")
        print(f"Destination MAC: {packet[ARP].hwdst}, Destination IP: {packet[ARP].pdst}")

    if IP in packet:
        print("\nIP Packet:")
        print(f"Source IP: {packet[IP].src}, Destination IP: {packet[IP].dst}")

    if TCP in packet:
        print("\nTCP Segment:")
        print(f"Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")

    if UDP in packet:
        print("\nUDP Datagram:")
        print(f"Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")


sniff(iface='enp1s0', prn=packet_handler, store=0)


  #pip install scapy OR sudo apt-get install python3-scapy : Install Scapy
  #ifconfig : Check for network interfacev card - eth0
  #python3 packet_sniffer.py : locate directory and run script
  #sudo python3 packet_sniffer.py : For sudo priviledge
  #save file as : packet_sniffer.py
  #python --version (Check Python Installed or not in Linux)
  #sudo apt-get update , sudo apt-get install python3 - Install Python on Ubuntu
  #More about: https://www.geeksforgeeks.org/packet-sniffing-using-scapy/
  #Install Wireshark to anyalize packets
  #sudo apt install python3-pip

