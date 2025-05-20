# adicionei os dois valores requisitados
usuario_certo = 'adim'
senha_certo = 123456

# área que o usuário vai digitar
usuario = input('Insire seu login ')
senha = input('Insira sua senha')

# lógica de comparação para ver se estará correto a entrada de dados
if usuario_certo and senha_certo == usuario and senha:
    print('Login feito com sucesso')
else:
    print('Usuário ou senha incorretos')

