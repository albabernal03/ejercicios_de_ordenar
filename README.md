<h1 align="center">	Ejercicios de ordenar</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_de_ordenar)
***
<h2>¿De qué trata esta tarea?</h2>

***
## Indice
1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercicio 3](#id3)

***

## Ejercicio 1:<a name="id1"></a>

```

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
```

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
```

***
**UML**

![ejercicio1](https://user-images.githubusercontent.com/91721875/158390552-ac8423ac-7339-4e6a-abdb-f13f059c73ed.PNG)

***

## Ejercicio 2:<a name="id2"></a>
```
class Tareas:
  def __init__(self, lista_tareas):
    self.lista_tareas = lista_tareas
  def bubbleSort(self):
    for i in range(len(self.lista-1)):
      for j in range(len(self.lista-1)):
        if self.lista[j] > self.lista[j+1]:
            self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]

lista= [8,13,5,6,13]
bubbleSort(lista)
print(lista)

```
***
**UML**

![ejercicio2](https://user-images.githubusercontent.com/91721875/158391870-d6a9d165-84d7-4717-b27b-36e6963948fe.PNG)

***

## Ejercicio 3:<a name="id3"></a>
```
#Algoritmo explorar
t= [15,65,76,19,33,45,84,66,68,34,67,54]
def explorar():
  di= 0
  fi = 0
  
  t.append(0)
  t.append(0)
  longitud = len(t)
  inicio = 0
  seg = []

  while inicio < longitud - 1:
    if t(inicio) < t(inicio+1):
      inicio = inicio + 1
    else:
      di = inicio
      if t[di] > t[di+1]:
        fi = di+1
        print(di,fi)
        while t[di] > t[fi]:
          if t[di] > t[fi+1] and fi < longitud-2:
            fi = fi+1
          else:
            break
        print(di,fi)
      else:
        fi = di+1
      seg.append((di,fi))
    print(seg)
    inicio = fi+2
    print(inicio)

```
***

**UML**

![ejercicio3](https://user-images.githubusercontent.com/91721875/158392745-97382653-2106-4e82-aab5-47b134e1806b.PNG)

***
