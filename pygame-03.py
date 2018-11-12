# 파이썬 모듈을 불러온다.
import pygame

# 초기화한다.
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


# 이미지를 불러온다.
player = pygame.image.load("resources/images/chatbot.png")
background = pygame.image.load("resources/images/background.png")

# 플레이어의 위치 관련 변수
player_pos = [100, 100]


# 키보드 관련 변수
keys = [False, False, False, False]

# 계속 화면이 보이도록 한다.
while True:
    # 화면을 깨끗하게 한다.
    screen.fill((0,0,0))
    
    # 플레이어의 위치를 이동한다.
    if keys[0]:
        player_pos[1] -= 5
    elif keys[2]:
        player_pos[1] += 5

    if keys[1]:
        player_pos[0] -= 5
    if keys[3]:
        player_pos[0] += 5
            
    # 모든 요소들을 다시 그린다.
    screen.blit(background, (0,0))
    screen.blit(player, player_pos)
    
    
    # 화면을 다시 그린다.
    pygame.display.flip()
    
    # 게임을 종료한다.
    for event in pygame.event.get():
        # 화면 종료 버튼(X)이 눌리면.
        if event.type == pygame.QUIT:
            # 게임을 종료한다
            pygame.quit()
            exit(0)
            
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
