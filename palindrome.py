def check(word):
    left = []
    right = []
    if len(word) % 2==0:
        l=len(word)
        h =int(l/2)
        left = word[0:h]
        right = word[h:l+1]
        right = right[::-1]
    else:
        l=len(word)-1
        h =int(l/2)
        left = word[0:h]
        right = word[h+1:l+1]
        right = right[::-1]
    count = 0
    for i in range(h):
        if right[i] != left[i]:
            count +=1
    if count == -1:
       print(0,0)  
    else:
        mul = 1
        for i in range(count):
            mul = mul *2
            mul = mul%(10**9+7)
        print(count,mul)


word = input()
check(word)