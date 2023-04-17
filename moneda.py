import requests

# Obtener las tasas de cambio más recientes de la API de Open Exchange Rates
response = requests.get('https://openexchangerates.org/api/latest.json?app_id=TU-API')
rates = response.json()['rates']

# Definir las tasas de conversión
MXN_TO_USD = rates['USD'] / rates['MXN']
MXN_TO_COP = rates['COP'] / rates['MXN']
MXN_TO_PEN = rates['PEN'] / rates['MXN']

# Pedir al usuario la cantidad de pesos mexicanos a convertir
mxn = float(input('Ingrese la cantidad de pesos mexicanos a convertir: '))

# Realizar las conversiones
usd = mxn * MXN_TO_USD
cop = mxn * MXN_TO_COP
pen = mxn * MXN_TO_PEN

# Imprimir los resultados
print(f'{mxn:.2f} pesos mexicanos son equivalentes a:')
print(f'{usd:.2f} dólares estadounidenses')
print(f'{cop:.2f} pesos colombianos')
print(f'{pen:.2f} soles peruanos')
