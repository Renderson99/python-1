nome = input("Digite seu nome: ")
users = []

while nome != "sair":
     idade = int(input("Digite sua idade: "))
     users.append([nome, idade])
     nome = input("Digite seu nome: ")

print(users)
