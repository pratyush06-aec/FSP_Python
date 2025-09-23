f= [1]
[f.append(f[-1]*i) for i in range(1, 6)]
print(f[-1])