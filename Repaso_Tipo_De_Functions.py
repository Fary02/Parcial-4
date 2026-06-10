# Function sin argumento y con return implicito;

def saludo():
  
  print("\n¡Hola, bienvenido/a!"); 
  
saludo(); 

# Function sin argumento y con return explicito;

def saludo():
  
   return print("\n¡Hola, bienvenido/a!"); 
  
saludo(); 

# Function con argumento y con return implicito;

nombre = str(input("\nDigita tu nombre: ")); 

def saludo(nombre):
  
  print(f"\n¡Hola {nombre}, bienvenido/a!"); 
  
saludo(nombre); 

# Function con argumento y con return explicito;

numero1 = int(input("\nDigita un numero: ")); 

numero2 = int(input("\nDigita otro numero: ")); 

def suma(a, b):
  
  return a + b; 

print(f"\n¡Hola el resultado es: {suma(numero1, numero2)}!"); 