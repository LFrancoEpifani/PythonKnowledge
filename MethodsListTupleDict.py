# append(x)
lista = [1, 2, 3]
lista.append(4)
print("append:", lista)

# extend(iterable)
lista.extend([5, 6, 7])
print("extend:", lista)

# insert(i, x)
lista.insert(0, 0)
print("insert:", lista)

# remove(x)
lista.remove(0)
print("remove:", lista)

# pop([i])
elemento_pop = lista.pop()
print("pop:", elemento_pop, lista)

# clear()
lista.clear()
print("clear:", lista)

# index(x[, start[, end]])
lista = [1, 2, 3, 4, 5]
index = lista.index(3)
print("index:", index)

# count(x)
count = lista.count(3)
print("count:", count)

# sort(key=None, reverse=False)
lista.sort(reverse=True)
print("sort:", lista)

# reverse()
lista.reverse()
print("reverse:", lista)

# copy()
lista_copia = lista.copy()
print("copy:", lista_copia)


tupla = (1, 2, 3, 2, 4, 2)

# count(x)
count = tupla.count(2)
print("count:", count)

# index(x[, start[, end]])
index = tupla.index(3)
print("index:", index)


diccionario = {'a': 1, 'b': 2, 'c': 3}

# get(key[, default])
valor = diccionario.get('a')
print("get:", valor)

# items()
items = diccionario.items()
print("items:", list(items))

# keys()
keys = diccionario.keys()
print("keys:", list(keys))

# values()
values = diccionario.values()
print("values:", list(values))

# pop(key[, default])
valor_pop = diccionario.pop('b')
print("pop:", valor_pop, diccionario)

# popitem()
item_pop = diccionario.popitem()
print("popitem:", item_pop, diccionario)

# clear()
diccionario.clear()
print("clear:", diccionario)

# update([other])
diccionario.update({'d': 4})
print("update:", diccionario)

# setdefault(key[, default])
diccionario.setdefault('e', 5)
print("setdefault:", diccionario)
