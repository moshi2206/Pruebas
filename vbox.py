import time
import subprocess


"""Lista de las VM"""
vm_name = [
    "Servidor Principal",
    "Sentinel"
]


def is_vm_running(vm_name):
    """Verifica si la VM está en ejecución."""
    result = subprocess.run(["VBoxManage", "showvminfo", vm_name, "--machinereadable"],
                            capture_output=True, text=True)
    return "VMState=\"running\"" in result.stdout


def start_vm(vm_name):
    """Inicia la máquina virtual si no está en ejecución."""
    if not is_vm_running(vm_name):
        print(f"Iniciando VM: {vm_name}")
        subprocess.run(["VBoxManage", "startvm", vm_name, "--type", "headless"])
    else:
        print(f"La VM {vm_name} ya está en ejecución.")


def stop_vm(vm_name):
    """Apaga la máquina virtual de forma segura."""
    print(f"Apagando VM: {vm_name}")
    subprocess.run(["VBoxManage", "controlvm", vm_name, "acpipowerbutton"])


def daemon_loop():
    """Loop del daemon para monitorear y mantener la VM en ejecución."""
    
    try:
        while True:
            for a in vm_name:
                start_vm(a)
                time.sleep(60)  # Verifica cada 60 segundos
        except KeyboardInterrupt:
            stop_vm(a)


if __name__ == "__main__":
    daemon_loop()
