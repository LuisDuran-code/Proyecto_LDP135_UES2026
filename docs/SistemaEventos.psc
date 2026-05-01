Algoritmo SistemaEventos
	
    Definir opcion, i, totalEventos Como Entero
	// i es un indice para recorrer los arreglos
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
                Escribir "=============================="
				Escribir "         CREAR EVENTO         "
				Escribir "=============================="
				
				Si totalEventos < 10 Entonces
					totalEventos <- totalEventos + 1
					
					Escribir "Nombre del evento:"
					Leer eventos[totalEventos] 
					
					Escribir "Ubicación del evento:"
					Leer ubicaciones[totalEventos]
					
					Repetir
						Escribir "Capacidad maxima de personas:"
						Leer capacidadMax
						Si capacidadMax <= 0 Entonces
							Escribir "Error: la capacidad debe ser mayor que 0"
						FinSi
					Hasta Que capacidadMax > 0
					
					capacidades[totalEventos] <- capacidadMax
					asistentes[totalEventos] <- 0
					estados[totalEventos] <- 0 // 0 = abierto
					
					Escribir ""
					Escribir "Evento registrado con éxito"
				SiNo
					Escribir "¡Error! Ha alcanzado el límite máximo de 10 eventos."
				FinSi
				
				Escribir ""
				Escribir "Presione una tecla para regresar al menú..."
				Esperar Tecla
                
            2:
                Escribir "==============================="
				Escribir "      REGISTRAR ASISTENTE      "
				Escribir "==============================="
				
                // VALIDAR SI HAY EVENTOS
				Si totalEventos = 0 Entonces
					Escribir "No hay eventos disponibles."
				SiNo
					// Mostrar eventos
					Escribir "Seleccione el número del evento:"
					Para i <- 1 Hasta totalEventos Con Paso 1 Hacer
						Si estados[i] = 0 Entonces
							Escribir i, ". ", eventos[i], " (Abierto)"
						SiNo
							Escribir i, ". ", eventos[i], " (Cerrado)"
						FinSi
					FinPara
					
					Leer i
					// Validar opcion
					Si i < 1 O i > totalEventos Entonces
						Escribir "Opción invalida"
					SiNo
						//Validar si ya esta lleno
						Si asistentes[i] < capacidades[i] Entonces
							asistentes[i] <- asistentes[i] + 1
							Escribir "Asistente registrado con éxito."
							
							//Cierre automatico
							Si asistentes[i] = capacidades[i] Entonces
								estados[i] <- 1 //1 = cerrado
								Escribir "El evento ha sido cerrado porque alcanzo su capacidad máxima."
							FinSi
						SiNo
							Escribir "El evento ya esta lleno."
						FinSi
					FinSi
				FinSi
				
                Escribir ""
				Escribir "Presione una tecla para regresar al menú..."
				Esperar Tecla
                
            3:
                Escribir "==============================="
				Escribir "            EVENTOS            "
				Escribir "==============================="
				
				Si totalEventos = 0 Entonces
					Escribir "No hay ningún evento programado actualmente."
				SiNo
					Escribir "Los eventos disponibles son:"
					Escribir ""
					
					Para i <- 1 Hasta totalEventos Con Paso 1 Hacer
						Escribir "--- Evento #", i, " ---"
						Escribir "Nombre: ", eventos[i]
						Escribir "Ubicación: ", ubicaciones[i]
						Escribir "Capacidad máxima: ", capacidades[i]
						Escribir "Asistentes: ", asistentes[i]
						Si estados[i] = 0 Entonces
							Escribir "Estado: Abierto"
						SiNo
							Escribir "Estado: Cerrado"
						FinSi
						Escribir ""
					FinPara
				FinSi
				
				Escribir "Presione una tecla para regresar al menú..."
				Esperar Tecla
                
            4:
                Escribir "Saliendo del sistema..."
                
            De Otro Modo:
                Escribir "Opcion invalida, intente de nuevo"
                
        FinSegun
        
    Hasta Que opcion = 4
FinAlgoritmo
