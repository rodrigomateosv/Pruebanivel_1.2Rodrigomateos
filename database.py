class Nodo:
    """Clase nodo simplemente enlazado"""
    def __init__(self):
        self.info = None
        self.sig = None


class DatoPolinomio:
    """Clase dato polinomio"""
    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término"""
        self.valor = valor  # coeficiente
        self.termino = termino  # exponente


class Polinomio:
    """Clase polinomio"""
    def __init__(self):
        """Crea un polinomio del grado cero"""
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(self, termino, valor):
        """Agrega un termino y su valor al polinomio"""
        nodo = Nodo()
        dato = DatoPolinomio(valor, termino)
        nodo.info = dato
        if termino > self.grado:
            nodo.sig = self.termino_mayor
            self.termino_mayor = nodo
            self.grado = termino
        else:
            actual = self.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            nodo.sig = actual.sig
            actual.sig = nodo

    def modificar_termino(self, termino, valor):
        """Modifica un termino del polinomio"""
        aux = self.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
        if aux is not None:
            aux.info.valor = valor

    def obtener_valor(self, termino):
        """Devuelve el valor de un termino del polinomio"""
        aux = self.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
        if aux is not None and aux.info.termino == termino:
            return aux.info.valor
        else:
            return 0

    def eliminar_termino(self, termino):
        """Elimina un termino del polinomio"""
        if self.termino_mayor is not None and self.termino_mayor.info.termino == termino:
            self.termino_mayor = self.termino_mayor.sig
        else:
            aux = self.termino_mayor
            while aux.sig is not None and aux.sig.info.termino != termino:
                aux = aux.sig
            if aux.sig is not None:
                aux.sig = aux.sig.sig

    def existe_termino(self, termino):
        """Determina si existe un termino en el polinomio"""
        aux = self.termino_mayor
        while aux is not None and aux.info.termino != termino:
            aux = aux.sig
        if aux is not None and aux.info.termino == termino:
            return True
        else:
            return False

    def mostrar(self):
        """Muestra el polinomio"""
        aux = self.termino_mayor
        pol = ""
        if aux is not None:
            while aux is not None:
                signo = ""
                if aux.info.valor >= 0:
                    signo += "+"
                pol += signo + str(aux.info.valor) + "x^" + str(aux.info.termino)
                aux = aux.sig
        else:
            pol = "0"
        return pol
    
# Creamos dos polinomios
p1 = Polinomio()
p2 = Polinomio()

# Agregamos términos a cada polinomio
p1.agregar_termino(2, 4) # 2x^4
p1.agregar_termino(3, 2) # 3x^2
p1.agregar_termino(1, 0) # 1

p2.agregar_termino(1, 3) # x^3
p2.agregar_termino(4, 2) # 4x^2
p2.agregar_termino(-1, 0) # -1

# Mostramos ambos polinomios
print("Polinomio 1: ", p1.mostrar()) # 2x^4+3x^2+1
print("Polinomio 2: ", p2.mostrar()) # x^3+4x^2-1

# Obtenemos el valor del término 2 en el polinomio 1
print("Valor de término 2 en polinomio 1: ", p1.obtener_valor(2)) # 3

# Modificamos el valor del término 0 en el polinomio 2
p2.modificar_termino(0, 5) # 5

# Verificamos que se haya modificado correctamente
print("Polinomio 2 modificado: ", p2.mostrar()) # x^3+4x^2+5

# Sumamos los dos polinomios
p3 = Polinomio.sumar(p1, p2)

# Mostramos el resultado de la suma
print("Suma de los polinomios: ", p3.mostrar()) # 2x^4+x^3+7x^2+6

# Restamos los dos polinomios
p4 = Polinomio.restar(p1, p2)

# Mostramos el resultado de la resta
print("Resta de los polinomios: ", p4.mostrar()) # 2x^4-x^3-x^2+2

# Eliminamos el término 2 en el polinomio 1
p1.eliminar_termino(2)

# Verificamos que se haya eliminado correctamente
print("Polinomio 1 modificado: ", p1.mostrar()) # 2x^4+1

# Verificamos si existe el término 2 en el polinomio 2
print("Existe término 2 en polinomio 2: ", p2.existe_termino(2)) # True

# Verificamos si existe el término 5 en el polinomio 2
print("Existe término 5 en polinomio 2: ", p2.existe_termino(5)) # False

