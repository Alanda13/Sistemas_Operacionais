import psutil
import subprocess
import time


def iniciar_processo(comando)
    try:
        processo = subprocess.Popen(comando)
        print(f"Processo '{comando[0]}' iniciado com PID {processo.pid}.")
        return processo
    except FileNotFoundError:
        print(f"O comando '{comando[0]}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao iniciar o processo: {e}")
    return None


def monitorar_processo(pid_alvo):
    try:
        proc = psutil.Process(pid_alvo)
        print(f"\nMonitorando processo com PID {pid_alvo}...\n")

        while True:
            if proc.is_running():
                status = proc.status()
                cpu_percent = proc.cpu_percent(interval=1)
                memoria = proc.memory_info().rss / (1024 ** 2)  

                print(f"Status: {status} | CPU: {cpu_percent}% | Memória: {memoria:.2f} MB")
            else:
                print(f"O processo com PID {pid_alvo} foi finalizado.")
                break
            time.sleep(2)

    except psutil.NoSuchProcess:
        print(f"O processo com PID {pid_alvo} não foi encontrado.")
    except psutil.AccessDenied:
        print(f"Sem permissão para acessar o processo com PID {pid_alvo}.")
    except Exception as e:
        print(f"Erro ao monitorar o processo: {e}")


def finalizar_processo(processo):
    if processo.poll() is None:  # Verifica se o processo ainda está em execução
        processo.terminate()
        print(f"\nProcesso com PID {processo.pid} foi finalizado.")
    else:
        print(f"\nProcesso com PID {processo.pid} já estava finalizado.")


def main():
    comando = ["notepad"] 

    print("Iniciando o processo...\n")
    processo = iniciar_processo(comando)

    if processo:
        monitorar_processo(processo.pid)
        finalizar_processo(processo)


if __name__ == "__main__":
    main()
