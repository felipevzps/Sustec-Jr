import pandas as pd

#################
#Requrirements:
#TODOS alergenicos - alergenicos = ["Nozes", "Nutella", "Leite"]
#TODOS sabores - sabores = ["Morango", "Chocolate", "Caramelo"]
#################

alergenicos_dict = {}
alergenicos = "nutella"
with open("donuts.csv" ,"r") as tabela_donuts:
    for line in tabela_donuts:
        #print(line)
        if alergenicos in line:
            #print(line)
            (k, v) = line.split()[1:]
            alergenicos_dict[("Alerg")] = v
            print("Alergenicos em tabela Donuts =", alergenicos_dict)

