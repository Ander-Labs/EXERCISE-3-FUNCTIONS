class Coche:
  def __init__(self, puertas):
    self.puertas = puertas
  
  def aumentar_puertas(self, num):
    self.puertas += num
    
  mi_coche = Coche(4)  # Crea un nuevo coche con 4 puertas
  print(mi_coche.puertas)  # Imprime 4
  mi_coche.aumentar_puertas(2)  # Aumenta el número de puertas en 2
  print(mi_coche.puertas)  # Imprime 6
