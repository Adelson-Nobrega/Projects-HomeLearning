from random import randint

with open('quiz-capitais.txt', 'r', encoding='UTF-8') as arquivo:
    perguntas = arquivo.readlines()

with open('gabarito.txt', 'r', encoding='UTF-8') as arquivo:
    respostas = arquivo.readlines()

def gerar_questao(id):
    for i in range(id, id + 5):
        pergunta = perguntas[i]
        if i == id:
            pais = pergunta[3:]
            print(f'Qual a capital do(a) {pais.strip()}?')
        else:
            print(pergunta.strip())

def responder(id, escolha):
    if escolha == respostas[id + 2]:


id = randint(0, 194) * 5