#FUNCIONES CREADAS

#Importamos librerias
import psycopg2
import csv


#Ubicacion de Postgresql:
HOST = 'localhost'
PORT = '5432'

#Usuario:
USERNAME = 'postgres'

#Contraseña del usuario:
PASSWORD = 'Barbara.95'

#Nombre de base de datos:
DATABASE = 'perez_barbara'


#Creamos una función para obtener el conector y el cursor

# def conector_y_cursor():
#     conector = psycopg2.connect(host=HOST, dbname=DATABASE, user=USERNAME, password=PASSWORD, port=PORT)
#     cursor = conector.cursor()
#     return conector, cursor


#Observamos las diferentes columnas que hay entre los DataFrame:

def compara_columns_df (df_train,df_test):
    """
    Compara las columnas entre dos Data Frames
	    Parametros:
		    df_train: DataFrame de entrenamiento
            df_test: DataFrame de testeo
	
        Retorno:
		    Entrega los campos que difieren entre un DataFrame y el otro. 
	"""	
    #Diferencia entre DF de entrenamiento y DF de testeo:
    diferencia_1 = set(df_train.columns.values).difference(set(df_test.columns.values))

    #Diferencia entre DF de testeo y DF de entrenamiento:
    diferencia_2 = set(df_test.columns.values).difference(set(df_train.columns.values))

    print(f'Campos que difieren entre DataFrame de entrenamiento y DataFrame de testeo: \n {diferencia_1}')

    print(f'\nCampos que difieren entre DataFrame de testeo y DataFrame de entrenamiento: \n {diferencia_2}')


##CONTADOR DE FILAS Y COLUMNAS DE DOS DATAFRAME
def contador_filas_columns(df_train,df_test):
    """
    Permite contar el numero de filas y de columnas del Data Frame de entrenamiento y el de testeo
	    Parametros:
		    df_train: DataFrame de entrenamiento
            df_test: DataFrame de testeo
            
        Retorno:
		    Devuelve la cantidad de registros en df de entrenamiento y el de testeo. 
	"""	
    
    #Observamos la cantidad de filas y de columnas que hay en los dos datos de los Data Frame ya procesados
    train_shape = df_train.shape
    test_shape = df_test.shape

    print(f'La cantidad de registros en df de entrenamiento:\n filas, columnas: {train_shape}')
    print(f'La cantidad de registros en df de testeo:\n filas, columnas: {test_shape}')




    