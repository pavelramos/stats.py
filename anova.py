from decimal import *
#http://docs.python.org/library/decimal.html

#mostrando listas
def show_listas(srt):
	i = 0
	abcdario = "%s" % (srt)
	for item in abcdario:
		i = i + 1
		list = eval(item)
		print "%s = %s" % (item, list)
	return i

#mostrando items (n) para cada lista
def show_muestra(srt):
	abcdario = "%s" % (srt)
	total = []
	for item in abcdario:
		list = eval(item)
		n = len(list)
		print "En (%s) hay %s items" % (item, n)
	for i in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(i)
		total += letra
	ntotal = len(total)
	return ntotal

#mostrando todo sumatoria
def show_sumatoria(srt):
	abcdario = "%s" % (srt)
	total = []
	for item in abcdario:
		list = eval(item)
		suma = Decimal(str(sum(list))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		print "Sumatoria en (%s) es: %s" % (item, suma)
	for i in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(i)
		total += letra
	sumatotal = sum(total)
	return sumatotal


def media(lista):
	prom = sum(lista)/len(lista)
	return prom

#mostrando todo media
def show_media(srt):
	abcdario = "%s" % (srt)
	total = []
	for item in abcdario:
		list = eval(item)
		media = sum(list)/len(list)
		media = Decimal(str(media)).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		print "Media en (%s) es: %s" % (item, media)
	for i in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(i)
		total += letra
	mediatotal = sum(total)/len(total)
	mediatotal = Decimal(str(mediatotal)).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	return mediatotal

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
	for i in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(i)
		total += letra
	for item in abcdario:
		list = eval(item)
		y = sc_entre(list, total)
		print "SC-entre-(%s) es: %s" % (item, y)
		x += sc_entre(list, total)
	return x

def operar_sc_entre(srt):
	x = 0
	total = []
	abcdario = "%s" % (srt)
	for i in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(i)
		total += letra
	for item in abcdario:
		list = eval(item)
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

# sumar todo sc-dentro-
def operar_sc_dentro(srt):
	x = 0
	abcdario = "%s" % (srt)
	for item in abcdario:
		list = eval(item)
		x += sc_dentro(list)
	return x

#grado de libertad -entre-
def gl_sc_entre(srt):
	i = 0
	gl = 0
	abcdario = "%s" % (srt)
	for item in abcdario:
		i = i + 1
	gl = i -1
	return gl

#grado de libertad -dentro-
def gl_sc_dentro(srt):
	abcdario = "%s" % (srt)
	i = 0
	total = []
	for item in abcdario: #aqui se juntan todas las listas es algo como "a+b+c+d+e+...."
		letra = eval(item)
		total += letra
		i = i + 1
	n = len(total)
	gl = n - i
	return gl

#cuadrado medio y razon de variacion
def cuadrado_medio(srt):
	cm1 = Decimal(str(operar_sc_entre(srt)/gl_sc_entre(srt))).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	cm2 = Decimal(str(operar_sc_dentro(srt)/gl_sc_dentro(srt))).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	return cm1, cm2

def razon_variacion(srt):
	cm1, cm2 = cuadrado_medio(srt)
	rv = Decimal(str(cm1/cm2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	return rv

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
print """-----------------------------
En total hay %s grupos por analizar
""" % show_listas("abcde")

#mostrando n
print """-----------------------------
En total hay %s items
""" % show_muestra("abcde")

#mostrando sumatoria
print """-----------------------------
Sumatoria total es %s
""" % show_sumatoria("abcde")

#mostrando media
print """-----------------------------
Media Total es: %s
""" % show_media("abcde")

#mostrando SC-entre-
print """-----------------------------
SC-entre- Total es: %s
""" % show_sc_entre("abcde")

#mostrando SC-dentro-
print """-----------------------------
SC-dentro- Total es: %s
""" % show_sc_dentro("abcde")

#mostrando grados de libertad sc-entre-
print """K - 1 = %s
N - K = %s""" % (gl_sc_entre("abcde"), gl_sc_dentro("abcde"))

print """
CM-entre- es: %s
CM-dentro- es: %s
"""% cuadrado_medio("abcde")

print """Razon de variacion es: %s""" % razon_variacion("abcde")