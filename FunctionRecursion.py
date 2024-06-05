#Print 1-50 using recursive function
def numbers(n):
    if n<=50:
        print(n)
        numbers(n+1)
numbers(1)

# Print 50-1 using recursive function
def numbers(n):
    if n<=50:
        numbers(n+1)
        print(n)
numbers(1)