import pygame
import random
def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('jogo Artur e Mateus')
    assets = {}
    coracao= pygame.image.load('fotos_pygame/coracao.png')
    assets['coracao'] =pygame.transform.scale(coracao,(50,50))
    assets['pocao']= pygame.image.load('fotos_pygame/pocao.png')
    assets['pocao']=pygame.transform.scale(assets['pocao'],(50,50))
    assets['bau'] = pygame.image.load('fotos_pygame/bau.png')
    assets['bau']=pygame.transform.scale(assets['bau'],(50,50))
    assets['chave'] = pygame.image.load('fotos_pygame/chave.png')
    assets['chave']=pygame.transform.scale(assets['chave'],(50,50))
    assets['raio'] = pygame.image.load('fotos_pygame/raio.png')
    assets['raio']=pygame.transform.scale(assets['raio'],(50,50))
    assets['maca'] = pygame.image.load('fotos_pygame/maca.png')
    assets['maca']=pygame.transform.scale(assets['maca'],(50,50))
    fundo= pygame.image.load('fotos_pygame/fundo.png')
    assets['fundo']=pygame.transform.scale(fundo,(1000,700))
    assets['vida']=3


    
    return tela, assets

game = True

vida=3
primeira=True
qtd_pocao=0
qtd_bau=0
qtd_chave=0
qtd_raio=0
qtd_maca=0
lista=[]
lista_pocao=[]     
lista_bau=[]
lista_chave=[]
lista_raio=[]
lista_maca=[]   
def desenha(tela,assets):
    tela.fill((255, 255, 255))
    fundo=assets['fundo']
    tela.blit(fundo,(0,0))
    coracao=assets['coracao']
    pocao=assets['pocao']
    bau=assets['bau']
    chave=assets['chave']
    raio=assets['raio']
    maca=assets['maca']
    global lista
    global lista_pocao
    global lista_bau
    global lista_chave
    global lista_raio
    global lista_maca
    global vida
    global qtd_pocao
    global qtd_bau
    global qtd_chave
    global qtd_raio
    global qtd_maca
    x=10
   
        
    for i in range(vida):
        tela.blit(coracao,(x,630))
        x+=50
    #desenhar imagens abaixo (vou fazer um loop ultilizando aquele sorteio do assets,assim sorteio a quantidade de imagens,e adicionar elas a uma lista respectiva)
    global primeira #coloquei essa variavel para so passar pelo sorteio da quantidade de imagens,uma vez apenas
    if primeira:
        qtd_pocao=random.randint(1,6)
        qtd_bau=random.randint(1,6)
        qtd_chave=random.randint(1,6)
        qtd_raio=random.randint(1,6)
        qtd_maca=random.randint(1,6)
        lista_pocao = []
        for n in range(qtd_pocao):
            lista=[]
            x_pocao = random.randint(50,950)
            y_pocao = random.randint(50,600)
            lista.append(x_pocao)
            lista.append(y_pocao)
            if lista not in lista_bau or lista_chave or  lista_maca or  lista_raio or  lista_maca:
                lista_pocao.append(lista)
    
        for n in range(qtd_bau):
            lista=[]
            x_bau = random.randint(50,950)
            y_bau = random.randint(50,600)
            lista.append(x_bau)
            lista.append(y_bau)
            if lista not in lista_bau or not lista_chave or not lista_maca or not lista_raio or not lista_maca:
                lista_bau.append(lista)
        for n in range(qtd_chave):
            lista=[]
            x_qtd_chave = random.randint(50,950)
            y_qtd_chave = random.randint(50,600)
            lista.append(x_qtd_chave)
            lista.append(y_qtd_chave)
            if lista not in lista_bau or not lista_chave or not lista_maca or not lista_raio or not lista_maca:
                lista_chave.append(lista)
        for n in range(qtd_raio):
            lista=[]
            x_qtd_raio = random.randint(50,950)
            y_qtd_raio = random.randint(50,600)
            lista.append(x_qtd_raio)
            lista.append(y_qtd_raio)
            if lista not in lista_bau or not lista_chave or not lista_maca or not lista_raio or not lista_maca:
                lista_raio.append(lista)
        for n in range(qtd_maca):
            lista=[]
            x_qtd_maca = random.randint(50,950)
            y_qtd_maca = random.randint(50,600)
            lista.append(x_qtd_maca)
            lista.append(y_qtd_maca)
            if lista not in lista_bau or not lista_chave or not lista_maca or not lista_raio or not lista_maca:
                lista_maca.append(lista)
    #desenha pocao
    
    for i in range(qtd_pocao): 
        tela.blit(pocao,(lista_pocao[i][0],lista_pocao[i][1]))
       
    for i in range(qtd_bau): 
        tela.blit(bau,(lista_bau[i][0],lista_bau[i][1]))
    
    for i in range(qtd_chave): 
        tela.blit(chave,(lista_chave[i][0],lista_chave[i][1]))
    for i in range(qtd_raio): 
        tela.blit(raio,(lista_raio[i][0],lista_raio[i][1]))
    for i in range(qtd_maca): 
        tela.blit(maca,(lista_maca[i][0],lista_maca[i][1]))
       

    pygame.display.update()
    primeira=False
def game_loop(tela,assets):
    global vida
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                vida-=1    
        desenha(tela,assets)

if __name__ == '__main__':
    tela,assets= inicializa()
    game_loop(tela,assets)





