# Sistemas Contínuos - Ejercicio 5: Tanque de agua

## Autores

- D'Autilio Joel
- Rossi Pablo


## Archivos

El trabajo consta de 4 archivos:

- [main.py](main.py): ejecutable principal
- [euler.py](euler.py): define la clase Euler, que utiliza el método de Euler para simular
- [constantes.py](constantes.py): contiene algunas constantes para el programa
- [funciones.py](funciones.py): contiene funciones para el problema:
    - Funciones de entrada
    - Función de salida
    - Función de derivada de altura


## Dependencias

Se deben instalar las dependencias con el siguiente comando. Es recomendable hacerlo dentro de un environment de Python. En Linux:

Para crear el environment

    python -m venv .env
    source .env/bin/activate

Para instalar las dependencias

    pip install -r requirements.txt


## Uso
El script [main.py](main.py) permite ejecutar una simulación del tanque de agua con los parámetros proveeidos. Hay una vista de ayuda disponible con

    python main.py -h

Se utiliza la librería matplotlib para generar una gráfica de la simulación.

### Parámetros requeridos
- f_entrada: función de entrada deseada. Las opciones son
    - constante_20: entrada constante de 20 unidades de agua por unidad de tiempo
    - constante_100: entrada constante de 100
    - oscilante: entrada que causa una oscilación perpetua de la altura de agua

### Parámetros opcionales
- -p, --paso: Paso de la simulación (default: 0.1)
- -t, --tiempo: Tiempo de simulación
- -i, --inicial: Altura inicial (default: 500)
- -k, --factor: Factor de multiplicación de la función de salida (default: 1)

Si no se pasa el parámetro de tiempo, la simulación continuará hasta que el sistema se estabilice.

Si la función de entrada es la oscilante, el sistema nunca se estabiliza. Por lo tanto, si no se pasa el parámetro --tiempo el programa no terminará.


### Ejemplo de uso
    python main.py constante_20 -k 0.5
    python main.py oscilante -t 1000 --inicial 300
