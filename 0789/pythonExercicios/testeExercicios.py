"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
menor_acidentes = float('inf')
maior_acidentes = float('-inf')
soma_veiculos = 0
soma_acidentes = 0
soma_cidades_menos_2000 = 0

for i in range(1, 6):
    codigo_cidade = int(input(f"Código da cidade {i}: "))
    num_veiculos = int(input(f"Cidade {i} - Número de veículos de passeio: "))
    num_acidentes_vitimas = int(input(f"Cidade {i} - Acidentes de trânsito com vítimas: "))

    if num_acidentes_vitimas < menor_acidentes:
        menor_acidentes = num_acidentes_vitimas
        codigo_menor_acidentes = codigo_cidade

    if num_acidentes_vitimas > maior_acidentes:
        maior_acidentes = num_acidentes_vitimas
        codigo_maior_acidentes = codigo_cidade

    soma_veiculos += num_veiculos

    if num_veiculos < 2000:
        soma_acidentes += num_acidentes_vitimas
        soma_cidades_menos_2000 += 1

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes / soma_cidades_menos_2000

print(f"\nO menor indice de acidentes corresponde a cidade {codigo_menor_acidentes} com: {menor_acidentes} acidentes")
print(f"\nO maior indice de acidentes corresponde a cidade {codigo_maior_acidentes} com: {maior_acidentes} acidentes")
print(f"\nA media dos veiculos da: {media_veiculos} veiculos")
print(f"\nA media de acidentes nas cidades com menos de 2000 veiculos da: {int(media_acidentes)} acidentes")