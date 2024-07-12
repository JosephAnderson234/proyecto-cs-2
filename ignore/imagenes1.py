import pandas as pd
from sklearn import datasets

digitos= datasets.load_digits()

print(digitos)

print("\nLa primera matriz aplanada es: ")
print(digitos["data"][0])

print("\nLa ultima matriz aplanada es: ")
print(digitos["data"][-1])

print("\nEl primer target es: ") #numero
print(digitos["target"][0])

print("\nEl ultimo target es: ")
print(digitos["target"][-1])

print("\nLa primera matriz es: ")
print(digitos["images"][0])

#cuantos elementos hay?
print("\nCantidad de elementos: ", len(digitos["data"]))
print("\nCantidad de elementos: ", len(digitos["target"]))
print("\nCantidad de elementos: ", len(digitos["images"]))

#a partir de esta linea, comenzamos a armar el .xls que aparece en Canvas

#paso 1 guardamos laprimera matriz en un dataframe
print()
df1 = pd.DataFrame(data = digitos["images"][0])
print(df1)

#Vamis a crear un DataFrame con 0,0,0,0,0,0,0,0
separador= pd.DataFrame(data= [[0,0,0,0,0,0,0,0]])

#concatenamos el separador debajo de df1
df1=pd.concat([df1,separador], ignore_index=True)

#temporalmente guardo la segunda matriz en otro data frame
df2 = pd.DataFrame(data = digitos["images"][1])

#concatenamos df1 y df2
print("Va quedando así: ")
df1= pd.concat([df1, df2], ignore_index=True)
print(df1)

#concatenamos a todas las demas matrices iterativamente
i=2
while i<=1796:
    df1= pd.concat([df1, separador], ignore_index=True)
    df2= pd.DataFrame(data= digitos["images"][i])
    df1= pd.concat([df1, df2], ignore_index=True)
    i=i+1
df1= pd.concat([df1,separador], ignore_index=True)

unalista= []
for i in range(1797):
    for _ in range(9):
        unalista.append(digitos["target"][i])

df1["target"]= unalista
df1.to_csv("haquedadoasi.csv")

print(df1)
print(len(unalista))
