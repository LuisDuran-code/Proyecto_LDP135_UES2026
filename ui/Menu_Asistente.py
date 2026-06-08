class MenuAsistente:

    def __init__(self, asistente_service, evento_service):

        self.asistente_service = asistente_service
        self.evento_service = evento_service

    def mostrar_menu(self):

        while True:

            print("\n=================================")
            print("    GESTIÓN DE ASISTENTES")
            print("=================================")
            print("1. Registrar Asistente")
            print("2. Mostrar Asistentes")
            print("3. Buscar Asistente")
            print("4. Regresar")
            print("=================================")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_asistente()

            elif opcion == "2":
                self.mostrar_asistentes()

            elif opcion == "3":
                self.buscar_asistente()

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")

    # =====================================
    # REGISTRAR ASISTENTE
    # =====================================

    def registrar_asistente(self):

        eventos = self.evento_service.obtener_eventos()

        if len(eventos) == 0:
            print("\nNo hay eventos registrados.")
            return

        print("\nEventos disponibles:")

        for i, evento in enumerate(eventos):

            print(
                f"{i + 1}. {evento.nombre} "
                f"- Estado: {evento.estado}"
            )

        try:

            indice = int(
                input("\nSeleccione el número del evento: ")
            ) - 1

            if indice < 0 or indice >= len(eventos):

                print("Evento inválido.")
                return

        except ValueError:

            print("Debe ingresar un número.")
            return

        evento = eventos[indice]

        nombre = input("Nombre del asistente: ")

        try:

            edad = int(input("Edad: "))

        except ValueError:

            print("La edad debe ser numérica.")
            return

        correo = input("Correo electrónico: ")

        try:

            self.asistente_service.registrar_asistente(
                nombre,
                edad,
                correo,
                evento
            )

            print("\nAsistente registrado correctamente.")

        except ValueError as error:

            print(f"\nError: {error}")

    # =====================================
    # MOSTRAR ASISTENTES
    # =====================================

    def mostrar_asistentes(self):

        asistentes = self.asistente_service.mostrar_asistentes()

        if len(asistentes) == 0:

            print("\nNo hay asistentes registrados.")
            return

        print("\n===== LISTA DE ASISTENTES =====")

        for asistente in asistentes:

            print(asistente)

    # =====================================
    # BUSCAR ASISTENTE
    # =====================================

    def buscar_asistente(self):

        nombre = input(
            "\nIngrese el nombre del asistente: "
        )

        resultados = self.asistente_service.buscar_asistente(
            nombre
        )

        if len(resultados) == 0:

            print("\nNo se encontraron coincidencias.")
            return

        print("\n===== RESULTADOS =====")

        for asistente in resultados:

            print(asistente)
