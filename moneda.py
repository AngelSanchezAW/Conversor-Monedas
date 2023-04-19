import requests

# Obtener las tasas de cambio más recientes de la API de Open Exchange Rates
response = requests.get('https://openexchangerates.org/api/latest.json?app_id=TU-API')
rates = response.json()['rates']

# Definir las tasas de conversión
MXN_TO_USD = rates['USD'] / rates['MXN']
MXN_TO_COP = rates['COP'] / rates['MXN']
MXN_TO_PEN = rates['PEN'] / rates['MXN']
USD_TO_MXN = rates['MXN'] / rates['USD']

# Pedir al usuario si desea pasar de MXN a Varias momendas o de USD a MXN
print('\n¿Qué desea hacer?')
print('\n1.- Pasar de MXN a otras momendas\n2.- Pasar de USD a MXN')
option = float(input('\nIngresa la opción deseada:'))

if option==1:
    # Pedir al usuario la cantidad de pesos mexicanos a convertir
    mxn = float(input('\nIngrese la cantidad de pesos mexicanos a convertir: '))

    # Realizar las conversiones
    usd = mxn * MXN_TO_USD
    cop = mxn * MXN_TO_COP
    pen = mxn * MXN_TO_PEN

    # Imprimir los resultados
    print(f'\n[{mxn:.2f} pesos mexicanos son equivalentes a]:')
    print(f'--> {usd:.2f} dólares estadounidenses')
    print(f'--> {cop:.2f} pesos colombianos')
    print(f'--> {pen:.2f} soles peruanos\n')
else:
    # Pedir al usuario la cantidad de pesos USD a convertir
    usd = float(input('\nIngrese la cantidad de USD a convertir: '))

    # Realizar las conversiones
    mxn = usd * USD_TO_MXN

    # Imprimir los resultados
    print(f'\n[{usd:.2f} USD son equivalentes a]:')
    print(f'--> {mxn:.2f} pesos mexicanos\n')
