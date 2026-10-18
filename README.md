# 📋 TaskTracker CLI

Projeto desenvolvido para a disciplina de Bootcamp (Análise e Desenvolvimento de Sistemas - CEUB). 
O **TaskTracker** é uma aplicação em linha de comando (CLI) desenvolvida para gerenciar tarefas diárias com foco em simplicidade, eficiência e organização de prazos.

## 🚀 Tecnologias e Conceitos
* Linguagem: Python (Estruturas de Dados, Lógica de Programação)
* Interface: Linha de Comando (CLI)
* Versionamento: Git e GitHub

## 📂 Documentação do Projeto
A documentação completa contendo o planejamento lógico, diagrama IPO, dicionário de dados e pseudocódigo encontra-se na pasta [docs/especificacao_projeto.md](docs/especificacao_projeto.md).

---
Desenvolvido por **Paulo** — Estudante de ADS no CEUB.
## 🐳 Como Executar com Docker (Fase 3)

Se preferires executar a aplicação de forma isolada utilizando Docker, segue os passos abaixo:

1. Certifica-te de que tens o Docker instalado na tua máquina.
2. Na raiz do projeto, constrói a imagem Docker:
   ```bash
   docker build -t tasktracker-app .
   docker run -it tasktracker-app
