Planejamento Lógico e Estruturação do Projeto (TaskTracker)
1. Apresentação e Entendimento do Problema
1.1 Apresentação do Estudante
Nome Completo: Paulo Vitor Sousa Araujo
Curso: Análise e Desenvolvimento de Sistemas (CEUB)
Polo/Turma: CEUB EaD
E-mail Institucional: (insira seu e-mail do CEUB aqui)
1.2 Definição do Problema
No dia a dia, a ausência de um fluxo organizado para gerenciar tarefas diárias gera desorganização, perda de prazos e dificuldade na priorização de compromissos. Sem uma ferramenta centralizada e acessível, a gestão do tempo torna-se ineficiente e propensa a falhas, afetando a produtividade pessoal, acadêmica e profissional.
1.3 Visão Geral da Solução (TaskTracker)
Para resolver esse problema, projetei o TaskTracker, uma aplicação em linha de comando (CLI) focada em simplicidade, eficiência e organização. O sistema permite cadastrar tarefas com parâmetros essenciais (título, descrição, prazo e prioridade), listar demandas pendentes, marcar itens concluídos e gerar relatórios simplificados de desempenho.
1.4 Público-Alvo e Objetivo Principal
Público-Alvo: Estudantes, profissionais e indivíduos que buscam uma solução leve e direta via terminal para organizar suas rotinas diárias.
Objetivo Principal: Oferecer uma estrutura confiável de controle de tarefas que reduza o esquecimento de prazos, otimize a gestão do tempo e forneça um histórico claro do progresso das atividades executadas.
2. Decomposição do Problema e Dados do Sistema
2.1 Mapeamento de Entradas, Processamento e Saídas (IPO / EPS)
Entradas de Dados (Input):
Dados da Tarefa: Título (texto), Descrição (texto), Prazo/Data de Vencimento (texto/data) e Nível de Prioridade (Alta, Média, Baixa).
Comandos do Usuário: Opção numérica selecionada no menu principal (1 - Cadastrar Tarefa, 2 - Listar Tarefas, 3 - Concluir Tarefa, 4 - Exibir Relatório, 0 - Sair).
Identificador para Ação: Número do ID da tarefa informado pelo usuário para alteração de status.
Processamento (Logic & Rules):
Validação de Entradas: Verificação de campos obrigatórios (garantindo que Título e Prioridade não fiquem vazios).
Geração de ID: Atribuição autoincremental de um identificador único para cada nova tarefa criada.
Gestão de Estado: Definição do status padrão inicial como "Pendente" e atualização para "Concluída" quando solicitado.
Processamento de Relatório: Cálculo consolidado contabilizando o total de tarefas, quantidade de pendentes, quantidade de concluídas e percentual de conclusão.
Tratamento de Exceções: Validação de opções do menu e entradas inválidas para evitar interrupções inesperadas na execução.
Saídas de Dados (Output):
Feedback Interativo: Mensagens de confirmação de ações executadas com sucesso ou alertas de erro no terminal.
Visualização da Listagem: Exibição tabular/formatada com ID, Título, Prioridade, Prazo e Status de cada tarefa.
Painel de Relatório: Resumo estatístico do desempenho da gestão de tarefas.
2.2 Modelagem da Estrutura de Dados (Entidade Tarefa)
Para representar e manipular cada tarefa na aplicação, projetei a estrutura de dados baseada em dicionário/objeto com as seguintes propriedades:
Campo
Tipo de Dado
Descrição
Exemplo de Aplicação
id
Inteiro (int)
Identificador único e sequencial da tarefa
1
titulo
Texto (string)
Nome resumido da atividade
"Estudar Engenharia de Requisitos"
descricao
Texto (string)
Detalhamento sobre a tarefa a ser executada
"Revisar e validar Seção 2 do documento"
prioridade
Texto (string)
Gravação de urgência ("Alta", "Média", "Baixa")
"Alta"
prazo
Texto / Data (string)
Data estipulada para a entrega da atividade
"25/10/2026"
status
Texto (string)
Situação atual da tarefa ("Pendente" ou "Concluída")
"Pendente"

