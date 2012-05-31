def sumatoria(lista):
	suma = 0
	for itemlista in lista:
		suma += itemlista
	return suma

def promedio(lista):
	prom = sumatoria(lista)/len(lista)
	return prom

a = [726.4, 732.8, 889.6]
b = [1291.2, 905.6]
c = [863, 876.7]
d = [995.2, 984.3]
e = [1193.6, 1272, 1457.6]

#mostrando n
print """Caculando n:

En A hay %s items.
En B hay %s items.
En C hay %s items.
En D hay %s items.
En E hay %s items.
----------------------------
En Total hay %s items.
""" % (len(a), len(b), len(c), len(d), len(e), len(a+b+c+d+e))

#mostrando sumatoria
print """Calculando sumatoria:

En A es %s
En B es %s
En C es %s
En D es %s
En E es %s
-----------------
La Sumatoria Total es %s
""" % (sumatoria(a), sumatoria(b), sumatoria(c), sumatoria(d), sumatoria(e), sumatoria(a+b+c+d+e))


print promedio(a)
print promedio(b)
print promedio(c)
print promedio(d)
print promedio(e)