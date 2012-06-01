from decimal import *
#http://docs.python.org/library/decimal.html

def sumatoria(lista):
	suma = 0
	for itemlista in lista:
		suma += itemlista
	return suma

def media(lista):
	prom = sumatoria(lista)/len(lista)
	return prom

def sc_entre(lista, total):
	var1 = Decimal(str(media(lista))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var2 = Decimal(str(media(total))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var3 = Decimal(str(len(lista)*(var2-var1)**2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	return var3

# sumar todo sc-entre-
def show_sc_entre(srt):
	x = 0
	y = 0
	total = []
	abcdario = "%s" % (srt)
	for i in abcdario:
		letra = eval(i)
		total += letra
	for item in abcdario:
		list = eval(item)
		y = sc_entre(list, total)
		print "SC-dentro-(%s) es: %s" % (item, y)
		x += sc_entre(list, total)
	return x

def sc_dentro(lista):
	suma = 0
	i = 0
	for item in lista:
		var1 = Decimal(str(lista[i])).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		i = i+1
		var2 = Decimal(str(media(lista))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		var3 = (var1 - var2)**2
		suma += var3
	return suma

# sumar todo sc-dentro-
def show_sc_dentro(srt):
	x = 0
	y = 0
	abcdario = "%s" % (srt)
	for item in abcdario:
		list = eval(item)
		y = sc_dentro(list)
		print "SC-dentro-(%s) es: %s" % (item, y)
		x += sc_dentro(list)
	return x

a = [726.4, 732.8, 889.6]
b = [1291.2, 905.6]
c = [863, 876.7]
d = [995.2, 984.3]
e = [1193.6, 1272, 1457.6]

#Bienvenida
print """Prueba F
Analisis de varianza (ANOVA)
"""

#mostrando listas
print "A = " + str(a)
print "B = " + str(b)
print "C = " + str(c)
print "D = " + str(d)
print "E = " + str(e)

#mostrando n
print """
Caculando n:

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

#mostrando promedios
print """Calculando media:

Media en A es %.2f
Media en B es %.2f
Media en C es %.2f
Media en D es %.2f
Media en E es %.2f
------------------------
Media del Total es %.2f
""" % (media(a), media(b), media(c), media(d), media(e), media(a+b+c+d+e))

#mostrando SC-entre-
print """-----------------------------
SC-entre- Total es: %s
""" % show_sc_entre("abcde")

#mostrando SC-dentro-
print """-----------------------------
SC-dentro- Total es: %s
""" % show_sc_dentro("abcde")
