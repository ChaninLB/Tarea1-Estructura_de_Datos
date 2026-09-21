class numeroPrimo:
    def __init__(self):
        self.historial = []

    def es_primo(self, numero):
        self.historial.append(numero)
        primo = True
        if numero < 2:
            primo = False
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

        return primo

    def primos_en_rango(self, *args):
        primos = []
        for num in args:
            if self.es_primo(num):
                primos.append(num)
        return primos

    def cantidad_de_ferificados(self):
        return len(self.historial)

    @staticmethod
    def get_primos_verificados():
        return len(NumeroPrimo.primos_verficados)


primo1 = numeroPrimo()
primo1.es_primo(-5)
print(primo1.primos_en_rango(2, 7, 9, 10))
print(primo1.historial)
print(primo1.cantidad_de_ferificados())


#Ejercicio 1

class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for num in args:
            if self.validar_nota(num):
                self.notas.append(num)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


num1 = Calificador()
print(num1.cargar_notas(-60,80,40,200))
print(num1.promedio())

#Ejercicio 2

class AnalizadorTexto:

    def __init__(self):
        self.palabras_unicas = set()
        self.lista_palabras = []


    def agregar_palabra(self, palabra):
        if palabra not in self.palabras_unicas:
            self.lista_palabras.append(palabra)
            self.palabras_unicas.add(palabra)


    def contar_palabras(self):
        return len(self.lista_palabras)


    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

palabras1 = AnalizadorTexto()
palabras1.agregar_palabra("Hola")
palabras1.agregar_multiples("Hola", "Mundo", "Hola")

#Ejercicio 3

class CarroCompras:
    def __init__(self):
        self.articulos = []

    def agregar_articulo(self, nombre, precio):
        self.articulos.append({"nombre": nombre, "precio": precio})


    def total_carrito(self):
        total = 0
        precios = self.articulos
        for articulo in precios:
            total += articulo["precio"]
        return total

    def articulo_por_rango(self, precio_min, precio_max):
        articulos = []
        for articulo in self.articulos:
            if precio_min <= articulo["precio"] <= precio_max:
                articulos.append(articulo["nombre"])
        return articulos


carrito1 = CarroCompras()
carrito1.agregar_articulo("Manzanas", 3.5)
carrito1.agregar_articulo("Bananas", 2.0)
print(carrito1.articulo_por_rango(2, 4))
print(carrito1.total_carrito())
print(carrito1.articulos)

#Ejercicio 4

class InversorSecuencias:

    def invertir_lista(self, lista):
        invertida_list = []
        for i in range(len(lista) - 1, -1, -1):
            invertida_list.append(lista[i])
        return invertida_list

        
    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida
        return resultado

inv = InversorSecuencias()
lista = [1, 2, 3, 4, 5]
print(inv.invertir_lista(lista))
resultado = inv.invertir_multiples( [1, 2, 3], [4, 5, 6], [7, 8, 9] ) 
print(resultado)

#Ejercicio 5
class AnalizadorNumeros:
    def __init__(self):
        self.numeros = []

    def espar_numero(self, numero):
        es_par = True
        if numero % 2 == 0:
            es_par = True
        else:
            es_par = False

        return es_par

    def separar_numeros(self, *numeros):
        self.numeros = numeros
        par = []
        impar = []
        for num in numeros:
            resultado = self.espar_numero(num)
            if resultado:
                par.append(num)
            else:
                impar.append(num)

        return {
        'pares' : par,
        'impares' : impar
        }


    def cantidad_pares_Impares(self):
        resultado = self.separar_numeros(*self.numeros)
        cant_pares = len(resultado['pares'])
        cant_impares = len(resultado['impares'])

        return (cant_pares, cant_impares)


an = AnalizadorNumeros()
print(an.separar_numeros(1,2,3,4,5))
resultado = an.cantidad_pares_Impares()
print(resultado)

#Ejercicio 6
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    
    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)
        
    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        promedio = 0
        numeros = self.temperaturas
        for num in numeros:
            promedio = promedio + num

        return promedio / len(numeros)

    def registrar_multiples(self, temp):
        for num in temp:
            self.registrar_temperatura(num)


