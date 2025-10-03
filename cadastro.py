import hashlib

def sistema_cadastro():
    usuarios = []

    print("\n===== Sistema de Usuários =====")
    
    while True:
        nome = input("Nome completo (máx. 50 caracteres): ").strip().title()
        if nome.replace(" ", "").isalpha() and len(nome) <= 50:
            break
        elif len(nome) > 50:
            print("Nome muito longo!")
        else:
            print("Digite apenas letras e espaços.")
                    
    while True:
        telefone = input("Telefone (máx. 15 caracteres): ").strip()
        telefone = ''.join(filter(str.isdigit, telefone)) 
        if telefone and len(telefone) <= 15:
            break
        print("Telefone inválido! Digite apenas números (máx. 15).")

    while True:
        email = input("E-mail (máx. 50 caracteres): ").strip().lower()
        if email and len(email) <= 50 and "@" in email and "." in email:
            break
        print("E-mail inválido! Preencha corretamente e não ultrapasse 50 caracteres.")

    while True:
        senha = input("Senha (máx. 10 caracteres): ").strip()
        if senha and len(senha) <= 10:
            break
        print("Senha inválida! Preencha corretamente e não ultrapasse 10 caracteres.")
    
    while True:
        confirmar_senha = input("Confirme sua senha (máx. 10 caracteres): ").strip()
        if confirmar_senha == senha:
            break
        print("As senhas não coincidem! Tente novamente!")

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    usuario = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "senha": senha_hash
    }
    usuarios.append(usuario)
    print(f"\nUsuário {nome} cadastrado com sucesso!")

    return usuarios


if __name__ == "__main__":
    sistema_cadastro()
