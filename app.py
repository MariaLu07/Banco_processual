import re
import firebase_admin
from firebase_admin import credentials, firestore

# ===== Conexão com Firebase =====
cred = credentials.Certificate("register-c4290-firebase-adminsdk-fbsvc-2f58299ece.json")  # seu arquivo de chave
firebase_admin.initialize_app(cred)
db = firestore.client()

# ===== Validações =====
def validar_nome(nome):
    return bool(re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]{1,50}$", nome.strip()))

def validar_telefone(telefone):
    digitos = re.sub(r"\D", "", telefone)
    return 8 <= len(digitos) <= 15

def validar_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email)) and len(email) <= 50

def validar_senha(senha):
    return senha.strip() != "" and 4 <= len(senha) <= 10

# ===== Sistema de Cadastro =====
def sistema_cadastro():
    print("\n===== Sistema de Usuários =====")
    
    while True:
        nome = input("Nome completo (máx. 50 caracteres): ").strip()
        if validar_nome(nome):
            break
        print("Nome inválido!")

    while True:
        telefone = input("Telefone (pode ter +, -, () ): ").strip()
        if validar_telefone(telefone):
            telefone = re.sub(r"\D", "", telefone)
            break
        print("Telefone inválido!")

    while True:
        email = input("E-mail: ").strip()
        if validar_email(email):
            break
        print("E-mail inválido!")

    while True:
        senha = input("Senha (4 a 10 caracteres): ")
        if validar_senha(senha):
            break
        print("Senha inválida!")

    while True:
        confirmar = input("Confirme a senha: ")
        if confirmar == senha:
            break
        print("Senhas não coincidem!")

    # ===== Salvando no Firebase =====
    usuario = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }
    db.collection("usuarios").add(usuario)  # cria um documento dentro da coleção "usuarios"

    print(f"\nUsuário {nome} cadastrado com sucesso no Firebase!")

# ===== Executando =====
if __name__ == "__main__":
    while True:
        sistema_cadastro()
        continuar = input("\nCadastrar outro usuário? (s/n): ").lower()
        if continuar != "s":
            print("\nCadastro finalizado. Confira no Firebase Firestore.")
            break
