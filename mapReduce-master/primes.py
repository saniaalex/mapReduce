import mincemeat
import sys

datasource = dict(enumerate(range(2,10000001)))

def mapfn(k,v):
	number=v
	if (str(number)==str(number)[::-1]):
		yield "number",int(number)
	
				
def reducefn(k,vs):
	a=[]
	for i in vs:
		x=0
		for j in range(2,int((i**0.5)+1)):
			if i%j==0:
				x=x+1
		if x==0:
			a.append(i)
	return a

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
reslist=[]
for k in results.keys():
	reslist=results[k]

print(reslist)
print "Length is:"
print len(reslist)
print "Sum is:"
print sum(reslist)

	
	
	