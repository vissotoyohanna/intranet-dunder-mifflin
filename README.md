# 🏢 Dunder Mifflin Intranet - Scranton Branch

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

Este é um projeto **Full Stack** desenvolvido do zero para simular a Intranet corporativa da filial de Scranton da Dunder Mifflin (The Office). O objetivo deste projeto é aplicar conceitos avançados de Engenharia de Software, Administração de Sistemas e Segurança da Informação.

## 🎯 Objetivos Técnicos Alcançados

* **Segurança e Autenticação:** Implementação de login com proteção de rotas (Sessões) e criptografia de senhas (Hashing) utilizando Werkzeug.
* **RBAC (Role-Based Access Control):** Controle de Acesso Baseado em Cargos com 3 níveis de permissão distintos (Vendas, Gerência e RH).
* **Banco de Dados Relacional:** Modelagem de dados e operações integradas usando SQLAlchemy (ORM) e SQLite.
* **Operações CRUD Completas:** Sistema robusto para Criar, Ler, Atualizar e Deletar registros de funcionários diretamente pela interface da aplicação.
* **Arquitetura Front-End:** Design responsivo e modular utilizando CSS Grid, Flexbox e renderização dinâmica de HTML com Jinja2.

## 🚀 Funcionalidades

- **🔒 Tela de Login Restrito:** Acesso bloqueado para usuários não autenticados. Validação de e-mail e senha com mensagens de erro (Flash Messages).
- **📊 Dashboard Dinâmico:** Painel de boas-vindas que reconhece o usuário logado e exibe comunicados e atalhos.
- **📇 Diretório Corporativo:** Geração automática de "cartões" de funcionários consumindo dados diretamente do banco de dados relacional.
- **⚙️ Painel de Administração (CRUD):** - Acesso exclusivo para Gerência (Nível 2) e RH (Nível 3).
  - Cadastro de novos funcionários com geração automática de senhas seguras.
  - Edição de dados (cargo, ramal, departamento).
  - Exclusão (Demissão) de funcionários com travas de segurança.

## 🛠️ Tecnologias Utilizadas

**Back-End & Infraestrutura:**
* Python
* Flask (Web Framework)
* Flask-SQLAlchemy (ORM)
* Werkzeug (Security / Password Hashing)
* SQLite (Banco de Dados)

**Front-End:**
* HTML5 (Semântico)
* CSS3 (Grid, Flexbox, Variáveis, Arquitetura Modular)
* Jinja2 (Template Engine)

## 💻 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a Intranet na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/vissotoyohanna/intranet-dunder-mifflin.git
