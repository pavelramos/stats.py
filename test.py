from decimal import *
#http://docs.python.org/library/decimal.html

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

bar = 0
for i in xrange(k):
	print "%s y %s y %.2f" % (len(l[bar]), sum(l[bar]), media(l[bar]))
	bar += 1
print "%s y %s y %.2f" % (n, suma, suma/n)

bar2 = 0
var4 = 0
for i in xrange(k):
	var1 = Decimal(str(media(l[bar2]))).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var2 = Decimal(str(suma/n)).quantize(Decimal('1.00'),rounding=ROUND_HALF_UP)
	var3 = Decimal(str(len(l[bar2])*(var1-var2)**2)).quantize(Decimal('1.0000'),rounding=ROUND_HALF_UP)
	var4 += var3
	bar2 += 1
	print "%.4f" % var3
print "%.4f" % var4

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
		print "( %s - %s )^2 = %.4f" % (var5, var6, var7)
		var8 += var7
		var9 += var7
	bar3 += 1
	print """-------------------------\nSCdentro-%s : %.4f\n""" % (bar3, var9) #imprime suma dentro de cada columna
print "%.4f" % var8 #imprime la suma total de todos los valores de var9

