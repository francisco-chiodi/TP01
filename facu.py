beneficiario = input("Ingrese el nombre del paciente:")
codigo = input()
monto_base = int(input("Ingrese el monto base:"))

monto_total = monto_base + 25000 
letra = codigo[0] 
porcentaje = int(codigo[5])/100 
if letra >= "A" and letra <= "L": 
    monto_total+25000 
elif letra >= "M" and letra <= "Z" and letra != "U": 
    monto_total+40000 
elif "U" == letra: monto_total+100000



print(monto_total+(monto_total*porcentaje))