2.3 Regras de Negócio Inegociáveis
Unicidade de Identificador (ID): Todo registro deve receber um ID numérico exclusivo e imutável no momento de sua criação.
Obrigatoriedade de Atributos: O sistema não deve aceitar o cadastro de tarefas sem o preenchimento dos campos Título e Prioridade.
Consistência do Histórico: Quando uma tarefa é marcada como "Concluída", ela permanece registrada na base de dados para garantir a acurácia dos relatórios estatísticos.
Resiliência e Tolerância a Falhas: Digitações incorretas ou opções inválidas no menu devem ser tratadas amigavelmente com alertas explicativos, mantendo o programa em loop até que o usuário decida sair explicitamente.





3. Receita Lógica do Sistema
INÍCIO

    // 1. Inicialização de Variáveis e Estruturas de Dados
    DEFINIR lista_de_tarefas COMO Lista Vazia
    DEFINIR proximo_id COMO 1
    DEFINIR executando COMO Verdadeiro

    // 2. Loop Principal da Aplicação
    ENQUANTO executando FOR IGUAL A Verdadeiro FAÇA
        
        // Exibição do Menu
        ESCREVER "================================="
        ESCREVER "        TASKTRACKER - MENU       "
        ESCREVER "================================="
        ESCREVER "1. Cadastrar Nova Tarefa"
        ESCREVER "2. Listar Todas as Tarefas"
        ESCREVER "3. Concluir Tarefa"
        ESCREVER "4. Exibir Relatório de Desempenho"
        ESCREVER "0. Sair do Sistema"
        ESCREVER "================================="
        ESCREVER "Escolha uma opção: "
        LER opcao

        // 3. Processamento da Opção Selecionada
        ESCOLHA opcao:

            CASO "1": // Cadastrar Nova Tarefa
                ESCREVER "--- CADASTRAR TAREFA ---"
                
                // Validação do Título
                REPETIR
                    ESCREVER "Digite o título da tarefa (Obrigatório): "
                    LER titulo
                    SE titulo ESTIVER VAZIO ENTÃO
                        ESCREVER "Erro: O título não pode ser vazio!"
                    FIM_SE
                ATÉ QUE titulo NÃO ESTEJA VAZIO

                ESCREVER "Digite a descrição da tarefa (Opcional): "
                LER descricao

                ESCREVER "Digite o prazo (ex: DD/MM/AAAA): "
                LER prazo

                // Validação da Prioridade
                REPETIR
                    ESCREVER "Selecione a prioridade (Alta, Média, Baixa): "
                    LER prioridade
                    SE prioridade NÃO FOR ("Alta" OU "Média" OU "Baixa") ENTÃO
                        ESCREVER "Erro: Prioridade inválida! Escolha entre Alta, Média ou Baixa."
                    FIM_SE
                ATÉ QUE prioridade SEJA IGUAL A ("Alta" OU "Média" OU "Baixa")

                // Criação do registro
                DEFINIR nova_tarefa COMO Dicionário:
                    - id = proximo_id
                    - titulo = titulo
                    - descricao = descricao
                    - prazo = prazo
                    - prioridade = prioridade
                    - status = "Pendente"

                ADICIONAR nova_tarefa EM lista_de_tarefas
                INCREMENTAR proximo_id EM 1
                ESCREVER "Sucesso: Tarefa cadastrada com sucesso!"

            CASO "2": // Listar Todas as Tarefas
                ESCREVER "--- LISTA DE TAREFAS ---"
                SE lista_de_tarefas ESTIVER VAZIA ENTÃO
                    ESCREVER "Nenhuma tarefa cadastrada até o momento."
                SENÃO
                    PARA CADA tarefa EM lista_de_tarefas FAÇA
                        ESCREVER "ID: " + tarefa.id + " | Título: " + tarefa.titulo
                        ESCREVER "Descrição: " + tarefa.descricao
                        ESCREVER "Prazo: " + tarefa.prazo + " | Prioridade: " + tarefa.prioridade
                        ESCREVER "Status: " + tarefa.status
                        ESCREVER "---------------------------------"
                    FIM_PARA
                FIM_SE

            CASO "3": // Concluir Tarefa
                ESCREVER "--- CONCLUIR TAREFA ---"
                SE lista_de_tarefas ESTIVER VAZIA ENTÃO
                    ESCREVER "Nenhuma tarefa disponível para concluir."
                SENÃO
                    ESCREVER "Digite o ID da tarefa que deseja marcar como concluída: "
                    LER id_busca
                    DEFINIR encontrada COMO Falso

                    PARA CADA tarefa EM lista_de_tarefas FAÇA
                        SE tarefa.id FOR IGUAL A id_busca ENTÃO
                            DEFINIR encontrada COMO Verdadeiro
                            SE tarefa.status FOR IGUAL A "Concluída" ENTÃO
                                ESCREVER "Aviso: Esta tarefa já se encontra concluída!"
                            SENÃO
                                DEFINIR tarefa.status COMO "Concluída"
                                ESCREVER "Sucesso: Tarefa ID " + id_busca + " marcada como Concluída!"
                            FIM_SE
                        FIM_SE
                    FIM_PARA

                    SE encontrada FOR IGUAL A Falso ENTÃO
                        ESCREVER "Erro: Nenhuma tarefa foi encontrada com o ID informado."
                    FIM_SE
                FIM_SE

            CASO "4": // Exibir Relatório
                ESCREVER "--- RELATÓRIO DE DESEMPENHO ---"
                DEFINIR total COMO TAMANHO(lista_de_tarefas)
                
                SE total FOR IGUAL A 0 ENTÃO
                    ESCREVER "Sem dados para gerar relatório. Cadastre tarefas primeiro."
                SENÃO
                    DEFINIR concluídas COMO 0
                    DEFINIR pendentes COMO 0

                    PARA CADA tarefa EM lista_de_tarefas FAÇA
                        SE tarefa.status FOR IGUAL A "Concluída" ENTÃO
                            INCREMENTAR concluídas EM 1
                        SENÃO
                            INCREMENTAR pendentes EM 1
                        FIM_SE
                    FIM_PARA

                    DEFINIR percentual COMO (concluídas / total) * 100

                    ESCREVER "Total de tarefas cadastradas: " + total
                    ESCREVER "Tarefas Pendentes: " + pendentes
                    ESCREVER "Tarefas Concluídas: " + concluídas
                    ESCREVER "Taxa de Conclusão: " + percentual + "%"
                FIM_SE

            CASO "0": // Sair
                ESCREVER "Encerrando o TaskTracker... Até logo!"
                DEFINIR executando COMO Falso

            OUTRO CASO: // Opção Inválida
                ESCREVER "Erro: Opção inválida! Por favor, escolha um número de 0 a 4."

        FIM_ESCOLHA

    FIM_ENQUANTO

