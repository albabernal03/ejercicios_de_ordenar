<h1 align="center">	Ejercicios de ordenar</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_de_ordenar)
***
<h2>¿De qué trata esta tarea?</h2>

***
## Indice
1.
2.
3.

***

## Ejercicio 1:

´´´

#Algoritmo dicotómica:
#Apartado 1
t = [15,68,75,34,2,35,56] 
class ordenacion_dicotomica:

  def __init__(self,tabla,inicio,fin):
    self.t=t
    self.inicio=inicio
    self.fin=fin
    
  def ordenar(self):
    self.inicio= 0
    self.fin= len(self.t)
    while self.inicio < self.fin:
      for i in range (self.inicio+1,self.fin):
        if self.t[i] < self.t[self.inicio]:
          x= self.t[self.inicio]
          self.t[self.inicio]= self.t[i]
          self.t[i] = x
    print(self.t)      
  
#Apartado 2

class ordenacion_dicotomica_2:

  def __init__(self,t,t2,inicio,fin):
    self.t=t
    self.t2 = t2
    self.inicio= inicio
    self.fin= fin

  def ordenar_tabla_vacia(self):
    self.inicio= 0
    self.fin = len(self.t)
    self.t2= []
    for i in range (self.inicio,self.fin):
      valor_min= min(self.t)
      self.t2.append(valor_min)
      self.t2.remove(valor_min)

    print(self.t2)


   
  


´´´

***


## Ejercicio 2:

***

## Ejercicio 3:

***
