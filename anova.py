from decimal import *
#http://docs.python.org/library/decimal.html

print """
DISENO POR BLOQUES COMPLETAMENTE ALEATORIZADO
Tabla para el Analisis de Varianza (ANOVA)
http://github.com/pavelramos/estadistica.py/anova.py
Escrito en Python por: @pavelramos (c)2012
---------------------------------------------------------
"""

k = int(raw_input("Ingrese numero de columnas:"))
l = []
cont1 = 0
n = 0 #N total de datos
suma = 0
for i in xrange(k):
	l2 = []
	cont1 = cont1 + 1
	var = int(raw_input("Ingrese cantidad de datos para columna N-" + str(cont1) + ":"))
	for i in xrange(var):
		n = n + 1
		x = float(raw_input("Ingrese dato para columna N-" + str(cont1) + ":"))
		l2.append(x)
	print l2
	l.append(l2)
	suma += sum(l2)

def media(list):
	media = sum(list)/len(list)
	return media

print """\nCalculando...\n"""

bar = 0
cont2 = 0
for i in xrange(k):
	cont2 += 1
	print """Columna-%s: n= %s, sumatoria= %s, media= %.2f""" % (cont2, len(l[bar]), sum(l[bar]), media(l[bar]))
	bar += 1
print """--------------------------\nTotal: N= %s, sumatoria= %s, media= %.2f\n""" % (n, suma, suma/n)

bar2 = 0
var4 = 0
for i in xrange(k):
	var1 = Decimal(str(media(l[bar2]))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var2 = Decimal(str(suma/n)).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var3 = Decimal(str(len(l[bar2])*(var1-var2)**2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	var4 += var3
	bar2 += 1
	print """SCentre-%s : %.4f""" % (bar2, var3)
print """-------------------------\nSCentre total: %.4f""" % var4

print ""
bar3 = 0
var8 = 0
for i in xrange(k):
	bar4 = 0
	var9 = 0
	for i in xrange(int(len(l[bar3]))):
		var5 = Decimal(str(l[bar3][bar4])).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		var6 = Decimal(str(media(l[bar3]))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
		var7 = Decimal(str((var5-var6)**2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
		bar4 += 1
		print """(%s - %s)^2 = %.4f""" % (var5, var6, var7)
		var8 += var7
		var9 += var7
	bar3 += 1
	print """-------------------------\nSCdentro-%s : %.4f\n""" % (bar3, var9) #imprime suma dentro de cada columna
print """SCdentro total: %.4f\n""" % var8 #imprime la suma total de todos los valores de var9

print """==============================================\n"""

gl1 = k - 1
gl2 = n - k
print """Hallando Grados de Libertad:\nK - 1 = %s\nN - K = %s\n""" % (gl1, gl2)

cm1 = Decimal(str(var4/gl1)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
cm2 = Decimal(str(var8/gl2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
print """Hallando Cuadrado Medio:\nCMentre = %.4f\nCMdentro = %.4f\n""" % (cm1, cm2)

rv = cm1/cm2
rv = Decimal(str(rv)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
print """Hallando Razon de Variacion:\nRV = CMentre/CMdentro = %.4f""" % rv