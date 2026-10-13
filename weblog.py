import re
from collections import Counter

pattern = r'(\S+) - - \[.*?\] "(\S+) (\S+) [^"]*" (\d+) \S+ ".*?" "([^"]*)"'

ip_counts = Counter()
path_counts = Counter()
status_counts = Counter()
scanner  = Counter ()
notfound_by_ip = Counter()

scanner_names = ["sqlmap", "nikto", "nmap", "masscan", "hydra"]

with open ("access.log") as f:
	for line in f:
		match = re.search(pattern, line)
		if match:
			ip = match.group(1)
			path = match.group(3)
			status = match.group(4)
			agent = match.group(5)

			ip_counts[ip] += 1
			path_counts[path] += 1
			status_counts[status] += 1

			for name in scanner_names:
				if name in agent.lower():
					scanner[agent] += 1

					if status == "404":
						notfound_by_ip[ip] += 1

print("Top IPs:")
for ip, n in ip_counts.most_common(10):
	print(" ", ip, n)

print("\nTop Paths:")
for path, n in path_counts.most_common(10):
	print(" ", path, n)

print("\nStatus Codes:")
for status, n in status_counts.most_common():
	print(" ", status,"Times:", n)

print("\nScanners Detected:")
for agent, n in scanner.most_common():
	print(" ", agent, n)

print("\nIPs with many 404s (possible probing):")
THRESHOLD_404 = 3
for ip, n in notfound_by_ip.most_common():
	if n >= THRESHOLD_404:
		print(" ", ip, "->", n, "not-found requests")
