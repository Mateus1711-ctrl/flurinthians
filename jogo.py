import pygame
import random
def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('jogo Artur e Mateus')
    assets = {}
    coracao= pygame.image.load('fotos_pygame/coracao.png')
    assets['coracao'] =pygame.transform.scale(coracao,(50,70))
    assets['pocao'] = pygame.image.load('fotos_pygame/pocao.png')
    assets['bau'] = pygame.image.load('fotos_pygame/bau.png')
    assets['chave'] = pygame.image.load('fotos_pygame/chave.png')
    assets['raio'] = pygame.image.load('fotos_pygame/raio.png')
    assets['maca'] = pygame.image.load('fotos_pygame/maca.png')
    fundo= pygame.image.load('fotos_pygame/fundo.png')
    assets['fundo']=pygame.transform.scale(fundo,(1000,700))
    assets['vida']=3


    
    return tela, assets

game = True


vida=3
primeira=True
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

    x=10
    global vida
    for i in range(vida):
        tela.blit(coracao,(x,630))
        x+=50
    #desenhar imagens abaixo (vou fazer um loop ultilizando aquele sorteio do assets,assim sorteio a quantidade de imagens,e adicionar elas a uma lista respectiva)
    global primeira #coloquei essa variavel para so passar pelo sorteio da quantidade de imagens,uma vez apenas
    if primeira:
        qtd_pocao=random.randint(0,10)
        qtd_bau=random.randint(0,10)
        qtd_chave=random.randint(0,10)
        qtd_raio=random.ranint(0,10)
        qtd_maca=random.randint(0,10)
        
    #desenha pocao
    for i in range(qtd_pocao):   
        tela.blit()     

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
