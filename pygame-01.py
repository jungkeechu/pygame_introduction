# 파이썬 모듈을 불러온다.
import pygame

# 초기화한다.
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


# 이미지를 불러온다.


# 게임이 진행되는 동안 계속 화면이 보이도록 한다.
while True:
    # 화면을 깨끗하게 한다.
    screen.fill((0,0,0))
    
    
    # 모든 요소들을 다시 그린다.
    
    
    
    # 화면을 실제로 그림다.
    pygame.display.flip()
    
    # 게임을 종료한다.
    for event in pygame.event.get():
        # 화면 종료 버튼(X)이 눌리면.
        if event.type == pygame.QUIT:
            # 게임을 종료한다
            pygame.quit()
            exit(0)
