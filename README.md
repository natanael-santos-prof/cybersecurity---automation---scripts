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
# 🚀 Miniguia de Estudo - CCNA 200-301 & Automação

Este repositório foi criado para organizar meus materiais de preparação para a certificação Cisco CCNA 200-301 e documentar meus primeiros passos na automação de redes com Python.

## 🛠️ Automação de Tarefas de Redes (Scripts Práticos)

O foco principal do meu aprendizado é eliminar tarefas manuais e repetitivas do dia a dia de um analista de infraestrutura.

### 📌 Script: Consulta Automática de Interfaces (`consulta_roteador.py`)

* **O Problema Manual:** Para verificar o status das portas de um roteador, um técnico precisa abrir o terminal (como o Putty), digitar as credenciais de acesso, rodar os comandos de verificação e caçar os erros visualmente.
* **A Solução Automatizada:** Este script em Python utiliza a biblioteca **Netmiko** para se conectar via SSH de forma automática ao dispositivo. Ele executa de forma ultra rápida o comando `show ip interface brief` e exibe o "raio-X" da saúde de todas as portas direto na tela do terminal em menos de 2 segundos.
* **Aplicações Práticas:** É utilizado no dia a dia para **Troubleshooting rápido** (descobrir instantaneamente se um link de internet caiu) e para **Validação de Configurações** (conferir se o IP correto foi colado na interface sem precisar acessar o equipamento manualmente).

### ⚙️ Como executar o projeto:
Para rodar este script em seu ambiente de laboratório, instale a biblioteca de automação necessária via terminal:
```bash
pip install netmiko
```

*Aviso: Este script possui fins estritamente educacionais e de automação defensiva.*

Atenciosamente,

Natanael Santos

