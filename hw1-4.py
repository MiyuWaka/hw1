#Try optimizing your choice of anagrams to find the highest scoring one, rather than just the longest one.
#最も長い単語ではなく、一番点数が高い単語を計算するように工夫
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
score = 0
score_d = []


for i in newlist:
        x = ''.join(sorted(i))
        #print(x)
        for j in dictionary:
                if x == dictionary[j]:
                        for m in i:
                                if m == "j" or "k" or "q" or "x" or "z":
                                        score = score + 3
                                elif m == "c" or "f" or "h" or "l" or "m" or "p" or "v" or "w" or "y":
                                        score = score + 2
                                else:
                                        score = score + 1 
                        score_d.append([j,(score + 1) * (score + 1)])
                        score = 0


score_d.sort(key=lambda x:-x[1])

for i in score_d:
        print(i[0])    