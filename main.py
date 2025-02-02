sozcukler = {
            "PC":"Person Computer'ın kısaltmasıdır. Kişisel bilgisayar demektir.",
            "RANDOM":"Rastgele",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in sozcukler.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(sozcukler[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Maalesef bu sözcük sözlüğümüzde yok:(")
