# Función para verificar credenciales
def verificar_usuario(correo, contrasena):
    with open("usuarios.txt", "r") as archivo_verificador:
        for linea in archivo_verificador:
            valores = linea.strip().split(",")
            if len(valores) == 3:
                nombre, usuario, clave = valores
                if usuario == correo and clave == contrasena:
                    return nombre  
    return None  

def registrar_usuario(nombre, correo, contrasena):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{correo},{contrasena}\n")


def registro_empresa(pedido):
    with open("Registros Empresa.txt", 'a') as archivo_registro_empresa:
        archivo_registro_empresa.write("Datos del pedido:\n")
        for clave, valor in pedido.items():
            archivo_registro_empresa.write(f"{clave}: {valor}\n")
        archivo_registro_empresa.write("------------------------------------------\n")