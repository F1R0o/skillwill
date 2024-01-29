dictionary = {
    "luka": 2,
    "saba": 4,
    "giorgi": 5,
    "lasha": 6
}

def gamotvla(x):
    minumaluri =    None
    
    for i in dictionary:
        key = dictionary[i]
        if minumaluri is None or key < minumaluri:
            minumaluri = key
    
    return f"minumaluri ricxvi am valuebidan aris wyvili {i}:{minumaluri}"

x = gamotvla(dictionary)
print(x)

####################programa2#####################

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

try:
    n = int(input("enter n: "))
    result = factorial(n)
    print(f"{n}-is faqtoriali aris: {result}")
except ValueError:
    print("araswori inputisa shemoiyavene intigeri .")
