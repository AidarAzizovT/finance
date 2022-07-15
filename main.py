population = int(input("Население"))
salary = int(input("Зарлпата"))
ndfl = population * (salary * 0.13 * 12)

Nndfl = int(input("Нормативный ндфл"))
Db  = int(input())
#〖ПН〗_НДФЛ = (Н_НДФЛ / (НДФЛ * Н_НДФЛ /100))*(НДФЛ* Н_НДФЛ / 100 + Д_Б),
Pndfl = (Nndfl / (ndfl * Nndfl / 100)) * (ndfl * Nndfl / 100 + Db)
print(Pndfl)