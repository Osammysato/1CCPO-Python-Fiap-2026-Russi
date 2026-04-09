# Atividade 3 -->
# Faça um programa que receba a quantidade de produtos que o usuário deseja
# A seguir, seu programa deve exibir a mensagem “Produto” a quantidade de vezes que o usuário solicitou.
# Utilize o laço for

qtd_musicas = int(input("Quantas músicas vc tem na playlist? (db): "))

for i in range(qtd_musicas):
    print(f"Música {i}")