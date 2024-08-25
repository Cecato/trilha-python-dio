import re

def validar_cpf(cpf):
    return re.match(r"^\d{11}$", cpf) is not None
