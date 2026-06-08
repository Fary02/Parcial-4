# Mensaje de bienvenida;

print("\n*****Bienvenido/a docente*****")

# Function para calcular promedio;

def promedio(a, b):

  # Retorno de function;

  return a / b; 

# Se inician las variables para la opcion 2;

nombre = []; 

asignaturas = []; 

notas = []; 

promedio_Notas = []; 
 
# Creacion de menu;

while True:
    
  print("\nMenu registro de notas"); 

  print("\n1. Ingresar asignaturas y notas"); 
  print("2. Consultar promedio"); 
  print("3. Salir"); 

  # Intenta;

  try:

    # Solicitud de opcion; 

    opcion = int(input("\nDigite una opcion: "));   
    
    if opcion == 1: 

      # Solicitud de nombre;

      nombre = str(input("\nDigite el nombre del alumno: ")); 

      # Ciclo for in para registro de asignatura y nota;
      
      for i in range (5):

        # Contador para tener informacion sobre el registro;

        print(f"\nRegistro {i + 1} de 5"); 
        
        # Solicitud de datos; 

        asignatura = str(input("\nDigite el nombre de la asignatura: ")); 

        nota = float(input("\nDigite la nota de la asignatura: ")); 

        # Si las notas cumplen la condicion;

        if nota >= 1.0 and nota <= 7.0:

          # Coloca la asignatura y nota al final del array;

          asignaturas.append(asignatura); 

          notas.append(nota); 
        
        # Si no se cumple la condicion;
    
        else: 

          # Mensaje de error;

          print("\n¡ERROR!, solo se aceptan notas superiores a 1.0 y inferiores a 7.0"); 

          # Vuelta al menu principal;

          break; 
    
    # Si opcion 2;

    elif opcion == 2:

      # Si no se registra el nombre;

      if len(nombre) <= 0:

        # Mensaje de error;

        print("\n¡ERROR!, primero debe seleccionar la opcion 1"); 

      # De lo contrario crea un objeto con el resumen del alumno y ocupa round para la precision de decimales;
        
      else:

        promedio_Notas = promedio(sum(notas), len(notas)); 

        informacion = {

          "Alumno": nombre,

          "Asignaturas": asignaturas,

          "Notas": notas,

          "Promedio": round(promedio_Notas, 1)

        }; 

        # Mensaje con la informacion de el alumno;

        print(f"\nEsta es la informacion del alumno: {informacion}"); 
    
    # Si opcion 3;

    elif opcion == 3:

      # Mensaje de aviso;

      print("\n***** Finalizando programa *****"); 

      # Cierre de programa;
        
      break; 

    # En caso de digitar una opcion numerica distinta;
  
    else:

      # Mensaje de error;

      print("\n¡ERROR!, digite una opcion valida"); 

  # except Exception para mayor y mejor manejo de erorres;
  
  except Exception:

    # Mensaje de error;

    print("\n¡ERROR!, digite una opcion valida"); 