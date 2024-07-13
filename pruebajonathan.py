trabajadores = {
    "nombre": ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"],
    "sueldo":[]
    }


from statistics import mean , geometric_mean
from random import randint 
def menu ():
    print ("1) asignar sueldos aleatorios ")
    print ("2) clasificar sueldos ")
    print ("3)  ver estadisticas")
    print ("4) reporte de sueldos ")
    print ("5) reporte de salir del programa ")
    
    
opc = 0
while opc !=5:
    menu()
    opc=int(input("ingrese opcion deseada:"))
    try:
        
        if opc == 1:
            for t in trabajadores["nombre"]:  
                print (f"{trabajadores["sueldo"].append((randint(300000,2500000 )))} ") 
            print ("sueldos agregados: ")
        elif opc == 2:
            for i in trabajadores["sueldo"]:
                if i < 800000:
                    
                    print (f"sueldos menosres a 800000{i}")
                if i < 2000000 and  i > 800000:
                        print (f"sueldos entre 800000 y 2000000,{i}")
                if i > 2000000:
                            print (f"sueldos mayores a 2000000",{i})
        elif opc == 3: 
                print ("sueldo minimo")
                print (min(trabajadores["sueldo"]))
                print ("sueldo maximo")
                print (max(trabajadores["sueldo"]))
                print ("sueldo promedio")
                print (mean(trabajadores["sueldo"]))
                print ("media geometrica")
                print (geometric_mean(trabajadores["sueldo"]))
        elif opc == 4:
           print ("lol")
            
                
        elif opc == 5:
            print ( "saliendo del programa ......")          
        else:
            print("ingrese solo numeros")
    except:
        print ("error vuelva a intentarlo")
    
    
      
            
            
    


      