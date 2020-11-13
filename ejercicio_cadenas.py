
email=input("Ingrese su email: ")
arroba=email.count("@")

if arroba!=1 or email.rfind("@")==(len(email)-1) or email.find("@")==0:
    print("Email incorrecto")
else:
    print("Email correcto")

