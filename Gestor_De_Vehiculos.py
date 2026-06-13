# Creacion de arrays a ocupar;

Vehiculos = []; 

vehiculo = []; 

modelo = []; 

año = []; 

precio = []; 

disponibilidad = []; 

disponible = True; 

no_Disponble = False; 

# Inicio de menu;

while True:

  print("\n*****MENU PRINCIPAL****"); 
  print("1. Agregar vehiculo"); 
  print("2. Buscar vehiculo"); 
  print("3. Eliminar vehiculo"); 
  print("4. Actualizar disponibilidad"); 
  print("5. Mostrar vehiculos"); 
  print("6. Salir"); 

  # Intenta;
  
  try:
    
    # Solicitar opcion;
    
    opcion = int(input("\nDigite una opcion: ")); 
    
    # Validar opcion;
    
    if opcion == 1:
      
      # Solicito informacion;
      
      modelo = str(input("\nPor favor, digite el modelo del vehiculo: ")); 
      
      # Filtro la informacion; 
      
      modeloFiltro = len(modelo); 
      
      modeloFiltro2 = modelo.isspace(); 
      
      # Valido los filtros;
    
      if modeloFiltro > 0 and  modeloFiltro2 == False:
        
        # Agrego el modelo;
        
        vehiculo.append(f"Modelo: {modelo}"); 
        
        # Solicito año;
      
        año = int(input("\nPor favor, digite el año del vehiculo: ")); 
        
        # Valido año;
        
        if año > 1900:
          
          # Agrego el año;
          
          vehiculo.append(f"Año: {año}"); 
          
          # Solicito año;
          
          precio = float(input("\nPor favor, digite el precio de el vehiculo: ")); 
          
          # Valido año;
          
          if precio > 0:
            
            # Agrego precio;
            
            vehiculo.append(f"Precio: {precio}"); 

            # Agrego disponibilidad, por defecto false;

            disponibilidadFiltro = bool(input("\n¿El vehiculo esta disponible para la venta? True / False: ")); 

            # Agrego condiciones para disponibilidad;

            if disponibilidadFiltro == False or disponibilidad == [] and no_Disponble == False:

              # Agrego disponibilidad por defecto; 

              vehiculo.append(f"¿El vehiculo esta disponible para la venta?: {no_Disponble}"); 

              # Falto agregar opcion para que no se duplicaran los vehiculos al ingresar uno nuevo

            # De lo contrario lanzo mensaje de error para que use la opcion 4;

            else:

              print("\n¡ERROR!, para cambiar disponibilidad seleccione la opcion 4");  
             
            # Mensaje informativo;
            
            print("\nVehiculo agregado"); 
        
            # De lo contrario;
            
          else:
            
            # Mensaje informativo, elimino valor agregado;
          
            print("\n¡ERROR!, precio invalido por favor reintente"); 
            
            vehiculo.remove(precio); 
            
        # De lo contrario;  
              
        else:
          
          # Mensaje informativo, elimino valor agregado;
          
          print("\n¡ERROR!, año invalido por favor reintente"); 
          
          vehiculo.remove(año); 
           
       # De lo contrario;
        
      else:
        
        # Mensaje informativo, elimino valor agregado;
      
        print("\n¡ERROR!, modelo invalido por favor reintente"); 
        
        vehiculo.remove(modelo); 
        
      # Agrego vehiculo a vehiculos 
         
      Vehiculos.append(vehiculo); 

    # Si opcion 2;

    if opcion == 2:

      busqueda = str(input("\nEscriba el modelo que desea buscar: ")); 
    
      if busqueda.find == Vehiculos(modelo):

        print(f"\nModelo encontrado: {vehiculo(modelo)}"); 

      # Falta de logica a la hora de realizar el filtro 

    if opcion == 5:
        
      print(f"\nVehiculos disponibles: {Vehiculos}"); 
      
    # Si opcion 6;
    
    if opcion == 6:
      
      # Mensaje de despedida;
      
      print("\nGracias por usar el sistema. Vuelva Pronto"); 
      
      # Cierre;
      
      break; 
    
  # Manejo de errores;  
      
  except Exception: 
    
    # Mensaje informativo;
    
    print("\n¡ERROR!, digite una opcion valida"); 
