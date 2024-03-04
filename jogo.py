import pygame

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('jogo Artur e Matheus')
    return tela

game = True



def desenha(tela):
    tela.fill((250, 250, 250))
    
    
    pygame.display.update()

def game_loop(tela):

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == '__main__':
    tela = inicializa()
    game_loop(tela)
