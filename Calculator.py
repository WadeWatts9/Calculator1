# -*- coding: utf-8 -*-
#
# ============================================================
#  SUPER CALCULATOR v1.0  -  by Alan Canto
# ============================================================
#
#  NOTA IMPORTANTE:
#  Este no es el mejor código, ni el más optimizado.
#  Fue mi PRIMER programa, escrito mientras aprendía
#  Python como hobby. Lo guardo tal cual como recuerdo
#  de dónde empecé. Si estás leyendo esto y también
#  estás empezando, ¡ánimo! Todo gran programador
#  tuvo su primer "Calculator.py".
#
#  Actualizado de Python 2 a Python 3 sin modificar la lógica.
#
# ============================================================
#
# Programa calculador de:
# pendiente, regla de tres,
# área: triángulo, cuadrado, circunferencia, paralelogramo, trapecio,
# volumenes: prisma, base cuadrada, base rectangular, pirámide base cuadrada, cubo
# y créditos/licencia.
#
#      --------/---------/---------/---------/ Regla de 40 caracteres

while True:


	print()
	print("-----------------(S)(U)(P)(E)(R)  (C)(A)(L)(C)(U)(L)(A)(T)(O)(R)---------------")		
	print("                  _______________V 1.0 by Alan Canto__________                 ")
	
	accion = 0

	print("                INGRESA EL NUMERO DEL CALCULO QUE DESEAS REALIZAR")
	print("                             LUEGO PRESIONA LA TECLA")
	print("                               ----> [ENTER] <----")
	print()
	print("1-CALCULO DE PENDIENTE")
	print("2-REGLA DE TRES")
	print("3-PERIMETRO Y AREA TRIANGULOS")
	print("4-PERIMETRO Y AREA RECTANGULOS")
	print("5-PERIMETRO Y AREA CIRCULOS") 
	print("6-PERIMETRO Y AREA PARALELOGRAMOS") 
	print("7-PERIMETRO Y AREA TRAPECIOS")
	print("8-PERIMETRO Y AREA CUADRADOS")
	print("9-VOLUMEN PRISMA BASE RECTANGULAR")
	print("10-VOLUMEN CUBOS")
	print("11-VOLUMEN PRISMA BASE CUADRADA")
	print("12-VOLUMEN CILINDROS")
	print("13-VOLUMEN PIRAMIDE BASE CUADRADA")
	print("14-Creditos y Licencia")
	print()
	print()

	accion = int(input("INGRESE EL NUMERO DE LA ACCION AQUI, LUEGO [ENTER] -->  "))
	print()

	#CALCULADOR DE PENDIENTES V1.0
	if accion == 1:

		print()
		print("                  _____________________________________________                 ")
		print("                  [[Calculador de Pendiente v1.0 by AlanCanto]]")
		print("---------------------------------------//---------------------------------------")		
		print("                  _____________________________________________                 ")
		
		print()
		#Instrucciones de uso del programa
		print("     INGRESE UNA MEDIDA Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		
		print()
		print("         INGRESE LAS ALTURAS Y DISTANCIA ENTRE LOS PUNTOS EN METROS")
		
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		              ES MAS PRECISO""")
		
		print()
		print("""    LUEGO DE INGRESAR LAS MEDIDAS DE ALTURA Y DISTANCIA, PRESIONE [ENTER] 
		              PARA OBTENER SU RESULTADO""")
		
		print()

		#Ingreso de datos al programa 
		punto_mas_alto=float(input("****Ingrese el punto de mayor altura-->  "))
		punto_mas_bajo=float(input("****Ingrese el punto de menos altura-->  "))
		distancia_entre_los_puntos=float(input("****Ingrese la distancia entre los puntos-->  "))

		#Cálculo de pendiente
		metros_ascendidos=punto_mas_alto-punto_mas_bajo
		multiplicacion_mascendidos_x_100=metros_ascendidos*100
		pendiente=multiplicacion_mascendidos_x_100/distancia_entre_los_puntos

		#muestra de los datos al usuario
		print()
		print("EL VALOR DE SU PENDIENTE ES DE [[[", pendiente, "%]]]")
		
		print()
		print()
		print()
		print()
		print("             MUCHAS GRACIAS POR UTILIZAR EL PROGRAMA")
		print()

		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()

	#CALCULADOR DE REGLAS DE TRES
	if accion == 2:
		print()
		print("                  ______________________________________________                 ")
		print("                  [[Calculador de Regla de 3 v1.0 by AlanCanto]]")
		print("---------------------------------------//---------------------------------------")		
		print("                  ______________________________________________                 ")
		
		print()
		#Instrucciones de uso del programa
		print("            EL MODELO DE REGLA DE TRES QUE UTILIZAMOS ES EL SIGUIENTE")
		print()
		print("                                      A------B ")
		print("                                      C------X ")
		print()
		print()
		#Ingreso de datos al programa
		A = float(input("Introduce el dato A, luego presiona [ENTER] -->  "))
		B = float(input("Introduce el dato B, luego presiona [ENTER] -->  "))
		C = float(input("Introduce el dato C, luego presiona [ENTER] -->  "))
		#Cálculo de Regla de Tres
		CxB = C*B
		X = CxB/A
		print()
		print()
		#Muestra de los datos al usuario
		print("El resultado de su regla de tres es igual a -->  [[[ ", X, "]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()

	#CALCULADOR DE PERÍMETRO Y ÁREA DE TRIÁNGULO
	if accion == 3:
		print()
		print("                  ______________________________________________                 ")
		print("          [[Calculador Perimetro y Area de Triangulos v1.0 by AlanCanto]]      ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		#Ingreso de datos al programa
		unidad_de_medida1 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_1 = float(input("Ingresa la medida del LADO 1, luego presiona [ENTER]-->  "))
		lado_2 = float(input("Ingresa la medida del LADO 2, luego presiona [ENTER]-->  "))
		lado_3 = float(input("Ingresa la medida del LADO 3, luego presiona [ENTER]-->  "))
		base_triangulo = float(input("Ingresa la medida de la base, luego presiona [ENTER]-->  "))
		altura_triangulo = float(input("Ingresa la medida de la altura, luego presiona [ENTER]-->  "))
		print()
		#Cálculo de perímetro y área del triángulo
		perimetro_del_triangulo = lado_1 + lado_2 + lado_3 
		area_del_triangulo = base_triangulo * altura_triangulo / 2
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su triangulo es igual a ---->  [[[", perimetro_del_triangulo, unidad_de_medida1, "]]]")
		print()
		print("El area de su triangulo es igual a ---->  [[[", area_del_triangulo, unidad_de_medida1, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()

	#CALCULADOR DE PERÍMETRO Y ÁREA DE RECTANGULOS
	if accion == 4:
		print()
		print("                  ______________________________________________                 ")
		print("         [[Calculador Perimetro y Area de Rectangulos v1.0 by AlanCanto]]      ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		#Ingreso de datos al programa
		unidad_de_medida2 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		ancho_rectangulo = float(input("Ingresa la medida del ancho, luego presiona [ENTER]-->  "))
		largo_rectangulo = float(input("Ingresa la medida del largo, luego presiona [ENTER]-->  "))
		print()
		#Cálculo de perímetro y área del rectángulo
		perimetro_del_rectangulo = ancho_rectangulo + largo_rectangulo * 2
		area_del_rectangulo = ancho_rectangulo * largo_rectangulo
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su rectangulo es igual a ---->  [[[", perimetro_del_rectangulo, unidad_de_medida2, "]]]")
		print()
		print("El area de su triangulo es igual a ---->  [[[", area_del_rectangulo, unidad_de_medida2, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE PERÍMETRO Y ÁREA DE CIRCULOS
	if accion == 5:
		print()
		print("                  ______________________________________________                 ")
		print("           [[Calculador Perimetro y Area de Circulos v1.0 by AlanCanto]]      ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		#Ingreso de datos al programa
		unidad_de_medida3 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		radio_del_circulo = float(input("Ingresa el radio del circulo, luego presiona [ENTER]-->  "))
		print()
		#Cálculo de perímetro y área del rectángulo
		pi = 3.1416
		diametro_circulo = radio_del_circulo * 2
		perimetro_del_circulo = pi * diametro_circulo
		area_del_circulo = radio_del_circulo ** 2 * pi
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su circulo es igual a ---->  [[[", perimetro_del_circulo, unidad_de_medida3, "]]]")
		print()
		print("El area de su circulo es igual a ---->  [[[", area_del_circulo, unidad_de_medida3, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE PERÍMETRO Y ÁREA DE PARALELOGRAMOS
	if accion == 6:
		print()
		print("                  ______________________________________________                 ")
		print("         [[Calculador Perimetro y Area de Paralelogramos v1.0 by AlanCanto]]     ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida4 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_a_del_paralelogramo = float(input("Ingresa la medida del lado A, luego presiona [ENTER]-->  "))
		lado_base_del_paralelogramo = float(input("Ingresa la medida del lado BASE, luego presiona [ENTER]-->  "))
		altura_del_paralelogramo = float(input("Ingresa la medida de la altura relativa al lado BASE, luego presiona [ENTER]-->  "))
		#Cálculo de perímetro y área del paralelogramo
		perimetro_del_paralelogramo = (lado_a_del_paralelogramo + lado_base_del_paralelogramo) * 2
		area_del_paralelogramo = lado_base_del_paralelogramo * altura_del_paralelogramo
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su paralelogramo es igual a ---->  [[[", perimetro_del_paralelogramo, unidad_de_medida4, "]]]")
		print()
		print("El area de su paralelogramo es igual a ---->  [[[", area_del_paralelogramo, unidad_de_medida4, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE PERÍMETRO Y ÁREA DE TRAPECIOS
	if accion == 7:
		print()
		print("                  ______________________________________________                 ")
		print("           [[Calculador Perimetro y Area de Trapecios v1.0 by AlanCanto]]        ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida5 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		base_menor_trapecio = float(input("Ingresa la medida de la base menor, luego presiona [ENTER]-->  "))
		base_mayor_trapecio = float(input("Ingresa la medida de la BASE MAYOR, luego presiona [ENTER]-->  "))
		lado_trapecio1 = float(input("Ingresa la medida del lado 1, luego presiona [ENTER]-->  "))
		lado_trapecio2 = float(input("Ingresa la medida del lado 2, luego presiona [ENTER]-->  "))
		altura_del_trapecio = float(input("Ingresa la altura relativa a la base menor, luego presiona [ENTER]-->  "))
		#Cálculo de perímetro y área del trapecio
		perimetro_del_trapecio = base_menor_trapecio + base_mayor_trapecio + lado_trapecio1 + lado_trapecio2
		area_del_trapecio = (base_mayor_trapecio + base_menor_trapecio) / 2 * altura_del_trapecio
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su trapecio es igual a ---->  [[[", perimetro_del_trapecio, unidad_de_medida5, "]]]")
		print()
		print("El area de su trapecio es igual a ---->  [[[", area_del_trapecio, unidad_de_medida5, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE PERÍMETRO Y ÁREA DE CUADRADOS
	if accion == 8:
		print()
		print("                  ______________________________________________                 ")
		print("          [[Calculador Perimetro y Area de Cuadrados v1.0 by AlanCanto]]         ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida6 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_del_cuadrado = float(input("Ingresa la medida del lado, luego presiona [ENTER]-->  "))
		#Cálculo de perímetro y área del cuadrado
		perimetro_del_cuadrado = lado_del_cuadrado * 4
		area_del_cuadrado = lado_del_cuadrado * lado_del_cuadrado
		print()
		print()
		#Muestra de los datos al usuario
		print("El perimetro de su cuadrado es igual a ---->  [[[", perimetro_del_cuadrado, unidad_de_medida6, "]]]")
		print()
		print("El area de su cuadrado es igual a ---->  [[[", area_del_cuadrado, unidad_de_medida6, "2(cuadrados)]]]")
		print()
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE VOLUMEN PRISMA BASE RECTANGULAR
	if accion == 9:
		print()
		print("                  ______________________________________________                 ")
		print("        [[Calculador Volumen de Prisma Base Rectangular v1.0 by AlanCanto]]      ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida7 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		largo_de_la_base_rectangular = float(input("Ingresa la medida del largo de la base, luego presiona [ENTER]-->  "))
		ancho_de_la_base_rectangular = float(input("Ingresa la medida del ancho de la base, luego presiona [ENTER]-->  "))
		altura_del_prisma_de_base_rectangular = float(input("Ingresa la medida de la altura, luego presiona [ENTER]-->  "))
		#Cálculo deL volúmen de prisma de base rectangular
		area_base_prisma_base_rectangular = largo_de_la_base_rectangular * ancho_de_la_base_rectangular
		volumen_del_prisma_de_base_rectangular = area_base_prisma_base_rectangular * altura_del_prisma_de_base_rectangular
		print()
		print()
		#Muestra de los datos al usuario
		print("El volumen de su prisma base rectangular es igual a ---->  [[[", volumen_del_prisma_de_base_rectangular, unidad_de_medida7, "3(cubicos)]]]")
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE VOLUMEN CUBOS
	if accion == 10:
		print()
		print("                  _______________________________________________                ")
		print("                 [[Calculador Volumen de Cubos v1.0 by AlanCanto]]               ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida8 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_de_la_base_del_cubo = float(input("Ingresa la medida del lado de la base, luego presiona [ENTER]-->  "))
		#Cálculo deL volúmen de cubo
		volumen_del_cubo = lado_de_la_base_del_cubo * lado_de_la_base_del_cubo * lado_de_la_base_del_cubo
		print()
		print()
		#Muestra de los datos al usuario
		print("El volumen de su cubo es igual a ---->  [[[", volumen_del_cubo, unidad_de_medida8, "3(cubicos)]]]")
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE VOLUMEN DE PRISMAS DE BASE CUADRADA
	if accion == 11:
		print()
		print("                  _______________________________________________                ")
		print("       [[Calculador Volumen de Prismas de Base Cuadrada v1.0 by AlanCanto]]      ")
		print("---------------------------------------//--------------------------------------- ")		
		print("                  ______________________________________________                 ")
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida9 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_de_la_base_del_prisma_de_base_cuadrada = float(input("Ingresa la medida del lado de la base, luego presiona [ENTER]-->  "))
		altura_del_prisma_de_base_cuadrada = float(input("Ingresa la medida de la altura, luego presiona [ENTER]-->  "))
		#Cálculo deL volúmen de prisma de base cuadrada
		area_base_prisma_base_cuadrada = lado_de_la_base_del_prisma_de_base_cuadrada * 4
		volumen_del_prisma_de_base_cuadrada = area_base_prisma_base_cuadrada * altura_del_prisma_de_base_cuadrada
		print()
		print()
		#Muestra de los datos al usuario
		print("El volumen de su prisma de base cuadrada es igual a ---->  [[[", volumen_del_prisma_de_base_cuadrada, unidad_de_medida9, "3(cubicos)]]]")
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE VOLUMEN DE CILINDROS
	if accion == 12:
		print()
		print("                  _______________________________________________                ")
		print("               [[Calculador Volumen de Cilindros v1.0 by AlanCanto]]             ")
		print("---------------------------------------//--------------------------------------- ")		
		print() 
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		pi = 3.1416
		unidad_de_medida10 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		radio_de_la_base_del_cilindro = float(input("Ingresa la medida del radio de la base, luego presiona [ENTER]-->  "))
		altura_del_cilindro = float(input("Ingresa la medida de la altura, luego presiona [ENTER]-->  "))
		#Cálculo del volúmen de cilindro
		area_base_del_cilindro = radio_de_la_base_del_cilindro ** 2 * pi
		volumen_del_cilindro = area_base_del_cilindro * altura_del_cilindro
		print()
		print()
		#Muestra de los datos al usuario
		print("El volumen de su cilindro es igual a ---->  [[[", volumen_del_cilindro, unidad_de_medida10, "3(cubicos)]]]")
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CALCULADOR DE VOLUMEN DE PIRAMIDES DE BASE CUADRADA
	if accion == 13:
		print()
		print("                  _______________________________________________                ")
		print("      [[Calculador Volumen de Piramides de Base Cuadrada v1.0 by AlanCanto]]     ")
		print("---------------------------------------//--------------------------------------- ")		
		print() 
		#Instrucciones de uso del programa
		print()
		print("INGRESE UNA MEDIDA O UNIDAD Y LUEGO PRESIONE [ENTER] PARA INGRESAR LA SIGUIENTE")
		print()
		print("             EL PROGRAMA SOLO ADMITE CARACTERES NUMERICOS")
		print()
		print(""" INGRESE LAS MEDIDAS RESPETANDO LOS DECIMALES [ejemplo: 1.0], ASI EL CALCULO
		             ES MAS PRECISO""")
		print()
		print("""        LUEGO DE INGRESAR TODOS LOS DATOS SOLICITADOS, PRESIONE [ENTER] 
		             PARA OBTENER SU RESULTADO""")
		print()
		print()
		#Ingreso de datos al programa
		unidad_de_medida11 = input("Ingresa la unidad de medida que estas utilizando ejemplo: cm, m, Km ---->  ")
		lado_de_base_piramide_cuadrada = float(input("Ingresa la medida del lado de la base, luego presiona [ENTER]-->  "))
		altura_de_piramide_cuadrada = float(input("Ingresa la medida de la altura, luego presiona [ENTER]-->  "))
		#Cálculo del volúmen de cilindro
		area_base_de_piramide_cuadrada = lado_de_base_piramide_cuadrada * 4
		volumen_de_piramide_de_base_cuadrada = area_base_de_piramide_cuadrada * altura_de_piramide_cuadrada / 3
		print()
		print()
		#Muestra de los datos al usuario
		print("El volumen de su piramide base cuadrada es igual a ---->  [[[", volumen_de_piramide_de_base_cuadrada, unidad_de_medida11, "3(cubicos)]]]")
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
	#CREDITOS Y LICENCIA
	if accion == 14:
		print()
		print("                  _______________________________________________                ")
		print("                      [[Super Calculator v1.0 by AlanCanto]]    ")
		print("---------------------------------------//--------------------------------------- ")		
		print() 
		print("""                                SUPER CALCULATOR
                                 ES UN PROGRAMA 
                             QUE BUSCA FACILITARLE 
                                 LA VIDA A TODOS 
                             AQUELLOS QUE NECESITEN
                              REALIZAR UN CALCULO
                                     RAPIDO

                              EL PRESENTE PROGRAMA 
                                      PUEDE 
                                  DISTRIBUIRSE
                                  MODIFICARSE
                               Y USAR LIBREMENTE 

                                       BY
                                   ALAN CANTO

                                    LICENCIA 
                            GNU General Public License """)
		print() 
		print()
		print()
		print()
		#Reinicio del programa
		reinicio=int(input("-->Para reiniciar digite 0 y presione [ENTER]   ")) #REINICIO DEL PROGRAMA CON PRESIÓN DE LA TECLA O
		if reinicio==0:
			continue #CONTINUE CON DOBLE TABULACIÓN, INDENTADO A "IF"
			print()
			print()
			print("---------------------------------------//---------------------------------------") #SEPARACIÓN DEL REINICIO DEL PROGRAMA
			print()
			print()
