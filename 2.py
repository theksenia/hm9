def filecub(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    res = [int(i) for i in data.split()]
    n = []
    for p in res:
        n.append(p ** 2)
    with open(file_name, 'a') as f:
        for d in range(0, 1010, 10):
            f.write(str(n[d - 10:d]) + "\n")
    return d


print(filecub("Random.txt"))









