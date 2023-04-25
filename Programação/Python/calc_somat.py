import sympy


lim_inferior = None
lim_superior = None

def clear ():
    print("\n" * 130)

def reIS():
    try:
        res = int(res)
        if res == 1:
            obter_inputs()
            
        if res == 0:
            obter_inputs()
            
        else:
            print("O valor deve ser 0 ou 1, digite novamente!")
            return
    
    except ValueError:
        print("Tipo de dado incorreto, digite novamente!")
        return False, None

def validar_lim_superior(lim_superior, lim_inferior):
    try:
        lim_superior = int(lim_superior)
        if lim_superior <= lim_inferior:
            print("O limite superior deve ser maior que o inferior")
            return False, None
        else:
            return True, lim_superior

    except ValueError:
        print("Tipo de dado incorreto, digite novamente!")
        return False, None

def validar_lim_inferior(lim_inferior):
    try:
        lim_inferior = int(lim_inferior)
        if lim_inferior > 1:
            return True, lim_inferior
        else: 
            print("O limite inferior tem que ser maior que 1, digite novamente!")
            return False, None
        
    except ValueError:
        print("Tipo de dado incorreto, digite novamente!")
        return False, None

def validar_termo_geral(termo_geral):
    try:
        if "n" in termo_geral:
            expr = sympy.sympify(termo_geral)
            try:
                if not isinstance(expr, sympy.Expr) or 'n' not in str(expr):
                    raise ValueError
                return True, termo_geral
            except:
                return False, None     
        else:
            print("Use n como variavel!")
    except:
        return False, None
    
def resolverSomatrio():
    pass

def obter_inputs(lim_superior, lim_inferior):
    '''while lim_inferior == None:
        lim_inferior = input("Digite o limite inferior: ")
        clear()
        valido, lim_inferior = validar_lim_inferior(lim_inferior)
        if valido:
            break
        else:
            pass
        
    while lim_superior == None:
        lim_superior = input("Digite o limite superior: ")
        clear()
        valido, lim_superior = validar_lim_superior(lim_superior, lim_inferior)
        if valido:
            break
        else:
            pass'''
        
    while True:
        termo_geral = input("Digite o termo geral usando \"n\" como variavel: ")
        valido, termo_geral = validar_termo_geral(termo_geral)
        if valido:
            print(valido)
            #resolverSomatrio()
        #else:
           # pass  
         
clear()
obter_inputs(lim_superior, lim_inferior)