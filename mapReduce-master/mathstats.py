import mincemeat
import sys


file= open(sys.argv[1],'r')
data=list(file)
file.close

datasource=dict(enumerate(data))


def mapfn(k,v):
    
	for num in v.split():
		number=num.strip()
		yield "number",int(number)
	
def reducefn(k,vs):
	import math
	result={'sum':0,'count':0,'sd':0}
	result['sum']=sum(vs)
	result['count']=len(vs)
	mean=result['sum']/result['count']
	sigma=0
	for i in vs:
		numer=i-mean
		sigma=sigma+(numer*numer)
		
	
	res=sigma/result['count']
	result['sd']=math.sqrt(res)
	
	return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")


for k in results.keys():
	print str(results[k])
	
	
	