tp = GestorTemperatura()
resultado1 = tp.registrar_temperatura(10)
tp.registrar_temperatura(35)
tp.registrar_multiples([22, 28, 39])
print(tp.minima())
print(tp.maxima)
print(tp.promedio())

#Ejercicio 7
class GestorPersonas:
    def __init__(self):
        self.usuarios = {}
    
    def agregar_persona(self, nombre, edad):
        self.usuarios[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        personas = self.usuarios.items()
        for nombre, edad in personas:
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        suma = 0
        for edad in self.usuarios.values():
            suma = suma + edad
            promedio = suma / len(self.usuarios)
            return promedio

gp = GestorPersonas()
gp.agregar_persona("luis", 21)
gp.agregar_persona("melissa",21)
gp.agregar_persona("nancy", 17)
print(gp.personas_mayores(18))
print(gp.edad_promedio())

#Ejercicio 8
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = 0
        nombre_mayor = ""
        for equipo in self.equipos:
            cantidad = len(self.equipos[equipo])
            if cantidad > mayor:
                mayor = cantidad
                nombre_mayor = equipo

        return nombre_mayor

eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.crear_equipo("B")
eq.agregar_jugador("B", "Luis")
print(eq.equipo_mayor_integrantes())

#Ejercicio 9
class AnalizadorString:
    def __init__(self):
        self.texto_largo = ""

    def solo_vocales(self, letras):
        vocales = "aeiouAEIOU"
        if letras in vocales:
            return True
        else:
            return False

    def contar_por_tipo(self, texto):
        vocales = 0
        consonates = 0
        digitos = 0
        
        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto
        
        for letra in texto:
            if self.solo_vocales(letra):
                vocales += 1
            elif letra.isdigit():
                digitos += 1
            elif letra.isalpha():
                consonates += 1 

        return {
            "vocales" : vocales,
            "consonates" : consonates,
            "digitos" : digitos
        }


astr = AnalizadorString()
astr.contar_por_tipo("Hola123")
astr.contar_por_tipo("hello Word")
astr.contar_por_tipo("Holasoyluis")


#Ejercicio 10
class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []
        for tarea in self.tareas:
            if tarea[1] == "alta":
                prioritarias.append(tarea)
        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break

tareas = Tareas()
tareas.agregar_tarea("Hacer tarea de Python", "alta")
tareas.agregar_tarea("Estudiar para el examen", "alta")
tareas.agregar_tarea("Ver televisión", "baja")
tareas.agregar_tarea("Jugar videojuegos", "baja")
print(tareas.tareas_prioritarias())

#Ejercicio 11
class ContadorFrecuencia():
    def __init__(self):
        self.frecuencias = {} 

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] = self.frecuencias[elemento] + 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        elemento_mayor = None
        frecuencia_mayor = 0

        for elemento in self.frecuencias:
            frecuencia = self.frecuencias[elemento]

            if frecuencia > frecuencia_mayor:
                elemento_mayor = elemento
                frecuencia_mayor = frecuencia

        return elemento_mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0

contador = ContadorFrecuencia()
contador.agregar_elemento("perro")
contador.agregar_elemento("gato")
contador.agregar_elemento("perro")
contador.agregar_elemento("pájaro")
contador.agregar_elemento("gato")
contador.agregar_elemento("perro")
print("Elemento más frecuente:", contador.elemento_mas_frecuente())
print("Frecuencia de perro:", contador.frecuencia_elemento("perro"))
print("Frecuencia de gato:", contador.frecuencia_elemento("gato"))
print("Frecuencia de pez:", contador.frecuencia_elemento("pez"))

#Ejercicio 12
class SelectorRango:
    def crear_rango(self, inicio, fin):
        sel_rango = []
        for num in range(inicio, fin +1):
            sel_rango.append(num)

        return tuple(sel_rango)

    def elementos_en_multiples_rangos(self, *rangos):
        conjuntos = set()

        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]

        for numero in range(inicio, fin + 1):
            conjuntos.add(numero)

        return list(conjuntos)

slr = SelectorRango()
print(slr.crear_rango(1, 10))
resultado = slr.elementos_en_multiples_rangos(
    (1, 5),
    (4, 8),
    (10, 12)
)
print(resultado)

#Ejercicio 13
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado1 = listas[0]
        for i in range(1, len(listas)):
            resultado1 = self.intercalar(resultado1, listas[i])

        return resultado1

