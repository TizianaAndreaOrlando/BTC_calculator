#Definimos la función "Calculadora".Todos los datos estan en USD exceptuando por la salida final representada en BTC
def calculator(C_0,BTC_price):
    value1 = str(C_0/BTC_price)         #Regla de 3; nos da el valor en moneda por capital inicial invertido (C_0)
    value1 = value1 + " " + moneda
    print(f"\nUsted tiene: {value1}")
    return value1       

#************* ***************** **************** *********************
# Ingresamos los datos iniciales de la operación y aplicamos los calculos escenciales.

moneda = str(input("Ingrese el tipo de moneda: "))
C_0 = float(input("Ingrese su capital inicial en USD: "))
BTC_price= float(input("Ingrese el precio de BTCxUSD ")) #Trabajar en API's para no tenerlo que hacer manual. 
if BTC_price == 0:
    exit          #En el caso de que nos de un valor = 0, el programa se cierra.
else:
    calculator(C_0,BTC_price)
value = (C_0/BTC_price)        #La defino como variable global y así poder usarla en otras funciones

sumary = {"moneda": moneda,   #Creamos un diccionario para poder resumir al final del codigo nuestros datos. 
          "Monto inicial": C_0,
          "Precio BTC inicial": BTC_price,
          "Cant. BTC en posesión" : value,
          }  

#************* ***************** **************** ********************* 
print("\n************* **************** CALCULO DE RENTABILIDAD **************** *********************\n")         

def profitableness():
    
    """Esta función nos permite ingresar una rentabilidad estimada y ver a que valor en USD debe llegar BTC 
    para lograr dicho objetivo.
    También, podemos convertir el capital final en USD a pesos Argentinos."""
    
    i = float(input("Ingrese la rentabilidad esperada (en %): "))
    i = (i/100)
    absolut_value = C_0 * i
    C_f = C_0*(1 + i)
    convertor = (C_f/value)
    convertor = round(convertor,2)
    print(f"\nUsted espera sacar {absolut_value}$ USD de la transacción y su capital final será de: {C_f}$ USD. " 
          f"\nEl valor de BTC debería llegar a {convertor}$ para obtener una rentabilidad del {i*100} % de los {C_0}$ invertidos.")
    
    print("\n************* **************** CONVERSIÓN PESO-ARGENTINO **************** *********************\n") 
    print("Esta parte del programa nos permitira convertir nuestros dolares en pesos Argentinos.\n")
    dollar_blue = float(input("Ingrese el valor del dolar actual: "))
    value3 = (dollar_blue*C_f)
    profit = int(dollar_blue*absolut_value)
    print(f"\nUsted obtuvo una ganancia de {profit}$ pesos Argentinos y posee unos {value3}$ pesos en total.\n")
    
    sumary["Capital final"] = C_f
    sumary["Cotización dolar"] = dollar_blue
    sumary["Ganancia"] = profit
        
    
profitableness()

print("Datos finales:\n ",sumary)


#************* ***************** **************** *********************

    
