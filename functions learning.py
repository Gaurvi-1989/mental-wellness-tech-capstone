# def smallest(l):
#     m = l[0]
#     g= l[0]
#     for i in l[1:]:
#         if(m>i):
#             m=i
#         if(g<i):
#             g=i

#     return m,g


#question 1
# f=open('c:/users/mitan/Desktop/hello nitj.txt','r')
# ans=f.read()
# print(ans)
# f.close()

#question 2
# f=open('c:/users/mitan/Desktop/hello nitj.txt','r')
# n=int(input('how many lines to read'))
# for i in range(n):
#     i=f.readline()
#     print(i)
# f.close()

#question 3
# f=open('hello nitj.txt','a+')
# f.write("\nthis is the appended text")
# f.close()
# f=open('hello nitj.txt','r')
# text=f.read()
# print(text)
# f.close()

#question 4
# f=open('hello nitj.txt','r')
# n=int(input('how many lines to rrad from the end'))
# ans=f.readlines()
# for x in ans[-n:]:
#     print(x)
# f.close()

#question 5
# f=open('hello nitj.txt','r')
# l=f.read()
# f.close()
# print(l)
  
# question 6
# f=open('hello nitj.txt','r')
# l=f.readlines()
# print('number of lines=',len(l))
# f.close()

#question 7 
# f1=open('hello nitj.txt','r')
# f2=open('copied hello.txt', 'w')
# for i in f1:
#         f2.write(i)
# f1.close()
# f2.close()

# f2= open('copied hello.txt', 'r')
# a = f2.read()
# print(a)

#question 8
# with open("c:/users/mitan/Desktop/data.txt","rb") as file: 
#     contents = file.read()
# print(contents)

# f=open('c:/users/mitan/Desktop/data.txt', 'r')
# l=f.readline()
# f.seek(0)
# a=f.read()
# print(a)
# print(l)
# f.close()