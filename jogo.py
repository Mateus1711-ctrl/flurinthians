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
posicoes=[] 
loop=0  
texto=''
passou=False
relogio = 0


def desenha(tela,assets):
    fonte=pygame.font.SysFont(None,100)

    tela.fill((255, 255, 255))
    fundo=assets['fundo']
    tela.blit(fundo,(0,0))
    coracao=assets['coracao']
    pocao=assets['pocao']
    bau=assets['bau']
    chave=assets['chave']
    raio=assets['raio']
    maca=assets['maca']
    global posicoes
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
    global texto
    global passou 
    global relogio
    x=10
   
        
    for i in range(vida):
        tela.blit(coracao,(x,630))
        x+=50
    #desenhar imagens abaixo (vou fazer um loop ultilizando aquele sorteio do assets,assim sorteio a quantidade de imagens,e adicionar elas a uma lista respectiva)
    global primeira #coloquei essa variavel para so passar pelo sorteio da quantidade de imagens,uma vez apenas
    
    if primeira:
        if loop==0:
            qtd_chave=random.randint(15,20)
        elif loop==1:
            print('tela2')  
            passou=False
        elif loop==2:
            qtd_chave=random.randint(5,10)
            qtd_raio=random.randint(5,10)
            qtd_maca=random.randint(5,10) 
        elif loop==3:
            print('tela4')
        elif loop==4:
            qtd_pocao=random.randint(5,10)
            qtd_bau=random.randint(5,10)
            qtd_chave=random.randint(5,10)
            qtd_raio=random.randint(5,10)
            qtd_maca=random.randint(5,10)
        elif loop==5:
            print('tela6')   

        if loop%2==0:
            
            for n in range(qtd_pocao):
                
                lista=[]
                x_pocao = random.randint(50,950)
                y_pocao = random.randint(50,600)
                lista = [x_pocao, y_pocao]
                colidiu = False
                for pos in posicoes:
                    if abs(lista[0]-pos[0])<50 or abs(lista[1]-pos[1])<50: 
                        colidiu = True
                if not colidiu:
                    lista_pocao.append(lista)
                    posicoes.append(lista)
            
            for n in range(qtd_bau):
            
                lista=[]
                x_bau = random.randint(50,950)
                y_bau = random.randint(50,600)
                lista = [x_bau, y_bau]
                colidiu = False
                for pos in posicoes:
                    if abs(lista[0]-pos[0])<50 or abs(lista[1]-pos[1])<50: 
                        colidiu = True
                if not colidiu:
                    lista_bau.append(lista)
                    posicoes.append(lista)
            
                    
            for n in range(qtd_chave):
                lista=[]
                x_qtd_chave = random.randint(50,950)
                y_qtd_chave = random.randint(50,600)
                lista = [x_qtd_chave, y_qtd_chave]
                
                colidiu = False
                for pos in posicoes:
                    if abs(lista[0]-pos[0])<50 or abs(lista[1]-pos[1])<50: 
                        colidiu = True
                if not colidiu:
                    lista_chave.append(lista)
                    posicoes.append(lista)
            
        #desenha pocao 
                        
            for n in range(qtd_raio):
                lista=[]
                x_qtd_raio = random.randint(50,950)
                y_qtd_raio = random.randint(50,600)
                lista = [x_qtd_raio, y_qtd_raio]
                colidiu = False
                for pos in posicoes:
                    if abs(lista[0]-pos[0])<50 or abs(lista[1]-pos[1])<50: 
                        colidiu = True
                if not colidiu:
                    lista_raio.append(lista)
                    posicoes.append(lista)
                
            for n in range(qtd_maca):
                lista=[]
                x_qtd_maca = random.randint(50,950)
                y_qtd_maca = random.randint(50,600)
                lista = [x_qtd_maca, y_qtd_maca]
                for pos in posicoes:
                    if abs(lista[0]-pos[0])<50 or abs(lista[1]-pos[1])<50: 
                        colidiu = True
                if not colidiu:
                    lista_maca.append(lista)
                    posicoes.append(lista)
                
    #desenha pocao
    if loop%2==0:
        for i in range(len(lista_pocao)): 
            tela.blit(pocao,(lista_pocao[i][0],lista_pocao[i][1]))
       
        for i in range(len(lista_bau)): 
            tela.blit(bau,(lista_bau[i][0],lista_bau[i][1]))
    
        for i in range(len(lista_chave)): 
            tela.blit(chave,(lista_chave[i][0],lista_chave[i][1]))
        for i in range(len(lista_raio)): 
            tela.blit(raio,(lista_raio[i][0],lista_raio[i][1]))
        for i in range(len(lista_maca)): 
            tela.blit(maca,(lista_maca[i][0],lista_maca[i][1]))
        texto=''
    else:
        tex=fonte.render(texto,True,(0,0,0))
        tela.blit(tex,(500,350))
        
    pygame.display.update()
    primeira=False

def game_loop(tela,assets):
    global relogio
    relogio += 1
    print(relogio)
    global vida
    global loop
    global primeira
    global texto
    global lista_chave
    global passou
    while game:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                  
                loop+=1
                primeira=True
              
            elif event.type==pygame.KEYDOWN:
                
                texto+=event.unicode
                
                if passou:
                    primeira=True    
                if int(texto)==(len(lista_chave)):
                    passou=True
                    
                if event.key==pygame.K_RETURN:
                    if passou==True:
                        print('foi')
                        loop+=1
            
                        primeira=True
                        
                    else:
                        print("nao foi")
                        loop+=1
                      
                        vida-=1  
                        primeira=True
                    
         
                    
                        
        desenha(tela,assets)

if __name__ == '__main__':
    tela,assets= inicializa()
    game_loop(tela,assets)





