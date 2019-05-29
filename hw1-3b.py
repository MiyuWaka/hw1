#Adapt that program to find anagrams that use only a subset of characters
#上のプログラムを与えられた文字の一部しか入っていない文字の単語も作れるプログラムに変更してみてください。
#Feel free to experiment in ways to do that faster!
#より速い工夫もぜひ試してみてください。

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
        if y in x:
                print(i)
        y = ""
