import os 


def clear ():
    print("\n" * 130)

def reIS():
    pass

def validar_lim_superior(lim_superior):
    try:
        lim_superior = int(lim_superior)
        return True, lim_superior

    except ValueError:
        print("Tipo de dado incorreto, digite novamente!")
        return False, None

def validar_lim_inferior(lim_inferior):
    try:
        lim_inferior = int(lim_inferior)
        if lim_inferior < lim_superior and lim_inferior != 0:
            return True, lim_inferior
        if lim_inferior > lim_superior:
            while True:
                clear()
                print("O limite inferior deve ser menor que o superior")
                res = input("Deseja alterar o limite inferior(0) ou superior(1)")
                valido, res = reIS(res)
                if valido:
                    if res == 1:
                        lim_superior = None
                        break
                else: break

                    
        if lim_inferior == 0:
            clear ()
            print ("O limite inferior deve ser diferente de 0, digite novamente!")
            return False, None
    except: return False, None

def obter_inputs():
    while True:
        lim_superior = input("Digite o limite superior: ")
        clear()
        valido, lim_superior = validar_lim_superior(lim_superior)
        if valido:
            break
        else:
            pass

    while True:
        lim_inferior = input("Digite o limite inferior: ")
        clear()
        valido, lim_inferior = validar_lim_inferior(lim_inferior)
        if valido:
            break
        else:
            pass
        
    while True:
        regra = input("aaa ") 
        print(regra)
        break        
clear()
obter_inputs()