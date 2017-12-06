import re,math
r838 = re.compile('838 .+')
r1024 = re.compile('1024 .+')
counts = {}
counts838 = {}
Class = {}
mu = {}
sigma = {}
with open('train_faces_clean.arff') as f:
    c = f.readlines()
data = c[1029:]
total=0.0
for d in data:
    d = d.split(',')
    
    d838 = filter(lambda x: re.match(r838,x),d)
    d1024 = filter(lambda x: re.match(r1024,x),d)[0].split()[1]
    if d838 != []:
        d838 = d838[0].split()[1]
        counts838[d838] = counts838.get(d838,0) + 1
        if d1024 in counts:
                counts[d1024].append(float(d838))
        else: counts[d1024] = [float(d838)]
    Class[d1024] = Class.get(d1024,0) + 1
    total += 1.0
for k in counts:
     mu[k] = sum(counts[k]) / len(counts[k])
     print counts[k],mu[k]
     sigma[k] = sum(map(lambda x: pow(x - mu[k],2),counts[k])) / len(counts[k])
     print mu[k],sigma[k]
     exit()
exit()
pCg8 = {}
for i in range(1,11):
    i = str(i)
    pCg8[i] = []
    for k in counts838:
        try: num = counts[i][counts[i].index(k)+1]
        except: num = 0
        den = float(counts838[k])
        p = num/den
        pCg8[i] += [p]

eClass8 = []
e = 0.0

eClass = 0.0
print total
for k in Class:
    p = Class[k]/total
    eClass -= p * math.log(p,2)
print eClass / math.log(len(Class),2)
exit()
