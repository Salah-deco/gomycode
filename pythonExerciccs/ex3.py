dic = {}
def createDict(dic, x):
    for x in range(x+1):
        dic[x] = x*x

createDict(dic,8)
print(dic)
