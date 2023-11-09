from funciones import verificar_usuario
from funciones import registrar_usuario
from funciones import registro_empresa


print("\n¡¡ ＢＩＥＮＶＥＮＩＤＯＳ Ａ ＬＡ ＣＡＬＣＵＬＡＤＯＲＡ ＤＥ ＨＯＲＭＩＧＯＮ  !!")

bandera = False
while not bandera:
    print("\nSistema de Registro e Inicio de Sesión".upper())

    accion = input("\n¿Desea registrarse (R) o iniciar sesión (I)? ").strip().lower()

    if accion == "r":
        nombre = input("✅ Ingrese su nombre: ")
        correo = input("✅ Ingrese un Correo electrónico: ")
        contrasena = input("✅ Elija su Contraseña: ")
        registrar_usuario(nombre, correo, contrasena)
        print("Su registro se realizo con exito 🥳, ahora intente iniciar sesión..")
    elif accion == "i":
        correo = input("\n➡️ Correo electrónico: ")
        contrasena = input("➡️ Contraseña: ")

        usuario_valido = verificar_usuario(correo, contrasena)

        if usuario_valido:
            print(f"\nInicio de sesión exitoso. Bienvenido 👋, {usuario_valido}!")
            bandera = True
        else:
            print("❌ Usuario o contraseña incorrectos, intente de nuevo...")
    else:
        print("❌ Opción incorrecta, vuelva a intentarlo...")

nombre = usuario_valido  

while bandera:
    unidad = input("\nSeleccione unidad a trabajar:\n\n📐 CENTIMETROS=cm\n📐 METROS=m\n📐 PIES=pies\n\n➡️  Su opcion: ")

    if unidad == "cm":
        factor = 1000000
    elif unidad == "m":
        factor = 1
    elif unidad == "pies":
        factor = 35.3147
    else:
        print("❌ Unidad ingresada no válida, vuelva a intentarlo..")
        continue

    try:
        longitud = float(input(f"\nIngrese la longitud (en {unidad}): "))
        anchura = float(input(f"Ingrese el ancho (en {unidad}): "))
        altura = float(input(f"Ingrese la altura (en {unidad}): "))

        resultado_total = round((longitud * anchura * altura) / factor, 2)
        resultado_total_recumido = "{:.2f}".format(resultado_total)

        pedido = {
            "• Cliente": nombre,
            "• Unidad": unidad,
            "• Longitud": longitud,
            "• Ancho": anchura,
            "• Altura": altura,
            "• Metros cúbicos necesarios de hormigón": resultado_total_recumido
        }

        print("\n→ Datos del pedido:\n")
        for clave, valor in pedido.items():
            print(f"{clave}: {valor}")

        with open(f"resultados cliente {nombre}.txt", 'a') as archivo_cliente:
            archivo_cliente.write("Datos del pedido:\n")
            for clave, valor in pedido.items():
                archivo_cliente.write(f"{clave}: {valor}\n")
            archivo_cliente.write("--------------------------------------\n")

        registro_empresa(pedido)

        print("\nSus resultados han sido registrados con éxito 🤩\n".upper())

        continuar = input("¿Desea cargar otros datos (Sí/No)? ").strip().lower()
        if continuar != "si":
            print("\n✅  El programa se cerrará, ¡Gracias por utilizarlo! \n")
            bandera = False
    except ValueError:
        print("\n⚠️  Error: Solo valores numéricos, vuelva a intentarlo...")
