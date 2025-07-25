class Alumno():
    Nombre = ''
    Apellido = ''
    Notas = []
    def __init__(self):
        self.Nombre = input("Ingrese nombre: ")
        self.Apellido = input("Ingrese apellido: ")
        a = float(input("Ingrese nota entre 1 y 10: "))
        notas_ingresadas = []
        while a!=0:
            if a>=1 and a<=10:
                notas_ingresadas.append(a)
                a = float(input("Ingrese nota entre 1 y 10: "))
            else:
                print("La nota ingresada no es válida")
                a = float(input("Ingrese nota entre 1 y 10: "))
        self.Notas = notas_ingresadas
        
        suma=0
        for j in range (len(notas_ingresadas)):
            suma=suma+notas_ingresadas[j]
            
        Promedio=(suma)/(len(notas_ingresadas))
        self.Promedio=str(Promedio)
        
        if Promedio < 4:
           self.Estado = "Recursa"
        elif 4 <= Promedio and Promedio < 7 :
           self.Estado = "Rinde final"
        else :
           self.Estado = "Promociona"
        
    def __str__(self):
        mensaje = "Nombre:"+self.Nombre+" - "+"Apellido:"+self.Apellido+" - "+"Promedio:"+self.Promedio+" - ""Estado: "+self.Estado
        return mensaje
