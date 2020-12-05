# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: NANDI GUO
"""
import pygame,os,Main_Game,Start_Screen,How_to_play

Orange = (119,0,255)
White = (255,255,255)
Blue = (0,238,255)
Width,Height = (780,366)

class Button():
    
    def __init__(self, text, color, x=None, y=None):

        self.surf = font.render(text, True, color)
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()   
        self.x = x    
        self.y = y
    
    def display(self):
    	screen.blit(self.surf, (self.x, self.y))
    
    def check_click(self, position):  
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT
        
        if x_match and y_match:
            return True
        else:
            return False
        
def Show(screen,Text,x,y) :
    score_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    surf = score_font.render(Text,False,(255,255,255))
    screen.blit(surf,(x,y))
        
def Modes_Screen():
    global screen,font,Total_Scores
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))  
    font = pygame.font.Font(pygame.font.get_default_font(), 25)
    pygame.display.set_caption("Game Modes")
    background = pygame.image.load("Images/Backgrounds/Start2_Background.png")
    background1 = pygame.image.load("Images/Backgrounds/p.png")
    screen.blit(background, (0,0))
    bgm2_sound = pygame.mixer.Sound("Sounds/Modes_Bgm.mp3")
    bgm2_sound.play()
    Total_Scores =  Main_Game.Scores
    b1x,b1y=155,155
    b2x,b2y=550,155
    b3x,b3y=155,320
    b4x,b4y=550,320
    b5x,b5y=350,165   
    if Main_Game.Scores <= 3 :
        screen.blit(background, (0,0))
    else :
        screen.blit(background1, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    Easy,Normal,Hard,Ultimate,Back = 'Easy','Normal','Hard','Locked','Back'
    play_button = Button(Easy, White, b1x, b1y)
    play2_button = Button(Normal, White, b2x, b2y)
    play3_button = Button(Hard, White, b3x, b3y)
    play4_button = Button(Ultimate, White, b4x, b4y)
    back_button = Button(Back, Orange, b5x, b5y)
    
    play_button.display()
    play2_button.display()
    play3_button.display()
    play4_button.display()
    back_button.display()
    pygame.display.update() 
    Show(screen,f"Total Scores = {Total_Scores}",0,0) 
    
    while True:  
        if not (play_button.check_click(pygame.mouse.get_pos()) or \
                play2_button.check_click(pygame.mouse.get_pos()) or \
                play3_button.check_click(pygame.mouse.get_pos()) or \
                play4_button.check_click(pygame.mouse.get_pos()) or\
                back_button.check_click(pygame.mouse.get_pos())):                
            pygame.mixer.music.play() 
             
        if play_button.check_click(pygame.mouse.get_pos()):              
            play_button = Button(Easy, Blue, b1x, b1y)                        
        else:            
            play_button = Button(Easy, White, b1x, b1y)
            
        if play2_button.check_click(pygame.mouse.get_pos()):              
            play2_button = Button(Normal, Blue, b2x, b2y)                        
        else:            
            play2_button = Button(Normal, White, b2x, b2y)
            
        if play3_button.check_click(pygame.mouse.get_pos()):              
            play3_button = Button(Hard, Blue, b3x, b3y)                        
        else:            
            play3_button = Button(Hard, White, b3x, b3y)
            
        if play4_button.check_click(pygame.mouse.get_pos()):              
            play4_button = Button(Ultimate, Blue, b4x, b4y)                        
        else:            
            play4_button = Button(Ultimate, White, b4x, b4y)
        
        if back_button.check_click(pygame.mouse.get_pos()):              
            back_button = Button(Back, Blue, b5x, b5y)                        
        else:            
            back_button = Button(Back, Orange, b5x, b5y)
            
        play_button.display()
        play2_button.display()
        play3_button.display()
        play4_button.display()
        back_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
# =============================================================================
#                 Easy
#                 Screen_Width = 890
#                 Screen_Height = 476
#                 Fps = 24
#                 Highest_y = 200
#                 Lowest_y = 370
# =============================================================================
                Main_Game.Game_Main(850,476,150,305,"Images/Backgrounds/Snow_Background.jpg","Sounds/Normal_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play2_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
# =============================================================================
#                 Normal 
#                 Screen_Width = 890
#                 Screen_Height = 476
#                 Fps = 24
#                 Highest_y = 200
#                 Lowest_y = 370
# =============================================================================
                Main_Game.Game_Main(890,476,180,370,"Images/Backgrounds/Game_Background.png","Sounds/Normal_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play3_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
# =============================================================================
#                 Hard
#                 Screen_Width = 850
#                 Screen_Height = 476
#                 Fps = 40
#                 Highest_y = 150
#                 Lowest_y = 305
# =============================================================================
                Main_Game.Game_Main(850,476,145,305,"Images/Backgrounds/Road_Background.png","Sounds/Hard_Bgm.mp3")
                pygame.quit()                
                os._exit(0)
                break
            
            if play4_button.check_click(pygame.mouse.get_pos()):
                if Total_Scores <= 3 :
                    Show(screen,"Your scores are not enought!",b4x-50,b4y+20)                   
                else :
                    Main_Game.Game_Main(850,476,145,305,"Images/Backgrounds/Road_Background.png","Sounds/Hard_Bgm.mp3")
                    pygame.quit()                
                    os._exit(0)
                    break
                
            if back_button.check_click(pygame.mouse.get_pos()):
                bgm2_sound.stop()
                # Start_Screen.Firstscreen()
                How_to_play.How_screen()
                pygame.quit()                
                os._exit(0)
                break
                    

