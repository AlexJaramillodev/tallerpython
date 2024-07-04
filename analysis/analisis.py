from generator.generadorventas import generardorVentasApple
import pandas as pd

def analizarDatos():
    datos = generardorVentasApple()
    tabla = pd.DataFrame(datos, columns=["producto", "categoria"])
    tabla.to_csv('./productos.csv', index=False)
analizarDatos()
