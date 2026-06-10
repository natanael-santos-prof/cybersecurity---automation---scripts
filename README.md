# Port Scanner Automatizado em Python:

Este projeto faz parte dos meus estudos em automação de processos repetitivos voltados para a área de segurança da informação e cibersegurança.

## 🚀 Objetivo:
Automatizar a checagem manual de portas de rede ativas em servidores ou domínios, otimizando o tempo gasto em análises rotineiras de infraestrutura e validação de firewalls.

## 🛠️ Tecnologias Utilizadas:

* **Python 3**
* **Biblioteca Socket:** Para comunicação de rede e testes de conexão TCP.
* **Biblioteca Datetime:** Para registrar o horário de início da varredura.

## 📋 Portas Verificadas por Padrão:

O script realiza testes rápidos nas seguintes portas comuns:
* **21** (FTP)
* **22** (SSH)
* **23** (Telnet)
* **25** (SMTP)
* **53** (DNS)
* **80** (HTTP)
* **110** (POP3)
* **443** (HTTPS)
* **3389** (RDP)

## 💻 Como Executar:

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo no terminal:
   ```bash
   python port_scanner.py
   ```
3. Insira o IP ou Domínio que deseja escanear quando solicitado.

---
*Aviso: Este script possui fins estritamente educacionais e de automação defensiva.*

Atenciosamente,

Natanael Santos 
