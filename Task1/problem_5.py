def is_palindrome(word):
    n = int(len(word))
    for i in range(0,n//2):
        if word[i] != word[n-i-1] :
            return False
    return True
word = input().split()
result= is_palindrome(word) 
if (result):
    print("The word ",word,"is palindrome")
else:
    print("The word ",word,"is not palindrome")       