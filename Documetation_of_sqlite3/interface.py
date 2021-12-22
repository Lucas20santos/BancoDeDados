import PySimpleGUI as sg
import time
import pandas as pd

#CLASSES
class Animal:
    def __init__(self, especie, raca, nome, peso, castracao, mes, ano, alimentacao_dia, horarios):
        self.especie = especie
        self.raca = raca
        self.nome = nome
        self.peso = peso
        self.castracao = castracao
        self.mes = mes
        self.ano = ano
        self.alimentacao = alimentacao_dia
        self.horarios = horarios

class Racao:
    def __init__(self, marca, nome, animal, slot, quantidade):
        self.marca = marca
        self.nome = nome
        self.animal = animal
        self.slot = slot
        self.quantidade = quantidade

#DATA BASE
animal_db = pd.read_excel('animais.xlsx')
racao_db = pd.read_excel('racoes.xlsx')


#LISTA DE ANIMAIS E RAÇÕES DO USUÁRIO
animais = []
racoes = []
#LEITURA DOS ANIMAIS JA ADICIONADOS
if not(animal_db.empty):
    for i in range(0, animal_db.shape[0]):
        animais.append(Animal(str(animal_db['especie'][i]), str(animal_db['raca'][i]), str(animal_db['nome'][i]), float(animal_db['peso'][i]), bool(animal_db['castracao'][i]), int(animal_db['mes'][i]), int(animal_db['ano'][i]), int(animal_db['alimentacao'][i]), animal_db['horarios'][i]))
#LEITURA DAS RAÇÕES JA ADICIONADAS
if not(racao_db.empty):
    for i in range(0, racao_db.shape[0]):
        racoes.append(Racao(str(racao_db['marca'][i]), str(racao_db['nome'][i]), str(racao_db['animal'][i]),  int(racao_db['slot'][i]), int(racao_db['quantidade'][i])))

#FUNÇÕES PARA ATUALIZAR OS DADOS DAS RAÇÕES E ANIMAIS
def atualizar_animais(animais):
    animais_DF = pd.DataFrame([vars(f) for f in animais])
    animais_DF.to_excel('animais.xlsx')

def atualizar_racoes(racoes):
    racoes_DF = pd.DataFrame([vars(f) for f in racoes])
    racoes_DF.to_excel('racoes.xlsx')

#LISTA DE RAÇAS
cachorros_populares = ['Vira-lata', 'Shin Tzu', 'Yorkshire Terrier', 'Poodle', 'Lhasa Apso', 'Buldogue Francês', 'Pinscher', 'Golden Retriever', 'Spitz Alemão', 'Maltês']
gatos_populares = ['Persa', 'Himalaia', 'Siamês', 'Maine Coon', 'Angorá', 'Sphynx', 'Ragdoll', 'Ashera', 'American Shorthair', 'Exótico', 'Vira-lata']

#LISTA DE MARCAS
cachorros_marca = ['cachorro marca 1', 'cachorro marca 2']
gatos_marca = ['gato marca 1', 'gato marca 2']

#LISTA DE RAÇÕES
cachorros_racao = ['Tipo c1', 'Tipo c2', 'Tipo c3']
gatos_racao = ['Tipo g1', 'Tipo g2', 'Tipo g3']

aviso_erro = '\nError, espaços vazios \n ou \n resposta incorreta'

#CHAVES PARA OS HORARIOS
hora_key = ['hora1', 'hora2', 'hora3', 'hora4', 'hora5', 'hora6']
min_key = ['min1', 'min2', 'min3', 'min4', 'min5', 'min6']

#CONFIGURAÇÃO DA JANELA
tamanho_window = (800,600)
sg.theme('DarkTeal9')


menu = [
    [sg.Button('ADICIONAR ANIMAIS', size = (40,15), enable_events = True, key = 'ADICIONAR_ANIMAIS'), sg.Button('ADICIONAR RAÇÕES', size = (40,15), enable_events = True, key = 'ADICIONAR_RACOES')],
    [sg.Button('MOSTRAR ANIMAIS', size = (40,15), enable_events = True, disabled=True, key = 'MOSTRAR_ANIMAIS'), sg.Button('MOSTRAR RAÇÕES', size = (40,15), enable_events = True, disabled=True, key = 'MOSTRAR_RACOES')],
    [sg.Exit()]
]

