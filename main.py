listaDesordenada = [10, 3, 99, 14, 13, 26]
print(listaDesordenada)
# sort e sorted
# sort -> ordena a propria lista
# sorted -> ordena da lista original e retorna para outra variavel

listaOrdenada = sorted(listaDesordenada, reverse=True)
listaDesordenada.sort(reverse=True)

print(listaDesordenada) # ORDENADO COM SORT
print(listaOrdenada) # ORDENADO COM SORTED


lista = [
    {"name": "João", "age": 70},
    {"name": "Cícero", "age": 31},
    {"name": "Maria", "age": 14}
]

novaLista = sorted(lista, key=lambda x: x["age"], reverse=True)
print(novaLista)