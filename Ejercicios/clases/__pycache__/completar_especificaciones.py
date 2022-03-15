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

    
  