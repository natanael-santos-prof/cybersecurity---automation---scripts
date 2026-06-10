from netmiko import ConnectHandler

print("--- Iniciando conexão com o roteador Cisco ---")

# 1. Dados de acesso do roteador (Configuração simples)
roteador = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "SenhaSegura123",
}

# 2. Conectando ao equipamento via SSH
conexao = ConnectHandler(**roteador)

# 3. Enviando o comando básico do CCNA
print("Conectado! Coletando informações das interfaces...")
resultado = conexao.send_command("show ip interface brief")

# 4. Exibindo o resultado direto na tela do terminal
print("\n=== RESULTADO DO COMANDO ===")
print(resultado)

# 5. Fechando a conexão de forma segura
conexao.disconnect()
print("\n--- Conexão encerrada com sucesso ---")
