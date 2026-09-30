nombre_correcto = "Ovidio"
contrasena_correcta = "1234"

usuario = input("Ingese su nombre de usuario: ")
contrasena = input("Ingrese su contrasena: ")

if nombre_correcto==usuario and contrasena_correcta==contrasena:
    print("==LOGIN LAB==")
    print("Bienvendio a la plataforma", nombre_correcto)
else:
    print("Usuario o contrasena incorrecta")
