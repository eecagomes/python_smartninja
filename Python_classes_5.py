from functions import ola_mundo ## other alternative is to import functions and then functions. the function you want to use
from functions import somar_numeros,nr_cubo,nr_steps,absolute_dif
#1 funcão pode retornar mais do que um valor no return desde que seja return x,y,z,f
# por exemplo desde que ao chamar a função se tenha o mesmo nr de variaveis. a,b,c,d=function(ert,vft)

texto=ola_mundo(nome="Bernardo")

print(texto + "!!!!!")

#1
primeiro_nr=2
segundo_nr=3

soma=somar_numeros(primeiro_nr,segundo_nr)

print(str(soma))

#2
numero_a_elevar_ao_cubo=5

resultado=nr_cubo(numero_a_elevar_ao_cubo)

print(str(resultado))

#3

distance_walked=float(input("Please insert the distance walked in meters"))
step_size=float(input("Please state the length of your foot in meters"))

number_steps=nr_steps(distance_walked,step_size)

print(str(number_steps))

#4

real_nr_1=3
real_nr_2=-2

resultado=absolute_dif(real_nr_1,real_nr_2)

print(str(resultado))






