import re
import firebase_admin
from firebase_admin import credentials, firestore
import webview

# ===== Conexão com Firebase =====
cred = credentials.Certificate("register-c4290-firebase-adminsdk-fbsvc-86ac68d5a4.json")
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


# ===== Classe que o HTML pode chamar =====
class API:
    def cadastrar(self, nome, email, telefone, senha, confirmar):
        if not validar_nome(nome):
            return "❌ Nome inválido!"
        if not validar_email(email):
            return "❌ E-mail inválido!"
        if not validar_telefone(telefone):
            return "❌ Telefone inválido!"
        if not validar_senha(senha):
            return "❌ Senha inválida!"
        if senha != confirmar:
            return "❌ As senhas não coincidem!"

        usuario = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "senha": senha
        }
        db.collection("usuarios").add(usuario)
        return f"✅ Usuário {nome} cadastrado com sucesso no Firebase!"


# ===== Inicia a janela com o HTML =====
if __name__ == "__main__":
    api = API()
    webview.create_window("Cadastro - Hábitos+", "cadastro.html", js_api=api)
    webview.start()
