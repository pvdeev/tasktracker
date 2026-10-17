"""
TaskTracker - Aplicação CLI em Python
Fase 2: Etapa Intermediária do Bootcamp II
Estudante: Paulo - Análise e Desenvolvimento de Sistemas (CEUB)
"""

def exibir_menu():
    print("\n=================================")
    print("        TASKTRACKER - MENU       ")
    print("=================================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=================================")


def cadastrar_tarefa(lista_tarefas, proximo_id):
    print("\n--- CADASTRAR NOVA TAREFA ---")
    
    # Validação do Título: Obrigatório, rejeita vazios ou espaços em branco
    while True:
        titulo = input("Digite o título da tarefa (Obrigatório): ").strip()
        if titulo:
            break
        print("❌ Erro: O título não pode ser vazio ou composto apenas por espaços!")

    # Descrição: Detalhamento livre da tarefa
    descricao = input("Digite a descrição da tarefa (Opcional): ").strip()
    if not descricao:
        descricao = "Sem descrição informada"

    # Data Limite
    prazo = input("Digite a data limite (ex: DD/MM/AAAA): ").strip()
    if not prazo:
        prazo = "Não informada"

    # Validação estrita da Prioridade: Apenas Alta, Média/Media ou Baixa
    prioridades_validas = ["alta", "média", "media", "baixa"]
    while True:
        prioridade_input = input("Selecione a prioridade (Alta, Média, Baixa): ").strip()
        prioridade_lower = prioridade_input.lower()
        if prioridade_lower in prioridades_validas:
            if prioridade_lower == "media":
                prioridade = "Média"
            else:
                prioridade = prioridade_input.capitalize()
            break
        print("❌ Erro: Prioridade inválida! Escolha estritamente entre 'Alta', 'Média' ou 'Baixa'.")

    # Dicionário representando a entidade Tarefa com status padrão "Pendente"
    nova_tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "Pendente"
    }

    lista_tarefas.append(nova_tarefa)
    print(f"\n✅ Sucesso: Tarefa #{proximo_id} cadastrada com sucesso!")
    return proximo_id + 1


def visualizar_tarefas(lista_tarefas):
    print("\n--- LISTA DE TAREFAS CADASTRADAS ---")
    if not lista_tarefas:
        print("📭 Nenhuma tarefa cadastrada no momento.")
        return

    print(f"Total de registros: {len(lista_tarefas)}\n")
    for tarefa in lista_tarefas:
        print(f"ID: {tarefa['id']}")
        print(f"📌 Título: {tarefa['titulo']}")
        print(f"📝 Descrição: {tarefa['descricao']}")
        print(f"📅 Data Limite: {tarefa['prazo']}")
        print(f"⚡ Prioridade: {tarefa['prioridade']}")
        print(f"🔄 Status: {tarefa['status']}")
        print("-" * 35)


def main():
    lista_tarefas = []
    proximo_id = 1

    print("🚀 Bem-vindo ao TaskTracker - Sistema de Controle de Tarefas via CLI")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(lista_tarefas, proximo_id)
        elif opcao == "2":
            visualizar_tarefas(lista_tarefas)
        elif opcao == "3":
            print("\n👋 Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("\n❌ Erro: Opção inválida! Escolha um número entre 1 e 3.")


if __name__ == "__main__":
    main()