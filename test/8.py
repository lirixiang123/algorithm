
s = "PPPPPGPPMP"
m = []
num = 0
for i in range(len(s)):

    if s[i] == "P":
        if s[i-1] == "P" and s[i-2] == "P" and s[i-3] == "P":
            num += 250
        else:
            num += 200

    elif s[i] == "G":
        num += 100

    elif s[i] == "M":
        m.append(s[i])
        num += 0
        if len(m) == 3:
            num = 0

print(num)