'''                                    Descricao
    Este script foi desenvolvido para automatizar a execucao de tabelas nutricionais 
'''

import itertools

# Listas de ingredientes com suas respectivas composicoes
massas = ["Cacau Proteina=10g Carboidrato=5g", "Nozes Proteina=2g Carboidrato=1g"] # rendimento de 60g cada
adicionais = ["Baunilha Carboidrato=5g", "Chocolate Carboidrato=10g"]

# Combinar as duas listas
combinacao = list(itertools.product(massas, adicionais))

# OBS: Para obter a composicao nutricional total, deve-se somar a composicao dos dois itens da tupla
# e.g. ('Cacau Proteina=10g Carboidrato=5g', 'Baunilha Carboidrato=5g') -> Proteina = 10g e Carboidrato = 10g
print(combinacao)
print(len(combinacao))

######## TESTES ########

# Para evitar o processo manual de somar cada componente, a ideia eh criar um dict
# que sera responsavel por somar automaticamente os itens da tupla

Cacau = {"item": "Cacau", "Proteina": 10, "Carboidrato": 5}
Nozes = {"item": "Nozes", "Proteina": 2, "Carboidrato": 1}
Massas = {"Cacau":Cacau, "Nozes":Nozes}

#for k,v in Massas.items():
#    prot = int(v["Proteina"])
#    print(max(prot))
