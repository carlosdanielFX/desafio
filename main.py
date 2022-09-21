import uuid
import pandas as pd

class Jogo:
    def __init__(self, nome=None, lancamento=None, fabricante=None):
        self.nome = nome
        self.lancamento = lancamento
        self.fabricante = fabricante
        self.id = uuid.uuid4()

    def save(self):
        data = {
            "id": self.id,
            "name" : self.nome,
            "lancamento": self.lancamento,
            "fabricante": self.fabricante
        }
        data_list = []
        data_list.append(data)
        df = pd.DataFrame.from_dict(data=data_list)
        try:
            pd.read_csv('dados.csv')
            df.to_csv('dados.csv',index=True, header=False, mode='a')
        except:
            df.to_csv('dados.csv',index=True, header=True)

        

    def listar(self):
        Jogo = pd.read_csv('dados.csv')
        print(Jogo)   

    def ExibirInformacoesDesteJogo(self):
         print (f'nome do jogo e: {self.nome}\nlancamento: {self.lancamento}\nfabricante: {self.fabricante}\nID e :{self.id}\n')

# save_do_call = input('Digite Salvar que seu game seja salvo: \n')
# print('foi salvo')
# lista = input('digite listar para mostrar game : \n')

# call_of_duty = Jogo(nome ='call_of_duty', lancamento ='2019', fabricante='actvison', id='dadwad')
# call_of_duty.listar()
# call_of_duty.save()

# Aqui começa a aplicaçao
entrada = None
while entrada != 'x': # Enquanto entrada for diferente de x, rode a linha de baixo
    entrada = input('Você está na aplicação do carlos. Digite x para sair ou:  \n Digite s para salvar: \n')
    if entrada == 's':
        nome = input('digite um nome para seu jogo: \n')
        fabricante = input('digite um fabricante para seu jogo: \n')
        lancamento = input('em qual ano seu jogo foi lançado: \n')
        jogo = Jogo(nome=nome, fabricante=fabricante, lancamento=lancamento)
        jogo.save()
while entrada != 'e':
    entrada = input('Se voce deseja listar tabela use l para poder listar ou : \n use e para poder sair: \n')
    if entrada == 'l':
        jogo.listar()





      