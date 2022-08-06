from statistics import variance
from tkinter import Variable
from Persona import Persona
from Turno import Turno



class Paciente(Persona):
    def __init__(self,nombre,apellido,edad,dni,obrasocial): 
        self.obrasocial=obrasocial
        self.turno=None
        Persona.__init__(self,nombre,apellido,edad,dni)
    
    def AgregarTurno(self,dia,mes,año,hora,minutos):
        if (self.turno==None):
            self.turno=Turno(dia,mes,año,hora,minutos,0)   #los paréntesis ¿? preguntar!

    def EliminarTurno(self):
        self.turno=None

    def ImprimirTurno(self):
        if(self.turno == None):
            print("Este paciente no tiene un turno.")
        else:
            print(self.turno.GetFechaYHora())

    def GetObraSocial(self):
        return self.obrasocial
        
        
        
        
# El paciente arranca con un turno vacío
# no es lo mismo que null, pero para que lo entiendas
#arranca con un turno vacio, el agregar lo que hace es chequear si está vacio,
# y en ese caso agrega un turno con los parametros que recibe. 
# El eliminar turno lo deja vacio otra vez. 
# Y el imprimir turno lo que hace es un print del turno.getTurno
        