from scapy.all import IP, UDP, DNS, DNSQR, wrpcap

packets = []

base_time = 1000000.0
for n in range(60):
	pkt = IP(src="10.0.0.99", dst="8.8.8.8") / \
		UDP(sport=50000, dport=53) / \
		DNS(rd=1, qr=0, qd=DNSQR (qname="example.com"))
	pkt.time = base_time + (n * 0.1)
	packets.append(pkt)

wrpcap("fake_dns.pcap", packets)
print("Wrote", len(packets), "packets to fake_dns.pcap")
