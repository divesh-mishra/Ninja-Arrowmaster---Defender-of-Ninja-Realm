import pygame
from sys import exit
from random import randint, choice

pygame.init()

# Creating Game Window
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("NINJA ARROWMASTER")
iconImg = pygame.image.load('ninja.png')
pygame.display.set_icon(iconImg)

background = pygame.image.load('Assets/sky.png').convert()
ground = pygame.image.load('Assets/ground.png').convert()
# tutorial screen

text_font = pygame.font.Font('Assets/font_space_n.otf', 30)
tutorial_font = pygame.font.Font('Assets/ShortBaby-Mg2w.ttf', 40)
tutorial_text1 = tutorial_font.render('1) Use Space-bar to jump.', True, 32)
tutorial_text2 = tutorial_font.render('2) Use Right key to shoot the arrow.', True, 32)
return_button = pygame.image.load('Assets/return_button.png')
return_rect = return_button.get_rect(center=(400, 400))
return_text = text_font.render('RETURN', True, 32)
return_text_rect = return_text.get_rect(center=(400, 400))

# Score
score_var = 0
score_values_list = [0]
# score_max = 0
if len(score_values_list) > 3:
    score_values_list.remove(min(score_values_list))

score_font = pygame.font.Font('Assets/ShortBaby-Mg2w.ttf', 40)


def score_board():
    score_surf = score_font.render(f'Score:{score_var}', True, 32)
    screen.blit(score_surf, (370, 10))
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_1 = pygame.image.load('Game/Walking/pw_1.png').convert_alpha()
        player_2 = pygame.image.load('Game/Walking/pw_2.png').convert_alpha()
        player_3 = pygame.image.load('Game/Walking/pw_3.png').convert_alpha()
        player_4 = pygame.image.load('Game/Walking/pw_4.png').convert_alpha()
        player_5 = pygame.image.load('Game/Walking/pw_5.png').convert_alpha()
        player_6 = pygame.image.load('Game/Walking/pw_6.png').convert_alpha()
        player_7 = pygame.image.load('Game/Walking/pw_7.png').convert_alpha()
        player_8 = pygame.image.load('Game/Walking/pw_8.png').convert_alpha()

        self.player_walk = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
        self.player_walk_index = 0

        player_b1 = pygame.image.load('Game/Shooting/Bow4.png').convert_alpha()
        player_b2 = pygame.image.load('Game/Shooting/Bow5.png').convert_alpha()
        player_b3 = pygame.image.load('Game/Shooting/Bow6.png').convert_alpha()
        player_b4 = pygame.image.load('Game/Shooting/Bow7.png').convert_alpha()

        self.player_bow = [player_b1, player_b2, player_b3, player_b4]
        self.player_bow_index = 0

        self.jump = pygame.image.load('Game/Walking/pw_1.png').convert_alpha()
        self.image = self.player_walk[self.player_walk_index]

        self.rect = self.image.get_rect(midbottom=(100, 415))
        self.gravity = 0

        self.instantaneous_health = 200
        self.max_health = 1200
        self.health_bar_length = 300
        self.heath_bar_ratio = 4

    def player_jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 415:
            self.gravity = -25

    def act_gravity(self):
        global arrow_pos_y
        self.gravity += 1
        self.rect.bottom += self.gravity
        arrow_pos_y = self.rect.centery

        if self.rect.bottom >= 415:
            self.rect.bottom = 415
            self.gravity = 0

    def player_anim(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.player_bow_index += 0.1
            if self.player_bow_index >= len(self.player_bow):
                self.player_bow_index = 0
            self.image = self.player_bow[int(self.player_bow_index)]

        else:
            if self.rect.bottom < 300:
                self.image = self.jump

            else:
                self.player_walk_index += 0.1
                if self.player_walk_index >= len(self.player_walk):
                    self.player_walk_index = 0
                self.image = self.player_walk[int(self.player_walk_index)]

    def generate_arrow(self):

        return Arrow(self.rect.centerx, arrow_pos_y)

    def health_decrease(self, amt):
        if self.instantaneous_health > 0:
            self.instantaneous_health -= amt
        if self.instantaneous_health < 0:
            self.instantaneous_health = 0
        pygame.display.update()

    def draw_health_bar(self):
        # colour, (x,y,width,height), margin width
        heart_img = pygame.image.load('Assets/heartImg.png').convert_alpha()
        heart_img_rect = heart_img.get_rect(topright=(30, 16))
        screen.blit(heart_img, heart_img_rect)
        pygame.draw.rect(screen, 'Red', (30, 20, self.health_bar_length, 15))
        pygame.draw.rect(screen, 'Green', (30, 20, self.instantaneous_health / self.heath_bar_ratio, 15))

    def update(self):
        global score_var
        global game_on
        global frames
        self.player_jump()
        self.act_gravity()
        self.player_anim()
        # self.score_board()
        self.draw_health_bar()
        if self.instantaneous_health == 0:
            # frames = 0
            score_values_list.append(score_var)
            self.instantaneous_health = 1200
            game_on = 3


player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(Player())    
