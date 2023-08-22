# Librería de operaciones de números complejos 
Este proyecto consiste en desarrollar una calculadora que permita realizar operaciones matemáticas avanzadas con números complejos. La calculadora permite realizar las siguientes operaciones:
* Suma 
* Resta
* Multiplicación
* División
* Módulo
* Conjugado
* Convertir:
  * Polar a Cartesianas
  * Cartesianas a Polar
* Fase
## ¿Cómo obtener una copia del repositorio?
### Pre-requisitos
Antes de comenzar con la ejecución de este proyecto, es necesario asegurarse de que se tiene instalado Python en su computador, debido a que este es el lenguaje de programación utilizado para desarrollar este proyecto. 
En caso de no tenerlo siga los siguientes pasos:
1. Dirigirse a la página https://www.python.org/downloads/
2. Dar click en la opción de descarga
   ![image](https://github.com/alexandrac1420/CNYT/assets/138069735/03d02dfb-a346-4bc8-8e9c-066816e2f80e)
3. Ejecutar el programa que se descarga automáticamente.

### Instalación 
Para instalar la librería debe tener en cuenta estos pasos:
1. Abra la carpeta en donde desea guardar la librería.
2. De click derecho y seleccione la opción "Git Bash"
3. Clone el repositorio utilizando el comando 'git clone https://github.com/alexandrac1420/CNYT.git'
4. Importe el modulo de la libreria en el programa que vaya a utilizar.
   
Completado el proceso anterior podrá trabajar con la librería proporcionada.

## Modo de uso
Para utilizar esta librería es necesario conocer la estructura de entrada de las operaciones disponibles junto con la sintaxis adecuada de cada una de las operaciones.

### Representación 
El programa reconoce de entrada de numero complejo una parte real y una imaginaria representadas en tuplas. Por ejemplo, si quiero realizar alguna operación con el numero 5 + 2i, este se ingresará al programa de la siguiente manera (5,2).

### Sintaxis operaciones 
A continuación se presenta la sintaxis correcta para el uso de las operaciones disponibles:
* __Suma__: sum_complex (_numero 1, numero 2_)
* __Resta__: res_complex (_numero 1, numero 2_)
* __Multiplicación__: mult_complex (_numero 1, numero 2_)
* __División__: div_complex (_numero 1, numero 2_)
* __Módulo__: modu_complex (_numero_)
* __Conjugado__: conju_complex (_numero_)
* __Convertir__:
   * __Polar a Cartesianas__: polar_to_cart (_numero_)
   * __Cartesianas a Polar__: cart_to_polar (_numero_)
 * __Fase__: fase_complex (_numero_)

Tenga en cuenta que es necesario utilizar la representacion de los numeros mencionada anteriormente.

### Ejemplo de uso 
~~~python
import complex_lib

# Ingrese los números que desea operar
c1 = (2,5)
c2 = (-8,-4)

# Realice las operaciones disponibles

# Ejemplo entradas binarias
suma = complex_lib.sum_complex(c1,c2)
print("La suma de los números complejos {} y {} es de {}".format(c1,c2,suma))

# Ejemplo entradas unitarias
modulo = complex_lib.modu_complex(c1)
print("El modulo del numero {} es {}".format(c1, modulo))
~~~


## Construido con
* Phyton 3.11.4
  
## Autor 
__Alexandra Cortes Tovar__ 



