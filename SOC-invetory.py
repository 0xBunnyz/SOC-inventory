''''
Developed by Johnathan Frabetti from the SOC team
'''
import os
import platform
import subprocess

# Aqui irei adcionar a funcionalidade de criar uma tarefa no Windows para se auto executar mensalemnte
# Aqui irei adcionar a funcionalidade de criar uma CRON no Ubuntu para se auto executar mensalmente
# Aqui irei adcionar a funcionalidade de criar uma CRON no Red Hat para se auto executar mensalmente

# Função para obter os softwares instalados no Windows
def get_installed_software_windows():
    output = subprocess.check_output("wmic product get name,version", shell=True)
    software = output.decode()
    return software

# Função para obter os softwares instalados no Ubuntu
def get_installed_software_ubuntu():
    software_list = []
    output = subprocess.check_output("apt list --installed", shell=True)
    software = output.decode().split("\n")
    for s in software:
        s = s.strip()
        if s != "":
            s = s.split("/")
            name = s[0]
            version = s[1]
            path = "N/A"
            software_list.append({"name": name, "version": version, "path": path})
    return software_list

# Função para obter os softwares instalados no Red Hat
def get_installed_software_redhat():
    software_list = []
    output = subprocess.check_output("dnf list installed", shell=True)
    software = output.decode().split("\n")
    for s in software:
        s = s.strip()
        if s != "" and "Installed" not in s:
            s = s.split(" ")
            name = s[0]
            version = s[1]
            path = "N/A"
            software_list.append({"name": name, "version": version, "path": path})
    return software_list

# Verifica o tipo do sistema operacional
if platform.system() != "Windows":
    dist = platform.linux_distribution()[0]
    if dist == "Ubuntu":
        software_list = get_installed_software_ubuntu()
        file_name = "ubuntu-softwares.txt"
    elif dist == "Fedora" or dist == "Red Hat Enterprise Linux":
        software_list = get_installed_software_redhat()
        file_name = "redhat-softwares.txt"
    else:
        print("Este script funciona apenas para sistemas Ubuntu e Red Hat")
        exit()
else:
    software_list = get_installed_software_windows()
    file_name = "windows-softwares.txt"


with open(file_name, "w") as f:
    for software in software_list:
        f.write(software)

print("""
  ▄████████  ▄██████▄   ▄████████     ███      ▄██████▄   ▄██████▄   ▄█       
  ███    ███ ███    ███ ███    ███ ▀█████████▄ ███    ███ ███    ███ ███       
  ███    █▀  ███    ███ ███    █▀     ▀███▀▀██ ███    ███ ███    ███ ███       
  ███        ███    ███ ███            ███   ▀ ███    ███ ███    ███ ███       
▀███████████ ███    ███ ███            ███     ███    ███ ███    ███ ███       
         ███ ███    ███ ███    █▄      ███     ███    ███ ███    ███ ███       
   ▄█    ███ ███    ███ ███    ███     ███     ███    ███ ███    ███ ███▌    ▄ 
 ▄████████▀   ▀██████▀  ████████▀     ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ 
                                                                     ▀
""")
print("Lista de software salva em --> {}".format(file_name))
os.system("pause")
# Aqui você pode adicionar o código para carregar o arquivo na conta de armazenamento do Azure