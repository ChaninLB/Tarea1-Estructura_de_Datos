#Ejercicio 1

class ControlNotas:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota > 0 and nota <= 100:
            return True
        else:
            return False


    def cargar_notas(self, *args):
        nota = []
        for num in args:
            if self.validar_nota(num):
                nota.append(num)
                self.notas.append(num)
        
        return nota

    def nota_mayor(self):
        nota_may = 0
        for num in self.notas:
            if num > nota_may:
                nota_may = num

        return nota_may

control = ControlNotas()
print(control.cargar_notas(80, 120, 65, -10, 95, 70))
print(control.nota_mayor())

#Ejercicio 2
class RegistraProductos:
    def __init__(self):
        self.productos_unicos = set()
        self.orden_productos = []

    def agregar_producto(self, producto):
        self.productos_unicos.add(producto)
        self.orden_productos.append(producto)

    def contar_productos(self):
        return len(self.productos_unicos)

    def agregar_varios(self, *args):
        for produc in args:
            self.agregar_producto(produc)

registro = RegistraProductos()
registro.agregar_producto("Laptop")
registro.agregar_producto("Mouse")
registro.agregar_producto("Laptop")
registro.agregar_varios("Teclado", "Monitor", "Mouse")
print(registro.contar_productos())

#Ejercicio 3
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def total_productos(self):
        suma = 0
        producto = self.productos.values()
        for cantidad in producto:
            suma += cantidad

        return suma

    def productos_por_rango(self, cantidad_min, cantidad_max):
        productos = []
        producto = self.productos.items()
        for nombre, cantidad in producto:
            if cantidad >= cantidad_min and cantidad <= cantidad_max:
                productos.append(nombre)

        return productos

inventario = Inventario()
inventario.agregar_producto("Laptop", 5)
inventario.agregar_producto("Mouse", 10)
inventario.agregar_producto("Teclado", 7)
inventario.agregar_producto("Monitor", 2)
print(inventario.total_productos())
print(inventario.productos_por_rango(5, 8))

#Ejercicio 4
class ContadorSecuencias:

    def contar_pares(self, lista):
        contador = 0
        for num in lista:
            if num % 2 == 0:
                contador += 1
            
        return contador

    def contar_multiples(self, *listas):
        cantidad = {}
        for lista in listas:
            pares = self.contar_pares(lista)
            cantidad[tuple(lista)] = pares

        return cantidad


contador = ContadorSecuencias()
lista1 = [1, 2, 4, 7]
lista2 = [3, 6, 8, 10]
lista3 = [1, 2, 2 ,3]
print(contador.contar_pares(lista1))
print(contador.contar_multiples(lista1, lista2, lista3))

#Ejercicio 5
class AnalizadorEdades:
    def __init__(self):
        self.edades = []

    def es_mayor(self, edad):
        return edad >= 18

    def separar(self, *edades):
        self.edades = edades
        mayores = []
        menores = []
        for edad in edades:
            if self.es_mayor(edad):
                mayores.append(edad)
            else:
                menores.append(edad)

        return {
            "mayores": mayores,
            "menores": menores
        }

    def cantidad_mayores_menores(self):
        cant_mayores = 0
        cant_menores = 0
        for edad in self.edades:
            if self.es_mayor(edad):
                cant_mayores += 1
            else:
                cant_menores += 1

        return (cant_mayores, cant_menores)


analizador = AnalizadorEdades()
print(analizador.separar(15, 20, 17, 25, 30, 16))
print(analizador.cantidad_mayores_menores())

#Ejercicio 6
class GestorCalificaciones:

    def __init__(self):
        self.notas = []

    def registrar_nota(self, nota):
        self.notas.append(nota)

    def minima(self):
        return min(self.notas)

    def maxima(self):
        return max(self.notas)

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_nota(nota)


gestor = GestorCalificaciones()
gestor.registrar_nota(15)
gestor.registrar_nota(18)
gestor.registrar_nota(12)
gestor.registrar_multiples(20, 17, 14)
print("Notas:", gestor.notas)
print("Mínima:", gestor.minima())
print("Máxima:", gestor.maxima())
print("Promedio:", gestor.promedio())

#Ejercicio 7
class GestorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_caros(self, precio_minimo):
        caros = []
        for nombre, precio in self.productos.items():
            if precio >= precio_minimo:
                caros.append(nombre)

        return caros

    def precio_promedio(self):
        suma = 0
        for precio in self.productos.values():
            suma = suma + precio
        promedio = suma / len(self.productos)

        return promedio


gestor = GestorProductos()
gestor.agregar_producto("Mouse", 15)
gestor.agregar_producto("Teclado", 25)
gestor.agregar_producto("Monitor", 200)
gestor.agregar_producto("Audifonos", 30)
caros = gestor.productos_caros(30)
print("Productos caros:", caros)
promedio = gestor.precio_promedio()
print("Precio promedio:", promedio)

#Ejercicio 8
class Cursos:
    def __init__(self):
        self.cursos = {}

    def crear_curso(self, nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)

    def curso_mayor_estudiantes(self):
        mayor = 0
        nombre_mayor = ""
        for curso in self.cursos:
            cantidad = len(self.cursos[curso])
            if cantidad > mayor:
                mayor = cantidad
                nombre_mayor = curso

        return nombre_mayor

