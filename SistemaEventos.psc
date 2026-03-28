Algoritmo SistemaEventos
	
    Definir opcion, i, totalEventos Como Entero
	//La variable i es un índice
    Definir nombreEvento, ubicacion Como Cadena
    Definir capacidadMax Como Entero
    
    // Arreglos
    Dimension eventos[10]
    Dimension ubicaciones[10]
    Dimension capacidades[10]
    Dimension asistentes[10]
    Dimension estados[10]
    
    totalEventos <- 0
    
    Repetir
        
        Escribir "=============================="
        Escribir "   SISTEMA DE EVENTOS"
        Escribir "=============================="
        Escribir "1. Crear Evento"
        Escribir "2. Registrar Asistente"
        Escribir "3. Mostrar Eventos"
        Escribir "4. Salir"
        Escribir "=============================="
        
        Leer opcion
        
        Segun opcion Hacer
			1:
                // CREAR EVENTO
                
                
            2:
                // REGISTRAR ASISTENTE
                // VALIDAR SI HAY EVENTOS
                
                
            3:
                // MOSTRAR EVENTOS
                // VALIDAR SI HAY EVENTOS
                
                
            4:
                Escribir "Saliendo del sistema..."
                
            De Otro Modo:
                Escribir "Opcion invalida, intente de nuevo"
                
        FinSegun
        
    Hasta Que opcion = 4
FinAlgoritmo
