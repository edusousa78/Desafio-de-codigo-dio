class UsuarioTelefone:
    
  def __init__(self, nome, numero, plano):
   
    self.nome = nome
    self.numero = numero
    self.plano = plano

  def __str__(self):
      return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  

usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)