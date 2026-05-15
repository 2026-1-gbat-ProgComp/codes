maior_palidromo = 0
for i in range (100, 1000):
    for j in range (100, 1000):
        num = i * j
        num_str = str(num)
        if num_str == num_str[::-1]:
            if num > maior_palidromo:
                maior_palidromo = num
print (maior_palidromo)