FIM


4. Arquitetura do Repositório Git e Estrutura de Arquivos
4.1 Árvore de Diretórios do Repositório
tasktracker/
├── .gitignore
├── README.md
├── docs/
│   └── especificacao_projeto.md
└── src/
    ├── __init__.py
    ├── main.py
    ├── modelos.py
    └── utilitarios.py

4.2 Detalhamento e Responsabilidade de Cada Arquivo
README.md: Arquivo de documentação principal do projeto no repositório. Contém o título do projeto, descrição geral, instruções passo a passo de como executar a aplicação via terminal, exemplos de uso e dados do autor/estudante.
.gitignore: Arquivo de configuração do Git responsável por ignorar arquivos temporários, diretórios do sistema operacional e arquivos gerados pela linguagem de programação (como __pycache__/, .venv/ e .DS_Store), mantendo o repositório limpo.
docs/especificacao_projeto.md: Pasta e arquivo destinados ao armazenamento da documentação arquitetural, requisitos do sistema e planejamento lógico elaborado para a entrega.
src/main.py: Ponto de entrada (entry point) do programa em linha de comando. É responsável por inicializar o loop do menu principal, ler as entradas do usuário, invocar as funções/módulos e controlar o encerramento do sistema.
src/modelos.py: Módulo reservado para a definição das estruturas de dados (dicionários e classes que representam a entidade Tarefa) e armazenamento em memória da lista de tarefas.
src/utilitarios.py: Módulo contendo funções auxiliares para validação de entradas (como verificar se o título não está vazio ou se a prioridade é válida) e formatação de saídas/relatórios no terminal.

