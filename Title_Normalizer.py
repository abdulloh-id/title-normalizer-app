txt = "no time to die"
S = txt.split()
print(S)

max_el = len(S)

print(max_el)

for i in range(0, max_el):
	S[i] = S[i].capitalize()

S = ' '.join(S)
print(S)

