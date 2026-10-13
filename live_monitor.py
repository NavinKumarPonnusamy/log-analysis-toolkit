import time

logfile = "/var/log/nginx/access.log"

with open(logfile) as f:
	f.seek(0, 2)
	print("Watching", logfile, "...(Ctrl+C to stop)")

	while True:
		line = f.readline()
		if not line:
			time.sleep(0.5)
			continue
		print("NEW:", line.strip())

