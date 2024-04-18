"""
Pruebas logicas


"""

# print(2 == 2)
# print(2!= 2)
# print(5>8)
# print(3>=3)
# print(4<3)
# print(3 <= 4)

#Definicion de variables
nombre = "Juan"
edad = 27 # años
n_hijos = 0
graduacion_colegio = 17 # años duracion_uni = 6 # años
duracion_pololeo = 3 # años
exp_laboral = 4 # años
duracion_uni = 6

#caso 1
#Juan es mayor de edad?
    #print(edad >= 18)# se cumple
#Juan se graduo del colegio antes de los 18 años?
    # print(graduacion_colegio < 18)# se cumple
#Experiencia laboral de Juan?
    # print(exp_laboral != 4)# se cumple
#Juan tiene hijos?
    # print(n_hijos > 0) # no se cumple
#Juan no tiene hijos
# print(n_hijos == 0)# se cumple
#Juan tiene con su novia mas de los años de experiencia
#print(duracion_pololeo > exp_laboral)
#Edad de universidad
#edad_uni = (graduacion_colegio + duracion_uni)
#print(edad_uni > 22)# se cumple 
#Juan comenzo a pololear a los 25 años
# edad_inicio_pololeo = edad - duracion_pololeo
# print(edad_inicio_pololeo)
# print(edad_inicio_pololeo == 25)
#Juan lleva más tiempo estudiando que trabajando?
# print(duracion_uni > exp_laboral)
# hola = "hola" # asignando valor
# hola == "hola" #comparando valor

me_llamo = nombre == "Juan"
# print(me_llamo)
#tipos de datos
#number
#string
#boolean
#print(type(nombre))
#print(type(me_llamo))

#AND
#print((2>3)and(3>2)) # comparacion 1 y comparacion 2 deben cumplise
#OR
#print((2>3)or(3>2)) #compara los valores y con que se cumpla uno resultado True

#print((edad > 18) and (duracion_pololeo > 0))
        #true                #true

# print((duracion_uni >= 6) or (exp_laboral > 5))    
        #true                      #false
    
#comparaciones
#1    
menor_28 = edad < 28
# print(menor_28)
    #true
#2
exp_menor_3 = exp_laboral < 3
#print(exp_menor_3) 
    #false

print(menor_28 ^ exp_menor_3)
        #true        #false