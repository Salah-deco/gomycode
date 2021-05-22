# difine list
res = []
for x in range(2000,3201):
    if(x%7 & (not x%5) ):
        res.append(x)

print(res)
