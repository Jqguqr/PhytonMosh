# Declaracion: Objetos en los que se agupan datos por key y valor
# point = {"x": 1, "y":2}
point = dict(x=1, y=2)

# Asignacion
point['x'] = 10

# Agregar elemento
point["z"] = 20

# Obtener valor
if "a" in point:
    print(point["a"])

print(point.get("a", 0))

# Eliminar item
del point["x"]
print(point)

# Iterar en un diccionario
for key in point:
    print(key, point[key])

# iterar estilo Tuples
for key, value in point.items():
    print(key, value)
