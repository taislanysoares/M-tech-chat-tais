import json
import os

def carregar_faq():
    if os.path.exists("faq.json"):
        with open("faq.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def salvar_faq(faq):
    with open("faq.json", "w", encoding="utf-8") as f:
        json.dump(faq, f, ensure_ascii=False, indent=4)

def treinar_bot(faq):
    print("Modo de treinamento iniciado. Digite `sair` para sair.")
    while True:
        pergunta = input("Pergunta: ").strip()
        if pergunta.lower() == "sair":
            break
        resposta = input("Resposta: ").strip()
        if not pergunta or not resposta:
            print("Pergunta ou resposta inválida! Tente novamente.")
            continue
        faq[pergunta] = resposta
        print("Treinamento concluído.")
    salvar_faq(faq)

def chabot(faq):
    print("Chatbot: Olá! Sou seu assistente virtual. Pergunte algo ou digite `sair` para encerrar.")
    while True:
        entrada_usuario = input("Você: ").strip()
        if entrada_usuario.lower() in ["sair", "tchau", "adeus", "falo"]:
            print("Chatbot: Tchau! Foi um prazer conversar com você!")
            break
        elif entrada_usuario in faq:
            print(f"Chatbot: {faq[entrada_usuario]}")
        else:
            print("Chatbot: Desculpe, não entendi sua pergunta. Você pode me ensinar?")
            treinar_bot(faq)

def principal():
    faq = carregar_faq()
    while True:
        print("Escolha uma opção:")
        print("1. Iniciar chat")
        print("2. Treinar chatbot")
        print("3. Sair")
        escolha = input("Escolha: ").strip()
        if escolha == "1":
            chabot(faq)
        elif escolha == "2":
            treinar_bot(faq)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()
