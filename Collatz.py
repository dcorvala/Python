"""La conjetura de Collatz es un problema matemático no resuelto que involucra secuencias numéricas.
Se inicia con cualquier número entero positivo.
Si es par, se divide entre 2; si es impar, se multiplica por 3 y se le suma 1.
El proceso se repite con el nuevo número generado.
La conjetura afirma que siempre se llega al número 1, sin importar con qué número se empiece."""

def f(n):
    sucesion=[n]
    if n<=0 or type(n)!=int:
        print("El número debe ser entero y positivo")
    elif n==2 or n==1:
        print("El número ingresado no cumple la conjetura de Collatz")
    else:
        while n!=1:
            if n%2==0:
                n=int(n/2)
                sucesion.append(n)
            else:
                n=int(3*n+1)
                sucesion.append(n)
        #print(sucesion)
        if [sucesion[len(sucesion)-3],sucesion[len(sucesion)-2],sucesion[len(sucesion)-1]]==[4,2,1]:
            print("El número ingresado cumple la conjetura de Collatz")
        else:
            print("El número ingresado no cumple la conjetura de Collatz")
        print("La cantidad de pasos para llegar a 1 es: {} y el máximo valor alcanzado es: {}".format(len(sucesion)-1,max(sucesion)))
