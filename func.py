#palindrome with function concept
def palin(word):
    if word[::-1]==word:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")

palin("madam")
palin("abhi")
