<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Cadastro de Usuários</title>
</head>
<body>
  <h1>Cadastro de Usuários</h1>
  <form action="/cadastrar" method="POST">
    <label>Nome:</label><br>
    <input type="text" name="nome" maxlength="50" required><br><br>

    <label>Telefone:</label><br>
    <input type="text" name="telefone" maxlength="15" required><br><br>

    <label>Email:</label><br>
    <input type="email" name="email" maxlength="50" required><br><br>

    <label>Senha:</label><br>
    <input type="password" name="senha" maxlength="10" required><br><br>

    <button type="submit">Cadastrar</button>
  </form>
</body>
</html>
