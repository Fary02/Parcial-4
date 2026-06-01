# Mensaje de bienvenida;

print("\n*****Bienvenido/a docente*****")

# Function para calcular promedio;

def promedio(a, b, c, d, e, f):

  # Retorno de function;

  return (a + b + c + d + e) / f; 

# Se inician las variables para la opcion 2;

nombre = None; 

notas = None; 

promedio_Notas = None; 

asignatura_1 = None; 

asignatura_2 = None; 

asignatura_3 = None; 

asignatura_4 = None; 

asignatura_5 = None; 

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

    # Si opcion 1;

    if opcion == 1:

      # Solicitud de datos;

      nombre = str(input("\nDigite el nombre de el alumno: ")); 

      asignatura_1 = str(input("\nDigite el nombre de la asignatura: ")); 

      Nota_1 = float(input("Digite la nota de la asignatura: ")); 

      asignatura_2 = str(input("Digite el nombre de la segunda asignatura: ")); 

      Nota_2 = float(input("Digite la nota de la asignatura: ")); 

      asignatura_3 = str(input("Digite el nombre de la tercera asignatura: ")); 

      Nota_3 = float(input("Digite la nota de la asignatura: ")); 

      asignatura_4 = str(input("Digite el nombre de la cuarta asignatura: ")); 

      Nota_4 = float(input("Digite la nota de la asignatura: ")); 

      asignatura_5 = str(input("Digite el nombre de la quinta asignatura: ")); 

      Nota_5 = float(input("Digite la nota de la asignatura: ")); 

      # Array con las notas;

      notas = [Nota_1, Nota_2, Nota_3, Nota_4, Nota_5]; 

      # Promedio de notas; 
    
      promedio_Notas = promedio(Nota_1, Nota_2, Nota_3, Nota_4, Nota_5, 5); 

    # Si opcion 2; 

    elif opcion == 2:

      # Si nombre es None arroja el error;

      if nombre is None:

        print("\n¡ERROR!, primero debe seleccionar la opcion 1")

      # De lo contrario crea un objeto con el resumen del alumno;
        
      else:

        informacion = {
      
        "Alumno": nombre,

        "Asignatura 1": asignatura_1,

        "Nota 1": notas[0],

        "Asignatura 2": asignatura_2,

        "Nota 2": notas[1],

        "Asignatura 3": asignatura_3,

        "Nota 3": notas[2],

        "Asignatura 4": asignatura_4,

        "Nota 4": notas[3],

        "Asignatura 5": asignatura_5,

        "Nota 5": notas[4],

        "Promedio": round(promedio_Notas, 1)

        }

        print(f"\nEsta es la informacion de el alumno: {informacion}"); 
    
    # Si opcion 3, mensaje de despedida y aviso de salida de aplicacion;
  
    if opcion == 3:
    
      print("\nGracias por ocupar la aplicacion"); 
  
      print("*****Saliendo de la aplicacion*****"); 

      # Termino;

      break; 
  
  # except Exception para manejo de datos invalidos;
  
  except Exception:
    
    print("¡ERROR!, digite un valor valido"); 