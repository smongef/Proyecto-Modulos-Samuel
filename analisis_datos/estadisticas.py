# estadisticas.py
def media(datos):
    media_Arimetica = sum(datos) / len(datos)
    
    return media_Arimetica

def mediana(datos):
    datos.sort()
    n = len(datos)
    
    if n % 2 == 0:
        mediana = (datos[n // 2 - 1] + datos[n // 2]) / 2
    else:
        mediana = datos[n // 2]
    
    return mediana


if __name__ == "__main__":
    notas = [100, 50, 100, 78, 100]
    print(media(notas))