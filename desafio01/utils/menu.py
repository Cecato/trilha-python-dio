import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def formatar_conta(conta):
    return f"""\
    Agência:\t{conta['agencia']}
    C/C:\t\t{conta['numero_conta']}
    Titular:\t{conta['usuario']['nome']}
    """
