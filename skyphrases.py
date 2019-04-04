def skyphrases(text):
    tab = text.split()
    x=True
    for i in tab:
        z = tab.count(i)
        if z==1:
            x=True
        else:
            x=False
    return x

file = open("skyphrases.txt", "r+")
tab = file.readlines()
x=0
for i in tab:
    z = skyphrases(i)
    if z == True:
        x=x+1
    else:
        pass
print(x)
