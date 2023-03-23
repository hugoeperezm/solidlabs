import re 


DOMAINS = ['gmail.com', 'yahoo.com', 'hotmail.com', 'msn.com']
MAX_EMAIL_LENGHT = 254


def main():
    email = input("\nIngrese su direccion de correo electrónico: ")
    if validate_email(email):
        print(f"La direccion {email} es valida.")
    else:
        print(f"La direccion {email} no es correcta.")



def validate_email(email):    
    # Verificar que el correo tenga longitud razonable
    if len(email) > MAX_EMAIL_LENGHT:
        return False

    # Verificar que correo tenga el simbolo @
    if '@' not in email:
        return False
    
    # Verificar que el correo tenga un dominio valido
    domain = email.split('@')[1]
    if domain not in DOMAINS:
        return False
    
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(pattern, email):
        return False

    return True


if __name__ == "__main__":
    main()