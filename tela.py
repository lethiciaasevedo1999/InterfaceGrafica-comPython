#Interface gráfica com python utilizando a biblioteca PySimpleGUI 

import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(10,0)), sg.Input(size=(15,0), key='nome')],
            [sg.Text('Ídade', size=(10,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key = 'yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes', key= 'aceitaCartao'), sg.Radio('Não', 'cartoes', key= 'naoAceitaCartao')],
            [sg.Slider(range=(0,260), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')], 
            # Assim que os dados forem preenchidos, os mesmos serão exibidos instantâneamente nesse espaço
            [sg.Output(size=(30,20))]

        ]


        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        


       

    def Iniciar(self):
        # Este loop mostra como manter a tela aberta e pronta para receber dados novamente, mesmo depois de enviá-los
        while True:
            # Extrair dados da tela
            self.button, self.values = self.janela.Read()



            # Nesse bloco podemos ver como se organiza melhor as informações no print, para que não seja tudo impresso em apenas uma linha,
            #atribuindo valores nas chaves
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não Aceita Cartão: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')



tela = TelaPython()
tela.Iniciar()
