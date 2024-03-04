import pygame

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('jogo Artur e Matheus')
    assets = {}
    assets['coracao'] = pygame.image.load('fotos pygame\coracao.png')
    assets['pocao'] = pygame.image.load('fotos pygame\pocao.png')
    assets['bau'] = pygame.image.load('fotos pygame\bau.png')
    assets['chave'] = pygame.image.load('fotos pygame\chave.png')
    assets['raio'] = pygame.image.load('fotos pygame\raio.png')
    assets['maca'] = pygame.image.load('fotos pygame\maca.png')

    
    return tela, assets

game = True



def desenha(tela,assets):
    tela.fill((255, 255, 255))
    tela.blit(())
    
    
    pygame.display.update()

def game_loop(tela):

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        desenha(tela)

if __name__ == '__main__':
    tela = inicializa()
    game_loop(tela)
