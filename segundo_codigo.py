class PlanoTelefone:
       
  def __init__(self, nome, saldo):
   
    self.nome = nome
    self.__saldo = saldo  # Atributo privado para o saldo

  def verificar_saldo(self):
    
    return self.__saldo

  def mensagem_personalizada(self):
   
    saldo = self.verificar_saldo()

    if saldo < 10:
      mensagem = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
    elif saldo >= 50:
      mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."
    else:
      mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    return mensagem

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
    
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)