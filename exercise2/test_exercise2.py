#Criando a função admin_command, que recebe a ferramenta sudo
def admin_command(command, sudo=True):

    if sudo:
        ["sudo"] + command
    return command