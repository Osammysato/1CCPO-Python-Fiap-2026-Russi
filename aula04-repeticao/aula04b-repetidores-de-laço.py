cp = 0
while cp < 10:
    cp += 1

    if cp == 3 or cp == 5:     #não exibir
        continue

    if cp == 7:    # Break - não exibi e sai do lasso
        break


    print(f"Produto {cp}")