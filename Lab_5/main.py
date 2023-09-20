#A recursive function called reverse_word which takes in a string and returns the string
#backwards (so if the inputted string was hello, this method would return olleh.
#A function named palindrome_check which returns true if the String parameter is a palindrome
#(A palindrome is a word, phrase, or sentence that reads the same forward and backward, such as:
#noon, racecar, desserts I stressed. You will need to Handle odd-length and even-length palindromes.)

def reverse_word(word):
    if len(word) == 0:
        return
    else:
        l.append(word[-1])
        word = word.rstrip(word[-1])
        reverse_word(word)
    return ''.join(l)

def palidrome_check(w):
    if w.lower() == w.lower()[::-1]:
        print(w + ' is a palindrome')
    else:
        print(w + ' is not a palindrome')

def sumOfnum(num):
    if num == 0:
        return 0
    else:
        return num + sumOfnum(num - 1)

def findMax(list):
    if len(list) == 0:
        pass

    elif list[0] > list[-1]:
        list.remove(list[-1])
        findMax(list)

    elif list[-1] > list[0]:
        list.remove(list[0])
        findMax(list)

    return str(list[0])

def multiplication(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiplication(x,y - 1)

def line(n):
    if n < 0:
        return
    else:
        for i in range(n):
            print (i + 1, end = ' ')
        print('\r')
        line(n-1)

l = []

print(reverse_word('run'))
palidrome_check('run')

line(7)
print(findMax([2,5,20,2,3,6]))

print(sumOfnum(3))

print(multiplication(4,7))
