import pygame

from quiz import Quiz
import maze as mz
class Quad:
        
        def __init__(self):
                self.block =0
                self.b_press=False
                

        def make_button(self, event, left, top, width, height, blockNum):
                
                mouse = pygame.mouse.get_pos()
                
                   
                if not self.b_press:
                    if left+width > mouse[0] > left and top < mouse[1] < top+height: 
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            self.b_press=True
                else: 
                    if blockNum==1:
                            quiz = Quiz()        
                            quiz.run_screen()
                    elif blockNum==4: 
                            mz.maze()



        def run_screen(self):
        
                pygame.display.set_caption("Quiz App Launching")
                
                zFrame_background = pygame.image.load("QuadAdjust.jpg")
                backgroundRect=zFrame_background.get_rect()
                size = (width, length) = zFrame_background.get_size()
                self.screen = pygame.display.set_mode(size)        
                
                
                
                done = False
                while not done: 
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done=True #true or false value
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            print("will play sound\n")
                            #click_sound.play()
                        
                        self.screen.blit(zFrame_background, backgroundRect) 
                        self.make_button(event, 460, 0, 100, 840, 1)
                        self.make_button(event, 0, 480, 71, 375, 4)
                                       
                        
                        
                        pygame.display.flip()
                    
                pygame.quit()        




quad = Quad()

quad.run_screen()

