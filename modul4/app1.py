def check_passwd():
    requires_chars = ["!", "@", "%"]
    passwd = input("Introduceti o parola : ")
    print(passwd)
    if len(passwd) < 7:
        print("Parola cu lungime gresita")
        check_passwd()
    else:

        for character in requires_chars:
            if character in passwd:
                break
        else:
            print("Parola trebuie sa contina : ! @ %")
            check_passwd()
    print('test')

check_passwd()