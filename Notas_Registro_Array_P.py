# Solicitamos nombre;

nombre = input("Por favor, digita tu nombre: "); 

# Creamos un array para almacenar las notas;

notas = []; 

# Creamos un ciclo para las notas;

for i in range (3):
  
  # Se solicitan las notas;
  
  nota = float(input(f"Ingrese la nota {i + 1} : ")); 
  
  # Se almacenan en notas;
  
  notas.append(nota); 
  
# Se crea la Variable suma;
  
suma = 0; 

# Se crea un bucle para la nota dentro de el array;

for nota in notas:
  
  # Se redefine la variable suma;
  
  suma = suma+ nota; 
  
# Se calcula el promedio;
  
promedio = suma / len(notas); 

# Se genera el resumen del estudiante;

estudiante = {
  
  "Nombre": nombre,
  
  "Notas": notas,
  
  "Promedio": promedio.__round__(1)
  
}; 

# Se imprime el resumen del estudiante;

print("\nResumen"); 

print("____________________________"); 

print("\nNombre:", estudiante["Nombre"]); 

print("Notas:", estudiante["Notas"]); 

print("Promedio:", estudiante["Promedio"]); 