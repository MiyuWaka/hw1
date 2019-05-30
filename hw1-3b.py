#Adapt that program to find anagrams that use only a subset of characters
#上のプログラムを与えられた文字の一部しか入っていない文字の単語も作れるプログラムに変更してみてください。
#Feel free to experiment in ways to do that faster!
#より速い工夫もぜひ試してみてください。

import itertools

list_o = input().rstrip().split()

list_o = [str.lower() for str in list_o]         #リスト中の文字列を大文字→小文字に変換

newlist = []

for i in range(1,len(list_o)+1):
        list_1 = list(itertools.combinations(list_o,i))
        newlist = list_1 + newlist

newlist = [list(x) for x in newlist]

#print(newlist)

f = open("MyDictionary.txt")
lines = f.readlines()
f.close()

y = ""
dictionary = {}

for i in lines:
        i = i.rstrip("\\\n")
        v_list = list(i.lower())
        v_list.sort()
        for m in v_list:
                y += m
        dictionary[i] = y
        y = ""

#print(dictionary)


for i in newlist:
        x = ''.join(sorted(i))
        #print(x)
        for j in dictionary:
                if x == dictionary[j]:
                        print(j)
        