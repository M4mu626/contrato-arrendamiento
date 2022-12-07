from datetime import datetime   # esta es la libreria para poder colocar la fecha actual 


def reemplazartexto(texto, nombreCompañia, arrendador, ciudad, pais, arrendatario, fiador, precio):

    resultado = texto.reemplazar("[NOMBRE_COMPAÑIA]", nombreCompañia)
    resultado = resultado.reemplazar("[FECHA]", datetime.today().strftime('%Y-%m-%d'))   # si no se necesita la fecha actual se puede reemplazar por fecha 
    resultado = resultado.reemplazar("[ARRENDADOR]", arrendador)
    resultado = resultado.reemplazar("[CIUDAD]", ciudad)
    resultado = resultado.reemplazar("[PAIS]", pais)
    resultado = resultado.reemplazar("[ARRENDATARIO]", arrendatario)
    resultado = resultado.reemplazar("[FIADOR]", fiador)
    resultado = resultado.reemplazar("[PRECIO]", precio)

# si desea agregar mas datos , solo tiene que poner en el contrato lo que desea modificar, se reemplaza el dato que esta todo en mayuscula 
# por ejemplo si se tiene mas fiadores entonces colocar en el contrato [FIADOR 2] [FIADOR 3]  y asi dependiendo de lo que desea reemplazar 

    return resultado

ArchivoContrato = open("contrato.docx", "r")    # donde dice contrato.docx , se reemplaza con el nombre del contrato mas la extencion del archivo
resultado= ""


print("¿Cual es el nombre de la compañia?")
nombreCompañia= input()
print("¿Cual es el nombre del arrendador?")
arrendador= input()
print("¿Cual es la ciudad?")
ciudad= input()
print("¿Cual es el pais?")
pais= input()
print("¿Cual es el nombre del arrendatario?")
arrendatario= input()
print("¿Cual es el nombre del fiador?")
fiador= input()
print("¿Cual es el precio a pagar?")
precio= input()

# si la fecha no es la del momento, se puede colocar aqui la fecha que se necesite


for row in ArchivoContrato:
    resultado += reemplazartexto(row, nombreCompañia, arrendador, ciudad, pais, arrendatario, fiador, precio)

with open("copiaContrato", "w" ) as Archivotexto:
    Archivotexto.write(resultado)


