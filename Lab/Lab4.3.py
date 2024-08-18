#Create a function that takes  word and check whether it is Palindrome or not
def check(word):
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Example usage
check("madam")
check("hello")
