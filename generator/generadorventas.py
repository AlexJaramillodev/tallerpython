import random 

def generardorVentasApple():
    tipoProducto = ['musica', 'tv', 'aplicaciones', 'pc', 'celulares', 'tablets', 'accesorios']
    datos = []
    for producto in tipoProducto:
        dataApple = {}        
        categoria = random.choice(['plus', 'mega', 'basic'])
        dataApple = [producto, categoria]
        datos.append(dataApple)

    return datos

print(generardorVentasApple())