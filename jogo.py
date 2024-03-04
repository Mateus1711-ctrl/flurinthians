import pygame

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
    for i in range(3):
        tela.blit(coracao,(x,630))
        x+=50
    
    
    pygame.display.update()

def game_loop(tela,assets):

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        desenha(tela,assets)

if __name__ == '__main__':
    tela,assets= inicializa()
    game_loop(tela,assets)
