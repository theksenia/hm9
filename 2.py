with open("Random.txt", 'r') as f:
    data = f.read()
res = [int(i) for i in data.split()]
n = []
for p in res:
    n.append(p**2)


with open("Random.txt", 'a') as f:
    for d in range(0,1010,10):
        f.write(str(n[d-10:d])+"\n")





#f.write(str(n[d-10:d])+"\n")