def criar_menu1(MES, ANO):
    menu1 = [
        [sg.Text('Porfavor adicione os dados do animal:')],
        [sg.Text('Qual a espécie do animal:', size = (25,1)), sg.Radio('Cachorro', 'RADIO2', key = 'especie_cachorro', default = True, enable_events = True), sg.Radio('Gato', 'RADIO2', key = 'especie_gato', enable_events = True)],
        [sg.Text('Qual a raça do animal:', size = (25,1)), sg.Combo(cachorros_populares, size = (20,1), key = 'raca')],
        [sg.Text('Qual o nome do animal:', size = (25,1)), sg.InputText(key = 'nome')],
        [sg.Text('Qual o peso do animal:', size = (25,1)), sg.Slider(range = (1,100), size = (60,15), default_value = 50, orientation='horizontal', key = 'peso')],
        [sg.Text('O animal é castrado:', size = (25,1)), sg.Radio('Sim', 'RADIO1', key = 'castracao'), sg.Radio('Não', 'RADIO1', default = True)],
        [sg.Text('Quando o animal nasceu:', size = (25,1)), sg.Combo([i for i in range(1,13)], default_value=MES, key = 'mes'), sg.Text('/'), sg.Combo([i for i in range(ano_hoje, ano_hoje-31, -1)], default_value=ANO, key = 'ano')],
        [sg.Text('Quantas alimentações por dia:', size = (25,1)), sg.Slider(range = (1,6), size = (20,15), default_value = 3, orientation='horizontal', key = 'alimentacao_dia')],
        [sg.Submit(), sg.Exit()]
    ]
    return menu1

def criar_menu1_5(quantidade):
    menu1_5 = [
        [sg.Text('Horários de alimentação: ', size = (25,1))]
    ]
    for j in range(0, quantidade):
        menu1_5 = menu1_5 + [[sg.Combo([i for i in range(0,24)], default_value=6, key = hora_key[j]), sg.Text(':'), sg.Combo([i for i in range(0,60)], default_value=00, key = min_key[j])]]
    menu1_5 = menu1_5 + [[sg.Submit(), sg.Exit()]]
    return menu1_5

def criar_menu2():
    menu2 = [
        [sg.Text('Porfavor adicione os dados da ração:')],
        [sg.Text('A ração é para que animal:', size = (25,1)), sg.Radio('Cachorro', 'RADIO2', key = 'para_cachorro', default = True, enable_events = True), sg.Radio('Gato', 'RADIO2', key = 'para_gato', enable_events = True)],
        [sg.Text('Qual a marca da ração:', size = (25,1)), sg.Combo(cachorros_marca, size = (20,1), key = 'marca')],
        [sg.Text('Qual o nome/tipo da ração:', size = (25,1)), sg.Combo(cachorros_racao, size = (20,1), key = 'nome')],
        [sg.Text('Em que slot esta a ração:', size = (25,1)), sg.Slider(range = (1,6), size = (20,15), default_value = 1, orientation='horizontal', key = 'slot')],
        [sg.Submit(), sg.Exit()]
    ]
    return menu2

def criar_menu3(lista_animais):
    nomes = []
    for i in range(0, len(lista_animais)):
        nomes.append(lista_animais[i].nome)
    menu3 = [
        [sg.Text('Lista de animais adicionados')],
        [sg.Listbox(values = nomes, size = (30,6), default_values = nomes[0], enable_events = True, key = 'nome_animal')],
        [sg.Text(f'Nome: {lista_animais[0].nome}', key = 'nome')],
        [sg.Text(f'Espécie: {lista_animais[0].especie}', key = 'especie')],
        [sg.Text(f'Raça: {lista_animais[0].raca}', key = 'raca')],
        [sg.Text(f'Peso: {lista_animais[0].peso}', key = 'peso')],
        [sg.Text(f'Castrado: {lista_animais[0].castracao}', key = 'castracao')],
        [sg.Text(f'Nascimento: {lista_animais[0].mes}/{lista_animais[0].ano}', key = 'nascimento')],
        [sg.Text(f'Alimentações por dia: {lista_animais[0].alimentacao}', key = 'alimentacao')],
        [sg.Text(f'Os horários são: {lista_animais[0].horarios}', key = 'horario')],
        [sg.Button('Deletar', enable_events=True, key = 'deletar'), sg.Exit()]
    ]
    return menu3, nomes

def criar_menu4(lista_racoes):
    slots = []
    for i in range(0, len(lista_racoes)):
        slots.append(str(lista_racoes[i].slot))
    menu4 = [
        [sg.Text('Lista de animais adicionados')],
        [sg.Listbox(values = slots, size = (30,6), default_values = slots[0], enable_events = True, key = 'slot_racao')],
        [sg.Text(f'Nome: {lista_racoes[0].nome}', key = 'nome')],
        [sg.Text(f'Marca: {lista_racoes[0].marca}', key = 'marca')],
        [sg.Text(f'Animal destinado: {lista_racoes[0].animal}', key = 'animal')],
        [sg.Text(f'Slot: {lista_racoes[0].slot}', key = 'slot')],
        [sg.Text(f'Quantidade (g): {lista_racoes[0].quantidade}', key = 'quantidade')],
        [sg.Button('Deletar', enable_events=True, key = 'deletar'), sg.Exit()]
    ]
    return menu4, slots

