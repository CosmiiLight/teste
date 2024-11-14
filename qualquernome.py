nome = input("Qual o seu nome?: ")
sobrenome = input("E seu sobrenome?: ")
mes = input("Que mês você fez a compra?: ")
preco = input("Qual foi o preço da sua compra?: ")
preco2 = int(preco)
disconto = 10
disconto2 = "10"
cupom = nome + "É" + disconto2



print ("Olá, " + nome + " " + sobrenome + ". Em " + mes + " "+"você reaizou uma compra no valor de R$" + preco +" e ganhou um desconto de "+ disconto2 + "% em sua próxima compra. Use o cupom " + cupom + "!")


porcentagem_disconto = (preco2 * disconto)/100

print(f"O valor original da compra é R${preco2}. Com um desconto de {disconto}%, o preço final é R${preco2 * (1 - disconto / 100):.2f}.")
