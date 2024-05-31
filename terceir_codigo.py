# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
        
        
    def fazer_chamada(self, destinatario, duracao):
        
        custo_chamada = self.plano.custo_chamada(duracao)

        if self.plano.verificar_saldo(custo_chamada):
            self.plano.deduzir_saldo(custo_chamada)
            mensagem = f"Chamada para {destinatario} realizada com sucesso. " \
                        f"Saldo: ${self.plano.saldo:.2f}"
        else:
            mensagem = f"Saldo insuficiente para fazer a chamada."

        return mensagem


# Classe Pano, ela representa o plano de um usuário de telefone:
import re
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self, valor):
        
        return self.saldo >= valor

    def custo_chamada(self, duracao):
        
        return duracao * 0.10  # Custo por minuto: $0.10

    def deduzir_saldo(self, valor):
        
        self.saldo -= valor


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:

def formata_telefone(destinatario):
 padrao = r"(\d{2})(\d{5})(\d{4})"
  # Substitui o padrão por u0m formato com hifens
 formato = r"(\1) \2-\3"
 return re.sub(padrao, formato, destinatario)

nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

destinatario_formatado = formata_telefone(destinatario)

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario_formatado, duracao))