def criar_aviso():
    aviso = [
        [sg.Text('Falta dados serem preenchidos', size = (3, 1))]
    ]
    return aviso

window = sg.Window('Software de Ração', layout = menu, size = tamanho_window, element_justification='c',  no_titlebar=True)

i = 0
while True:
    #DATA ATUAL
    min_hoje = time.localtime().tm_min
    hora_hoje = time.localtime().tm_hour
    mes_hoje = time.localtime().tm_mon
    ano_hoje = time.localtime().tm_year

    #EVENTOS DO MENU
    if i == 0:
        event, values = window.read(timeout = 250)
        #VISIBILIDADE DE MOSTRAR ANIMAIS
        if len(animais)>=1:
            window['MOSTRAR_ANIMAIS'].update(disabled=False)
        else:
            window['MOSTRAR_ANIMAIS'].update(disabled=True)
        #VISIBILIDADE DE MOSTRAR RAÇÕES
        if len(racoes)>=1:
            window['MOSTRAR_RACOES'].update(disabled=False)
        else:
            window['MOSTRAR_RACOES'].update(disabled=True)

        if event == 'Exit':
            break
        if event == 'ADICIONAR_ANIMAIS':
            i = 1
            window1 = sg.Window('Software de Ração', layout = criar_menu1(mes_hoje, ano_hoje), size = tamanho_window, no_titlebar=True)
        if event == 'ADICIONAR_RACOES':
            i = 2
            window2 = sg.Window('Software de Ração', layout = criar_menu2(), size = tamanho_window, no_titlebar=True)
        if event == 'MOSTRAR_ANIMAIS':
            i = 3
            index = 0
            menu3, nomes = criar_menu3(animais)
            window3 = sg.Window('Software de Ração', layout = menu3, size = tamanho_window, no_titlebar=True)
        if event == 'MOSTRAR_RACOES':
            i = 4
            index = 0
            menu4, slots = criar_menu4(racoes)
            window4 = sg.Window('Software de Ração', layout = menu4, size = tamanho_window, no_titlebar=True)
    
    
    #EVENTOS DO MENU 1
    if i == 1:
        event1, values1 = window1.read(timeout=60000)
        if event1 == sg.WIN_CLOSED or event1 =='Exit':
            i = 0
            window1.close()
        if event1 == 'Submit':
            erro = False
            for keys in values1.keys():
                if values1[keys] == '' or (not(values1['raca'] in cachorros_populares) and values1['especie_cachorro']==True) or (not(values1['raca'] in gatos_populares) and values1['especie_gato']==True) or not(str(values1['mes']).isnumeric()) or not(str(values1['ano']).isnumeric()) or (int(values1['mes'])>12 or int(values1['mes'])<1) or (int(values1['ano'])>ano_hoje or int(values1['ano'])<(ano_hoje-30)) or (int(values1['ano']) == ano_hoje and int(values1['mes'])> mes_hoje):
                    erro = True
                elif erro == False:
                    erro = False

            #Definição da espécie
            if values1['especie_cachorro'] == True:
                esp = 'cachorro'
            else:
                esp = 'gato'
            #Adicionar a lista de animais do usuário
            if erro == False:
                i = 1.5
                window1_5 = sg.Window('Software de Ração', layout = criar_menu1_5(int(values1['alimentacao_dia'])), size = tamanho_window,  no_titlebar=True)
            else:
                sg.Popup(aviso_erro, no_titlebar=True, font = ('Helvetica', 24), background_color='red', auto_close_duration=2, auto_close=True)

        if event1 == 'especie_gato':
            window1['raca'].update(values = gatos_populares)
        elif event1 == 'especie_cachorro':
            window1['raca'].update(values = cachorros_populares)
    
    #EVENTOS DO MENU 1.5
    if i == 1.5:
        event1_5, values1_5 = window1_5.read(timeout=60000)
        if event1_5 == sg.WIN_CLOSED or event1_5 =='Exit':
            i = 1
            window1_5.close()
        if event1_5 == 'Submit':
            erro = False
            for keys in values1_5.keys():
                if values1_5[keys] == '' or not(str(values1_5[keys]).isnumeric()):
                    erro = True
                elif erro == False:
                    erro = False
            k = 0
            while erro == False:
                if int(values1_5[hora_key[k]]) > 23 or int(values1_5[hora_key[k]]) < 0 or int(values1_5[min_key[k]]) > 59 or int(values1_5[min_key[k]]) < 0:
                    erro = True
                elif k == int(values1['alimentacao_dia'])-1:
                    break
                k = k+1
            
            if erro == False:
                horario = []
                for x in range(0, int(values1['alimentacao_dia'])):
                    horario.append((values1_5[hora_key[x]], values1_5[min_key[x]]))

                animais.append(Animal(str(esp), str(values1['raca']), str(values1['nome']), float(values1['peso']), bool( values1['castracao']), int(values1['mes']), int(values1['ano']), int(values1['alimentacao_dia']), horario))
                atualizar_animais(animais)
                i = 0
                window1_5.close()
                window1.close()
            else:
                sg.Popup(aviso_erro, no_titlebar=True, font = ('Helvetica', 24), background_color='red', auto_close_duration=2, auto_close=True)


    #EVENTOS DO MENU 2
    if i == 2:
        event2, values2 = window2.read(timeout=60000)
        if event2 == sg.WIN_CLOSED or event2 =='Exit':
            i = 0
            window2.close()
        if event2 == 'para_gato':
            window2['marca'].update(values = gatos_marca)
            window2['nome'].update(values = gatos_racao)
        elif event2 == 'para_cachorro':
            window2['marca'].update(values = cachorros_marca)
            window2['nome'].update(values = cachorros_racao)
        
        if event2 == 'Submit':
            erro = False
            for keys in values2.keys():
                if values2[keys] == '' or (not(values2['nome'] in cachorros_racao) and values2['para_cachorro']==True) or (not(values2['nome'] in gatos_racao) and values2['para_gato']==True) or (not(values2['marca'] in cachorros_marca) and values2['para_cachorro']==True) or (not(values2['marca'] in gatos_marca) and values2['para_gato']==True):
                    erro = True
                elif erro == False:
                    erro = False
            if len(racoes)>0:
                for a in range(0, len(racoes)):
                    if values2['slot'] == racoes[a].slot:
                        erro = True

            #Definição da espécie
            if values2['para_cachorro'] == True:
                alvo = 'cachorro'
            else:
                alvo = 'gato'
            #Adicionar a lista de rações do usuário
            if erro == False:
                racoes.append(Racao(str(values2['marca']), str(values2['nome']), str(alvo),  int(values2['slot']), int(3000)))
                atualizar_racoes(racoes)
                i = 0
                window2.close()
            else:
                sg.Popup(aviso_erro, no_titlebar=True, font = ('Helvetica', 24), background_color='red', auto_close_duration=2, auto_close=True)
    
    #EVENTOS DO MENU 3
    if i == 3:
        event3, values3 = window3.read(timeout=60000)
        if event3 == sg.WIN_CLOSED or event3 =='Exit':
            i = 0
            window3.close()
        if event3 == 'nome_animal':
            index = nomes.index(values3['nome_animal'][0])
            window3['nome'].update(f'Nome: {animais[index].nome}')
            window3['especie'].update(f'Espécie: {animais[index].especie}')
            window3['raca'].update(f'Raça: {animais[index].raca}')
            window3['peso'].update(f'Peso: {animais[index].peso}')
            window3['castracao'].update(f'Castrado: {animais[index].castracao}')
            window3['nascimento'].update(f'Nascimento: {animais[index].mes}/{animais[index].ano}')
            window3['alimentacao'].update(f'Alimentações por dia: {animais[index].alimentacao}')
            window3['horario'].update(f'Os horários são: {animais[index].horarios}')
        if event3 == 'deletar':
            i = 0
            animais.pop(index)
            atualizar_animais(animais)
            window3.close()
    
    #EVENTOS DO MENU 4
    if i == 4:
        event4, values4 = window4.read(timeout=60000)
        if event4 == sg.WIN_CLOSED or event4 =='Exit':
            i = 0
            window4.close()
        if event4 == 'slot_racao':
            index = slots.index(values4['slot_racao'][0])
            window4['nome'].update(f'Nome: {racoes[index].nome}')
            window4['marca'].update(f'Marca: {racoes[index].marca}')
            window4['animal'].update(f'Animal destinado: {racoes[index].animal}')
            window4['slot'].update(f'Slot: {racoes[index].slot}')
            window4['quantidade'].update(f'Quantidade (g): {racoes[index].quantidade}')
        if event4 == 'deletar':
            i = 0
            racoes.pop(index)
            atualizar_racoes(racoes)
            window4.close()
    
    #comparar hora_hoje
    #alimentar animal

window.close()
window1.close()
window2.close()
window3.close()
window4.close()