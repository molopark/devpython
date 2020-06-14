f = open("t.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
f = open("t.txt","r")
pp = f.read()
print(pp)
f.close()
