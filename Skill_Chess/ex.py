# 팀플 게임
import pygame  # pygame 가져오기
from pygame.locals import *  # 로컬에서 가져오기
import sys
import random

pygame.init()  # 게임 초기화

width, height = 1280, 720  # 창 너비, 높이 설정
screen = pygame.display.set_mode((width, height))  # 스크린 띄우기
pygame.display.set_caption('Skill_Chess')  # 창 이름 지정


class Sprite_Button(pygame.sprite.Sprite):

    def __init__(self, image, pressed, position):
        pygame.sprite.Sprite.__init__(self)
        self.normal = pygame.image.load(image)
        self.position = position
        self.rotation = 0
        self.pressed = pygame.image.load(pressed)
        self.save = pygame.image.load(image)

    def update(self, pressed):
        if self in pressed:
            self.normal = self.pressed
        else:
            self.normal = self.save

class tile_spr(pygame.sprite.Sprite):

    def __init__(self, image, position):
        self.red = pygame.image.load("tile_r.png")
        self.yellow = pygame.image.load("tile_y.png")
        self.blue = pygame.image.load("tile_b.png")
        self.normal = pygame.image.load("tile.png")
        self.image = pygame.image.load(image)
        self.pos = position
        self.pos_x, self.pos_y = position

    def tile_stat(self, list):
        if list[0] == 1:
            self.now = self.normal
        if list[0] == 2:
            self.now = self.red
        if list[0] == 3:
            self.now = self.yellow
        if list[0] == 4:
            self.now = self.blue

