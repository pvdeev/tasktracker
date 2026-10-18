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
    print("3. Concluir tarefa")
    print("4. Sair da aplicação")
    print("=================================")


def cadastrar_tarefa(lista_tarefas, proximo_id):
    print("\n--- CADASTRAR NOVA TAREFA ---")

    # Validação do Título: Obrigatório, rejeita vazios ou apenas espaços
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

    # Dicionário representando a entidade Tarefa
    nova_tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "Pendente",
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


def concluir_tarefa(lista_tarefas):
    print("\n--- CONCLUIR TAREFA ---")
    if not lista_tarefas:
        print("📭 Nenhuma tarefa cadastrada para concluir.")
        return

    visualizar_tarefas(lista_tarefas)

    try:
        id_busca = int(input("\nDigite o ID da tarefa que deseja marcar como concluída: "))
    except ValueError:
        print("❌ Erro: Por favor, digite um número inteiro válido para o ID.")
        return

    for tarefa in lista_tarefas:
        if tarefa["id"] == id_busca:
            if tarefa["status"] == "Concluída":
                print(f"⚠️ A tarefa #{id_busca} já está marcada como concluída!")
            else:
                tarefa["status"] = "Concluída"
                print(f"✅ Sucesso: Tarefa #{id_busca} ('{tarefa['titulo']}') marcada como Concluída!")
            return

    print(f"❌ Erro: Nenhuma tarefa foi encontrada com o ID #{id_busca}.")


def main():
    lista_tarefas = []
    proximo_id = 1

    print("🚀 Bem-vindo ao TaskTracker - Sistema de Controle de Tarefas via CLI")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(lista_tarefas, proximo_id)
        elif opcao == "2":
            visualizar_tarefas(lista_tarefas)
        elif opcao == "3":
            concluir_tarefa(lista_tarefas)
        elif opcao == "4":
            print("\n👋 Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("\n❌ Erro: Opção inválida! Escolha um número entre 1 e 4.")


if __name__ == "__main__":
    main()