gestor = Cursos()
gestor.crear_curso("Programacion")
gestor.crear_curso("Matematicas")
gestor.crear_curso("Base de Datos")
gestor.agregar_estudiante("Programacion", "Juan")
gestor.agregar_estudiante("Programacion", "Pedro")
gestor.agregar_estudiante("Matematicas", "Ana")
gestor.agregar_estudiante("Matematicas", "Carlos")
gestor.agregar_estudiante("Matematicas", "Luis")
gestor.agregar_estudiante("Base de Datos", "Maria")
resultado = gestor.curso_mayor_estudiantes()
print("El curso con más estudiantes es:", resultado)

#Ejercicio 9
class AnalizarNumero:
    def __init__(self):
        self.lista = []

    def es_positivo(self, numero):
        if numero > 0:
            return True
        else:
            return False

    def analizar_lista(self, lista):
        positivos = 0
        negativos = 0
        ceros = 0
        if len(lista) > len(self.lista_mas_larga):
            self.lista_mas_larga = lista

        for numero in lista:
            if self.es_positivo(numero):
                positivos += 1
            elif numero < 0:
                negativos += 1
            else:
                ceros += 1

        return {
            "positivos": positivos,
            "negativos": negativos,
            "ceros": ceros
        }

analizador = AnalizadorNumeros()
resultado = analizador.analizar_lista([5, -2, 0, 8, -4])
print(resultado)
print(analizador.lista_mas_larga)

#Ejercicio 10
class Productos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))

    def productos_caros(self):
        productos_caros = []
        for producto in self.productos:
            if producto[1] >= 50:
                productos_caros.append(producto)

        return productos_caros

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto[0] == nombre:
                self.productos.remove(producto)
                break

productos = Productos()
productos.agregar_producto("Laptop", 800)
productos.agregar_producto("Mouse", 25)
productos.agregar_producto("Teclado", 60)
productos.agregar_producto("Audifonos", 40)
print(productos.productos)
print(productos.productos_caros())

#Ejercicio 11
class ContadorVotos:
    def __init__(self):
        self.votos = {}

    def registrar_voto(self, candidato):
        if candidato in self.votos:
            self.votos[candidato] = self.votos[candidato] + 1
        else:
            self.votos[candidato] = 1

    def candidato_mas_votado(self):
        candidato_mayor = None
        cantidad_mayor = 0
        for candidato in self.votos:
            cantidad = self.votos[candidato]
            if cantidad > cantidad_mayor:
                candidato_mayor = candidato
                cantidad_mayor = cantidad

        return candidato_mayor

    def votos_candidato(self, candidato):
        if candidato in self.votos:
            return self.votos[candidato]
        else:
            return 0

contador = ContadorVotos()
contador.registrar_voto("Ana")
contador.registrar_voto("Pedro")
contador.registrar_voto("Ana")
contador.registrar_voto("Pedro")
contador.registrar_voto("Ana")
print( contador.candidato_mas_votado())
print(contador.votos_candidato("Ana"))
print(contador.votos_candidato("Pedro"))
print(contador.votos_candidato("Luis"))

