#与えられた文字が全て入っている単語を作るプログラムを作ってみてください。

list_1 = input().rstrip().split()
#print(list_1)   
list_1.sort()
#print(list_1)

x = ""

for i in list_1:
    x += i

#print(x)

f = open("MyDictionary.txt")
lines = f.readlines()
f.close()

y = ""

for i in lines:
    i = i.rstrip("\\\n")
    v_list = list(i.lower())
    v_list.sort()
    for j in v_list:
        y += j
        if x == y:
            print(i)
    y = ""
