'''
ESTANCIAS PROFESIONALES
CIMAT
-----
Ejemplo de Función Logística del Modelo de Crecimiento Poblacional
--Solución analítica--
Autor: Christian Hernández
Fecha de Creación: 09/08/22
'''
#Sección importar librerías
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
#---------------------------

#Clase logistic
class logistic(object):

    def __init__(self,r,k,ti,tf,vInicial):
        """
        Constructor
            -----------
            Parameters:
            r : TYPE. int
                DESCRIPTION. Tasa de crecimiento
            k : TYPE. float
                DESCRIPTION. Capacidad de carga
            ti : TYPE. int
                DESCRIPTION. Tiempo inicial
            tf : TYPE. int 
                DESCRIPTION. Tiempo final
            vInicial : TYPE. int 
                DESCRIPTION. Condicion Inicial (poblacion inicial)
            tActual : TYPE. int
                DESCRIPTION. Contador del tiempo Actual 
            -------- 
            Returns:
            None         
        """
        self.r = r      
        self.k = k     
        self.ti = ti   
        self.tf = tf    
        self.vInicial = vInicial    
        self.tActual = ti    
    #----------------------------------------------------------------       
    """
    Método que muestra el valor de los atributos
    -----------
    Parameters:
    None
    -----------
    Returns:
    None
    """
    def mostrar(self):
        print("Tasa de Crecimiento r: ",self.r)
        print("Capacidad de Carga: ",self.k)
        print("tiempo inicial: ",self.ti)
        print("tiempo final: ",self.tf)
        print("Valor Inicial: ",self.vInicial)
        print("Tiempo Actual:",self.tActual)
    """
    Método que almacenar los DATOS obtenidos del modelo respecto a los valores del TIEMPO
    -----------
    Parameters:
    None
    -----------
    Return:
    Arreglo de DATOS obtenidos por el modelo
    """
    def ley(self):
        datos = []                            #Arreglo para guardar los datos obtenidos del modelo
        rangoTiempo = list(range(ti,tf))      #Arreglo de valores para el TIEMPO t
        for self.tActual in rangoTiempo:      #Ciclo de evalución de un tiempo t en el Modelo N(t)
            resultado = self.solve()          #Cálculo del dato
            datos.append(resultado)           #Almacenamiento del dato
        return datos
    """
    Método para evaluar t en N(t)
    -----------
    Parameters:
    None
    -----------
    Return:
    Dato obtenido por el modelo N(t)
    """
    def solve(self):
        #SOLUCIÓN DE FORMA ANALÍTICA:
        #N(t) = k / (1 + (k/N0 -1)*e^(-r*t))
        resultado = (self.k)/(1 + (((self.k/self.vInicial) - 1)*np.exp(-(self.r)*(self.tActual))))
        return resultado
    """
    Método para graficar los datos obtenidos del Modelo N(t)
    -----------
    Parameters:
    datos: TYPE.array
          Description: Arreglo de datos a graficar 
    -----------
    Returns:
    None
    """
    def graficar(self,datos):
        plt.plot(range(ti,tf), np.array(datos), label = 'Crecimiento Poblacional')
        plt.legend()
        plt.show()
    """
    Método para crear y almacenar los datos obtenidos en un archivo TXT
    ----------
    Parameters:
    datos: TYPE.array
        Description: Arreglo de datos a guardar
    ----------
    Returns:
    None
    """
    def guardarTxt(self,datos):
        #Guardamos en archivo de texto
        np.savetxt("datosCP.txt",datos)
        #Obtenemos
        y = np.loadtxt("datosCP.txt")
#Fin clase -----------------------------------------------------------------------------------------------

#INICIO MAIN---------------------
if __name__ == '__main__':

#Parámetros modificables
    r=1
    k=10
    ti=1
    tf=30
    vInicial = 1
#Instanciacion de objeto e invocacion de sus métodos.
    prueba = logistic(r,k,ti,tf,vInicial)
    misDatos = prueba.ley()
    prueba.graficar(misDatos)
    prueba.guardarTxt(misDatos)

   

