import scapy.all as scapy

def scan(ip):
    #scapy.arping(ip) #This will used to get the list of connectted devices to your network
    #print(arp_request.summary()) # This line will print the summary of the arp_request 
    #scapy.ls(scapy.ARP()) # This line will list the option which are available inside the ARP()
    arp_request = scapy.ARP(pdst=ip) 
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # this  line is used to set the destination mac to the broadcast mac
    arp_request_broadcast = broadcast/arp_request # the scapy provide the "/"  to combine the two packets line arp reqquest and broadcast request. 
    #arp_request_broadcast.show() # this line will print the ether and arp packet 
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1) 
    print(unanswered.summary())

scan("10.0.2.1/24")
