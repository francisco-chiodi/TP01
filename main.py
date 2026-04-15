#TPO1
name_lastname = input("input name and last name: ")

A1 = "CAPITULO I Ciertas enfermedades infecciosas y parasitarias"
B1 = "CAPITULO I Ciertas enfermedades infecciosas y parasitarias"
E1 = "CAPITULO IV Enfermedades endocrinas, nutricionales y metabólicas"
F1 = "CAPITULO V Trastornos mentales y del comportamiento"
G1 = "Capítulo VI Enfermedades del sistema nervioso"
H1 = "Capítulo VII Enfermedades del ojo y sus anexos" , "Enfermedades del oído y de la apófisis mastoides"
I1 = "CAPÍTULO VIII Enfermedades del sistema circulatorio"
J1 = "CAPITULO X Enfermedades del sistema respiratorio"
K1 = "CAPÍTULO XI Enfermedades del sistema digestivo"
L1 = "CAPÍTULO XII Enfermedades de la piel y del tejido subcutáneo"
M1 = "CAPÍTULO XIII Enfermedades del sistema osteomuscular y del tejido conjuntivo"
N1 = "CAPÍTULO XIV Enfermedades del sistema genitourinario "
O1 = "CAPÍTULO XV Embarazo, parto y puerperio"
P1 ="CAPÍTULO XVI Ciertas afecciones originadas en el período perinatal"
Q1 ="CAPÍTULO XVII Malformaciones congénitas, deformidades y anomalías cromosómicas"
R1 ="CAPÍTULO XVIII Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"
Z1 = "CAPÍTULO XXI Factores que influyen en el estado de salud y contacto con los servicios de salud"
U1 = "Capítulo XXII Códigos para propósitos especiales (U00–U99)"


ICD10_code = input("input ICD10 code: ") #H70.1
acces_chapter_block = ICD10_code[0]
if ICD10_code[0] == "A":
    print(A1)
elif ICD10_code[0] == "B":
    print(B1)
elif ICD10_code[0] == "E":
    print(E1)
elif ICD10_code[0] == "F":
    print(F1)
elif ICD10_code[0] == "G":
    print(G1)
elif ICD10_code[0] == "H":
    print(H1)
elif ICD10_code[0] == "I":
    print(I1)
elif ICD10_code[0] == "J":
    print(J1)
elif ICD10_code[0] == "K":
    print(K1)
elif ICD10_code[0] == "M":
    print(M1)
elif ICD10_code[0] == "L":
    print(L1)
elif ICD10_code[0] == "N":
    print(N1)
elif ICD10_code[0] == "O":
    print(O1)
elif ICD10_code[0] == "P":
    print(P1)
elif ICD10_code[0] == "Q":
    print(Q1)
elif ICD10_code[0] == "R":
    print(R1)
elif ICD10_code[0] == "N":
    print(N1)
elif ICD10_code[0] == "Z":
    print(Z1)
elif ICD10_code[0] == "U":
    print(U1)

if ICD10_code[0] == "D" and ICD10_code[1] == "5":
    print("CAPÍTULO III: Enfermedades de la sangre y de los órganos hematopoyéticos y/n ciertos transtornos que afectan el mecanismo de la inmunidad ")
else:
    print("CAPITULO II: Tumores [neoplasias]")

if ICD10_code[0] == "S" or ICD10_code[0] == "T":
    print("CAPÍTULO XIX Traumatismos, envenenamientos y algunas otras consecuencias de causas externas")

if ICD10_code[0] == "V" or ICD10_code[0] == "Y":
    print("CAPÍTULO XX Causas externas de morbilidad y de mortalidad (V01–Y98)")

"""
CAPITULO I Ciertas enfermedades infecciosas y parasitarias (A00–B99) 
CAPITULO II Tumores [neoplasias] (C00–D48) 
CAPÍTULO III Enfermedades de la sangre y de los órganos hematopoyéticos,
 y ciertos trastornos que afectan el mecanismo de la inmunidad (D50–D89) 
CAPITULO IV  Enfermedades endocrinas, nutricionales y metabólicas (E00–E90)
CAPITULO V  Trastornos mentales y del comportamiento (F00–F99)
Capítulo VI  Enfermedades del sistema nervioso (G00–G99)
Capítulo VII Enfermedades del ojo y sus anexos (H00–H59)
CAPÍTULO VIII Enfermedades del oído y de la apófisis mastoides (H60–H95)
CAPÍTULO IX Enfermedades del sistema circulatorio (I00–I99)
CAPITULO X Enfermedades del sistema respiratorio (J00–J99)
CAPÍTULO XI Enfermedades del sistema digestivo (K00–K93)
CAPÍTULO XII Enfermedades de la piel y del tejido subcutáneo (L00-L99)
CAPÍTULO XIII Enfermedades del sistema osteomuscular y del tejido conjuntivo (M00-M99)
CAPÍTULO XIV Enfermedades del sistema genitourinario (N00-N99)
CAPÍTULO XV Embarazo, parto y puerperio(O00–O99)
CAPÍTULO XVI Ciertas afecciones originadas en el período perinatal (P00–P96)
CAPÍTULO XVII Malformaciones congénitas, deformidades y anomalías cromosómicas (Q00–Q99)
CAPÍTULO XVIII Síntomas, signos y hallazgos anormales clínicos y de 
laboratorio, no clasificados en otra parte(R00–R99)
CAPÍTULO XIX Traumatismos, envenenamientos y algunas otras consecuencias de causas externas (S00–T98)
CAPÍTULO XX Causas externas de morbilidad y de mortalidad (V01–Y98)
CAPÍTULO XXI Factores que influyen en el estado de salud y contacto con los servicios de salud (Z00–Z99)
Capítulo XXII Códigos para propósitos especiales (U00–U99)
"""



