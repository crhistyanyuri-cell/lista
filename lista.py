#pizas
print("Pizas")
cardápio = ["piza de calabresa", "piza de frango com catupiri", "piza de carne"]
print(cardápio)

cardápio = ["piza de calabresa", "piza de frango com catupiri", "piza de carne", "piza com chocolate"]
print(len(cardápio))
print(cardápio[(0)])
print(cardápio[(1)])
cardápio[2] = "cachorro quente"
print(cardápio)

cardápio.append("piza de...abacaxi")
cardápio.remove("cachorro quente")

for x in cardápio:
    print(x)
print(cardápio)
#sucos
print("Sucos")
sucos = ["suco de uva", "suco de abacaxi", "suco de laranja", "suco de melancia"]
print(sucos)

sucos = ["suco de uva", "suco de abacaxi", "suco de laranja", "suco de melancia"]
print(len(sucos))
print(sucos[(0)])
print(sucos[(1)])

for y in sucos:
    print(y)
print(sucos)

#refrigerantes
print("Refrigerantes")
Refris = ["Fanta", "Coka", "Guarana Jesus", "Pepsi"]
print(Refris)

Refris = ["Fanta", "Coka", "Guarana Jesus", "Pepsi"]
print(len(Refris))
print(Refris[(0)])
print(Refris[(1)])

for a in Refris:
    print(a)
print(Refris)