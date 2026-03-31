Algoritmo SistemaEventos
	
    Definir opcion, i, totalEventos Como Entero
	//La variable i es un índice
    Definir nombreEvento, ubicacion, eventos, ubicaciones Como Cadena
    Definir capacidadMax, capacidades, asistentes, estados Como Entero
    
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
                Escribir "==============================";
				Escribir "         CREAR EVENTO         ";
				Escribir "==============================";
				
				Si totalEventos < 10 Entonces
					totalEventos <- totalEventos + 1; 
					
					Escribir "Nombre del evento:";
					Leer eventos[totalEventos]; 
					
					Escribir "Ubicación del evento:";
					Leer ubicaciones[totalEventos];
					
					Escribir "Capacidad maxima de personas:";
					Leer capacidades[totalEventos];
					
					Escribir "";
					Escribir "Evento registrado con éxito";
				SiNo
					Escribir "¡Error! Ha alcanzado el límite máximo de 10 eventos.";
				FinSi
				
				Escribir "";
				Escribir "Presione una tecla para regresar al menú...";
				Esperar Tecla;
                
                
            2:
                // REGISTRAR ASISTENTE
                // VALIDAR SI HAY EVENTOS
                
                
            3:
                Escribir "===============================";
				Escribir "            EVENTOS            ";
				Escribir "===============================";
				
				Si totalEventos = 0 Entonces
					Escribir "No hay ningún evento programado actualmente.";
				SiNo
					Escribir "Los eventos disponibles son:";
					Escribir "";
					
					Para i <- 1 Hasta totalEventos Con Paso 1 Hacer
						Escribir "--- Evento #", i, " ---";
						Escribir "Nombre: ", eventos[i];
						Escribir "Ubicación: ", ubicaciones[i];
						Escribir "Capacidad máxima: ", capacidades[i];
						Escribir "";
					FinPara
				FinSi
				
				Escribir "Presione una tecla para regresar al menú...";
				Esperar Tecla;
                
                
            4:
                Escribir "Saliendo del sistema..."
                
            De Otro Modo:
                Escribir "Opcion invalida, intente de nuevo"
                
        FinSegun
        
    Hasta Que opcion = 4
FinAlgoritmo
