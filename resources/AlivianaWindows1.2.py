import subprocess
import pyfiglet
from termcolor import colored
import os
import datetime

class CommandTool:
    def __init__(self):
        self.commands = {
            "BÁSICOS PARA MANTENIMIENTO": [
                ("1.1", "sfc /scannow", "Escanea y repara archivos del sistema.", self.run_sfc),
                ("1.2", "chkdsk C: /f /r", "Verifica y repara discos duros.", self.run_chkdsk),
                ("1.3", "defrag C: /O", "Desfragmenta el disco C:", self.run_defrag),
                ("1.4", "dism /online /cleanup-image /restorehealth", "Repara la imagen de Windows.", self.run_dism),
                ("1.5", "wuauclt /detectnow", "Busca nuevas actualizaciones de Windows.", self.run_wuauclt),
            ],
            "DISKPART": [
                ("2.1", "list disk", "Lista los discos disponibles.", self.run_list_disk),
                ("2.2", "select disk", "Selecciona un disco (requiere número).", self.run_select_disk),
                ("2.3", "list partition", "Lista las particiones del disco seleccionado.", self.run_list_partition),
                ("2.4", "create partition primary", "Crea una partición primaria.", self.run_create_partition),
                ("2.5", "format fs=ntfs quick", "Formatea la partición seleccionada como NTFS.", self.run_format_partition),
            ],
            "SEGURIDAD": [
                ("3.1", "netsh advfirewall show allprofiles", "Muestra el estado del firewall.", self.run_show_firewall),
                ("3.2", "netsh advfirewall set allprofiles state on", "Activa el firewall.", self.run_enable_firewall),
                ("3.3", "netsh advfirewall set allprofiles state off", "Desactiva el firewall.", self.run_disable_firewall),
                ("3.4", "cipher /w:C", "Elimina datos de forma segura del disco C.", self.run_secure_erase),
            ],
            "ADMINISTRACIÓN DE REDES": [
                ("4.1", "netsh wlan show profiles", "Muestra las redes Wi-Fi guardadas.", self.run_show_wifi_profiles),
                ("4.2", "netsh wlan delete profile name='nombre'", "Elimina una red Wi-Fi guardada.", self.run_delete_wifi_profile),
                ("4.3", "arp -a", "Muestra la tabla ARP.", self.run_arp_table),
                ("4.4", "route print", "Muestra la tabla de enrutamiento.", self.run_route_print),
            ],
            "OPTIMIZACIÓN DEL SISTEMA": [
                ("5.1", "powercfg /hibernate off", "Desactiva la hibernación.", self.run_disable_hibernation),
                ("5.2", "powercfg /hibernate on", "Activa la hibernación.", self.run_enable_hibernation),
                ("5.3", "cleanmgr", "Inicia el Liberador de espacio en disco.", self.run_cleanmgr),
                ("5.4", "schtasks /query", "Lista las tareas programadas.", self.run_list_schtasks),
                ("5.5", "bcdedit /set {current} bootmenupolicy legacy", "Activa el menú de arranque avanzado.", self.run_enable_legacy_boot),
            ],
            "HERRAMIENTAS DE DESARROLLADOR": [
                ("6.1", "systeminfo | findstr /B /C:'OS Name' /C:'OS Version'", "Muestra solo el nombre y la versión del sistema operativo.", self.run_filter_systeminfo),
                ("6.2", "taskkill /F /PID pid", "Finaliza un proceso por su PID.", self.run_taskkill_pid),
                ("6.3", "powershell Get-Process | Sort-Object CPU -Descending", "Lista los procesos ordenados por uso de CPU.", self.run_high_cpu_processes),
                ("6.4", "fc archivo1 archivo2", "Compara dos archivos línea por línea.", self.run_file_compare),
            ],
            "RED": [
                ("7.1", "ipconfig", "Muestra la configuración de red.", self.run_ipconfig),
                ("7.2", "ipconfig /flushdns", "Limpia la caché de DNS.", self.run_flushdns),
                ("7.3", "ping google.com", "Realiza un ping a Google.", self.run_ping),
                ("7.4", "netstat", "Muestra las conexiones de red activas.", self.run_netstat),
                ("7.5", "tracert google.com", "Rastrea la ruta a Google.", self.run_tracert),
                ("7.6", "nslookup google.com", "Consulta DNS para Google.", self.run_nslookup),
            ],
            "ARCHIVOS Y SISTEMA": [
                ("8.1", "tree", "Muestra la estructura de directorios.", self.run_tree),
                ("8.2", "dir", "Lista los archivos y carpetas en el directorio actual.", self.run_dir),
                ("8.3", "tasklist", "Muestra los procesos activos.", self.run_tasklist),
                ("8.4", "taskkill /IM nombre /F", "Finaliza un proceso por nombre.", self.run_taskkill),
                ("8.5", "systeminfo", "Muestra información del sistema.", self.run_systeminfo),
            ],
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_title(self):
        self.clear_screen()
        ascii_banner = pyfiglet.figlet_format("AlivianaWindows 1.2", width=110)
        print(colored(ascii_banner, 'cyan'))
        print(colored("Desarrollador: Iván Ayub. Documentación de comandos en Archivo MicrosoftLinks.txt. Con el fin de fomentar la divulgación y el libre acceso al conocimiento.", 'white'))
        print(colored(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 'cyan'))

    def show_instructions(self):
        print(colored("¡IMPORTANTE!", 'red', attrs=['bold', 'underline']))
        print(colored("EJECUTA ESTE PROGRAMA COMO ADMINISTRADOR.", 'red', attrs=['bold']))
        print(colored("1. Escoge una opción de la lista de comandos.", 'yellow'))
        print(colored("2. Ingresa el número del comando y presiona Enter.", 'yellow'))
        print(colored("3. Escribe 'exit' para salir.", 'yellow'))

    def show_menu(self):
        print(colored("Comandos Disponibles:", 'cyan'))
        for category, commands in self.commands.items():
            print(colored(f"{category}:", 'yellow', attrs=['bold']))
            for cmd in commands:
                print(f"  {colored(cmd[0], 'yellow')}: {colored(cmd[1], 'white')} - {colored(cmd[2], 'green')}")
            print(colored("-" * 50, 'blue'))

    def get_user_choice(self):
        return input(colored("Ingresa el número del comando a ejecutar: ", 'cyan'))

    def run_command(self, choice):
        for category, commands in self.commands.items():
            for cmd in commands:
                if cmd[0] == choice:
                    print(colored(f"\nEjecutando: {cmd[1]}\n", 'white'))
                    cmd[3]()
                    print(colored("\nComando ejecutado correctamente.\n", 'white'))
                    self.log_command(choice, cmd[1])
                    return
        print(colored("Comando no válido. Intenta de nuevo.\n", 'red'))

    def run_subprocess(self, command):
        try:
            process = subprocess.Popen(
                ["cmd", "/c", command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    print(colored(output.strip(), 'cyan'))

            stderr = process.stderr.read()
            if stderr:
                print(colored(stderr.strip(), 'red'))
        except Exception as e:
            print(colored(f"Error: {e}", 'red'))

    def log_command(self, choice, command):
        with open("comandos_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Comando: {choice} - {command}\n")

    def run_sfc(self):
        self.run_subprocess("sfc /scannow")

    def run_chkdsk(self):
        self.run_subprocess("chkdsk C: /f /r")

    def run_defrag(self):
        self.run_subprocess("defrag C: /O")

    def run_dism(self):
        self.run_subprocess("dism /online /cleanup-image /restorehealth")

    def run_wuauclt(self):
        self.run_subprocess("wuauclt /detectnow")

    def run_list_disk(self):
        self.run_subprocess("list disk")

    def run_select_disk(self):
        # Deberías obtener el número del disco de alguna manera (por ejemplo, entrada del usuario)
        disk_number = input("Ingresa el número del disco: ")
        self.run_subprocess(f"select disk {disk_number}")

    def run_list_partition(self):
        self.run_subprocess("list partition")

    def run_create_partition(self):
        self.run_subprocess("create partition primary")

    def run_format_partition(self):
        self.run_subprocess("format fs=ntfs quick")

    def run_show_firewall(self):
        self.run_subprocess("netsh advfirewall show allprofiles")

    def run_enable_firewall(self):
        self.run_subprocess("netsh advfirewall set allprofiles state on")

    def run_disable_firewall(self):
        self.run_subprocess("netsh advfirewall set allprofiles state off")

    def run_secure_erase(self):
        self.run_subprocess("cipher /w:C")

    def run_show_wifi_profiles(self):
        self.run_subprocess("netsh wlan show profiles")

    def run_delete_wifi_profile(self):
        wifi_name = input("Ingresa el nombre de la red Wi-Fi: ")
        self.run_subprocess(f"netsh wlan delete profile name='{wifi_name}'")

    def run_arp_table(self):
        self.run_subprocess("arp -a")

    def run_route_print(self):
        self.run_subprocess("route print")

    def run_disable_hibernation(self):
        self.run_subprocess("powercfg /hibernate off")

    def run_enable_hibernation(self):
        self.run_subprocess("powercfg /hibernate on")

    def run_cleanmgr(self):
        self.run_subprocess("cleanmgr")

    def run_list_schtasks(self):
        self.run_subprocess("schtasks /query")

    def run_enable_legacy_boot(self):
        self.run_subprocess("bcdedit /set {current} bootmenupolicy legacy")

    def run_filter_systeminfo(self):
        self.run_subprocess("systeminfo | findstr /B /C:'OS Name' /C:'OS Version'")

    def run_taskkill_pid(self):
        pid = input("Ingresa el PID del proceso a finalizar: ")
        self.run_subprocess(f"taskkill /F /PID {pid}")

    def run_high_cpu_processes(self):
        self.run_subprocess("powershell Get-Process | Sort-Object CPU -Descending")

    def run_file_compare(self):
        file1 = input("Ingresa el primer archivo: ")
        file2 = input("Ingresa el segundo archivo: ")
        self.run_subprocess(f"fc {file1} {file2}")

    def run_ipconfig(self):
        self.run_subprocess("ipconfig")

    def run_flushdns(self):
        self.run_subprocess("ipconfig /flushdns")

    def run_ping(self):
        self.run_subprocess("ping google.com")

    def run_netstat(self):
        self.run_subprocess("netstat")

    def run_tracert(self):
        self.run_subprocess("tracert google.com")

    def run_nslookup(self):
        self.run_subprocess("nslookup google.com")

    def run_tree(self):
        self.run_subprocess("tree")

    def run_dir(self):
        self.run_subprocess("dir")

    def run_tasklist(self):
        self.run_subprocess("tasklist")

    def run_taskkill(self):
        process_name = input("Ingresa el nombre del proceso a finalizar: ")
        self.run_subprocess(f"taskkill /IM {process_name} /F")

    def run_systeminfo(self):
        self.run_subprocess("systeminfo")

def run_subprocess(self, command):
    try:
        result = subprocess.run(
            ["cmd", "/c", command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True  # Esto hace que se lance una excepción si el comando falla
        )
        print(colored(result.stdout.strip(), 'cyan'))
        if result.stderr:
            print(colored(result.stderr.strip(), 'red'))
    except subprocess.CalledProcessError as e:
        print(colored(f"Error al ejecutar el comando: {e}", 'red'))
    except Exception as e:
        print(colored(f"Error desconocido: {e}", 'red'))

if __name__ == "__main__":
    tool = CommandTool()
    tool.show_title()
    tool.show_instructions()
    
    while True:
        tool.show_menu()
        user_choice = tool.get_user_choice()
        
        if user_choice.lower() == "exit":
            print(colored("Saliendo del programa. Hasta luego.", 'cyan'))
            break
        
        tool.run_command(user_choice)