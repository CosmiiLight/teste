nome = input("Qual o seu nome?: ")


a = input("Coloque a primeira nota em reais: ")
ar = int(a)
b = input("Coloque a segunda nota em reais: ")
br = int(b)
c = input("Coloque a terceira nota em reais: ")
cr = int(c)
d = input("Coloque a quarta nota em reais: ")
dr = int(d)

soma = ar + br + cr + dr

print("Olá", nome, "sua média de notas deu", soma /4)
