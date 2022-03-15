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
