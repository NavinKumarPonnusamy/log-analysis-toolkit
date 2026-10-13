from scapy.all import rdpcap, IP, DNS
from collections import defaultdict

packets = rdpcap("dns_capture.pcap")

queries = defaultdict(list)

for pkt in packets:
	if pkt.haslayer(DNS) and pkt.haslayer(IP):
		if pkt[DNS].qr == 0:
			src_ip = pkt[IP].src
			timestamp = float(pkt.time)
			queries[src_ip].append(timestamp)

THRESHOLD = 50
WINDOW = 10

for ip, times in queries.items():
	times.sort()
	for start in range(len(times) - THRESHOLD + 1):
		first = times[start]
		last = times[start + THRESHOLD + 1]
		gap = last - first
		if gap <= WINDOW:
			print(ip, "-possible DNS recon:", THRESHOLD, "queries in", round(gap, 1), "seconds")
			break 


