from collections import Counter

user_counts = Counter()
ip_counts = Counter()

with open("auth.log") as f:
	for line in f:
		if "Failed password" in line:
			words = line.split()
			i = words.index("from")
			user = words[i-1]
			user_counts[user] += 1
			ip= words[i+1]
			ip_counts[ip] += 1

print("Username Tried:")
for user , n in user_counts.most_common():
	print(user, n)
print()
print("Attempts per IP")
for ip, n in ip_counts.most_common():
	print(ip, n)

