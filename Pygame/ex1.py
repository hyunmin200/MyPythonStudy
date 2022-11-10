import pygame
from sys import exit

pygame.init() # pygame을 호출하는 init()
screen = pygame.display.set_mode((800, 400)) # 게임 화면의 사이즈를 결정
# 크기를 바꾸기 쉽게 변수로 지정해줘도 된다.

pygame.display.set_caption('Runner')
#제목을 정하기

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() # Sys에 Exit로 완전히 꺼버리는 것
    # draw all our elements
    #update everything
    pygame.display.update() #위에 screen을 계속 불러오는 역활 
    #update는 특정부분만 update한다
    #하지만 위처럼 update() 괄호안을 비워놓는다면 전체 surface를 대사응로 하기 떄문에 flip와 똑같은 역활을 한다.
    #pygame.display.flip()은 update와 다르게 전체 surface를 업데이트를 한다.
    clock.tick(60) #프레임 설정
