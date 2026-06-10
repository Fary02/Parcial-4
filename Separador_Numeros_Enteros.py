# Mensaje bienvenida;

print("\n*****¡Hola, bienvenido/a!*****"); 

# Separador visual de mensaje;

print("-" * 30); 

# Inicializacion de arrays;

numeros = []; 

numeros_Pares = []; 

numeros_Impares = []; 

# Functions para separar los numeros;

def numero_Par():

  # for in a numeros para buscar los pares;

  for i in numeros:

    if i % 2 == 0:

      # Y los coloca en su array correspondiente;

      numeros_Pares.append(i); 

def numero_Impar(): 

  # for in a numeros para buscar los impares;

  for i in numeros:

    if i % 2 == 1:

      # Y los coloca en su array correspondiente;

      numeros_Impares.append(i); 

# Inicio de programa;

while True:
  
  # Intenta;
  
  try: 
    
    # Menu;
  
    print("\n*****Menu*****"); 
    print("1. Comenzar"); 
    print("2. Mostrar resultados"); 
    print("3. Finalizar programa"); 
    
    # Solicitud de opcion;
  
    opcion = int(input("\nPor, favor digite una opcion: ")); 
    
    # Si opcion 1;
    
    if opcion == 1:

      # Se pregunta al usuario, para agregar dinamismo;

      eleccion = int(input("\n¿Cuantos numeros ENTEROS deseas ocupar?: ")); 
      
      # For in para los numeros;

      for i in range(eleccion):
        
        # Aviso de cantidad de numeros restantes a digitar;
        
        print(f"\n¡Registro {i + 1} de {eleccion}!"); 

        # Solicitud de ingreso de numeros; 
    
        numero = int(input("\nPor, favor Digite SOLO numeros enteros:  ")); 

        # Coloca todos los numeros en su array correspondiente; 
  
        numeros.append(numero); 

        # Mensaje informativo con espaciado correspondiente;
      
        print("\nLista actual de numeros: ", *numeros, sep = " "); 
    
    # Si opcion 2;

    elif opcion == 2:

      # Si no hay numeros guardados imprime el error;

      if len(numeros) == 0:

        print("\n¡ERROR!, aun no hay numeros guardados. Elige la opcion 1 primero."); 
      
      # De lo contrario;

      else:

        # Muestra todos los resultados, por separado y con su espaciado correspondiente;

        numero_Par(); 

        numero_Impar(); 

        print("\nNumeros ingresados:", *numeros, sep = " "); 

        print("-" * 30); 

        print("\nNumeros pares:", *numeros_Pares, sep = " "); 

        print("-" * 30); 

        print("\nNumeros impares:", *numeros_Impares, sep = " "); 
    
        print("-" * 30);  
    
    # Si opcion 3;

    elif opcion == 3:

      # Mensaje de finalizacion;

      print("\n¡Programa finalizado!"); 

      # Termino de ciclo;

      break

    # De lo contrario a las anteriores opciones;

    else:

      # Mensaje de error;

      print("\n¡ERROR!, opcion invalida. Selecciona 1, 2 o 3."); 

  # except Exception para manejo de errores;

  except Exception:
  
    print("\n¡ERROR!, digite una opcion valida"); 