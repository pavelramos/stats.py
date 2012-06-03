from decimal import *
#http://docs.python.org/library/decimal.html

# Ejemplo:
#
#C:\Users\Pavel\python>test.py
#
#DISENO POR BLOQUES COMPLETAMENTE ALEATORIZADO
#Tabla para el Analisis de Varianza (ANOVA)
#http://github.com/pavelramos/estadistica.py/anova.py
#Escrito en Python por: @pavelramos
#---------------------------------------------------------
#
#Ingrese numero de columnas:5
#Ingrese cantidad de datos para columna N-1:3
#Ingrese dato para columna N-1:726.4
#Ingrese dato para columna N-1:732.8
#Ingrese dato para columna N-1:889.6
#[726.4, 732.8, 889.6]
#Ingrese cantidad de datos para columna N-2:2
#Ingrese dato para columna N-2:1291.2
#Ingrese dato para columna N-2:905.6
#[1291.2, 905.6]
#Ingrese cantidad de datos para columna N-3:2
#Ingrese dato para columna N-3:863
#Ingrese dato para columna N-3:876.7
#[863.0, 876.7]
#Ingrese cantidad de datos para columna N-4:2
#Ingrese dato para columna N-4:995.2
#Ingrese dato para columna N-4:984.3
#[995.2, 984.3]
#Ingrese cantidad de datos para columna N-5:3
#Ingrese dato para columna N-5:1193.6
#Ingrese dato para columna N-5:1272
#Ingrese dato para columna N-5:1457.6
#[1193.6, 1272.0, 1457.6]
#
#Calculando...
#
#Columna-1: n= 3, sumatoria= 2348.8, media= 782.93
#Columna-2: n= 2, sumatoria= 2196.8, media= 1098.40
#Columna-3: n= 2, sumatoria= 1739.7, media= 869.85
#Columna-4: n= 2, sumatoria= 1979.5, media= 989.75
#Columna-5: n= 3, sumatoria= 3923.2, media= 1307.73
#--------------------------
#Total: N= 12, sumatoria= 12188.0, media= 1015.67
#
#SCentre-1 : 162503.7228
#SCentre-2 : 13688.5058
#SCentre-3 : 42526.9448
#SCentre-4 : 1343.6928
#SCentre-5 : 255897.1308
#-------------------------
#SCentre total: 475959.9970
#
#(726.40 - 782.93)^2 = 3195.6409
#(732.80 - 782.93)^2 = 2513.0169
#(889.60 - 782.93)^2 = 11378.4889
#-------------------------
#SCdentro-1 : 17087.1467
#
#(1291.20 - 1098.40)^2 = 37171.8400
#(905.60 - 1098.40)^2 = 37171.8400
#-------------------------
#SCdentro-2 : 74343.6800
#
#(863.00 - 869.85)^2 = 46.9225
#(876.70 - 869.85)^2 = 46.9225
#-------------------------
#SCdentro-3 : 93.8450
#
#(995.20 - 989.75)^2 = 29.7025
#(984.30 - 989.75)^2 = 29.7025
#-------------------------
#SCdentro-4 : 59.4050
#
#(1193.60 - 1307.73)^2 = 13025.6569
#(1272.00 - 1307.73)^2 = 1276.6329
#(1457.60 - 1307.73)^2 = 22461.0169
#-------------------------
#SCdentro-5 : 36763.3067
#
#SCdentro total: 128347.3834
#
#==============================================
#
#Hallando Grados de Libertad:
#K - 1 = 4
#N - K = 7
#
#Hallando Cuadrado Medio:
#CMentre = 118989.9993
#CMdentro = 18335.3405
#
#Hallando Razon de Variacion:
#RV = CMentre/CMdentro = 6.4897

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