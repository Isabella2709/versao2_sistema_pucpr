estudantes_lista:str = [
    {"codigo": 4572,"nome": "Luana", "cpf": "966541531"},
    {"codigo": 4578,"nome": "João", "cpf": "458925318"},
    {"codigo": 4574,"nome": "Lucas", "cpf": "21441531"},

                        ]

print("Bem vindo ao sistema academico:")
print("================================")

operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
operacao = operacao.upper()

if(operacao != "N" and operacao != "S"):
  print("Opção invalida")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
  operacao = operacao.upper()

operacao = operacao.upper()


while(operacao == "S"):

  escolha_menu = int(input("Bem vindo ao menu principal, por favor escolha a opção desejada: \n 1. Estudantes \n 2. Disciplinas \n 3. Professores \n 4. Turmas \n 5. Matriculas \n 6. Sair \n"))

  if(escolha_menu == 1):
   escolha_pergunta = int(input("====== [ESTUDANTES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   if(escolha_pergunta == 1):

     codigo_estudante = str(input("Digite o codigo de 4 digitos do estudante: "))
     nome_estudante = str(input("Digite o nome do estudante que voce deseja inserir: "))
     cpf_estudante = str(input("Digite o cpf de 9 digitos do estudante "))
     estudantes_lista.append({"codigo": codigo_estudante, "nome": nome_estudante, "cpf": "cpf_estudante"})

     print("Estudante adicionado com sucesso")
   elif(escolha_pergunta == 2):

    for estudante in estudantes_lista:
                print(estudante)

   elif(escolha_pergunta == 3):
    atualizar_estudante = str(input("Digite qual o nome do estudante que você quer alterar: "))
    for estudante in estudantes_lista:
        if estudante["nome"] == atualizar_estudante:
            nome_estudante = str(input("Digite o nome do estudante que você deseja inserir: "))
            cpf_estudante = str(input("Digite o CPF de 9 dígitos do estudante: "))
            estudante.update({"nome": nome_estudante, "cpf": cpf_estudante})
            print("Estudante atualizado com sucesso")
            break
    else:
        print("Estudante não encontrado.")

   elif(escolha_pergunta == 4):
    remover_estudante = int(input("Digite o código do estudante que você quer remover: "))
    nova_lista = [estudante for estudante in estudantes_lista if estudante["codigo"] != remover_estudante]
    if len(nova_lista) != len(estudantes_lista):
        estudantes_lista[:] = nova_lista
        print("Estudante removido com sucesso")
    else:
        print("Estudante não encontrado.")


   elif(escolha_pergunta == 5):
    print("Voltando ao menu inicial")



  elif(escolha_menu == 2):
   print("====== [DISCIPLINAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 3):
   print("====== [PROFESSORES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 4):
   print("====== [TURMAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 5):
   print("====== [MATRICULAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 6):
   print("Obrigada por ultilizar nosso sistema, esperamos te ver em breve.")
  else:
   print("Opção invalida, por favor informe um numero valido, você sera direcionado para o menu inicial.")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações e N para sair): "))
  operacao = operacao.upper()

  if(operacao == "N"):
   print("Bem vindo de volta ao menu do sistema academico")
   operacao = str(input("Deseja começar a fazer operações novamente? (S - Fazer operações e N para sair): "))
   operacao = operacao.upper()

print("===================================")
