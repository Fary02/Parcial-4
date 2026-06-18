# Se crean los arrays a utilizar;

pacientes = []; 

paciente = []; 

rut = []; 

nombre = []; 

edad = []; 

temperatura = []; 

atendido = []; 

# Creacion de function menu;

def menu_Principal():
  
  print("\n*****Menu Principal*****"); 
  print("1. Agregar paciente"); 
  print("2. Buscar paciente"); 
  print("3. Eliminar paciente"); 
  print("4. Actualizar estado"); 
  print("5. Mostrar pacientes"); 
  print("6. Salir"); 

# Creacion de function para agregar paciente;
  
def agregar_Paciente():

  # Solicitud de datos;
  
  nombre_Paciente = str(input("\nPor favor, digite su nombre: ")); 
  
  rut_Paciente = str(input("\nPor favor, digite su rut SIN DIGITO verificador: ")); 

  # Filtro para el rut;
  
  rutLen = len(rut_Paciente)

  # Validacion de datos;
  
  if rutLen == 8 and rut_Paciente.isdigit() and nombre_Paciente.strip() != "" and nombre_Paciente.isalpha():

    # Se solicita edad;

    edad_Paciente = int(input("\nPor favor, digite su edad: ")); 

    # Validacion de edad;

    if edad_Paciente > 0 and edad_Paciente.is_integer() and edad_Paciente <= 100:

      # Se solicita temperatura;

      temperatura_Paciente = float(input("\nPor favor, digite su temperatura: ")); 

      # Validacion de temperatura;

      if temperatura_Paciente >= 35.0 and  temperatura_Paciente <= 42.0:

        # Asignacion predeterminada de estado de atencion;

        atendido_Paciente = False; 

        # Comienza a juntar la informacion;

        atendido.append(atendido_Paciente); 

        nombre.append(nombre_Paciente); 

        rut.append(rut_Paciente); 

        edad.append(edad_Paciente); 

        temperatura.append(temperatura_Paciente); 

        # Se crea un objeto con la informacion recopilada

        paciente = {
          
          "nombre": nombre,

          "Rut": rut,

          "Edad": edad,

          "Temperatura": temperatura,

          "Atendido": atendido

        }; 

        # Se adjunta el objeto al array de pacientes;

        pacientes.append(paciente); 
      
      # Comienzo de condiciones no cumplidas;
    
      else:

        return print("\n¡ERROR!, la temperatura debe estar entre los 35 a 42 grados"); 
    
    else:

      return print("\n¡ERROR!, debe ingresar un numero entero mayor que 0 y menor o igual a 100"); 
  
    # Mensaje de confirmacion al registrar exitosamente un paciente;

    return print(f"\nPaciente: {nombre_Paciente}, Rut: {rut_Paciente}, Edad: {edad}, Temperatura: {temperatura}, Atendido: {atendido} ¡Registrado Exitosamente!"); 

  else:

     return print("\n¡ERROR!, debe ingresar un valor valido"); 

# Creacion de function para mostrar los pacientes;

def mostrar_Pacientes():

  # Retorna lo siguiente;

  return print(f"\nPacientes: {pacientes}"); 

# Comienzo de ciclo while;

while True:

  # Intenta;
  
  try:

    # Se llama a la function y muestra el menu;
    
    menu_Principal(); 

    # Solicitud de ingreso de opcion;
    
    opcion = int(input("\nPor favor, digite una opcion: ")); 

    # Si opcion;
    
    if opcion == 1:
     
     # Se llama a la function para agregar pacientes;
      
     agregar_Paciente(); 

    # Si seleccionamos la opc 5 y el array de pacientes no esta vacio;
  
    elif opcion == 5 and pacientes != []:
      
      # Mostramos los pacientes;

      mostrar_Pacientes(); 
    
    # Si seleccionamos la opc 5 y el array esta vacio;
  
    if opcion == 5 and pacientes == []:

      # Imprime el mensaje de error, con informacion al respecto;

      print("\n¡ERROR!, usted no posee pacientes agreguelos en la opcion 1"); 

    # Se realiza la opcion de salida; 
  
    elif opcion == 6:

      print("\n*****¡Muchas gracias por ocupar el servicio, vuelva pronto!*****"); 

      # Cierre de programa;
  
      break; 
  
  # Manejo de excepciones con valores incorrectos;

  except ValueError:
    
    print("\n¡ERROR!, digite un valor valido"); 