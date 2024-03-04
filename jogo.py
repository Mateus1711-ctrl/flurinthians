import pygame

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('jogo Artur e Matheus')
    assets = {}
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    assets['coracao'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 135754.png')
    assets['pocao'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 140048.png')
    assets['bau'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 140440.png')
    assets['chave'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 140618.png')
    assets['raio'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 140735.png')
    assets['maca'] = pygame.image.load('fotos pygame\Captura de tela 2024-03-04 140842.png')

    
    return tela

game = True



def desenha(tela):
    tela.fill((255, 255, 255))
    
    
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
