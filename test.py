a = [1,1,1,1,26,26,3,10,5,21,7, 22,20,24,100, 100]
sublists = [0,0,0,0]
b = []
DR = 0.1
N = len(sublists)
while len(sublists) > (sum(a) / max(a)):
	b.append(max(a))
	a.pop(a.index(max(a)))
print(b)
a.sort()
a.reverse()
arevageA = float(sum(a) / N)
arevageUp = arevageA  * (1 + DR)
arevageDown = arevageA * (1 - DR)
for x in range(0,len(sublists)):
	sublists[x] = []
	
c = []
for x in a:
	for index,y in enumerate(sublists):
		if  (sum(y) + x) <= arevageA:
			y.append(x)
			break
		else:
			if index == 3:
				c.append(x)
				# y.append(x)
			
print(c)
print(arevageDown, arevageA, arevageUp)
print(sum(a))
print(a)
print(sublists)
for x in sublists:
	print(sum(x))
	
