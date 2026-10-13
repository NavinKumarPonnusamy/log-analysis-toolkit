from datetime import datetime
from collections import defaultdict

fails = defaultdict(list)
threshold = 20
window = 120

with open ("auth.log") as f:
	for line in f:
		if "Failed password" in line:
			words = line.split()
			i = words.index("from")
			ip = words[i+1]

			timestamp_text = words[0] + " " + words[1] + " " + words[2]
			t = datetime.strptime("2026 " + timestamp_text, "%Y %b %d %H:%M:%S")

			fails[ip].append(t)

for ip, times  in fails.items():
	times.sort()

	for start in range (len(times) - threshold + 1):
		first = times[start]
		last = times[start + threshold - 1]
		gap = (last - first).total_seconds()

		if gap <= window:
			print(ip, "-Possible Brute Force:", threshold, "Failures in", int(gap), "Seconds")
			break
