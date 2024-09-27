#GABRIEL HENRIQUE REDEDE LOURENÇO ( ANÁLISE E DESENVOLVIMENTO DE SISTEMAS) - PUCPR

import json
import os

# Arquivos JSON para cada módulo
ARQUIVO_ESTUDANTES = 'estudantes.json'
ARQUIVO_PROFESSORES = 'professores.json'
ARQUIVO_DISCIPLINAS = 'disciplinas.json'
ARQUIVO_TURMAS = 'turmas.json'
ARQUIVO_MATRICULAS = 'matriculas.json'


# Função genérica para salvar dados em um arquivo JSON
def salvar_json(data, filename):
    with open(filename, 'w') as arquivo:
        json.dump(data, arquivo)


# Função genérica para recuperar dados de um arquivo JSON
def recuperar_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []


# Funções específicas para cada módulo

# Estudantes
def incluir_estudante():
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante (apenas números): ")

    estudantes = recuperar_json(ARQUIVO_ESTUDANTES)
    for estudante in estudantes:
        if estudante['cpf'] == cpf:
            print("CPF já cadastrado.")
            return

    novo_estudante = {'nome': nome, 'cpf': cpf}
    estudantes.append(novo_estudante)
    salvar_json(estudantes, ARQUIVO_ESTUDANTES)
    print(f"Estudante {nome} cadastrado com sucesso!")


def listar_estudantes():
    estudantes = recuperar_json(ARQUIVO_ESTUDANTES)
    if not estudantes:
        print("Não há estudantes cadastrados.")
    else:
        print("Lista de estudantes:")
        for estudante in estudantes:
            print(f"Nome: {estudante['nome']}, CPF: {estudante['cpf']}")



def editar_estudante():
    cpf = input("Digite o CPF do estudante que deseja editar: ")

    estudantes = recuperar_json(ARQUIVO_ESTUDANTES)
    for estudante in estudantes:
        if estudante['cpf'] == cpf:
            novo_nome = input("Digite o novo nome do estudante: ")
            estudante['nome'] = novo_nome
            salvar_json(estudantes, ARQUIVO_ESTUDANTES)
            print("Estudante editado com sucesso!")
            return

    print("Estudante não encontrado.")


def excluir_estudante():
    cpf = input("Digite o CPF do estudante que deseja excluir: ")

    estudantes = recuperar_json(ARQUIVO_ESTUDANTES)
    for estudante in estudantes:
        if estudante['cpf'] == cpf:
            estudantes.remove(estudante)
            salvar_json(estudantes, ARQUIVO_ESTUDANTES)
            print("Estudante excluído com sucesso!")
            return

    print("Estudante não encontrado.")


# Professores
def incluir_professor():
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor (apenas números): ")
    codigo = int(input("Digite o código do professor: "))

    professores = recuperar_json(ARQUIVO_PROFESSORES)
    for professor in professores:
        if professor['codigo'] == codigo:
            print("Código já cadastrado.")
            return

    novo_professor = {'nome': nome, 'cpf': cpf, 'codigo': codigo}
    professores.append(novo_professor)
    salvar_json(professores, ARQUIVO_PROFESSORES)
    print(f"Professor {nome} cadastrado com sucesso!")


def listar_professores():
    professores = recuperar_json(ARQUIVO_PROFESSORES)
    if not professores:
        print("Não há professores cadastrados.")
    else:
        print("Lista de professores:")
        for professor in professores:
            print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")



def editar_professores():
    codigo = int(input("Digite o código do professor que deseja editar: "))

    professores = recuperar_json(ARQUIVO_PROFESSORES)
    for professor in professores:
        if professor['codigo'] == codigo:
            novo_nome = input("Digite o novo nome do professor: ")
            professor['nome'] = novo_nome
            salvar_json(professores, ARQUIVO_PROFESSORES)
            print("Professor editado com sucesso!")
            return

    print("Professor não encontrado.")


def excluir_professores():
    codigo = int(input("Digite o código do professor que deseja excluir: "))

    professores = recuperar_json(ARQUIVO_PROFESSORES)
    for professor in professores:
        if professor['codigo'] == codigo:
            professores.remove(professor)
            salvar_json(professores, ARQUIVO_PROFESSORES)
            print("Professor excluído com sucesso!")
            return

    print("Professor não encontrado.")


# Disciplinas
def incluir_disciplina():
    nome = input("Digite o nome da disciplina: ")
    codigo = int(input("Digite o código da disciplina: "))

    disciplinas = recuperar_json(ARQUIVO_DISCIPLINAS)
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            print("Código já cadastrado.")
            return

    nova_disciplina = {'nome': nome, 'codigo': codigo}
    disciplinas.append(nova_disciplina)
    salvar_json(disciplinas, ARQUIVO_DISCIPLINAS)
    print(f"Disciplina {nome} cadastrada com sucesso!")