combinador = CombinadorListas()
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
lista3 = [7, 8, 9]
print(combinador.intercalar(lista1, lista2))
print(combinador.intercalar_multiples(lista1, lista2, lista3))

#Ejercicio 14
class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor_nota = -1
        mejor_nombre = ""

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return mejor_nombre, mejor_nota


registro = RegistroNotas()
registro.registrar("Luis", 85)
registro.registrar("Pedro", 60)
registro.registrar("Ana", 95)
registro.registrar("Carlos", 70)
print(registro.estudiantes_aprobados(70))
print(registro.mejor_estudiante())

#Ejercicio 15
class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = sum(divisores[:-1])

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


divisor = DivisorFinder()
print(divisor.encontrar_divisores(12))
print(divisor.es_perfecto(6))
print(divisor.es_perfecto(8))
print(divisor.encontrar_multiples_divisores(6, 8, 10))

#Ejercicio 16
class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        posicion = alfabeto.index(letra)
        nueva_posicion = (posicion + desplazamiento) % 26
        return alfabeto[nueva_posicion]

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            letra_codificada = self.codificar_letra(letra, desplazamiento)
            resultado = resultado + letra_codificada
        self.historial[palabra] = resultado

        return resultado


codificador = CodificadorCesar()
resultado = codificador.codificar_palabra("hola", 3)
print(resultado)
print(codificador.historial)

#Ejercicio 17
class AgrupadorEdades:

    def __init__(self):
        self.agrupadas = {}

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.agrupadas = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.agrupadas:
                self.agrupadas[categoria] = []
            self.agrupadas[categoria].append(edad)

        return self.agrupadas

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.agrupadas:
            return 0
        edades = self.agrupadas[categoria]
        return sum(edades) / len(edades)

#Ejercicio 18
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        distancia = (dx ** 2 + dy ** 2) ** 0.5
        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        distancia_minima = None
        punto_cercano = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if distancia_minima is None or distancia < distancia_minima:
                distancia_minima = distancia
                punto_cercano = punto

        return punto_cercano


calculador = CalculadorDistancia()
distancia = calculador.distancia_euclidiana((0, 0), (3, 4))
print("Distancia:", distancia)
punto = calculador.punto_mas_cercano(
    (0, 0),
    (3, 4),
    (1, 1),
    (10, 10)
)
print("Punto más cercano:", punto)
print("Distancias calculadas:", calculador.distancias)

#Ejercicio 19
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] = self.stock[producto] + cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] = self.stock[producto] - cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        productos = []
        for producto in self.stock:
            if self.stock[producto] < minimo:
                productos.append(producto)

        return productos


inventario = Inventario()
inventario.agregar_stock("arroz", 10)
inventario.agregar_stock("azucar", 3)
inventario.agregar_stock("leche", 20)
inventario.agregar_stock("pan", 2)
resultado = inventario.restar_stock("arroz", 4)
print("¿Se pudo restar?", resultado)
resultado = inventario.restar_stock("leche", 30)
print("¿Se pudo restar?", resultado)
bajo_stock = inventario.productos_bajo_stock(5)
print("Productos con bajo stock:", bajo_stock)

#Ejercicio 20
class AnalizadorPatrones:
    def __init__(self, texto):
        self.texto = texto

    def encontrar_palabras(self, texto, patron):
        resultados = []
        for palabra in texto.split():
            if palabra.startswith(patron):
                resultados.append(palabra)

        return resultados

    def agrupar_por_longitud(self, texto):
        grupos = {}
        for palabra in texto.split():
            if len(palabra) not in grupos:
                grupos[len(palabra)] = []
            grupos[len(palabra)].append(palabra)

        return grupos

    def palabras_unicas(self):
        palabras = self.texto.split()
        unicas = set(palabras)

        return unicas


texto = "python permite programar proyectos python"
analizador = AnalizadorPatrones(texto)
resultado1 = analizador.encontrar_palabras(texto, "pro")
print("Palabras que empiezan con 'pro':", resultado1)
resultado2 = analizador.agrupar_por_longitud(texto)
print("Palabras agrupadas por longitud:", resultado2)
resultado3 = analizador.palabras_unicas()
print("Palabras únicas:", resultado3)
