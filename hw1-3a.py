#Adapt that program to find anagrams that use only a subset of characters
#与えられた文字の一部しか入っていない文字の単語も作れるプログラムに変更
#The way that I described of trying all 2^16 possible subsets will work.
#このスライドで提案した「2^16通りの全ての組み合わせを試す」方法でも大丈夫です。

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



for i in newlist:
        x = ''.join(sorted(i))
        #print(x)
        for j in lines:
                j = j.rstrip("\\\n")
                v_list = list(j.lower())
                v_list.sort()
                for m in v_list:
                        y += m
                if y == x:
                        print(j)
                y = ""