def listar_disciplinas():
    disciplinas = recuperar_json(ARQUIVO_DISCIPLINAS)
    if not disciplinas:
        print("Não há disciplinas cadastradas.")
    else:
        print("Lista de disciplinas:")
        for disciplina in disciplinas:
            print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")


def editar_disciplina():
    codigo = int(input("Digite o código da disciplina que deseja editar: "))

    disciplinas = recuperar_json(ARQUIVO_DISCIPLINAS)
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            novo_nome = input("Digite o novo nome da disciplina: ")
            disciplina['nome'] = novo_nome
            salvar_json(disciplinas, ARQUIVO_DISCIPLINAS)
            print("Disciplina editada com sucesso!")
            return

    print("Disciplina não encontrada.")


def excluir_disciplina():
    codigo = int(input("Digite o código da disciplina que deseja excluir: "))

    disciplinas = recuperar_json(ARQUIVO_DISCIPLINAS)
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            disciplinas.remove(disciplina)
            salvar_json(disciplinas, ARQUIVO_DISCIPLINAS)
            print("Disciplina excluída com sucesso!")
            return

    print("Disciplina não encontrada.")


# Turmas
def incluir_turma():
    codigo = int(input("Digite o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))
    codigo_disciplina = int(input("Digite o código da disciplina: "))

    turmas = recuperar_json(ARQUIVO_TURMAS)
    for turma in turmas:
        if turma['codigo'] == codigo:
            print("Código de turma já cadastrado.")
            return

    nova_turma = {'codigo': codigo, 'codigo_professor': codigo_professor, 'codigo_disciplina': codigo_disciplina}
    turmas.append(nova_turma)
    salvar_json(turmas, ARQUIVO_TURMAS)
    print("Turma cadastrada com sucesso!")


def listar_turmas():
    turmas = recuperar_json(ARQUIVO_TURMAS)
    if not turmas:
        print("Não há turmas cadastradas.")
    else:
        print("Lista de turmas:")
        for turma in turmas:
            print(f"Código: {turma['codigo']}, Código do Professor: {turma['codigo_professor']}, "
                  f"Código da Disciplina: {turma['codigo_disciplina']}")

def editar_turmas():
    codigo = int(input("Digite o código da turma que deseja editar: "))

    turmas = recuperar_json(ARQUIVO_TURMAS)
    for turma in turmas:
        if turma['codigo'] == codigo:
            novo_codigo_professor = int(input("Digite o novo código do professor: "))
            novo_codigo_disciplina = int(input("Digite o novo código da disciplina: "))

            turma['codigo_professor'] = novo_codigo_professor
            turma['codigo_disciplina'] = novo_codigo_disciplina

            salvar_json(turmas, ARQUIVO_TURMAS)
            print("Turma editada com sucesso!")
            return

    print("Turma não encontrada.")


def excluir_turmas():
    codigo = int(input("Digite o código da turma que deseja excluir: "))

    turmas = recuperar_json(ARQUIVO_TURMAS)
    for turma in turmas:
        if turma['codigo'] == codigo:
            turmas.remove(turma)
            salvar_json(turmas, ARQUIVO_TURMAS)
            print("Turma excluída com sucesso!")
            return

    print("Turma não encontrada.")

# Matrículas
def incluir_matricula():
    codigo_turma = int(input("Digite o código da turma: "))
    codigo_estudante = int(input("Digite o código do estudante: "))

    matriculas = recuperar_json(ARQUIVO_MATRICULAS)
    for matricula in matriculas:
        if matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo_estudante:
            print("Matrícula já cadastrada.")
            return

    nova_matricula = {'codigo_turma': codigo_turma, 'codigo_estudante': codigo_estudante}
    matriculas.append(nova_matricula)
    salvar_json(matriculas, ARQUIVO_MATRICULAS)
    print("Matrícula realizada com sucesso!")


def listar_matriculas():
    matriculas = recuperar_json(ARQUIVO_MATRICULAS)
    if not matriculas:
        print("Não há matrículas cadastradas.")
    else:
        print("Lista de matrículas:")
        for matricula in matriculas:
            print(f"Código da Turma: {matricula['codigo_turma']}, Código do Estudante: {matricula['codigo_estudante']}")

def editar_matricula():
    codigo_turma_antigo = int(input("Digite o código antigo da turma da matrícula que deseja editar: "))
    codigo_estudante_antigo = int(input("Digite o código antigo do estudante da matrícula que deseja editar: "))

    matriculas = recuperar_json(ARQUIVO_MATRICULAS)
    for matricula in matriculas:
        if matricula['codigo_turma'] == codigo_turma_antigo and matricula['codigo_estudante'] == codigo_estudante_antigo:
            novo_codigo_turma = int(input("Digite o novo código da turma: "))
            novo_codigo_estudante = int(input("Digite o novo código do estudante: "))

            matricula['codigo_turma'] = novo_codigo_turma
            matricula['codigo_estudante'] = novo_codigo_estudante

            salvar_json(matriculas, ARQUIVO_MATRICULAS)
            print("Matrícula editada com sucesso!")
            return

    print("Matrícula não encontrada.")


def excluir_matricula():
    codigo_turma = int(input("Digite o código da turma da matrícula que deseja excluir: "))
    codigo_estudante = int(input("Digite o código do estudante da matrícula que deseja excluir: "))

    matriculas = recuperar_json(ARQUIVO_MATRICULAS)
    for matricula in matriculas:
        if matricula['codigo_turma'] == codigo_turma and matricula['codigo_estudante'] == codigo_estudante:
            matriculas.remove(matricula)
            salvar_json(matriculas, ARQUIVO_MATRICULAS)
            print("Matrícula excluída com sucesso!")
            return

    print("Matrícula não encontrada.")


# Menu Principal
def mostrar_menu_principal():
    print("\nMENU PRINCIPAL")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Finalizar Programa")
    opcao = input("Digite a opção desejada: ")
    return opcao


# Execução do programa
def main():
    while True:
        opcao = mostrar_menu_principal()

        if opcao == '1':
            while True:
                print("\nMENU ESTUDANTES")
                print("1. Incluir Estudante")
                print("2. Listar Estudantes")
                print("3. Editar Estudantes")
                print("4. Excluir Estudantes")
                print("5. Voltar ao Menu Principal")
                opcao_estudantes = input("Digite a opção desejada: ")

                if opcao_estudantes == '1':
                    incluir_estudante()
                elif opcao_estudantes == '2':
                    listar_estudantes()
                elif opcao_estudantes == '3':
                    editar_estudante()
                elif opcao_estudantes == '4':
                    excluir_estudante()
                elif opcao_estudantes == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == '2':
            while True:
                print("\nMENU PROFESSORES")
                print("1. Incluir Professor")
                print("2. Listar Professores")
                print("3. Editar Professores")
                print("4. Excluir Professores")
                print("5. Voltar ao Menu Principal")
                opcao_professores = input("Digite a opção desejada: ")

                if opcao_professores == '1':
                    incluir_professor()
                elif opcao_professores == '2':
                    listar_professores()
                elif opcao_professores == '3':
                    editar_professores()
                elif opcao_professores == '4':
                    excluir_professores()
                elif opcao_professores == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == '3':
            while True:
                print("\nMENU DISCIPLINAS")
                print("1. Incluir Disciplina")
                print("2. Listar Disciplinas")
                print("3. Editar Disciplinas")
                print("4. Excluir Disciplinas")
                print("5. Voltar ao Menu Principal")
                opcao_disciplinas = input("Digite a opção desejada: ")

                if opcao_disciplinas == '1':
                    incluir_disciplina()
                elif opcao_disciplinas == '2':
                    listar_disciplinas()
                elif opcao_disciplinas == '3':
                    editar_disciplina()
                elif opcao_disciplinas == '4':
                    excluir_disciplina()
                elif opcao_disciplinas == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == '4':
            while True:
                print("\nMENU TURMAS")
                print("1. Incluir Turma")
                print("2. Listar Turmas")
                print("3. Editar Turmas")
                print("4. Excluir Turmas")
                print("5. Voltar ao Menu Principal")
                opcao_turmas = input("Digite a opção desejada: ")

                if opcao_turmas == '1':
                    incluir_turma()
                elif opcao_turmas == '2':
                    listar_turmas()
                elif opcao_turmas == '3':
                    editar_turmas()
                elif opcao_turmas == '4':
                    excluir_turmas()
                elif opcao_turmas == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == '5':
            while True:
                print("\nMENU MATRÍCULAS")
                print("1. Realizar Matrícula")
                print("2. Listar Matrículas")
                print("3. Editar Matrícula")
                print("4. Excluir Matrícula")
                print("5. Voltar ao Menu Principal")
                opcao_matriculas = input("Digite a opção desejada: ")

                if opcao_matriculas == '1':
                    incluir_matricula()
                elif opcao_matriculas == '2':
                    listar_matriculas()
                elif opcao_matriculas == '3':
                    editar_matricula()
                elif opcao_matriculas == '4':
                    excluir_matricula()
                elif opcao_matriculas == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == '6':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
