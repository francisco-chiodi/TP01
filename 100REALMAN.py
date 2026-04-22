
beneficiario = input("Ingrese nombre completo: ")
codigo = input("Ingrese ICD10 X##.#: ") #L00-L99  #P00?P96
monto_base = int(input("Ingrese un monto base: "))

letra = codigo[0]
bloque = int(codigo[1] + codigo[2])


# Obtenci�n del porcentaje


porcentaje = int(codigo[4])

monto_final = monto_base + 25000

if "A" <= letra <= "L":
    monto_final += 25000
elif letra == "U":
    monto_final += 100000
elif "M" <= letra <= "Z":
    monto_final += 40000

monto_final += monto_final * porcentaje / 100

# Determinaci�n del cap�tulo
if letra == "A" or letra == "B":
    capitulo = "Ciertas enfermedades infecciosas y parasitarias"
elif letra == "C":
    capitulo = "Tumores[neoplasias]"
elif letra == "D":
    if bloque <= 48:
        capitulo = "Tumores[neoplasias]"
    else:
        capitulo = "Enfermedades de la sangre y de los �rganos hematopoy�ticos y ciertos trastornos que afectan el mecanismo de la inmunidad"
elif letra == "E":
    capitulo = "Enfermedades endocrinas, nutricionales y metab�licas"
elif letra == "F":
    capitulo = "Trastornos mentales y del comportamiento"
elif letra == "G":
    capitulo = "Enfermedades del sistema nervioso"
elif letra == "H":
    if bloque <= 59:
        capitulo = "Enfermedades del ojo y sus anexos"
    else:
        capitulo = "Enfermedades del o�do y de la ap�fisis mastoides"
elif letra == "I":
    capitulo = "Enfermedades del sistema circulatorio"
elif letra == "J":
    capitulo = "Enfermedades del sistema respiratorio"
elif letra == "K":
    capitulo = "Enfermedades del sistema digestivo"
elif letra == "L":
    capitulo = "Enfermedades de la piel y del tejido subcut�neo"
elif letra == "M":
    capitulo = "Enfermedades del sistema osteomuscular y del tejido conjuntivo"
elif letra == "N":
    capitulo = "Enfermedades del sistema genitourinario"
elif letra == "O":
    capitulo = "Embarazo, parto y puerperio"
elif letra == "P":
    capitulo = "Ciertas afecciones originadas en el per�odo perinatal"
elif letra == "Q":
    capitulo = "Malformaciones cong�nitas, deformidades y anomal�as cromos�micas"
elif letra == "R":
    capitulo = "S�ntomas, signos y hallazgos anormales cl�nicos y de laboratorio, no clasificados en otra parte"
elif letra == "S" or letra == "T":
    capitulo = "Traumatismos, envenenamientos y algunas otras consecuencias de causas externas"
elif letra == "V" or letra == "W" or letra == "X" or letra == "Y":
    capitulo = "Causas externas de morbilidad y de mortalidad"
elif letra == "Z":
    capitulo = "Factores que influyen en el estado de salud y contacto con los servicios de salud"
elif letra == "U":
    capitulo = "C�digos para prop�sitos especiales"
else:
    capitulo = "Cap�tulo no v�lido"



print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo) #modificar nombres de capitulos
print("Monto a pagar: ", monto_final)