#Ejercicio 12
class GestorConjuntos:
    def crear_secuencia(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def combinar_secuencias(self, *secuencias):
        conjunto = set()
        for secuencia in secuencias:
            inicio = secuencia[0]
            fin = secuencia[1]
            for numero in range(inicio, fin + 1):
                conjunto.add(numero)

        return list(conjunto)


gestor = GestorConjuntos()
resultado1 = gestor.crear_secuencia(2, 6)
print(resultado1)
resultado2 = gestor.combinar_secuencias((1, 4), (3, 7), (10, 12))
print(resultado2)

#Ejercicio 13
class MezcladorListas:

    def mezclar(self, lista1, lista2):
        resultado = []
        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def mezclar_multiples(self, *listas):
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.mezclar(resultado, listas[i])

        return resultado


mezclador = MezcladorListas()
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
print(mezclador.mezclar(lista1, lista2))
lista3 = [70, 80, 90]
print(mezclador.mezclar_multiples(lista1, lista2, lista3))


#Ejercicio 14
class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def registrar(self, producto, precio):
        self.productos[producto] = precio

    def productos_economicos(self, precio_maximo):
        economicos = []
        for producto, precio in self.productos.items():
            if precio <= precio_maximo:
                economicos.append(producto)

        return economicos

    def producto_mas_caro(self):
        precio_mayor = -1
        producto_mayor = ""
        for producto, precio in self.productos.items():
            if precio > precio_mayor:
                precio_mayor = precio
                producto_mayor = producto

        return producto_mayor, precio_mayor
    
registro = RegistroProductos()
registro.registrar("Laptop", 800)
registro.registrar("Mouse", 25)
registro.registrar("Teclado", 45)
registro.registrar("Monitor", 300)
print(registro.productos_economicos(50))
print(registro.producto_mas_caro())

#Ejercicio 15
class AnalizadorNumeros:
    def encontrar_pares(self, numero):
        pares = []
        for i in range(1, numero + 1):
            if i % 2 == 0:
                pares.append(i)

        return tuple(pares)

    def es_abundante(self, numero):
        pares = self.encontrar_pares(numero)
        suma = sum(pares[:-1])

        return suma > numero

    def analizar_multiples(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_pares(numero)

        return resultado

analizador = AnalizadorNumeros()
print(analizador.encontrar_pares(10))
print(analizador.analizar_multiples(5, 8, 10))

#ejercicio 16
class TransformadorNumeros:
    def __init__(self):
        self.historial = {}

    def transformar_numero(self, numero, desplazamiento):
        nuevo_numero = (numero + desplazamiento) % 10
        return nuevo_numero

    def transformar_lista(self, lista, desplazamiento):
        resultado = []
        for numero in lista:
            numero_transformado = self.transformar_numero(numero, desplazamiento)
            resultado.append(numero_transformado)
        self.historial[str(lista)] = resultado

        return resultado


transformador = TransformadorNumeros()
numeros = [1, 4, 8, 9]
resultado = transformador.transformar_lista(numeros, 3)
print(resultado)
print(transformador.historial)

#Ejercicio 17
class AgrupadorNotas:
    def __init__(self):
        self.agrupadas = {}

    def clasificar_nota(self, nota):
        if nota < 7:
            return "reprobado"
        elif nota < 9:
            return "aprobado"
        elif nota < 9.5:
            return "notable"
        else:
            return "excelente"

    def agrupar_por_categoria(self, *notas):
        self.agrupadas = {}
        for nota in notas:
            categoria = self.clasificar_nota(nota)
            if categoria not in self.agrupadas:
                self.agrupadas[categoria] = []
            self.agrupadas[categoria].append(nota)

        return self.agrupadas

    def nota_promedio_categoria(self, categoria):
        if categoria not in self.agrupadas:
            return 0
        notas = self.agrupadas[categoria]

        return sum(notas) / len(notas)

agrupador = AgrupadorNotas()
resultado = agrupador.agrupar_por_categoria(5, 6.5, 7.5, 8, 9.2, 9.8)
print(resultado)
promedio = agrupador.nota_promedio_categoria("reprobado")
print(promedio)


#Ejercicio 18
class CalculadorTemperaturas:
    def __init__(self):
        self.diferencias = []

    def calcular_diferencia(self, t1, t2):
        diferencia = abs(t1 - t2)
        self.diferencias.append(diferencia)

        return diferencia

    def temperatura_mas_cercana(self, referencia, *temperaturas):
        diferencia_minima = None
        temperatura_cercana = None
        for temperatura in temperaturas:
            diferencia = self.calcular_diferencia(referencia, temperatura)
            if diferencia_minima is None or diferencia < diferencia_minima:
                diferencia_minima = diferencia
                temperatura_cercana = temperatura

        return temperatura_cercana


calculador = CalculadorTemperaturas()
diferencia = calculador.calcular_diferencia(25, 20)
print("Diferencia:", diferencia)
temperatura = calculador.temperatura_mas_cercana(25, 20, 28, 31, 24)
print("Temperatura más cercana:", temperatura)
print("Diferencias calculadas:", calculador.diferencias)

#Ejercicio 19
class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro, cantidad):
        if libro in self.libros:
            self.libros[libro] = self.libros[libro] + cantidad
        else:
            self.libros[libro] = cantidad

    def prestar_libro(self, libro, cantidad):
        if libro in self.libros and self.libros[libro] >= cantidad:
            self.libros[libro] = self.libros[libro] - cantidad
            return True
        else:
            return False

    def libros_bajo_cantidad(self, minimo):
        libros_bajos = []
        for libro in self.libros:
            if self.libros[libro] < minimo:
                libros_bajos.append(libro)

        return libros_bajos

biblioteca = Biblioteca()
biblioteca.agregar_libro("Python", 10)
biblioteca.agregar_libro("Java", 5)
biblioteca.agregar_libro("HTML", 2)
resultado = biblioteca.prestar_libro("Python", 3)
print(resultado)
resultado = biblioteca.prestar_libro("HTML", 5)
print(resultado)

#Ejercicio 20
class AnalizadorNumeros:
    def __init__(self, lista):
        self.lista = lista

    def encontrar_mayores(self, lista, limite):
        resultados = []
        for numero in lista:
            if numero > limite:
                resultados.append(numero)

        return resultados

    def agrupar_por_paridad(self, lista):
        grupos = {
            "pares": [],
            "impares": []
        }
        for numero in lista:
            if numero % 2 == 0:
                grupos["pares"].append(numero)
            else:
                grupos["impares"].append(numero)

        return grupos

    def numeros_unicos(self):
        unicos = set(self.lista)

        return unicos
        

lista = [5, 12, 8, 20, 3, 15, 12, 8]
analizador = AnalizadorNumeros(lista)
resultado1 = analizador.encontrar_mayores(lista, 10)
print(resultado1)
resultado2 = analizador.agrupar_por_paridad(lista)
print(resultado2)
resultado3 = analizador.numeros_unicos()
print(resultado3)