class piece():

    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.pos_s = (0, 0)
        self.pos_p = self.pos_s

    def movement1(self, position, no, sel, player):  # 기동에 있어서 필요한 요소는 무엇인가  no는 밑에 기물리스트의 인덱스로써 이 이동함수를 어떤 클래스의 기물이 사용하는가를 나타내 준다.
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if 1 not in piece_clicked and spell_use[0] == 0:  # 클릭된 폰이 없다면, 폰의 위치를 눌렀을때,
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if mouse_x >= pawn_x and mouse_x <= pawn_x + 113 and mouse_y >= pawn_y and mouse_y <= pawn_y + 113:  # 마우스의 위치가 폰의 위치인 타일 내에 있다면,
                        piece_clicked[no] = 1
                if piece_clicked[no] == 1:  # 자기 자신이 클릭되었을때, 이동/공격 버튼을 눌렀다면,
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1:
                        if mov_x <= mouse_x <= mov_x + 132 and mov_y <= mouse_y <= mov_y + 42:
                            move_button.update([move_button])
                if piece_clicked[no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 1:  # 만약 보드의 색깔이 빨간색이고
                                move_x, move_y = board_pos[en][num]
                                if mouse_x >= move_x and mouse_x <= move_x + 113 and mouse_y >= move_y and mouse_y <= move_y + 113:
                                    piece_pos[player][no] = move_x, move_y
                                    move[player][0] -= 1
                                    piece_clicked[no] = 0
                                    piece_attack[player][no] = 0
            if event.type == MOUSEBUTTONUP:
                if piece_clicked[no] == 1 and move_b[1] == 0 and piece_attack[player][no] == 0:
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if pawn_x <= mouse_x <= pawn_x + 113 and pawn_y <= mouse_y <= pawn_y + 113:
                        move_b[1] = 1  # move / attack 버튼 출현 함수
                        move_b[0] = pawn_x + 79, pawn_y - 43
                        piece_attack[player][no] = 0
                    else:
                        piece_attack[player][no] = 0
                        piece_clicked[no] = 0
                if piece_clicked[no] == 1:
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1 and mouse_x >= mov_x and mouse_x <= mov_x + 132 and mouse_y >= mov_y and mouse_y <= mov_y + 42:
                        move_button.update([])
                        move_b[1] = 0
                        move_b[0] = 1280, 720
                        for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                            if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                                p = board_pos[en].index(position)
                                piece_attack[player][no] = 1
                                for til in range(4):
                                    if til == 0:
                                        if en + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p] = 1
                                    if til == 1:
                                        if en - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p] = 1
                                    if til == 2:
                                        if p + 1 == 5:
                                            pass
                                        else:
                                            board_col[en][p + 1] = 1
                                    if til == 3:
                                        if p - 1 == -1:
                                            pass
                                        else:
                                            board_col[en][p - 1] = 1
                    else:
                        move_button.update([])

    def movement2(self, position, no, sel, player):  # 기동에 있어서 필요한 요소는 무엇인가  no는 밑에 기물리스트의 인덱스로써 이 이동함수를 어떤 클래스의 기물이 사용하는가를 나타내 준다.  # 만약 폰의 배치가 끝난 상태라면
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if 1 not in piece_clicked and spell_use[0] == 0:  # 클릭된 폰이 없다면, 폰의 위치를 눌렀을때,
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if mouse_x >= pawn_x and mouse_x <= pawn_x + 113 and mouse_y >= pawn_y and mouse_y <= pawn_y + 113:  # 마우스의 위치가 폰의 위치인 타일 내에 있다면,
                        piece_clicked[no] = 1
                if piece_clicked[no] == 1:  # 자기 자신이 클릭되었을때, 이동/공격 버튼을 눌렀다면,
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1:
                        if mov_x <= mouse_x <= mov_x + 132 and mov_y <= mouse_y <= mov_y + 42:
                            move_button.update([move_button])
                if piece_clicked[no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 1:  # 만약 보드의 색깔이 빨간색이고
                                move_x, move_y = board_pos[en][num]
                                if mouse_x >= move_x and mouse_x <= move_x + 113 and mouse_y >= move_y and mouse_y <= move_y + 113:
                                    piece_pos[player][no] = move_x, move_y
                                    move[player][0] -= 1
                                    piece_clicked[no] = 0
                                    piece_attack[player][no] = 0
            if event.type == MOUSEBUTTONUP:
                if piece_clicked[no] == 1 and move_b[1] == 0 and piece_attack[player][no] == 0:
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if pawn_x <= mouse_x <= pawn_x + 113 and pawn_y <= mouse_y <= pawn_y + 113:
                        move_b[1] = 1  # move / attack 버튼 출현 함수
                        move_b[0] = pawn_x + 79, pawn_y - 43
                        piece_attack[player][no] = 0
                    else:
                        piece_attack[player][no] = 0
                        piece_clicked[no] = 0
                if piece_clicked[no] == 1:
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1 and mouse_x >= mov_x and mouse_x <= mov_x + 132 and mouse_y >= mov_y and mouse_y <= mov_y + 42:
                        move_button.update([])
                        move_b[1] = 0
                        move_b[0] = 1280, 720
                        for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                            if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                                p = board_pos[en].index(position)
                                piece_attack[player][no] = 1
                                for til in range(4):
                                    if til == 0:
                                        if en + 1 == 5 or p + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p + 1] = 1  # 오른쪽 위 대각선
                                    if til == 1:
                                        if en - 1 == -1 or p - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p - 1] = 1  # 왼쪽 아래 대각선
                                    if til == 2:
                                        if p + 1 == 5 or en - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p + 1] = 1  # 오른쪽 아래 대각선
                                    if til == 3:
                                        if p - 1 == -1 or en + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p - 1] = 1  # 왼쪽 아래 대각선
                    else:
                        move_button.update([])

    def movement3(self, position, no, sel, player):  # 모든 방향
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if 1 not in piece_clicked and spell_use[0] == 0:  # 클릭된 폰이 없다면, 폰의 위치를 눌렀을때,
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if mouse_x >= pawn_x and mouse_x <= pawn_x + 113 and mouse_y >= pawn_y and mouse_y <= pawn_y + 113:  # 마우스의 위치가 폰의 위치인 타일 내에 있다면,
                        piece_clicked[no] = 1
                if piece_clicked[no] == 1:  # 자기 자신이 클릭되었을때, 이동/공격 버튼을 눌렀다면,
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1:
                        if mov_x <= mouse_x <= mov_x + 132 and mov_y <= mouse_y <= mov_y + 42:
                            move_button.update([move_button])
                if piece_clicked[no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 1:  # 만약 보드의 색깔이 빨간색이고
                                move_x, move_y = board_pos[en][num]
                                if mouse_x >= move_x and mouse_x <= move_x + 113 and mouse_y >= move_y and mouse_y <= move_y + 113:
                                    piece_pos[player][no] = move_x, move_y
                                    move[player][0] -= 1
                                    piece_clicked[no] = 0
                                    piece_attack[player][no] = 0
            if event.type == MOUSEBUTTONUP:
                if piece_clicked[no] == 1 and move_b[1] == 0 and piece_attack[player][no] == 0:
                    pawn_x, pawn_y = position  # 폰의 포지션
                    if pawn_x <= mouse_x <= pawn_x + 113 and pawn_y <= mouse_y <= pawn_y + 113:
                        move_b[1] = 1  # move / attack 버튼 출현 함수
                        move_b[0] = pawn_x + 79, pawn_y - 43
                        piece_attack[player][no] = 0
                    else:
                        piece_attack[player][no] = 0
                        piece_clicked[no] = 0
                if piece_clicked[no] == 1:
                    mov_x, mov_y = move_b[0]
                    if move_b[1] == 1 and mov_x <= mouse_x <= mov_x + 132 and mouse_y >= mov_y and mouse_y <= mov_y + 42:
                        move_button.update([])
                        move_b[1] = 0
                        move_b[0] = 1280, 720
                        for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                            if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                                p = board_pos[en].index(position)
                                piece_attack[player][no] = 1
                                for til in range(8):
                                    if til == 0:
                                        if en + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p] = 1
                                    if til == 1:
                                        if en - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p] = 1
                                    if til == 2:
                                        if p + 1 == 5:
                                            pass
                                        else:
                                            board_col[en][p + 1] = 1
                                    if til == 3:
                                        if p - 1 == -1:
                                            pass
                                        else:
                                            board_col[en][p - 1] = 1
                                    if til == 4:
                                        if en + 1 == 5 or p + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p + 1] = 1  # 오른쪽 위 대각선
                                    if til == 5:
                                        if en - 1 == -1 or p - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p - 1] = 1  # 왼쪽 아래 대각선
                                    if til == 6:
                                        if p + 1 == 5 or en - 1 == -1:
                                            pass
                                        else:
                                            board_col[en - 1][p + 1] = 1  # 오른쪽 아래 대각선
                                    if til == 7:
                                        if p - 1 == -1 or en + 1 == 5:
                                            pass
                                        else:
                                            board_col[en + 1][p - 1] = 1  # 왼쪽 아래 대각선
                    else:
                        move_button.update([])

    def attack1(self, position, no, sel, n_player, o_player):  # 직선 1칸 공격
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if piece_clicked[no] == 1 and piece_attack[n_player][no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 4:  # 보드색이 초록색이고
                                attack_x, attack_y = board_pos[en][num]
                                if mouse_x >= attack_x and mouse_x <= attack_x + 113 and mouse_y >= attack_y and mouse_y <= attack_y + 113:
                                    now_attack.append(board_pos[en][num])
                                    attackin_piece_pos.append(position)
                                    respond_situation[0] = 1
            if respond_situation[0] == 2 and piece_attack[n_player][no] == 1:
                attack_x, attack_y = now_attack[-1]
                piece_pos[n_player][no] = attack_x, attack_y
                if piece_pos[n_player][no] == piece_pos[o_player][0]:
                    piece_pos[o_player][0] = (1280, 720)
                if piece_pos[n_player][no] == piece_pos[o_player][1]:
                    piece_pos[o_player][1] = (1280, 720)
                    dead_list.append(piece_pos[o_player][1])
                    dead_list2.append(1)
                if piece_pos[n_player][no] == piece_pos[o_player][2]:
                    piece_pos[o_player][2] = (1280, 720)
                    dead_list.append(piece_pos[o_player][2])
                    dead_list2.append(2)
                piece_clicked[no] = 0
                piece_attack[n_player][no] = 0
                move[n_player][0] -= 1
                respond_situation[0] = 0
            if piece_attack[n_player][no] == 1 and respond_situation[0] == 0:
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면, 영어열의 몇번째에 있는지 상수로 바꾸고 그것을 통해서 그 칸을 파란색으로 바꾼다.
                        p = board_pos[en].index(position)
                        for til in range(4):
                            if til == 0:
                                if en + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p] in piece_pos[o_player]:
                                        board_col[en + 1][p] = 4
                            if til == 1:
                                if en - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p] in piece_pos[o_player]:
                                        board_col[en - 1][p] = 4
                            if til == 2:
                                if p + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en][p + 1] in piece_pos[o_player]:
                                        board_col[en][p + 1] = 4
                            if til == 3:
                                if p - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en][p - 1] in piece_pos[o_player]:
                                        board_col[en][p - 1] = 4

    def attack2(self, position, no, sel, n_player, o_player):  # 직선 1칸 공격
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if piece_clicked[no] == 1 and piece_attack[n_player][no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 4:  # 보드색이 초록색이고
                                attack_x, attack_y = board_pos[en][num]
                                if mouse_x >= attack_x and mouse_x <= attack_x + 113 and mouse_y >= attack_y and mouse_y <= attack_y + 113:
                                    now_attack.append(board_pos[en][num])
                                    attackin_piece_pos.append(position)
                                    respond_situation[0] = 1
            if respond_situation[0] == 2 and piece_attack[n_player][no] == 1:
                attack_x, attack_y = now_attack[-1]
                piece_pos[n_player][no] = attack_x, attack_y
                if piece_pos[n_player][no] == piece_pos[o_player][0]:
                    piece_pos[o_player][0] = (1280, 720)
                if piece_pos[n_player][no] == piece_pos[o_player][1]:
                    piece_pos[o_player][1] = (1280, 720)
                    dead_list.append(piece_pos[o_player][1])
                    dead_list2.append(1)
                if piece_pos[n_player][no] == piece_pos[o_player][2]:
                    piece_pos[o_player][2] = (1280, 720)
                    dead_list.append(piece_pos[o_player][2])
                    dead_list2.append(2)
                piece_clicked[no] = 0
                piece_attack[n_player][no] = 0
                move[n_player][0] -= 1
                respond_situation[0] = 0
            if piece_attack[n_player][no] == 1 and respond_situation[0] == 0:
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면, 영어열의 몇번째에 있는지 상수로 바꾸고 그것을 통해서 그 칸을 파란색으로 바꾼다.
                        p = board_pos[en].index(position)
                        for til in range(4):
                            if til == 0:
                                if en + 1 == 5 or p + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p + 1] in piece_pos[o_player]:
                                        board_col[en + 1][p + 1] = 4  # 오른쪽 위 대각선
                            if til == 1:
                                if en - 1 == -1 or p - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p - 1] in piece_pos[o_player]:
                                        board_col[en - 1][p - 1] = 4  # 왼쪽 아래 대각선
                            if til == 2:
                                if p + 1 == 5 or en - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p + 1] in piece_pos[o_player]:
                                        board_col[en - 1][p + 1] = 4  # 오른쪽 아래 대각선
                            if til == 3:
                                if p - 1 == -1 or en + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p - 1] in piece_pos[o_player]:
                                        board_col[en + 1][p - 1] = 4  # 왼쪽 아래 대각선

    def attack3(self, position, no, sel, n_player, o_player):  # 직선 1칸 공격
        if sel == 1:
            if event.type == MOUSEBUTTONDOWN:
                if piece_clicked[no] == 1 and piece_attack[n_player][no] == 1:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 4:  # 보드색이 초록색이고
                                attack_x, attack_y = board_pos[en][num]
                                if mouse_x >= attack_x and mouse_x <= attack_x + 113 and mouse_y >= attack_y and mouse_y <= attack_y + 113:
                                    now_attack.append(board_pos[en][num])
                                    attackin_piece_pos.append(position)
                                    respond_situation[0] = 1
            if respond_situation[0] == 2 and piece_attack[n_player][no] == 1:
                attack_x, attack_y = now_attack[-1]
                piece_pos[n_player][no] = attack_x, attack_y
                if piece_pos[n_player][no] == piece_pos[o_player][0]:
                    piece_pos[o_player][0] = (1280, 720)
                if piece_pos[n_player][no] == piece_pos[o_player][1]:
                    piece_pos[o_player][1] = (1280, 720)
                    dead_list.append(piece_pos[o_player][1])
                    dead_list2.append(1)
                if piece_pos[n_player][no] == piece_pos[o_player][2]:
                    piece_pos[o_player][2] = (1280, 720)
                    dead_list.append(piece_pos[o_player][2])
                    dead_list2.append(2)
                piece_clicked[no] = 0
                piece_attack[n_player][no] = 0
                move[n_player][0] -= 1
                respond_situation[0] = 0
            if piece_attack[n_player][no] == 1 and respond_situation[0] == 0:
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if position in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면, 영어열의 몇번째에 있는지 상수로 바꾸고 그것을 통해서 그 칸을 파란색으로 바꾼다.
                        p = board_pos[en].index(position)
                        for til in range(8):
                            if til == 0:
                                if en + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p] in piece_pos[o_player]:
                                        board_col[en + 1][p] = 4
                            if til == 1:
                                if en - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p] in piece_pos[o_player]:
                                        board_col[en - 1][p] = 4
                            if til == 2:
                                if p + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en][p + 1] in piece_pos[o_player]:
                                        board_col[en][p + 1] = 4
                            if til == 3:
                                if p - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en][p - 1] in piece_pos[o_player]:
                                        board_col[en][p - 1] = 4
                            if til == 4:
                                if en + 1 == 5 or p + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p + 1] in piece_pos[o_player]:
                                        board_col[en + 1][p + 1] = 4  # 오른쪽 위 대각선
                            if til == 5:
                                if en - 1 == -1 or p - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p - 1] in piece_pos[o_player]:
                                        board_col[en - 1][p - 1] = 4  # 왼쪽 아래 대각선
                            if til == 6:
                                if p + 1 == 5 or en - 1 == -1:
                                    pass
                                else:
                                    if board_pos[en - 1][p + 1] in piece_pos[o_player]:
                                        board_col[en - 1][p + 1] = 4  # 오른쪽 아래 대각선
                            if til == 7:
                                if p - 1 == -1 or en + 1 == 5:
                                    pass
                                else:
                                    if board_pos[en + 1][p - 1] in piece_pos[o_player]:
                                        board_col[en + 1][p - 1] = 4  # 왼쪽 아래 대각선

    def long_dealer_sk1(self, no, sel, player):  #여기서 no는 손패의 위치를 나타내는 것이다. 위의 함수는 기물의 클래스를 나타낸다
        spell_pos = hand_pos[no][sel]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
                    sk_1[0] = 1
        if hand_sel[no][sel] == 1:
            if card_clicked[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] == piece_pos[no][0]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
        if hand_sel[no][sel] == 1 and card_clicked[0] == 1 and spell_use[0] == 1:
            for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                    p = board_pos[en].index(sp_piece[-1])
                    for til in range(8):
                        if til == 0:
                            if en + 1 == 5:
                                pass
                            else:
                                board_col[en + 1][p] = 3
                        if til == 1:
                            if en - 1 == -1:
                                pass
                            else:
                                board_col[en - 1][p] = 3
                        if til == 2:
                            if p + 1 == 5:
                                pass
                            else:
                                board_col[en][p + 1] = 3
                        if til == 3:
                            if p - 1 == -1:
                                pass
                            else:
                                board_col[en][p - 1] = 3
                        if til == 4:
                            if en + 1 == 5 or p + 1 == 5:
                                pass
                            else:
                                board_col[en + 1][p + 1] = 3  # 오른쪽 위 대각선
                        if til == 5:
                            if en - 1 == -1 or p - 1 == -1:
                                pass
                            else:
                                board_col[en - 1][p - 1] = 3  # 왼쪽 아래 대각선
                        if til == 6:
                            if p + 1 == 5 or en - 1 == -1:
                                pass
                            else:
                                board_col[en - 1][p + 1] = 3  # 오른쪽 아래 대각선
                        if til == 7:
                            if p - 1 == -1 or en + 1 == 5:
                                pass
                            else:
                                board_col[en + 1][p - 1] = 3  # 왼쪽 아래 대각선
        if spell_use[0] == 1 and hand_sel[no][sel] == 1:
            for en in range(5):
                for num in range(5):
                    if board_col[en][num] == 3 and sk_1[0] == 1:  # 만약 보드의 색깔이 파란색이라면,
                        if event.type == MOUSEBUTTONDOWN:
                            move_x, move_y = board_pos[en][num]
                            if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                k = piece_pos[no].index(sp_piece[-1])
                                piece_pos[no][k] = move_x, move_y
                                card_clicked[0] = 0
                                hand_sel[no][sel] = 0
                                spell_use[0] = 2
                                if player == 0 and no == 0:
                                    p1_hand.remove({"원딜 스킬 1"})
                                elif player == 1:
                                    p2_hand.remove({"원딜 스킬 1"})
                                sk_1[0] = 0
                                if respond_situation[0] == 3:
                                    respond_situation[0] = 2

    def long_dealer_sk2(self, no, sel, o_player, player):  # o_player가 0이면 p1, 1이면 p2
        sk_pos = hand_pos[no][sel]
        sk_x, sk_y = sk_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if sk_x < mouse_x < sk_x + 282 and sk_y < mouse_y < sk_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
        if hand_sel[no][sel] == 1:
            if card_clicked[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] == piece_pos[no][0]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece[player].append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
        if hand_sel[no][sel] == 1 and card_clicked[0] == 1 and spell_use[0] == 1:
            for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                if sp_piece[player][-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면, 영어열의 몇번째에 있는지 상수로 바꾸고 그것을 통해서 그 칸을 파란색으로 바꾼다.
                    p = board_pos[en].index(sp_piece[player][-1])
                    for til in range(4):
                        if til == 0:
                            if en + 1 == 5:
                                pass
                            else:
                                for num in range(4):
                                    if board_pos[num + 1][p] in piece_pos[o_player]:
                                        board_col[num + 1][p] = 4
                        if til == 1:
                            if en - 1 == -1:
                                pass
                            else:
                                for num in range(5):
                                    if board_pos[num - 1][p] in piece_pos[o_player]:
                                        board_col[num - 1][p] = 4
                        if til == 2:
                            if p + 1 == 5:
                                pass
                            else:
                                for num in range(4):
                                    if board_pos[en][num + 1] in piece_pos[o_player]:
                                        board_col[en][num + 1] = 4
                        if til == 3:
                            if p - 1 == -1:
                                pass
                            else:
                                for num in range(5):
                                    if board_pos[en][num - 1] in piece_pos[o_player]:
                                        board_col[en][num - 1] = 4
        if spell_use[0] == 1 and hand_sel[no][sel] == 1:
            for en in range(5):
                for num in range(5):
                    if board_col[en][num] == 4:  # 만약 보드의 색깔이 파란색이라면,
                        if event.type == MOUSEBUTTONDOWN:
                            move_x, move_y = board_pos[en][num]  # 공격하려는 적 기물의 좌표
                            if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                now_attack.append(board_pos[en][num])
                                if player1_turn == 1:
                                    attackin_piece_pos.append(p1_piece_pos[0])
                                if player2_turn == 1:
                                    attackin_piece_pos.append(p2_piece_pos[0])
                                card_clicked[0] = 0
                                hand_sel[no][sel] = 0
                                spell_use[0] = 2
                                respond_situation[0] = 1
        if respond_situation[0] == 2 and 1 not in p1_piece_attack and 1 not in p2_piece_attack:
            if now_attack[-1] == piece_pos[o_player][0]:
                piece_pos[o_player][0] = (1280, 720)
            if now_attack[-1] == piece_pos[o_player][1]:
                piece_pos[o_player][1] = (1280, 720)
                dead_list.append(piece_pos[o_player][1])
                dead_list2.append(1)
            if now_attack[-1] == piece_pos[o_player][2]:
                piece_pos[o_player][2] = (1280, 720)
                dead_list.append(piece_pos[o_player][2])
                dead_list2.append(2)
            respond_situation[0] = 0
            card_clicked[0] = 0
            hand_sel[no][sel] = 0
            spell_use[0] = 2
            skill_respond[0] = 0
            if player == 0:
                p1_hand.remove({"원딜 스킬 2"})
            elif player == 1:
                p2_hand.remove({"원딜 스킬 2"})

    def holly_knight_sk1(self, no, sel, o_player, player):
        sk_pos = hand_pos[no][sel]
        sk_x, sk_y = sk_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if sk_x < mouse_x < sk_x + 282 and sk_y < mouse_y < sk_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
        if hand_sel[no][sel] == 1:
            if card_clicked[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] == piece_pos[no][0]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
        if hand_sel[no][sel] == 1 and card_clicked[0] == 1 and spell_use[0] == 1:
            for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                if sp_piece[-1] in board_pos[
                    en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면, 영어열의 몇번째에 있는지 상수로 바꾸고 그것을 통해서 그 칸을 파란색으로 바꾼다.
                    p = board_pos[en].index(sp_piece[-1])
                    for til in range(4):
                        if til == 0:
                            for i in range(3):
                                if (en + i) < 5:
                                    if board_pos[en + i][p] in piece_pos[o_player]:
                                        board_col[en + i][p] = 4
                        if til == 1:
                            for i in range(3):
                                if (en - i) > -1:
                                    if board_pos[en - i][p] in piece_pos[o_player]:
                                        board_col[en - i][p] = 4
                        if til == 2:
                            for i in range(3):
                                if (p + i) < 5:
                                    if board_pos[en][p + i] in piece_pos[o_player]:
                                        board_col[en][p + i] = 4
                        if til == 3:
                            for i in range(3):
                                if (p - i) > -1:
                                    if board_pos[en][p - i] in piece_pos[o_player]:
                                        board_col[en][p - i] = 4
        if spell_use[0] == 1 and hand_sel[no][sel] == 1:
            count = 0
            for en in range(5):
                for num in range(5):
                    if board_col[en][num] == 4:  # 만약 보드의 색깔이 파란색이라면,
                        if event.type == MOUSEBUTTONDOWN:
                            move_x, move_y = board_pos[en][num]  # 공격하려는 적 기물의 좌표
                            if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                now_attack.append(board_pos[en][num])
                                if player1_turn == 1:
                                    attackin_piece_pos.append(p1_piece_pos[0])
                                if player2_turn == 1:
                                    attackin_piece_pos.append(p2_piece_pos[0])
                                respond_situation[0] = 1
                                skill_respond[0] = 1
                                card_clicked[0] = 0
                                spell_use[0] = 2
                                hand_sel[no][sel] = 0
                    if board_col[en][num] != 4:
                        count += 1
                        if count == 25:
                            respond_situation[0] = 0
                            card_clicked[0] = 0
                            hand_sel[no][sel] = 0
                            spell_use[0] = 2
        if respond_situation[0] == 2 and 1 not in p1_piece_attack and 1 not in p2_piece_attack:
            if now_attack[-1] == piece_pos[o_player][0]:
                piece_pos[o_player][0] = (1280, 720)
            if now_attack[-1] == piece_pos[o_player][1]:
                piece_pos[o_player][1] = (1280, 720)
                dead_list.append(piece_pos[o_player][1])
                dead_list2.append(1)
            if now_attack[-1] == piece_pos[o_player][2]:
                piece_pos[o_player][2] = (1280, 720)
                dead_list.append(piece_pos[o_player][2])
                dead_list2.append(2)
            # respond_situation[0] = 0
            card_clicked[0] = 0
            hand_sel[no][sel] = 0
            spell_use[0] = 2
            skill_respond[0] = 0
            if player == 0:
                p1_hand.remove({"성기사 스킬 1"})
            elif player == 1:
                p2_hand.remove({"성기사 스킬 1"})

    def holly_knight_sk2(self, no, sel, player):
        spell_pos = hand_pos[no][sel]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
                    sk_1[0] = 1
        if hand_sel[no][sel] == 1:
            if card_clicked[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] == piece_pos[no][0]:
                            board_col[en][num] = 1
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    spell_use[0] = 1
                                    revive[0] = 1
        if hand_sel[no][sel] == 1 and spell_use[0] == 1:
            if sk_1[0] == 1:
                if revive[0] == 1:
                    if dead_list[-1] == (1280, 720) and player == 0:
                        for en in range(2):
                            for num in range(3):
                                if piece_pos[en][num] in p1_dead_pos:
                                    p1_dead_pos.remove(piece_pos[en][num])
                                    random.shuffle(p1_dead_pos)
                                    dead_list[-1] = p1_dead_pos[0]
                        if piece_pos[player][1] == (1280, 720) and piece_pos[player][2] != (1280, 720):  # 나이트가 죽었을때
                            piece_pos[player][1] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                        elif piece_pos[player][2] == (1280, 720) and piece_pos[player][1] != (1280, 720):  # 폰이 죽었을때
                            piece_pos[player][2] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                        elif piece_pos[player][2] == (1280, 720) and piece_pos[player][1] == (1280, 720):
                            piece_pos[player][dead_list2[-1]] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                    elif dead_list[-1] == (1280, 720) and player == 1:
                        for en in range(2):
                            for num in range(3):
                                if piece_pos[en][num] in p2_dead_pos:
                                    p2_dead_pos.remove(piece_pos[en][num])
                                    random.shuffle(p2_dead_pos)
                                    dead_list[-1] = p2_dead_pos[0]
                        if piece_pos[player][1] == (1280, 720) and piece_pos[player][2] != (1280, 720):
                            piece_pos[player][1] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                        if piece_pos[player][2] == (1280, 720) and piece_pos[player][1] != (1280, 720):  # 폰이 죽었을때
                            piece_pos[player][2] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                        elif piece_pos[player][2] == (1280, 720) and piece_pos[player][1] == (1280, 720):
                            piece_pos[player][dead_list2[-1]] = dead_list[-1]
                            dead_list.remove(dead_list[-1])
                    card_clicked[0] = 0
                    hand_sel[no][sel] = 0
                    spell_use[0] = 2
                    sk_1[0] = 0
                    revive[0] = 0
                    if player == 0:
                        p1_hand.remove({"성기사 스킬 2"})
                    if player == 1:
                        p2_hand.remove({"성기사 스킬 2"})

    def holly_knight_sk3(self, no, sel, player):
        spell_pos = hand_pos[no][sel]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x <= mouse_x <= spell_x + 282 and spell_y <= mouse_y <= spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
                    sk_1[0] = 1
        if hand_sel[no][sel] == 1 and sk_1[0] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if hand_sel[no][sel] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                if respond_situation[0] == 3:
                    for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                        if now_attack[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                            now_attack.append(attackin_piece_pos[-1])
                            card_clicked[0] = 0
                            hand_sel[no][sel] = 0
                            spell_use[0] = 2
                            sk_1[0] = 0
                            if player == 0:
                                p1_hand.remove({"성기사 스킬 3"})
                            elif player == 1:
                                p2_hand.remove({"성기사 스킬 3"})
                            respond_situation[0] = 2
                            break # 대응 ㅇ

    def magician_sk1(self, no, sel, player):  # 아군 스킬 개수 늘림
        spell_pos = hand_pos[no][sel]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
                    sk_1[0] = 1
        if hand_sel[no][sel] == 1:
            if card_clicked[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] == piece_pos[no][1]:
                            board_col[en][num] = 1
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    spell_use[0] = 1
                                    magic_use[0] = 1
        if spell_use[0] == 1 and hand_sel[no][sel] == 1:
            if sk_1[0] == 1:
                if magic_use[0] == 1:
                    card_clicked[0] = 0
                    hand_sel[no][sel] = 0
                    spell_use[0] = 2
                    sk_1[0] = 0
                    magic_use[0] = 0
                    if player == 0:
                        if use_king_p1[0] == 1:
                            p1_hand.append({"원딜 스킬 1"})
                        if use_king_p1[1] == 1:
                            p1_hand.append({"성기사 스킬 1"})
                            p1_hand.append({"성기사 스킬 2"})
                        p1_hand.remove({"주술사 스킬 1"})
                    if player == 1:
                        if use_king_p2[0] == 1:
                            p2_hand.append({"원딜 스킬 1"})
                        if use_king_p2[1] == 1:
                            p2_hand.append({"성기사 스킬 1"})
                            p2_hand.append({"성기사 스킬 2"})
                        p2_hand.remove({"주술사 스킬 1"})

    def tanker_sk1(self, no, sel, player):
        spell_pos = hand_pos[no][sel]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x <= mouse_x <= spell_x + 282 and spell_y <= mouse_y <= spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[no][sel] = 1
                    sk_1[0] = 1
        if hand_sel[no][sel] == 1 and sk_1[0] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                if respond_situation[0] == 3:
                    for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                        if now_attack[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                            now_attack.append(attackin_piece_pos[-1])
                            card_clicked[0] = 0
                            hand_sel[no][sel] = 0
                            spell_use[0] = 2
                            sk_1[0] = 0
                            if player == 0:
                                p1_hand.remove({"탱커 스킬 1"})
                            elif player == 1:
                                p2_hand.remove({"탱커 스킬 1"})
                            respond_situation[0] = 2
                            break # 대응 ㅇ

class Spell():

    def move(self, no, who):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:   #아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x <= mouse_x <= spell_x + 282 and spell_y <= mouse_y <= spell_y + 29.75:  #카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  #현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1: #만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  #만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  #스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  #만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x,piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1 and hand_sel[who][no] == 1:  #주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                        p = board_pos[en].index(sp_piece[-1])
                        for til in range(8):
                            if til == 0:
                                if en + 1 == 5:
                                    pass
                                else:
                                    board_col[en + 1][p] = 3
                            if til == 1:
                                if en - 1 == -1:
                                    pass
                                else:
                                    board_col[en - 1][p] = 3
                            if til == 2:
                                if p + 1 == 5:
                                    pass
                                else:
                                    board_col[en][p + 1] = 3
                            if til == 3:
                                if p - 1 == -1:
                                    pass
                                else:
                                    board_col[en][p - 1] = 3
                            if til == 4:
                                if en + 1 == 5 or p + 1 == 5:
                                    pass
                                else:
                                    board_col[en + 1][p + 1] = 3  # 오른쪽 위 대각선
                            if til == 5:
                                if en - 1 == -1 or p - 1 == -1:
                                    pass
                                else:
                                    board_col[en - 1][p - 1] = 3  # 왼쪽 아래 대각선
                            if til == 6:
                                if p + 1 == 5 or en - 1 == -1:
                                    pass
                                else:
                                    board_col[en - 1][p + 1] = 3  # 오른쪽 아래 대각선
                            if til == 7:
                                if p - 1 == -1 or en + 1 == 5:
                                    pass
                                else:
                                        board_col[en + 1][p - 1] = 3  # 왼쪽 아래 대각선
            if spell_use[0] == 1:
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] ==  3:  #만약 보드의 색깔이 파란색이라면,
                            if event.type == MOUSEBUTTONDOWN:
                                move_x , move_y = board_pos[en][num]
                                if move_x <= mouse_x <= move_x +113 and move_y <= mouse_y <= move_y +113:
                                    k = piece_pos[who].index(sp_piece[-1])
                                    piece_pos[who][k] = move_x, move_y
                                    card_clicked[0] = 0
                                    hand_sel[who][no] = 0
                                    spell_use[0] = 2
                                    if who == 0:
                                        p1_hand.remove({"한칸 이동":1})
                                    elif who == 1:
                                        p2_hand.remove({"한칸 이동":1})
                                    if respond_situation[0] == 3:
                                        respond_situation[0] = 2

    def b2_card(self, no, who, o_player):  #no는 카드의 위치
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    for num in range(5):
                        if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                            board_col[1][1] = 3
                        # if piece_pos[o_player][0] in board_pos[en]:
                        #     board_col[1][1] = 4
            if spell_use[0] == 1 and hand_sel[who][no] == 1:
                if board_pos[1][1] in p1_piece_pos and board_pos[1][1] in p2_piece_pos:
                    respond_situation[0] = 0
                    card_clicked[0] = 0
                    hand_sel[no][who] = 0
                    spell_use[0] = 2
                else:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 3:  # 만약 보드의 색깔이 파란색이라면,
                                if event.type == MOUSEBUTTONDOWN:
                                    move_x, move_y = board_pos[en][num]
                                    if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                        k = piece_pos[who].index(sp_piece[-1])
                                        piece_pos[who][k] = move_x, move_y
                                        card_clicked[0] = 0
                                        hand_sel[who][no] = 0
                                        spell_use[0] = 2
                                        if who == 0:
                                            p1_hand.remove({"b2": 4})
                                        elif who == 1:
                                            p2_hand.remove({"b2": 4})
                                        if respond_situation[0] == 3:
                                            respond_situation[0] = 2

    def b4_card(self, no, who, o_player):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                        p = board_pos[en].index(sp_piece[-1])
                        board_col[3][1] = 3
            if spell_use[0] == 1:
                if board_pos[3][1] in p1_piece_pos and board_pos[3][1] in p2_piece_pos:
                    respond_situation[0] = 0
                    card_clicked[0] = 0
                    hand_sel[no][who] = 0
                    spell_use[0] = 2
                else:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 3:  # 만약 보드의 색깔이 파란색이라면,
                                if event.type == MOUSEBUTTONDOWN:
                                    move_x, move_y = board_pos[en][num]
                                    if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                        k = piece_pos[who].index(sp_piece[-1])
                                        piece_pos[who][k] = move_x, move_y
                                        hand_sel[who][no] = 0
                                        card_clicked[0] = 0
                                        spell_use[0] = 2
                                        if who == 0:
                                            p1_hand.remove({"b4": 5})
                                        elif who == 1:
                                            p2_hand.remove({"b4": 5})
                                        if respond_situation[0] == 3:
                                            respond_situation[0] = 2

    def c3_card(self, no, who, o_player):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no]:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                        p = board_pos[en].index(sp_piece[-1])
                        board_col[2][2] = 3
            if spell_use[0] == 1:
                if board_pos[2][2] in p1_piece_pos and board_pos[2][2] in p2_piece_pos:
                    respond_situation[0] = 0
                    card_clicked[0] = 0
                    hand_sel[no][who] = 0
                    spell_use[0] = 2
                else:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 3:  # 만약 보드의 색깔이 파란색이라면,
                                if event.type == MOUSEBUTTONDOWN:
                                    move_x, move_y = board_pos[en][num]
                                    if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                        k = piece_pos[who].index(sp_piece[-1])
                                        piece_pos[who][k] = move_x, move_y
                                        card_clicked[0] = 0
                                        hand_sel[who][no] = 0
                                        spell_use[0] = 2
                                        if who == 0:
                                            p1_hand.remove({"c3": 6})
                                        elif who == 1:
                                            p2_hand.remove({"c3": 6})
                                        if respond_situation[0] == 3:
                                            respond_situation[0] = 2

    def d2_card(self, no, who, o_player):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                        p = board_pos[en].index(sp_piece[-1])
                        board_col[1][3] = 3
            if spell_use[0] == 1:
                if board_pos[1][3] in p1_piece_pos and board_pos[1][3] in p2_piece_pos:
                    respond_situation[0] = 0
                    card_clicked[0] = 0
                    hand_sel[no][who] = 0
                    spell_use[0] = 2
                else:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 3:  # 만약 보드의 색깔이 파란색이라면,
                                if event.type == MOUSEBUTTONDOWN:
                                    move_x, move_y = board_pos[en][num]
                                    if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                        k = piece_pos[who].index(sp_piece[-1])
                                        piece_pos[who][k] = move_x, move_y
                                        hand_sel[who][no] = 0
                                        card_clicked[0] = 0
                                        spell_use[0] = 2
                                        if who == 0:
                                            p1_hand.remove({"d2": 7})
                                        elif who == 1:
                                            p2_hand.remove({"d2": 7})
                                        if respond_situation[0] == 3:
                                            respond_situation[0] = 2

    def d4_card(self, no, who, o_player):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x < mouse_x < spell_x + 282 and spell_y < mouse_y < spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                for en in range(5):
                    for num in range(5):
                        if board_pos[en][num] in piece_pos[who]:  # 만약 검색한 보드의 포지션이 현재 카드 소유주의 기물 포지션과 겹친다면
                            board_col[en][num] = 1  # 스킬을 적용가능한 기물의 바닥을 빨간색으로 변형시켜준다.
                for en in range(5):
                    for num in range(5):
                        if board_col[en][num] == 1:
                            piece_x, piece_y = board_pos[en][num]
                            if piece_x <= mouse_x <= piece_x + 113 and piece_y <= mouse_y <= piece_y + 113:  # 만약 마우스가 스킬 적용한 기물의 위치를 눌렀다면
                                if event.type == MOUSEBUTTONDOWN:
                                    sp_piece.append((piece_x, piece_y))
                                    spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                    if sp_piece[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                        p = board_pos[en].index(sp_piece[-1])
                        board_col[3][3] = 3
            if spell_use[0] == 1:
                if board_pos[3][3] in p1_piece_pos and board_pos[3][3] in p2_piece_pos:
                    respond_situation[0] = 0
                    card_clicked[0] = 0
                    hand_sel[no][who] = 0
                    spell_use[0] = 2
                else:
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 3:  # 만약 보드의 색깔이 파란색이라면,
                                if event.type == MOUSEBUTTONDOWN:
                                    move_x, move_y = board_pos[en][num]
                                    if move_x <= mouse_x <= move_x + 113 and move_y <= mouse_y <= move_y + 113:
                                        k = piece_pos[who].index(sp_piece[-1])
                                        piece_pos[who][k] = move_x, move_y
                                        card_clicked[0] = 0
                                        hand_sel[who][no] = 0
                                        spell_use[0] = 2
                                        if who == 0:
                                            p1_hand.remove({"d4": 8})
                                        elif who == 1:
                                            p2_hand.remove({"d4": 8})
                                        if respond_situation[0] == 3:
                                            respond_situation[0] = 2

    def move_plus(self, no, who):  #no는 카드의 위치
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x <= mouse_x <= spell_x + 282 and spell_y <= mouse_y <= spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                if who == 0:
                    p1_move[0] += 1
                elif who == 1:
                    p2_move[0] += 1
                card_clicked[0] = 0
                hand_sel[who][no] = 0
                spell_use[0] = 2
                if who == 0:
                    p1_hand.remove({"기동력 +1":3})
                elif who == 1:
                    p2_hand.remove({"기동력 +1":3})

    def defense(self, no, who):
        spell_pos = hand_pos[who][no]
        spell_x, spell_y = spell_pos
        if card_clicked[0] == 0:  # 아직 아무런 카드가 눌리지 않은 상태일때
            if spell_x <= mouse_x <= spell_x + 282 and spell_y <= mouse_y <= spell_y + 29.75:  # 카드위치를 클릭했다면
                if event.type == MOUSEBUTTONDOWN:
                    card_clicked[0] = 1  # 현재 카드가 눌렸음을 확인 한다.
                    hand_sel[who][no] = 1
        if hand_sel[who][no] == 1:
            if card_clicked[0] == 1:  # 만약 카드가 현재 눌린 상태라면,
                spell_use[0] = 1  # 주문을 발동 상태로 바꾼다
            if card_clicked[0] == 1 and spell_use[0] == 1:  # 주문이 클릭된 상태이고 주문의 효과가 현재 발동상태가 되었다면
                if respond_situation[0] == 3:
                    for en in range(5):  # 보드 포지션 내에서 폰의 위치를 검색한다.
                        if now_attack[-1] in board_pos[en]:  # 만약 눌린 폰의 위치가 보드 영어열 안에 위치에 있다면,
                            now_attack.append(attackin_piece_pos[-1])
                            card_clicked[0] = 0
                            hand_sel[who][no] = 0
                            spell_use[0] = 2
                            if who == 0:
                                p1_hand.remove({"방어":2})
                            elif who == 1:
                                p2_hand.remove({"방어":2})
                            respond_situation[0] = 2
                            break
                            # 중간에 갑자기 대응 안뜸 ???? 한번 안뜨고 다시 뜸c

def respond():
    if respond_situation[0] == 1:
        if event.type == MOUSEBUTTONDOWN:
            if 555 <= mouse_x <= 648 and 350 <= mouse_y <= 380:
                respond_situation[0] = 3
            if 655 <= mouse_x <= 748 and 350 <= mouse_y <= 380:
                respond_situation[0] = 2


start_button = Sprite_Button("start.jpg", 'pressed_start.jpg', (1000, 500))
exit_button = Sprite_Button("exit.jpg", "pressed_exit.jpg", (700, 500))
end_button1 = Sprite_Button("end.png", "end_push.png", (1000, 500))
end_button2 = Sprite_Button("end.png", "end_push.png", (1000, 500))

start_screen = pygame.image.load("main.jpg")
select_screen = pygame.image.load("team_image.jpg")
play_screen = pygame.image.load("chess_image.png")

card_b_k1 = pygame.image.load("k1_large.jpg")
card_b_k2 = pygame.image.load("k2_large.jpg")
card_b_n1 = pygame.image.load("n1_large.jpg")
card_b_n2 = pygame.image.load("n2_large.jpg")
card_s_k1 = Sprite_Button("k1_small.jpg", "pressed_k1.jpg", (1, 500))
card_s_k2 = Sprite_Button("k2_small.jpg", "pressed_k2.jpg", (120, 500))
card_s_n1 = Sprite_Button("n1_small.jpg", "pressed_n1.jpg", (240, 500))
card_s_n2 = Sprite_Button("n2_small.jpg", "pressed_n2.jpg", (360, 500))
card_big3 = pygame.image.load("pawn.jpg")

respond_box = pygame.image.load("respond_box.png")


starting = True
selecting_p1= False
selecting_p2 = False
playing = False
winning = False
mouse_x = 0
mouse_y = 0
mouse_position = []
whole_game = True
card_select= [0,0]
card_n = [0]
card_k = [0]


a1, a2, a3, a4, a5 = tile_spr("tile.png", (362, 528)), tile_spr("tile.png", (476, 528)), tile_spr("tile.png", (590, 528)), tile_spr("tile.png", (704, 528)), tile_spr("tile.png", (818, 528))
b1, b2, b3, b4, b5 = tile_spr("tile.png", (362, 414)), tile_spr("tile.png", (476, 414)), tile_spr("tile.png", (590, 414)), tile_spr("tile.png", (704, 414)), tile_spr("tile.png", (818, 414))
c1, c2, c3, c4, c5 = tile_spr("tile.png", (362, 300)), tile_spr("tile.png", (476, 300)), tile_spr("tile.png", (590, 300)), tile_spr("tile.png", (704, 300)), tile_spr("tile.png", (818, 300))
d1, d2, d3, d4, d5 = tile_spr("tile.png", (362, 186)), tile_spr("tile.png", (476, 186)), tile_spr("tile.png", (590, 186)), tile_spr("tile.png", (704, 186)), tile_spr("tile.png", (818, 186))
e1, e2, e3, e4, e5 = tile_spr("tile.png", (362, 72)), tile_spr("tile.png", (476, 72)), tile_spr("tile.png", (590, 72)), tile_spr("tile.png", (704, 72)), tile_spr("tile.png", (818, 72))

board = [[a1.image, a2.image, a3.image, a4.image, a5.image],
         [b1.image, b2.image, b3.image, b4.image, b5.image],
         [c1.image, c2.image, c3.image, c4.image, c5.image],
         [d1.image, d2.image, d3.image, d4.image, d5.image],
         [e1.image, e2.image, e3.image, e4.image, e5.image]]

board_pos = [[a1.pos, a2.pos, a3.pos, a4.pos, a5.pos],
             [b1.pos, b2.pos, b3.pos, b4.pos, b5.pos],
             [c1.pos, c2.pos, c3.pos, c4.pos, c5.pos],
             [d1.pos, d2.pos, d3.pos, d4.pos, d5.pos],
             [e1.pos, e2.pos, e3.pos, e4.pos, e5.pos]]

board_col = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

# board 리스트 의 [][] 앞부분은 영어 열 뒷부분은 숫자열

# 0은 일반 색상 1은 빨간색 2는 노란색 3은 파란색 4는 잔디색
king1_p1 = piece("king_w.png")
king2_p1 = piece("king_b.png")
knight1_p1 = piece("knight_w.png")
knight2_p1 = piece("knight_b.png")
pawn_p1 = piece("pawn_w.png")


king1_p2 = piece("p2_king1.png")
king2_p2 = piece("p2_king2.png")
knight1_p2 = piece("p2_knight1.png")
knight2_p2 = piece('p2_knight2.png')
pawn_p2 = piece("p2_pawn2.png")




allocated = 0
pieces = 0
# 이 폰의 리스트는 앞으로 기물들의 정보를 저장하는 리스트로써 사용될 것이다. 모든 리스트의 인덱스 0은 킹 1은 나이트 2는 폰으로서 사용될 것이다. 이 점 참고
p1_king = []  # 2번에서 고른 카드의 정보들 킹의 이미지를 순간적으로 받아놈
p1_king_pos = []  # 위치까지
p1_knight = []
p1_knight_pos =[]
p1_piece_list = []  # 2번 함수에서 고른 킹과 나이트의 이미지를 받아서 저장하는 리스트
p1_piece_pos = []   # 2번 함수에서 고른 킹과 나이트의 배치한 포지션을 저장하는 리스트
p1_piece_attack = [0, 0, 0]  # 이게 1이 되면 attack 실행
p1_move = [0]
player1_turn = 0  # 0은 턴 대기중 1은 진행중일 경우 2는 턴 종료
use_king_p1 = [0, 0]  # 사용하고자 하는 킹의 숫자를 1로 변경한다. 나이트도 마찬가지의 원리
use_knight_p1 = [0, 0]
p1_allocate_pos = [[a1.pos, a2.pos, a3.pos, a4.pos, a5.pos],
                   [b1.pos, b2.pos, b3.pos, b4.pos, b5.pos]]
p1_sp_piece = []
p1_dead_pos = [a1.pos, a2.pos, a3.pos, a4.pos, a5.pos, b1.pos, b2.pos, b3.pos, b4.pos, b5.pos]
# 여기가지 플레이어의 요소

p2_king = []  # 2 번에서 고른 카드의 정보들 킹의 이미지를 순간적으로 받아놈
p2_king_pos = []  # 위치까지
p2_knight = []
p2_knight_pos = []
p2_piece_list = []  # 2번 함수에서 고른 킹과 나이트의 이미지를 받아서 저장하는 리스트
p2_piece_pos = []   # 2번 함수에서 고른 킹과 나이트의 배치한 포지션을 저장하는 리스트
p2_piece_attack = [0, 0, 0]  # 이게 1이 되면 attack 실행
p2_move = [0]
player2_turn = 2  # 0은 턴 대기중 1은 진행중일 경우 2는 턴 종료
use_king_p2 = [0, 0]  # 사용하고자 하는 킹의 숫자를 1로 변경한다. 나이트도 마찬가지의 원리
use_knight_p2 = [0, 0]
p2_allocate_pos = [[d1.pos, d2.pos, d3.pos, d4.pos, d5.pos],
                   [e1.pos, e2.pos, e3.pos, e4.pos, e5.pos]]
p2_sp_piece = []
p2_dead_pos = [d1.pos, d2.pos, d3.pos, d4.pos, d5.pos, e1.pos, e2.pos, e3.pos, e4.pos, e5.pos]
# p2요소



piece_list = [p1_piece_list, p2_piece_list]
piece_pos = [p1_piece_pos, p2_piece_pos]
piece_attack = [p1_piece_attack, p2_piece_attack]
move = [p1_move, p2_move]
respond_situation = [0]
piece_clicked = [0, 0, 0]  #기물이 클릭되었는가? 1이면 클릭된상태
now_attack = []
attackin_piece_pos = []
move_button = Sprite_Button("move_attack.png", "pressed_move_attack.png", (1280, 720))
move_b = [move_button.position, 0]
allocate_pos = [p1_allocate_pos, p2_allocate_pos]
allocate_p = 0
responding = False
turn = [player1_turn, player2_turn]
# 공통 요소

dead_list2 = []
dead_list = []
revive = [0]
magic_use = [0]
skill_attack = []
skill_respond = [0]
sk_card_clicked = [0]
spell_act = [0, 0, 0]
spell_clicked = [0, 0, 0]
sp_piece = [p1_sp_piece, p2_sp_piece]
card_clicked = [0]
spell_use = [0]
sk_1 = [0]

king_check = [0, 0]
knight_check = [0, 0]
card_check = [0, 1]

p1_hand_pos = [(2, 357.0), (2, 386.75), (2, 416.5), (2, 446.25), (2, 476.0), (2, 505.75), (2, 535.5), (2, 565.25), (2, 595.0), (2, 624.75), (2, 654.5), (2, 684.25)]
p1_hand_sel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

p2_hand_pos = [(996, 357.0), (996, 386.75), (996, 416.5), (996, 446.25), (996, 476.0), (996, 505.75), (996, 535.5), (996, 565.25), (996, 595.0), (996, 624.75), (996, 654.5), (996, 684.25)]
p2_hand_sel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

hand_pos = [p1_hand_pos, p2_hand_pos]
hand_sel = [p1_hand_sel, p2_hand_sel]

p1_deck = [{"한칸 이동": 1}]*5 + [{"b2": 4}] + [{"b4": 5}] + [{"c3": 6}] + [{"d2": 7}] + [{"d4": 8}] + [{"기동력 +1": 3}]*3 + [{"방어": 2}]*5
p2_deck = [{"한칸 이동": 1}]*5 + [{"b2": 4}] + [{"b4": 5}] + [{"c3": 6}] + [{"d2": 7}] + [{"d4": 8}] + [{"기동력 +1": 3}]*3 + [{"방어": 2}]*5


p1_hand = []
p2_hand = []


start_card = [0]

while whole_game:
    while starting:
        screen.fill(0)
        screen.blit(start_screen,(0,0))
        screen.blit(start_button.normal, start_button.position)
        pygame.display.flip()
        pygame.mouse.get_pos()
        pressed = []
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= 1000 and mouse_x <= 1200:
                if mouse_y <= 572 and mouse_y >= 500:
                    if event.type == MOUSEBUTTONDOWN:
                        start_button.update([start_button])
            if mouse_x >= 1000 and mouse_x <= 1200:
                if mouse_y <= 572 and mouse_y >= 500:
                    if event.type == MOUSEBUTTONUP:
                        screen.fill(0)
                        selecting_p1 = True
                        starting = False
            if event.type == MOUSEBUTTONUP:
                start_button.update([])
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    while selecting_p1:
        exit_button.position = (700,500)
        font = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 40)
        screen.blit(select_screen, (0, 0))
        pick = font.render("P1", True, (225, 0, 0))
        if card_select[0] + card_select[1] == 2:
            screen.blit(start_button.normal, start_button.position)
        if card_k[0] > 0 or card_n[0] > 0:
            if card_k[0] == 1:
                screen.blit(card_b_k1,(20,20))
                if card_n[0] == 1:
                    screen.blit(card_b_k1,(20,20))
                    screen.blit(card_b_n1,(370,20))
                elif card_n[0] == 2:
                    screen.blit(card_b_k1,(20,20))
                    screen.blit(card_b_n2,(370,20))
            elif card_k[0] == 2:
                screen.blit(card_b_k2,(20,20))
                if card_n[0] == 1:
                    screen.blit(card_b_k2,(20,20))
                    screen.blit(card_b_n1,(370,20))
                elif card_n[0] == 2:
                    screen.blit(card_b_k2,(20,20))
                    screen.blit(card_b_n2,(370,20))
            elif card_n[0] == 1:
                screen.blit(card_b_n1,(370,20))
                if card_k[0] == 1:
                    screen.blit(card_b_n1,(370,20))
                    screen.blit(card_b_n1,(20,20))
                elif card_k[0] == 2:
                    screen.blit(card_b_n1,(370,20))
                    screen.blit(card_b_n2,(20,20))
            elif card_n[0] == 2:
                screen.blit(card_b_n2,(370,20))
                if card_k[0] == 1:
                    screen.blit(card_b_n2,(370,20))
                    screen.blit(card_b_n1,(20,20))
                elif card_k[0] == 2:
                    screen.blit(card_b_n2,(370,20))
                    screen.blit(card_b_n2,(20,20))
        screen.blit(card_big3, (680,20))
        screen.blit(card_s_k1.normal, card_s_k1.position)
        screen.blit(card_s_k2.normal, card_s_k2.position)
        screen.blit(card_s_n1.normal, card_s_n1.position)
        screen.blit(card_s_n2.normal, card_s_n2.position)
        screen.blit(exit_button.normal, exit_button.position)
        screen.blit(pick, (580, 10))
        pygame.display.flip()
        pressed = []
        push1 = []
        push2 = []
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()  #250*375 100*150
            if 21<mouse_x<271 and 29<mouse_y<406:
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 0
                    card_k[0] = 0
                    card_s_k1.update([])
                    card_s_k2.update([])
            if 319<mouse_x<571 and 29<mouse_y<406:
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 0
                    card_n[0] = 0
                    card_s_n1.update([])
                    card_s_n2.update([])
            if 0<mouse_x<101 and 499<mouse_y<651: #킹1 누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 1
                    card_k[0] = 1
                    card_s_k2.update([card_s_k2])
                    card_s_k1.update([])
                    p1_king.append(king1_p1.image)
                    p1_king_pos.append(king1_p1.pos_p)
                    use_king_p1[0] = 1
                    use_king_p1[1] = 0
            if 119<mouse_x<221 and 499<mouse_y<651:#킹 2누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 1
                    card_k[0] = 2
                    card_s_k1.update([card_s_k1])
                    card_s_k2.update([])
                    p1_king.append(king2_p1.image)
                    p1_king_pos.append(king2_p1.pos_p)
                    use_king_p1[0] = 0
                    use_king_p1[1] = 1
            if 239<mouse_x<341 and 499<mouse_y<651: #나이트 1누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 1
                    card_n[0] = 1
                    card_s_n2.update([card_s_n2])
                    card_s_n1.update([])
                    p1_knight.append(knight1_p1.image)
                    p1_knight_pos.append(knight1_p1.pos_p)
                    use_knight_p1[0] = 1
                    use_knight_p1[1] = 0
            if 359<mouse_x<461 and 499<mouse_y<651: #나이트 2누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 1
                    card_n[0] = 2
                    card_s_n1.update([card_s_n1])
                    card_s_n2.update([])
                    p1_knight.append(knight2_p1.image)
                    p1_knight_pos.append(knight2_p1.pos_p)
                    use_knight_p1[0] = 0
                    use_knight_p1[1] = 1
            if 699<mouse_x<901 and 499<mouse_y<573:
                if event.type == MOUSEBUTTONDOWN:
                    exit_button.update([exit_button])
            if 699<mouse_x<901 and 499<mouse_y<573:
                if event.type == MOUSEBUTTONUP:
                    card_s_k1.update([])
                    card_s_k2.update([])
                    card_s_n1.update([])
                    card_s_n2.update([])
                    card_select[0] = 0
                    card_select[1] = 0
                    card_k[0] = 0
                    card_n[0] = 0
                    screen.fill(0)
                    starting = True
                    selecting_p1 = False
            if card_select[0] + card_select[1] == 2:
                if mouse_x >= 1000 and mouse_x <= 1200:
                    if mouse_y <= 572 and mouse_y >= 500:
                        if event.type == MOUSEBUTTONDOWN:
                            start_button.update([start_button])
                if mouse_x >= 1000 and mouse_x <= 1200:
                    if mouse_y <= 572 and mouse_y >= 500:
                        if event.type == MOUSEBUTTONUP:
                            screen.fill(0)
                            card_s_k1.update([])
                            card_s_k2.update([])
                            card_s_n1.update([])
                            card_s_n2.update([])
                            card_select[0] = 0
                            card_select[1] = 0
                            card_k[0] = 0
                            card_n[0] = 0
                            p1_piece_list.append(p1_king[-1])
                            p1_piece_list.append(p1_knight[-1])
                            p1_piece_list.append(pawn_p1.image)
                            p1_piece_pos.append(p1_king_pos[-1])
                            p1_piece_pos.append(p1_knight_pos[-1])
                            p1_piece_pos.append(pawn_p1.pos_p)
                            selecting_p2 = True
                            selecting_p1 = False
            if event.type == MOUSEBUTTONUP:
                start_button.update([])
                exit_button.update([])
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    while selecting_p2:
        exit_button.position = (700,500)
        font = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 40)
        screen.blit(select_screen, (0, 0))
        pick = font.render("P2" , True ,(225, 0, 0))
        if card_select[0] + card_select[1] == 2:
            screen.blit(start_button.normal, start_button.position)
        if card_k[0] > 0 or card_n[0] > 0:
            if card_k[0] == 1:
                screen.blit(card_b_k1,(20,20))
                if card_n[0] == 1:
                    screen.blit(card_b_k1,(20,20))
                    screen.blit(card_b_n1,(370,20))
                elif card_n[0] == 2:
                    screen.blit(card_b_k1,(20,20))
                    screen.blit(card_b_n2,(370,20))
            elif card_k[0] == 2:
                screen.blit(card_b_k2,(20,20))
                if card_n[0] == 1:
                    screen.blit(card_b_k2,(20,20))
                    screen.blit(card_b_n1,(370,20))
                elif card_n[0] == 2:
                    screen.blit(card_b_k2,(20,20))
                    screen.blit(card_b_n2,(370,20))
            elif card_n[0] == 1:
                screen.blit(card_b_n1,(370,20))
                if card_k[0] == 1:
                    screen.blit(card_b_n1,(370,20))
                    screen.blit(card_b_n1,(20,20))
                elif card_k[0] == 2:
                    screen.blit(card_b_n1,(370,20))
                    screen.blit(card_b_n2,(20,20))
            elif card_n[0] == 2:
                screen.blit(card_b_n2,(370,20))
                if card_k[0] == 1:
                    screen.blit(card_b_n2,(370,20))
                    screen.blit(card_b_n1,(20,20))
                elif card_k[0] == 2:
                    screen.blit(card_b_n2,(370,20))
                    screen.blit(card_b_n2,(20,20))
        screen.blit(card_big3, (680,20))
        screen.blit(card_s_k1.normal, card_s_k1.position)
        screen.blit(card_s_k2.normal, card_s_k2.position)
        screen.blit(card_s_n1.normal, card_s_n1.position)
        screen.blit(card_s_n2.normal, card_s_n2.position)
        screen.blit(exit_button.normal, exit_button.position)
        screen.blit(pick, (580, 10))
        pygame.display.flip()
        pressed = []
        push1 = []
        push2 = []
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos() #250*375 100*150
            if 21<mouse_x<271 and 29<mouse_y<406:
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 0
                    card_k[0] = 0
                    card_s_k1.update([])
                    card_s_k2.update([])
            if 319<mouse_x<571 and 29<mouse_y<406:
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 0
                    card_n[0] = 0
                    card_s_n1.update([])
                    card_s_n2.update([])
            if 0<mouse_x<101 and 499<mouse_y<651: #킹1 누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 1
                    card_k[0] = 1
                    card_s_k2.update([card_s_k2])
                    card_s_k1.update([])
                    p2_king.append(king1_p2.image)
                    p2_king_pos.append(king1_p2.pos_p)
                    use_king_p2[0] = 1
                    use_king_p2[1] = 0
            if 119<mouse_x<221 and 499<mouse_y<651:#킹 2누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[0] = 1
                    card_k[0] = 2
                    card_s_k1.update([card_s_k1])
                    card_s_k2.update([])
                    p2_king.append(king2_p2.image)
                    p2_king_pos.append(king2_p2.pos_p)
                    use_king_p2[0] = 0
                    use_king_p2[1] = 1
            if 239<mouse_x<341 and 499<mouse_y<651: #나이트 1누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 1
                    card_n[0] = 1
                    card_s_n2.update([card_s_n2])
                    card_s_n1.update([])
                    p2_knight.append(knight1_p2.image)
                    p2_knight_pos.append(knight1_p2.pos_p)
                    use_knight_p2[0] = 1
                    use_knight_p2[1] = 0
            if 359<mouse_x<461 and 499<mouse_y<651: #나이트 2누르는거
                if event.type == MOUSEBUTTONDOWN:
                    card_select[1] = 1
                    card_n[0] = 2
                    card_s_n1.update([card_s_n1])
                    card_s_n2.update([])
                    p2_knight.append(knight2_p2.image)
                    p2_knight_pos.append(knight2_p2.pos_p)
                    use_knight_p2[0] = 0
                    use_knight_p2[1] = 1
            if 699<mouse_x<901 and 499<mouse_y<573:
                if event.type == MOUSEBUTTONDOWN:
                    exit_button.update([exit_button])
            if 699<mouse_x<901 and 499<mouse_y<573:
                if event.type == MOUSEBUTTONUP:
                    card_s_k1.update([])
                    card_s_k2.update([])
                    card_s_n1.update([])
                    card_s_n2.update([])
                    card_select[0] = 0
                    card_select[1] = 0
                    card_k[0] = 0
                    card_n[0] = 0
                    screen.fill(0)
                    starting = True
                    selecting_p2 = False
            if card_select[0] + card_select[1] == 2:
                if mouse_x >= 1000 and mouse_x <= 1200:
                    if mouse_y <= 572 and mouse_y >= 500:
                        if event.type == MOUSEBUTTONDOWN:
                            start_button.update([start_button])
                if mouse_x >= 1000 and mouse_x <= 1200:
                    if mouse_y <= 572 and mouse_y >= 500:
                        if event.type == MOUSEBUTTONUP:
                            screen.fill(0)
                            p2_piece_list.append(p2_king[-1])
                            p2_piece_list.append(p2_knight[-1])
                            p2_piece_list.append(pawn_p2.image)
                            p2_piece_pos.append(p2_king_pos[-1])
                            p2_piece_pos.append(p2_knight_pos[-1])
                            p2_piece_pos.append(pawn_p2.pos_p)
                            playing = True
                            selecting_p2 = False
            if event.type == MOUSEBUTTONUP:
                start_button.update([])
                exit_button.update([])
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    while playing:
        if start_card[0] == 0:
            random.shuffle(p1_deck)
            p1_hand.append(p1_deck[0])
            p1_deck.remove(p1_deck[0])
            random.shuffle(p2_deck)
            p2_hand.append(p2_deck[0])
            p2_deck.remove(p2_deck[0])
            p2_hand.append(p2_deck[0])
            p2_deck.remove(p2_deck[0])
            start_card[0] = 1
        if king_check[0] == 0:
            if use_king_p1[0] == 1:
                p1_hand.append({"원딜 스킬 1"})
                p1_hand.append({"원딜 스킬 1"})
                p1_hand.append({"원딜 스킬 1"})
                p1_hand.append({"원딜 스킬 2"})
                p1_hand.append({"원딜 스킬 2"})
                king_check[0] = 1
            if use_king_p1[1] == 1:
                p1_hand.append({"성기사 스킬 1"})
                p1_hand.append({"성기사 스킬 2"})
                p1_hand.append({"성기사 스킬 3"})
                king_check[0] = 1
        if knight_check[0] == 0:
            if use_knight_p1[0] == 1:
                p1_hand.append({"주술사 스킬 1"})
                knight_check[0] = 1
            if use_knight_p1[1] == 1:
                p1_hand.append({"탱커 스킬 1"})
                knight_check[0] = 1
        if king_check[1] == 0:
            if use_king_p2[0] == 1:
                p2_hand.append({"원딜 스킬 1"})
                p2_hand.append({"원딜 스킬 1"})
                p2_hand.append({"원딜 스킬 1"})
                p2_hand.append({"원딜 스킬 2"})
                p2_hand.append({"원딜 스킬 2"})
                king_check[1] = 1
            if use_king_p2[1] == 1:
                p2_hand.append({"성기사 스킬 1"})
                p2_hand.append({"성기사 스킬 2"})
                p2_hand.append({"성기사 스킬 3"})
                king_check[1] = 1
        if knight_check[1] == 0:
            if use_knight_p2[0] == 1:
                p2_hand.append({"주술사 스킬 1"})
                knight_check[1] = 1
            elif use_knight_p2[1] == 1:
                p2_hand.append({"탱커 스킬 1"})
                knight_check[1] = 1
        msg = ["Player1 turn", "Player2 turn"]
        p1_movemnet = [0, 1, 2]
        ai_movement = [0, 1, 2]
        turn_font = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 32)
        font = pygame.font.Font('c:/Windows/Fonts/malgun.ttf',18)
        card = pygame.font.Font('c:/Windows/Fonts/malgun.ttf',22)
        mov = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 30)
        end_button1.position = (50, 25)
        end_button2.position = (1030, 25)
        screen.blit(play_screen, (0, 0))
        if not pieces == 4:
            turns = turn_font.render("allocating...", True, (225, 0, 0))
            screen.blit(turns, (570, 0))
        else:
            if player1_turn == 1:
                turns = turn_font.render(msg[0], True, (225, 0, 0))
                move_p1 = mov.render("기동력 : " + str(p1_move[0]), True, (255,0,0))
                screen.blit(move_p1, (80,110))
                screen.blit(turns, (560, 0))
            if player2_turn == 1:
                turns = turn_font.render(msg[1], True, (225, 0, 0))
                move_p2 = mov.render("기동력 : " + str(p2_move[0]), True, (255,0,0))
                screen.blit(move_p2, (1068,110))
                screen.blit(turns, (560, 0))
        if player1_turn == 1 and pieces == 4:
            if card_check[0] == 0:
                p1_hand.append(p1_deck[0])
                p1_deck.remove(p1_deck[0])
                card_check[0] = 1
                card_check[1] = 0
            screen.blit(end_button1.normal, end_button1.position)
        if player2_turn == 1 and pieces == 4:
            if card_check[1] == 0:
                p2_hand.append(p2_deck[0])
                p2_deck.remove(p2_deck[0])
                card_check[1] = 1
                card_check[0] = 0
            screen.blit(end_button2.normal, end_button2.position)
        if pieces == 4:
            king1_1 = p1_hand.count({"원딜 스킬 1"})
            king1_2 = p1_hand.count({"원딜 스킬 2"})
            king2_sk1 = p1_hand.count({"성기사 스킬 1"})
            king2_sk2 = p1_hand.count({"성기사 스킬 2"})
            king2_sk3 = p1_hand.count({"성기사 스킬 3"})
            knight1_sk1 = p1_hand.count({"주술사 스킬 1"})
            knight2_sk1 = p1_hand.count({"탱커 스킬 1"})
            moves = p1_hand.count({"한칸 이동":1})
            b2 = p1_hand.count({"b2":4})
            b4 = p1_hand.count({"b4":5})
            c3 = p1_hand.count({"c3":6})
            d2 = p1_hand.count({"d2":7})
            d4 = p1_hand.count({"d4":8})
            mp = p1_hand.count({"기동력 +1":3})
            de = p1_hand.count({"방어":2})
            resp_1 = p1_hand.count({"원딜 스킬 1"}) + p1_hand.count({"한칸 이동":1}) + p1_hand.count({"b2":4}) + p1_hand.count({"b4":5}) + p1_hand.count({"c3":6}) + p1_hand.count({"d2":7}) + p1_hand.count({"d4":8}) + p1_hand.count({"방어":2}) + p1_hand.count({"성기사 스킬 3"}) + p1_hand.count({"탱커 스킬 1"})
            if card_clicked[0] == 0:
                k1_s1 = card.render("king.1 skill.1  " + str(king1_1), True, (255, 0, 0))
                k1_s2 = card.render("king.1 skill.2  " + str(king1_2), True, (255, 0, 0))
                k2_s1 = card.render("king.2 skill.1  " + str(king2_sk1), True, (255, 0, 0))
                k2_s2 = card.render("king.2 skill.2  " + str(king2_sk2), True, (255, 0, 0))
                k2_s3 = card.render("king.2 skill.3  " + str(king2_sk3), True, (255, 0, 0))
                n1_s1 = card.render("knight.1 skill.1  " + str(knight1_sk1), True, (255, 0, 0))
                n2_s1 = card.render("knight.2 skill.1  " + str(knight2_sk1), True, (255, 0, 0))
                cards = card.render("card_move  " + str(moves), True, (255, 0, 0))
                card1 = card.render("b2_card  " + str(b2), True, (255, 0, 0))
                card2 = card.render("b4_card  " + str(b4), True, (255, 0, 0))
                card3 = card.render("c3_card  " + str(c3), True, (255, 0, 0))
                card4 = card.render("d2_card  " + str(d2), True, (255, 0, 0))
                card5 = card.render("d4_card  " + str(d4), True, (255, 0, 0))
                card6 = card.render("move_plus  " + str(mp), True, (255, 0, 0))
                card7 = card.render("defense  " + str(de), True, (255, 0, 0))
            if player1_turn == 1:
                if card_clicked[0] == 1:
                    if p1_hand_sel[0] == 1:
                        k1_s1 = card.render("king.1 skill.1  " + str(king1_1), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[1] == 1:
                        k1_s2 = card.render("king.1 skill.2  " + str(king1_2), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[0] == 1:
                        k2_s1 = card.render("king.2 skill.1  " + str(king2_sk1), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[1] == 1:
                        k2_s2 = card.render("king.2 skill.2  " + str(king2_sk2), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[2] == 1:
                        k2_s3 = card.render("king.2 skill.3  " + str(king2_sk3), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[3] == 1:
                        n1_s1 = card.render("knght.1 skill.1  " + str(knight1_sk1), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[3] == 1:
                        n2_s1 = card.render("knght.2 skill.1  " + str(knight2_sk1), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[4] == 1:
                        cards = card.render("card_move  " + str(moves), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[5] == 1:
                        card1 = card.render("b2_card  " + str(b2), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[6] == 1:
                        card2 = card.render("b4_card  " + str(b4), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[7] == 1:
                        card3 = card.render("c3_card  " + str(c3), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[8] == 1:
                        card4 = card.render("d2_card  " + str(d2), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[9] == 1:
                        card5 = card.render("d4_card  " + str(d4), True, (225, 0, 0), (255, 255, 255))
                    if p1_hand_sel[10] == 1:
                        card6 = card.render("move_plus  " + str(mp), True, (255, 0, 0), (255, 255, 255))
                    if p1_hand_sel[11] == 1:
                        card7 = card.render("defense  " + str(de), True, (255, 0, 0)  ,(255, 255, 255))
            if player2_turn == 1:
                if respond_situation[0] == 3:
                    k1_s1 = card.render("king.1 skill.1  " + str(king1_1), True, (255, 0, 0), (255, 255, 255))
                    k2_s3 = card.render("king.2 skill.3  " + str(king2_sk3), True, (255, 0, 0), (255, 255, 255))
                    n2_s1 = card.render("knght.2 skill.1  " + str(knight2_sk1), True, (255, 0, 0), (255, 255, 255))
                    cards = card.render("card_move  " + str(moves), True, (225, 0, 0), (255, 255, 255))
                    card1 = card.render("b2_card  " + str(b2), True, (225, 0, 0), (255, 255, 255))
                    card2 = card.render("b4_card  " + str(b4), True, (225, 0, 0), (255, 255, 255))
                    card3 = card.render("c3_card  " + str(c3), True, (225, 0, 0), (255, 255, 255))
                    card4 = card.render("d2_card  " + str(d2), True, (225, 0, 0), (255, 255, 255))
                    card5 = card.render("d4_card  " + str(d4), True, (225, 0, 0), (255, 255, 255))
                    card7 = card.render("defense  " + str(de), True, (255, 0, 0)  ,(255, 255, 255))
            if use_king_p1[0] == 1 and p1_piece_pos[0] != (1280,720):
                screen.blit(k1_s1, (10, 357.0))
                screen.blit(k1_s2, (10, 386.75))
            if use_king_p1[1] == 1 and p1_piece_pos[0] != (1280, 720):
                screen.blit(k2_s1, (10, 357))
                screen.blit(k2_s2, (10, 386.75))
                screen.blit(k2_s3, (10, 416.5))
            if use_knight_p1[0] == 1 and p1_piece_pos[1] != (1280, 720):
                screen.blit(n1_s1, (10, 446.25))
            if use_knight_p1[1] == 1 and p1_piece_pos[1] != (1280, 720):
                screen.blit(n2_s1, (10, 446.25))
            screen.blit(cards, (10, 476.0))
            screen.blit(card1, (10, 505.75))
            screen.blit(card2, (10, 535.5))
            screen.blit(card3, (10, 565.25))
            screen.blit(card4, (10, 595.0))
            screen.blit(card5, (10, 624.75))
            screen.blit(card6, (10, 654.5))
            screen.blit(card7, (10, 684.25))
            king1_1_2 = p2_hand.count({"원딜 스킬 1"})
            king1_2_2 = p2_hand.count({"원딜 스킬 2"})
            king2_sk1_p2 = p2_hand.count({"성기사 스킬 1"})
            king2_sk2_p2 = p2_hand.count({"성기사 스킬 2"})
            king2_sk3_p2 = p2_hand.count({"성기사 스킬 3"})
            knight1_sk1_p2 = p2_hand.count({"주술사 스킬 1"})
            knight2_sk1_p2 = p2_hand.count({"탱커 스킬 1"})
            moves_2 = p2_hand.count({"한칸 이동":1})
            b2_2 = p2_hand.count({"b2":4})
            b4_2 = p2_hand.count({"b4":5})
            c3_2 = p2_hand.count({"c3":6})
            d2_2 = p2_hand.count({"d2":7})
            d4_2 = p2_hand.count({"d4":8})
            mp_2 = p2_hand.count({"기동력 +1":3})
            de_2 = p2_hand.count({"방어":2})
            resp_2 = p2_hand.count({"원딜 스킬 1"}) + p2_hand.count({"한칸 이동":1}) + p2_hand.count({"b2":4}) + p2_hand.count({"b4":5}) + p2_hand.count({"c3":6}) + p2_hand.count({"d2":7}) + p2_hand.count({"d4":8}) + p2_hand.count({"방어":2}) + p2_hand.count({"성기사 스킬 3"}) + p2_hand.count({"탱커 스킬 1"})
            if card_clicked[0] == 0:
                k1_s1_2 = card.render("king.1 skill.1  " + str(king1_1_2), True, (255, 0, 0))
                k1_s2_2 = card.render("king.1 skill.2  " + str(king1_2_2), True, (255, 0, 0))
                k2_s1_2 = card.render("king.2 skill.1  " + str(king2_sk1_p2), True, (255, 0, 0))
                k2_s2_2 = card.render("king.2 skill.2  " + str(king2_sk2_p2), True, (255, 0, 0))
                k2_s3_2 = card.render("king.2 skill.3  " + str(king2_sk3_p2), True, (255, 0, 0))
                n1_s1_2 = card.render("knight.1 skill.1  " + str(knight1_sk1_p2), True, (255, 0, 0))
                n2_s1_2 = card.render("knight.2 skill.1  " + str(knight2_sk1_p2), True, (255, 0, 0))
                cards_2 = card.render("card_move  " + str(moves_2), True, (225, 0, 0))
                card1_2 = card.render("b2_card  " + str(b2_2), True, (225, 0, 0))
                card2_2 = card.render("b4_card  " + str(b4_2), True, (225, 0, 0))
                card3_2 = card.render("c3_card  " + str(c3_2), True, (225, 0, 0))
                card4_2 = card.render("d2_card  " + str(d2_2), True, (225, 0, 0))
                card5_2 = card.render("d4_card  " + str(d4_2), True, (225, 0, 0))
                card6_2 = card.render("move_plus  " + str(mp_2), True, (255, 0, 0))
                card7_2 = card.render("defense  " + str(de_2), True, (255, 0, 0))
            if player2_turn == 1:
                if card_clicked[0] == 1:
                    if p2_hand_sel[0] == 1:
                        k1_s1_2 = card.render("king.1 skill.1  " + str(king1_1_2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[1] == 1:
                        k1_s2_2 = card.render("king.1 skill.2  " + str(king1_2_2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[0] == 1:
                        k2_s1_2 = card.render("king.2 skill.1  " + str(king2_sk1_p2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[1] == 1:
                        k2_s2_2 = card.render("king.2 skill.2  " + str(king2_sk2_p2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[2] == 1:
                        k2_s3_2 = card.render("king.2 skill.3  " + str(king2_sk3_p2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[3] == 1:
                        n1_s1_2 = card.render("knght.1 skill.1  " + str(knight1_sk1_p2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[3] == 1:
                        n2_s1_2 = card.render("knght.2 skill.1  " + str(knight2_sk1_p2), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[4] == 1:
                        cards_2 = card.render("card_move  " + str(moves_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[5] == 1:
                        card1_2 = card.render("b2_card  " + str(b2_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[6] == 1:
                        card2_2 = card.render("b4_card  " + str(b4_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[7] == 1:
                        card3_2 = card.render("c3_card  " + str(c3_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[8] == 1:
                        card4_2 = card.render("d2_card  " + str(d2_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[9] == 1:
                        card5_2 = card.render("d4_card  " + str(d4_2), True, (225, 0, 0), (255, 255, 255))
                    if p2_hand_sel[10] == 1:
                        card6_2 = card.render("move_plus  " + str(mp), True, (255, 0, 0), (255, 255, 255))
                    if p2_hand_sel[11] == 1:
                        card7_2 = card.render("defense  " + str(de_2), True, (255, 0, 0)  ,(255, 255, 255))
            if player1_turn == 1 :
                if respond_situation[0] == 3:
                    k1_s1_2 = card.render("king.1 skill.1  " + str(king1_1_2), True, (255, 0, 0), (255, 255, 255))
                    k2_s3_2 = card.render("king.2 skill.3  " + str(king2_sk3_p2), True, (255, 0, 0), (255, 255, 255))
                    n2_s1_2 = card.render("knght.2 skill.1  " + str(knight2_sk1_p2), True, (255, 0, 0), (255, 255, 255))
                    cards_2 = card.render("card_move  " + str(moves_2), True, (225, 0, 0), (255, 255, 255))
                    card1_2 = card.render("b2_card  " + str(b2_2), True, (225, 0, 0), (255, 255, 255))
                    card2_2 = card.render("b4_card  " + str(b4_2), True, (225, 0, 0), (255, 255, 255))
                    card3_2 = card.render("c3_card  " + str(c3_2), True, (225, 0, 0), (255, 255, 255))
                    card4_2 = card.render("d2_card  " + str(d2_2), True, (225, 0, 0), (255, 255, 255))
                    card5_2 = card.render("d4_card  " + str(d4_2), True, (225, 0, 0), (255, 255, 255))
                    card7_2 = card.render("defense  " + str(de_2), True, (255, 0, 0)  ,(255, 255, 255))
            if use_king_p2[0] == 1 and p2_piece_pos[0] != (1280,720):
                screen.blit(k1_s1_2, (1006, 357.0))
                screen.blit(k1_s2_2, (1006, 386.75))
            if use_king_p2[1] == 1 and p2_piece_pos[0] != (1280,720):
                screen.blit(k2_s1_2, (1006, 357))
                screen.blit(k2_s2_2, (1006, 386.75))
                screen.blit(k2_s3_2, (1006, 356.75 + 29.75*2))
            if use_knight_p2[0] == 1 and p2_piece_pos[1] != (1280,720):
                screen.blit(n1_s1_2, (1006, 356.75 + 29.75*3))
            if use_knight_p2[1] == 1 and p2_piece_pos[1] != (1280,720):
                screen.blit(n2_s1_2, (1006, 356.75 + 29.75*3))
            screen.blit(cards_2, (1006, 476.0))
            screen.blit(card1_2, (1006, 505.75))
            screen.blit(card2_2, (1006, 535.5))
            screen.blit(card3_2, (1006, 565.25))
            screen.blit(card4_2, (1006, 595.0))
            screen.blit(card5_2, (1006, 624.75))
            screen.blit(card6_2, (1006, 654.5))
            screen.blit(card7_2, (1006, 684.25))

        for en in range(5):
            for num in range(5):
                if board_col[en][num] == 0:
                    board[en][num] = pygame.image.load("tile.png")
                if board_col[en][num] == 1:
                    board[en][num] = pygame.image.load("tile_r.png") # 말배치 , 이동가능
                if board_col[en][num] == 2:
                    board[en][num] = pygame.image.load("tile_y.png") # 기동력 있을떄
                if board_col[en][num] == 3:
                    board[en][num] = pygame.image.load("tile_b.png") # 스킬 가능
                if board_col[en][num] == 4:
                    board[en][num] = pygame.image.load("tile_g.png") # 공격 가능
                screen.blit(board[en][num], board_pos[en][num])
        if p1_piece_pos[0] != (0,0):   # 폰의 위치가 (0,0)이 아닐 경우에 폰의 위치를 화면상에 출력시킨다.
            screen.blit(p1_piece_list[0], p1_piece_pos[0])
        if p1_piece_pos[1] != (0,0):
            screen.blit(p1_piece_list[1], p1_piece_pos[1])
        if p1_piece_pos[2] != (0,0):
            screen.blit(p1_piece_list[2], p1_piece_pos[2])
        if p2_piece_pos[0] != (0,0):   # 폰의 위치가 (0,0)이 아닐 경우에 폰의 위치를 화면상에 출력시킨다.
            screen.blit(p2_piece_list[0], p2_piece_pos[0])
        if p2_piece_pos[1] != (0,0):
            screen.blit(p2_piece_list[1], p2_piece_pos[1])
        if p2_piece_pos[2] != (0,0):
            screen.blit(p2_piece_list[2], p2_piece_pos[2])
        if move_b[1] == 1:
            screen.blit(move_button.normal, move_b[0])
        if respond_situation[0] == 1:
            res_font = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 30)
            ask_respond = res_font.render("대응하시겠습니까? 대응은 하나의 카드로만 가능합니다", True, (255, 255, 255))
            yes = res_font.render("   Y   ", True, (0, 0, 0), (255, 255, 255))
            no = res_font.render("   N   ", True, (0, 0, 0), (255, 255, 255))
            screen.blit(respond_box, (0, 240))
            if player1_turn == 1:
                if resp_2 > 0:
                    screen.blit(yes, (555, 350))  # 크기 가로 83 세로 30
                    screen.blit(no, (655, 350))
                    screen.blit(ask_respond, (265, 300))
                else:
                    screen.blit(no, (655, 350))
                    screen.blit(ask_respond, (265, 300))
            elif player2_turn == 1 and pieces == 4:
                if resp_1 > 0:
                    screen.blit(yes, (555, 350))  # 크기 가로 83 세로 30
                    screen.blit(no, (655, 350))
                    screen.blit(ask_respond, (265, 300))
                else:
                    screen.blit(no, (655, 350))
                    screen.blit(ask_respond, (265, 300))
        pygame.display.flip()  # 현재 전체화면의 상태를 업데이트 시킨다.
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if player1_turn == 1 and pieces == 4:  # end 버튼의 작동방식이다.
                if 20 <= mouse_x <= 217 and 25 <= mouse_y <= 111:
                    if event.type == MOUSEBUTTONDOWN:
                        end_button1.update([end_button1])
                if 20 <= mouse_x <= 217 and 25 <= mouse_y <= 111:
                    if event.type == MOUSEBUTTONUP:
                        screen.fill(0)
                        p1_move[0] = 0
                        p1_piece_attack[0] = 0
                        p1_piece_attack[1] = 0
                        p1_piece_attack[2] = 0
                        player1_turn = 2
                        end_button1.update([])
            if player2_turn == 1 and pieces == 4:  # end 버튼의 작동방식이다.
                if 1030 <= mouse_x <= 1227 and 25 <= mouse_y <= 111:
                    if event.type == MOUSEBUTTONDOWN:
                        end_button2.update([end_button2])
                if 1030 <= mouse_x <= 1227 and 25 <= mouse_y <= 111:
                    if event.type == MOUSEBUTTONUP:
                        screen.fill(0)
                        p2_move[0] = 0
                        p2_piece_attack[0] = 0
                        p2_piece_attack[1] = 0
                        p2_piece_attack[2] = 0
                        player2_turn = 2
                        end_button2.update([])
            for en in range(2):  #폰의 배치가 끝나지 않았을때,
                for num in range(5):
                    if allocate_p == 0 and pieces <= 3:
                        if not p1_allocate_pos[en][num] in p1_piece_pos: #플레이어의 배치공간의 포지션이 폰의 포지션리스트에 없다면 그 칸을 전부 빨간색으로 바꾼다
                            board_col[en][num] = 1
                        if p1_allocate_pos[en][num] in p1_piece_pos:  # 플레이어의 배치공간 리스트의 포지션이 폰의 포지션 리스트에 있다면 그 칸을 노란색으로 변환시킨다.
                            board_col[en][num] = 2
                    elif allocate_p == 1 and pieces <= 3:
                        if not p2_allocate_pos[en][num] in p2_piece_pos:
                            board_col[en + 3][num] = 1
                        if p2_allocate_pos[en][num] in p2_piece_pos:
                            board_col[en + 3][num] = 2
            if not (0, 0) in p1_piece_pos and allocate_p == 0:  # 폰의 배치가 모두 완료되었을 경우 폰의 개수를 4로 변환시킨다.
                    pieces = 0
                    allocate_p = 1
            if (0, 0) in p1_piece_pos:
                if event.type == MOUSEBUTTONDOWN:   #마우스를 클릭한다면
                    n_mouse_x, n_mouse_y = mouse_x, mouse_y
                    for en in range(2):
                        for num in range(5):
                            tile_x, tile_y = p1_allocate_pos[en][num]
                            if n_mouse_x >= tile_x and n_mouse_x <= tile_x + 113 and n_mouse_y >= tile_y and n_mouse_y <= tile_y + 113:  #현재 마우스의 위치가 타일의 범위내에 있다면
                                if board_col[en][num] == 1:   # 그리고 그 타일의 색깔이 빨간색이라면 -중복 배치 방지
                                    if piece_pos[allocate_p][pieces] == (0, 0):  #폰을 배치한다.
                                        piece_pos[allocate_p][pieces] = tile_x, tile_y
                                        pieces += 1
            if not (0, 0) in p2_piece_pos and allocate_p == 1:  # 폰의 배치가 모두 완료되었을 경우 폰의 개수를 4로 변환시킨다.
                    pieces = 4
            if (0, 0) in p2_piece_pos:    #폰의 배치가 완료되지 않았다면
                if event.type == MOUSEBUTTONDOWN:   #마우스를 클릭한다면
                    n_mouse_x, n_mouse_y = mouse_x, mouse_y
                    for en in range(2):
                        for num in range(5):
                            tile_x, tile_y = p2_allocate_pos[en][num]
                            if n_mouse_x >= tile_x and n_mouse_x <= tile_x + 113 and n_mouse_y >= tile_y and n_mouse_y <= tile_y + 113:  #현재 마우스의 위치가 타일의 범위내에 있다면
                                if board_col[en + 3][num] == 1:   # 그리고 그 타일의 색깔이 빨간색이라면 -중복 배치 방지
                                    if piece_pos[allocate_p][pieces] == (0, 0):  #폰을 배치한다.
                                        piece_pos[allocate_p][pieces] = tile_x, tile_y
                                        pieces += 1
            if pieces == 4:
                if player2_turn == 2 and player1_turn == 0:
                    p1_move[0] = 2
                    player1_turn = 1
                    player2_turn = 0
                if player1_turn == 2 and player2_turn == 0:
                    p2_move[0] = 2
                    player2_turn= 1
                    player1_turn = 0
            if pieces == 4 and player1_turn == 1:
                if p1_hand.count({"원딜 스킬 1"}) > 0:
                    king1_p1.long_dealer_sk1(0, 0, 0)
                if p1_hand.count({"원딜 스킬 2"}) > 0:
                    king1_p1.long_dealer_sk2(0, 1, 1, 0)
                if p1_hand.count({"성기사 스킬 1"}) > 0:
                    king2_p1.holly_knight_sk1(0, 0, 1, 0)
                if p1_hand.count({"성기사 스킬 2"}) > 0:
                    king2_p1.holly_knight_sk2(0, 1, 0)
                if p1_hand.count({"주술사 스킬 1"}) > 0:
                    knight1_p1.magician_sk1(0, 3, 0)
                p1_spell = Spell()
                if p1_hand.count({"한칸 이동":1}) > 0:
                    p1_spell.move(4, 0)
                if p1_hand.count({"b2":4}) > 0:
                    p1_spell.b2_card(5, 0, 1)
                if p1_hand.count({"b4":5}) > 0:
                    p1_spell.b4_card(6, 0, 1)
                if p1_hand.count({"c3":6}) > 0:
                    p1_spell.c3_card(7, 0, 1)
                if p1_hand.count({"d2":7}) > 0:
                    p1_spell.d2_card(8, 0, 1)
                if p1_hand.count({"d4":8}) > 0:
                    p1_spell.d4_card(9, 0, 1)
                if p1_hand.count({"기동력 +1":3}) > 0:
                    p1_spell.move_plus(10,0)
                if p2_hand.count({"방어":2}) > 0 and respond_situation[0] == 3:
                    p1_spell.defense(11,1)
                respond()
            if pieces == 4 and player2_turn == 1 and respond_situation[0] == 3:
                piece_clicked = [0,0,0]
                if p1_hand.count({"원딜 스킬 1"}) > 0:
                    king1_p1.long_dealer_sk1(0, 0, 0)
                if p1_hand.count({"성기사 스킬 3"}) > 0:
                    king2_p1.holly_knight_sk3(0, 2, 0)
                if p1_hand.count({"탱커 스킬 1"}) > 0:
                    knight2_p1.tanker_sk1(0, 3, 0)
                p1_spell = Spell()
                if p1_hand.count({"한칸 이동":1}) > 0:
                    p1_spell.move(4, 0)
                if p1_hand.count({"b2":4}) > 0:
                    p1_spell.b2_card(5, 0, 1)
                if p1_hand.count({"b4":5}) > 0:
                    p1_spell.b4_card(6, 0, 1)
                if p1_hand.count({"c3":6}) > 0:
                    p1_spell.c3_card(7, 0, 1)
                if p1_hand.count({"d2":7}) > 0:
                    p1_spell.d2_card(8, 0, 1)
                if p1_hand.count({"d4":8}) > 0:
                    p1_spell.d4_card(9, 0, 1)
            if pieces == 4 and player2_turn == 1:
                p2_spell = Spell()
                if p2_hand.count({"원딜 스킬 1"}) > 0:
                    king1_p2.long_dealer_sk1(1, 0, 1)
                if p2_hand.count({"원딜 스킬 2"}) > 0:
                    king1_p2.long_dealer_sk2(1, 1, 0, 1)
                if p2_hand.count({"성기사 스킬 1"}) > 0:
                    king2_p2.holly_knight_sk1(1, 0, 0, 1)
                if p2_hand.count({"성기사 스킬 2"}) > 0:
                    king2_p2.holly_knight_sk2(1, 1, 1)
                if p2_hand.count({"주술사 스킬 1"}) > 0:
                    knight1_p2.magician_sk1(1, 3, 1)
                if p2_hand.count({"한칸 이동":1}) > 0:
                    p2_spell.move(4, 1)
                if p2_hand.count({"b2":4}) > 0:
                    p2_spell.b2_card(5, 1, 0)
                if p2_hand.count({"b4":5}) > 0:
                    p2_spell.b4_card(6, 1, 0)
                if p2_hand.count({"c3":6}) > 0:
                    p2_spell.c3_card(7, 1, 0)
                if p2_hand.count({"d2":7}) > 0:
                    p2_spell.d2_card(8, 1, 0)
                if p2_hand.count({"d4":8}) > 0:
                    p2_spell.d4_card(9, 1, 0)
                if p2_hand.count({"기동력 +1":3}) > 0:
                    p2_spell.move_plus(10,1)
                if p1_hand.count({"방어":2}) > 0 and respond_situation[0] == 3:
                    p2_spell.defense(11,0)
                respond()
            if pieces == 4 and player1_turn == 1 and respond_situation[0] == 3:
                p2_spell = Spell()
                if p2_hand.count({"원딜 스킬 1"}) > 0:
                    king1_p2.long_dealer_sk1(1, 0, 1)
                if p2_hand.count({"성기사 스킬 3"}) > 0:
                    king2_p2.holly_knight_sk3(1, 2, 1)
                if p2_hand.count({"탱커 스킬 1"}) > 0:
                    knight2_p2.tanker_sk1(1, 3, 1)
                if p2_hand.count({"한칸 이동":1}) > 0:
                    p2_spell.move(4, 1)
                if p2_hand.count({"b2":4}) > 0:
                    p2_spell.b2_card(5, 1, 0)
                if p2_hand.count({"b4":5}) > 0:
                    p2_spell.b4_card(6, 1, 0)
                if p2_hand.count({"c3":6}) > 0:
                    p2_spell.c3_card(7, 1, 0)
                if p2_hand.count({"d2":7}) > 0:
                    p2_spell.d2_card(8, 1, 0)
                if p2_hand.count({"d4":8}) > 0:
                    p2_spell.d4_card(9, 1, 0)


            if pieces == 4 and p1_move[0] > 0 and player1_turn == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if 1 in piece_clicked and move_b[1] == 1:
                        mo_x, mo_y = move_b[0]
                        if mo_x <= mouse_x <= mo_x + 132 and mo_y <= mouse_y <= mo_y + 42:
                            pass
                        else:
                            move_b[0] = 1280, 720
                            move_b[1] = 0
                            for no in piece_clicked:
                                piece_clicked[no] = 0
                                p1_piece_attack[no] = 0
                if event.type == MOUSEBUTTONUP:  # 스킬이 종료 될때, 스킬을 종료함을 2로 나타냄 하지만 마우스 버튼업 조건이 없다면 2가 되는 순간0이 되어 이동함수랑 겹치게 되어서 무브 함수가 발동 그래서 마우스 버튼이 올라가기 전까지 종료가 대기로 바꾸는 시간을 두어 중복방지
                    if spell_use[0] == 2:
                        spell_use[0] = 0
                if card_clicked[0] == 0 and spell_use[0] == 0:
                    king1_p1.movement1(p1_piece_pos[0], 0, use_king_p1[0], 0)
                    king1_p1.attack3(p1_piece_pos[0], 0, use_king_p1[0], 0, 1)
                    #####
                    king2_p1.movement3(p1_piece_pos[0], 0, use_king_p1[1], 0)
                    king2_p1.attack1(p1_piece_pos[0], 0, use_king_p1[1], 0, 1)
                    #####
                    knight1_p1.movement1(p1_piece_pos[1], 1, use_knight_p1[0], 0)
                    knight1_p1.attack1(p1_piece_pos[1], 1, use_knight_p1[0], 0, 1)
                    #####
                    knight2_p1.movement2(p1_piece_pos[1], 1, use_knight_p1[1], 0)
                    knight2_p1.attack1(p1_piece_pos[1], 1, use_knight_p1[1], 0, 1)
                    #####
                    pawn_p1.movement1(p1_piece_pos[2], 2, 1, 0)
                    pawn_p1.attack1(p1_piece_pos[2], 2, 1, 0, 1)
                    #####
                    respond()
            if pieces == 4 and p2_move[0] > 0 and player2_turn == 1:
                if event.type == MOUSEBUTTONDOWN:
                    if 1 in piece_clicked and move_b[1] == 1:
                        mo_x, mo_y = move_b[0]
                        if mo_x <= mouse_x <= mo_x + 132 and mo_y <= mouse_y <= mo_y + 42:
                            pass
                        else:
                            move_b[0] = 1280, 720
                            move_b[1] = 0
                            for no in piece_clicked:
                                piece_clicked[no] = 0
                                p1_piece_attack[no] = 0
                if event.type == MOUSEBUTTONUP:  # 스킬이 종료 될때, 스킬을 종료함을 2로 나타냄 하지만 마우스 버튼업 조건이 없다면 2가 되는 순간0이 되어 이동함수랑 겹치게 되어서 무브 함수가 발동 그래서 마우스 버튼이 올라가기 전까지 종료가 대기로 바꾸는 시간을 두어 중복방지
                    if spell_use[0] == 2:
                        spell_use[0] = 0
                if card_clicked[0] == 0 and spell_use[0] == 0:
                    king1_p2.movement1(p2_piece_pos[0], 0, use_king_p1[0], 1)
                    king1_p2.attack3(p2_piece_pos[0], 0, use_king_p1[0], 1, 0)
                    #####
                    king2_p2.movement3(p2_piece_pos[0], 0, use_king_p1[1], 1)
                    king2_p2.attack1(p2_piece_pos[0], 0, use_king_p1[1], 1, 0)
                    #####
                    knight1_p2.movement1(p2_piece_pos[1], 1, use_knight_p1[0], 1)
                    knight1_p2.attack1(p2_piece_pos[1], 1, use_knight_p1[0], 1, 0)
                    #####
                    knight2_p2.movement2(p2_piece_pos[1], 1, use_knight_p1[1], 1)
                    knight2_p2.attack1(p2_piece_pos[1], 1, use_knight_p1[1], 1, 0)
                    #####
                    pawn_p2.movement1(p2_piece_pos[2], 2, 1, 1)
                    pawn_p2.attack1(p2_piece_pos[2], 2, 1, 1, 0)
                    #####
                    respond()


            if pieces >= 4:
                if respond_situation[0] == 3: # 기물의 배치가 종료되었을 때, 내 기물이 있는 위치를 제외한 모든 곳을 원래 보드 색깔로 변환시킨다. 보드 정리
                    for en in range(5):
                        for num in range(5):
                            if board_col[en][num] == 0:
                                pass
                            if board_col[en][num] == 1:
                                if spell_use[0] == 1:
                                    for no in range(2):
                                        if board_pos[en][num] in piece_pos[no]:
                                            board_col[en][num] = 0
                                elif card_clicked[0] == 1:
                                    if player1_turn == 1:
                                        if board_pos[en][num] in p2_piece_pos:
                                            board_col[en][num] = 1
                                        else:
                                            board_col[en][num] = 0
                                    if player2_turn == 1:
                                        if board_pos[en][num] in p1_piece_pos:
                                            board_col[en][num] = 1
                                        else:
                                            board_col[en][num] = 0
                            if board_col[en][num] == 2:
                                pass
                            if board_col[en][num] == 3:
                                if spell_use[0] == 1:
                                    for no in range(2):
                                        if board_pos[en][num] in piece_pos[no]:
                                            board_col[en][num] = 0
                            if board_col[en][num] == 4:
                                pass
                    pass
                elif 1 in piece_clicked:  # 기물이 클릭되었을때의 보드 색깔 정리 플레이어 1
                    if player1_turn == 1:
                        for en in range(5):
                            for num in range(5):
                                if board_col[en][num] == 1:
                                    if board_pos[en][num] in p1_piece_pos:
                                        board_col[en][num] = 2
                                    if board_pos[en][num] in p2_piece_pos:
                                        board_col[en][num] = 0
                                if board_col[en][num] == 3:
                                    board_col[en][num] = 0
                    if player2_turn == 1:
                        for en in range(5):
                            for num in range(5):
                                if board_col[en][num] == 1:
                                    if board_pos[en][num] in p2_piece_pos:
                                        board_col[en][num] = 2
                                    if board_pos[en][num] in p1_piece_pos:
                                        board_col[en][num] = 0
                    if respond_situation[0] == 1:
                        for en in range(5):
                            for num in range(5):
                                board_col[en][num] = 0
                elif card_clicked[0] == 1:
                    if respond_situation[0] == 1:
                        for en in range(5):
                            for num in range(5):
                                board_col[en][num] = 0
                    elif player1_turn == 1 or player2_turn == 1:
                        for en in range(5):
                            for num in range(5):
                                if board_col[en][num] == 3:
                                    if board_pos[en][num] in p1_piece_pos:
                                        board_col[en][num] = 0
                                    if board_pos[en][num] in p2_piece_pos:
                                        board_col[en][num] = 0
                elif card_clicked[0] == 0 and 1 not in piece_clicked:
                    if respond_situation[0] == 1:
                        for en in range(5):
                            for num in range(5):
                                board_col[en][num] = 0
                    elif player1_turn == 1:
                        for en in range(5):
                            for num in range(5):
                                if not board_pos[en][num] in p1_piece_pos:  # 보드 포지션이 자신 기물 포지션에 없다면
                                    board_col[en][num] = 0
                                elif board_pos[en][num] in p1_piece_pos:  # 보드 포지션이 자신 기물 포지션에 있고
                                    if p1_move[0] == 0:  # 플레이어1의 기동력이 모두 소모 되었다면
                                        board_col[en][num] = 0
                                    else:  # 기동력이 소모 되지 않았다면
                                        board_col[en][num] = 2
                                else:
                                    board_col[en][num] = 0
                    elif player2_turn == 1:
                        for en in range(5):
                            for num in range(5):
                                if not board_pos[en][num] in p2_piece_pos:  # 보드 포지션이 자신 기물 포지션에 없다면
                                    board_col[en][num] = 0
                                elif board_pos[en][num] in p2_piece_pos:  # 보드 포지션이 자신 기물 포지션에 있고
                                    if p2_move[0] == 0:  # 플레이어1의 기동력이 모두 소모 되었다면
                                        board_col[en][num] = 0
                                    else:  # 기동력이 소모 되지 않았다면
                                        board_col[en][num] = 2
                                else:
                                    board_col[en][num] = 0

            if p1_piece_pos == [(1280,720),(1280,720),(1280,720)]:
                screen.fill(0)
                winning = True
                playing = False
            elif p2_piece_pos == [(1280,720),(1280,720),(1280,720)]:
                screen.fill(0)
                winning = True
                playing = False
            if event.type == MOUSEBUTTONUP:
                end_button1.update([])
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    while winning:
        win = pygame.font.Font('c:/Windows/Fonts/malgun.ttf', 70)
        if p1_piece_pos == [(1280,720),(1280,720),(1280,720)]:
            p2_win = win.render("Player2 Win!!!!!", True, (225, 0, 0))
            screen.blit(p2_win, (375,275))
        elif p2_piece_pos == [(1280,720),(1280,720),(1280,720)]:
            p1_win = win.render("Player1 Win!!!!!", True, (225, 0, 0))
            screen.blit(p1_win, (375,275))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
