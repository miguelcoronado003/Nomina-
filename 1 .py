   
import os

n = int (input ('Ingresa cuantos nominas va a preguntar: '))
for i in range (1, n + 1):
   print ('PROCESO ' + repr (i))
    print("B I E N V E N I D O")
    print("____________________________________________________________")
    print("|                                                          |")
    nombre=input("| Digite el nombre y apellido del empleado  :  ")
    salario=float(input("| Digite el salario mensual  :  "))
    diaslaborados=int(input("| Digite los días laborados  :  "))
    horasextras=int(input("| Digite la cantidad de horas extras  :   "))
    print("|__________________________________________________________|")
    
    valorextras=salario//30//8
    
    totalextras=valorextras*horasextras
    
    totalsalario=salario//30*diaslaborados
    
    totdevengado=salario+totalextras
    
    salud=salario*4//100
    
    pension=salario*4//100
    
    
    totdeducido=salud+pension
    
    print("")
    print("________________________________")
    print("|                              |")
    print("| Nombre :  ",nombre)
    print("| Salario :  ",salario)
    print("| Dias Laborados :  ",diaslaborados)
    print("|------------------------------|")
    print("| Salud",salud)
    print("| Pension",pension)
    print("|------------------------------|")
    print("| Total salario :  ",totalsalario)
    print("| Horas Extras :  ",totalextras)
    print("| Valor Horas extras",valorextras)
    print("|------------------------------|")
    print("| Total Devengado:  ",totdevengado)
    print("|------------------------------|")
    print("| Total Deducido:  ",totdeducido)
    print("|------------------------------|")
    print("| Neto a Pagar  :  ")
    netoapagar=totdevengado-totdeducido
    print("| -->",netoapagar)
    print("|______________________________|")
    print()
