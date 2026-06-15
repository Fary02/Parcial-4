vehiculo = []; 

def mostrar_menu():
  
  print("\n*****Menu principal****"); 
  print("1. Agregar vehiculo"); 
  print("2. Actualizar vehiculo"); 
  print("3. Eliminar vehiculo"); 
  print("4. Actualizar vehiculo"); 
  print("5. Mostrar vehiculo"); 
  print("6. Salir"); 
  

def leer_opcion():
  
  try:
    
    opcion = int(input("\nDigita una opcion: ")); 
    
    if opcion >= 1 and opcion <= 6:
      
      return opcion; 
    
    else:
      
      print("\n¡ERROR!: Debe ingresar una opcion del 1 al 6"); 
      
      return 0; 
    
  except ValueError:
    
    print("\nIngresa un numero entero"); 
    
    return 0; 
  
def validacion_modelo(modelo): 
  
  if modelo.strip() != "":
    
    return True; 
  
  else:
    
    return False; 
  
def validar_anio(anio):
  
  if anio > 1900:
    
    return True; 
  
  else:
    
    return False; 
  
def validar_precio(precio):
  
  if precio > 0:
    
    return True; 
  
  else: 
    
    return False; 
  
def agregar_vehiculo(lista_vehiculos):
  
  print(); 
  
  print("\nAgregar Vehiculo"); 
  
  modelo = input("\nAgregue el modelo del vehiculo: "); 
  
  if not validacion_modelo(modelo):
    
    print("\n¡ERROR!, el modelo no existe"); 
    
    return
  
  try:
    
    anio = int(input("\nIngresa el año del vehiculo: ")); 
    
    if not validar_anio(anio):
      
      print("\n¡ERROR!, digite un valor valido"); 
      
      return
    
  except ValueError:
    
    print("\n¡ERROR!: Debe indicar un año valido"); 
    
    return
  
  try:
    
    precio = float(input("\nIngrese el valor del vehiculo: ")); 
    
    if not validar_precio(precio):
      
      print("\n¡ERROR!, el precio debe ser mayor a cero"); 
      
      return
    
  except ValueError:
    
    print("\n¡ERROR!, el precio deber ser un numero decimal"); 
    
    return
  
  def agregar_vehiculo(lista_vehiculos): 
    
    vehiculo = {
      
    "modelo": modelo.strip(),
    "anio": anio,
    "precio": precio,
    "disponibilidad": False
    
  }; 
  
  lista_vehiculos.append(vehiculo); 
  
  print("\nVehiculo agregado correctamente"); 