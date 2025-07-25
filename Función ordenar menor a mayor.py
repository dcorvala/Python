def selection_sort(x):
  for i in range(len(x)):
    swap = i + argmin(x[i:])
    (x[i],x[swap])=(x[swap],x[i])
return x
  
