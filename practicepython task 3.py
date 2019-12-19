a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

k=5

count = 0

for i in a:
    if i < k:
        count = count + 1
        print(i)
        
