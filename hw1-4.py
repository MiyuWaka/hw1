#Try optimizing your choice of anagrams to find the highest scoring one, rather than just the longest one.
#最も長い単語ではなく、一番点数が高い単語を計算するように工夫

list_1 = input().rstrip().split()
list_1.sort()

x = ""

for i in list_1:
    x += i

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
    if y in x:
        print(i)
    y = ""
