import mincemeat
import md5
import hashlib
import sys

givenHash = sys.argv[1]
#generating passwords
def passwordList(length, allowedCharacters):
	r = []
  	if (length == 1):
  		return list(allowedCharacters)
  	else:
  		substring = passwordList(length-1, allowedCharacters)
  		for c in allowedCharacters:
  			for s in substring:
  				r.append(str(c) + str(s))
  	return r

allowedCharacters = "abcdefghijklmnopqrstuvwxyz0123456789"

k=[]

for i in range(1, 5):
	allPossiblePasswords =[]
	allPossiblePasswords = passwordList(i,allowedCharacters)
	for j in range(len(allPossiblePasswords)):
		k.append(allPossiblePasswords[j])
    
temp = []
temp.append(givenHash)
data =[]
count = 1
for word in k:
  temp.append(word)
  if count % 4444 == 0:
    data.append(temp)
    temp = []
    temp.append(givenHash)	
  count += 1
if temp != []:
   data.append(temp)

datasource = dict(enumerate(data))
def mapfn(k, v):
    import md5, hashlib
    for value in v:
    	#printing all passwords that are being checked on server 
    	print (hashlib.md5(value).hexdigest()[:5])
        if (v[0]) == (hashlib.md5(str(value)).hexdigest()[:5]):
          # print value
          yield value, 1

def reducefn(k, vs):
    return list(set(vs))
    #remove redudant values 

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

#printng all matched passwords
print "Passwords found:"
for k in results.keys():
	print str(k)