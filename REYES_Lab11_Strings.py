c = 0 
words = []
match = []

while c < 10:
     w = input( f"{c + 1}. Enter a word: ")
     words.append(w)
     c += 1
    
n = int(input("Enter a number: "))
for i in words:
    if len(i) >= n:
        match.append(i)
print(match)