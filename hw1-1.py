#Make a program that can find single word anagrams that use all the characters in a given string (e.g. “omnsotare” -> “astronomer”)
#与えられた文字が全て入っている単語を作るプログラムを作ってみてください。

list_1 = input().rstrip().split()

list_1 = [str.lower() for str in list_1]
x = ''.join(sorted(list_1))

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
