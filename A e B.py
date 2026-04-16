#criando uma nova lista

listaA = ["A", "B", "C", "D"]
listaB = ["1", "2", "3", "4"]

#juntando duas listas
listão = listaA + listaB
print(listão)

#copiando uma lista
copia = listão.copy()

#removendo
copia.remove("A",)
print(copia)
copia.remove("3")
print(copia)

listaA.append("E")
print(len(listão))
