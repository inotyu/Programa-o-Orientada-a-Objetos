class Cliente:
  def __init__(self, nome, idade, telefone, email):
    self.nome = nome
    self.idade = idade
    self.telefone = telefone
    self.email = email
    
  def detalhes(self):
      print(f'Nome: {self.nome}')
      print(f'Idade: {self.idade}')
      print(f'Telefone: {self.telefone}')
      print(f'E-mail: {self.email}')

cliente1 = Cliente('Gean', 18, '(61) 99669182', 'contatogeanpls@gmail.com')
cliente2 = Cliente('Julia', 19, '(61) 982679873', 'jucontacte@gmail.com')

print('Informações dos Clientes:')
cliente1.detalhes()
cliente2.detalhes()


    



    