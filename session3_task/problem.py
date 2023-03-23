# user=input("sentence? ")
# a=user.split()
# print(len(a))

# num=input("number? ")
# idx=0
# while idx < len(num) // 2:
#     if num[idx] != num[-idx-1]:
#         print('no')
#         break
#     idx += 1
    
# if idx==len(num)//2:
#     print('yes')


# w="to be or not to be, that is the question."
# l=w.replace(".","")
# l=l.replace(",","")
# a=l.split()
# dic1=dict()
# for i in a:
#     if i in dic1:
#         dic1[i] += 1
#     else:
#         dic1[i] = 1
# print (dic1)

repeat=int(input("input: "))
for i in range(repeat):
    sen=input().split()
    for i in sen:
        print(i[::-1], end = " ")
    print()
    
# n="i am happy"
# print(n[::-1])
    



