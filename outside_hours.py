from datetime import datetime

with open ("auth.log") as f:
	for line in f:
		if "Accepted" in line:
			words = line.split()
			timestamp_text = words[0]+ " " + words[1]+ " " + words[2]
			t = datetime.strptime("2026 " + timestamp_text, "%Y %b %d %H:%M:%S")
		
			if t.weekday() >= 5:
				print(t, "- Outside Hours: Weekend")
			elif t.hour < 9 or t.hour >=18:
				print(t,"- Outside Hours: Night")
			else:
				print(t, "- Inside Working Hours")
