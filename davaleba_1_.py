sigrdze = 0

for i in range(5):
    x = input("sheiyaven rame ")
    y = len(x.replace(" ", ""))
    
    if y > sigrdze:
        sigrdze = y
        result = x.replace(" ", "")

print(f"{result} romlis sigrdzea {sigrdze}")