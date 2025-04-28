nomes = ["","","","",""]
for i in range(len(nomes)):
   nomes[i] = input(f"digite o {i+1}° nome: ")

pesquisa = input("digite o nome que você quer achar: ")
for x in range(len(nomes)):
    if pesquisa == nomes[x]:
        print(f"o sujeito {pesquisa} está na lista, na posição {[x]}")

