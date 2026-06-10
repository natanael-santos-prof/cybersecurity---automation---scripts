import socket
import sys
from datetime import datetime

# Define o alvo (pode ser um IP ou um domínio)
alvo = input("Digite o IP ou domínio para escanear: ")

# Resolve o nome de domínio para IP, se necessário
try:
    target_ip = socket.gethostbyname(alvo)
except socket.gaierror:
    print("\n[!] Não foi possível resolver o nome do host.")
    sys.exit()

print("-" * 50)
print(f"Escaneando o alvo: {target_ip}")
print(f"Início do escaneamento: {str(datetime.now())}")
print("-" * 50)

# Lista das portas mais comuns para testar
portas_comuns = [21, 22, 23, 25, 53, 80, 110, 443, 3389]

try:
    for porta in portas_comuns:
        # Configura o socket para IPv4 (AF_INET) e TCP (SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um tempo limite curto para não travar o script
        s.settimeout(1.0)
        
        # Tenta a conexão com a porta
        resultado = s.connect_ex((target_ip, porta))
        
        # Se o resultado for 0, a porta está aberta
        if resultado == 0:
            print(f"[+] Porta {porta}: ABERTA")
        else:
            print(f"[-] Porta {porta}: Fechada")
            
        s.close()

except KeyboardInterrupt:
    print("\n[!] Varredura interrompida pelo usuário.")
    sys.exit()

except socket.error:
    print("\n[!] Erro de conexão com o servidor.")
    sys.exit()
