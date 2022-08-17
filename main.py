from os import execl
import uuid
from IPython.display import display
import pandas as pd
import xml

class Jogo:
    def __init__(self,nome, lancamento, fabricante, id):
        self.nome = nome
        self.lancamento = lancamento
        self.fabricante = fabricante
        self.id = uuid.uuid4()
        self.ident = id

    # def save(self):
    #     data = [['call_of_duty', 'actvision','2019','e85f95c5'], ['farcry', 'ubisorft','2020','5841']]
    #     df = pd.DataFrame(data , columns=['nome', 'marca','Ano','ID'])
    #     print(df)
    #    'Banco_dados. df.to_excel(xls', index= False) 

    def listar(self):
        Jogo = pd.read_excel('Banco_dados.xls')
        filtered_df= Jogo.query(' Ano == 2020 ') 
        print(filtered_df)    

    def ExibirInformacoesDesteJogo(self):
         print (f'nome do jogo e: {self.nome}\nlancamento: {self.lancamento}\nfabricante: {self.fabricante}\nID e :{self.id}\n')

save_do_call = input('Digite Salvar que seu game seja salvo: \n')
print('foi salvo')
lista = input('digite listar para mostrar game : \n')

call_of_duty = Jogo(nome ='call_of_duty', lancamento ='2019', fabricante='actvison', id='dadwad')
call_of_duty.listar()
# call_of_duty.save()






      