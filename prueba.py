# Importar librerias
import os
import pathlib
import pandas as pd
import csv

# Declarar variables globales
dir_path = 'data'
ext_excel = '.xlsx'
ext_csv = '.csv'

# Funcion principal para la prueba tecnica
def prueba_tecnica():
    for file in os.listdir(dir_path):
        # Obtener la extension del archivo
        file_extension = pathlib.Path(file).suffix
        # Lectura de archivos csv
        if file_extension == ext_csv:
            print('Leyendo archivos CSV...')
            # Abrir el documento CSV con formato UTF-8
            with open(dir_path + '/' + file, encoding = 'utf-8') as archivo:
                # Leer el fichero CSV
                csv_reader = csv.reader(archivo)
                print(csv_reader)
                # Leer todas las columnas del fichero CSV
                for rows in csv_reader:
                    columna_id_empleado = rows[0]
                    columna_nombre = rows[1]
                    columna_apellido1 = rows[2]
                    columna_apellido2 = rows[3]
                    columna_sexo = rows[4]
                    columna_fecha_antiguedad = rows[5]
                    columna_salario_bruto_anual = rows[6]
                    columna_id_empresa = rows[7]
                    columna_nombre_empresa = rows[8]
                    columna_id_centro_trabajo = rows[9]
                    columna_nombre_centro_trabajo = rows[10]

                    # Enunciado 1: Indicar cuantos hombre y mujeres hay del total de empleado.
                    def enunciado_1():
                        if columna_sexo == 'H':
                            print('Hombre:', columna_sexo)
                        if columna_sexo == 'M':
                            print('Mujer:', columna_sexo)

                    # Enunciado 2: Indica la suma el salario bruto anual de los empleados de la empresa 1 (Equilibra IT)
                    # y el centro de trabajo CT2 (Alovera).
                    def enunciado_2():
                        print('test')
                        
                    # Enunciado 3: Imprime un listado de empleados (id empleado, nombre, apellidos, salario y empresa)
                    # de los empleados que cobren más de 28000 euros y que pertenezcan a la empresa 2 (Equilibra RRHH).
                    def enunciado_3():
                        print('test')
                    
                    # Ejecutar los ejercicios
                    enunciado_1()
                    enunciado_2()
                    enunciado_3()

        # Lectura de archivos xlsx
        if file_extension == ext_excel:
            df = pd.read_excel(dir_path + '/' + file)

# Ejecutar el ejercicio completo
prueba_tecnica()