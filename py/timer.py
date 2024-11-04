import time
m = 0
s = 0
t = input("Enter time limit: ")
while s < 60:
	print(m, ":", s)
	time.sleep(1)
	if s == 59:
		m += 1
		s = -1
	if m == int(t):
		break
	s += 1
print(f"Time elapsed: {t} minute")