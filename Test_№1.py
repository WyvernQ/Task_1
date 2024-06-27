#import time


#def count_sym(line):
    #for sym in set(line):
        #counter = 0
        #for sub_sym in line:
            #if sym == sub_sym:
                #counter += 1
        #print(sym, counter)

#start = time.time()

#count_sym('abcdefg' * 100)
#end = time.time()

#print('Время выполнения программы:', end - start)


#slovo = str(input())
#x = len(slovo)
#i = 0
#x = x - 1
#k = 0
#while x - i>=i:
    #if slovo[x - i] == slovo[i]:
        #i += 1
    #else:
        #k = 1
        #break
#if k == 1:
  #print("False")
#else:
  #print("True")





#def palindrome(s: str):
    #snew = s.replace(" ", "").lower()
    #ls = len(snew)
    #if snew[:ls // 2] == snew[ls // 2 + 1:][::-1]:
        #return("Палиндром")
    #return("Не палиндром")

#palindrome(s: 'helloworld')


#class Solution:
    #def twoSum(self, nums: list[int], target: int) -> list[int]:
        #deltas = {}
        #for i, num in enumerate(nums):
            #if num in deltas:
                #return deltas[num], i
            #delta = target - num
            #deltas[delta] = i
    

#def f(x, y):
    #if x == y:
        #return 1
    #if x > y:
        #return 0
    #return f(x + 2, y)+f(x * 5, y)
#print(f(2, 50))

import time

start = time.time()

for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (y + 2*x < a) or (x > 30) or (y > 20):
                k += 1
    if k == 90000:
        print(a)
        break

end = time.time()
print('Время выполнения программы:', end - start)