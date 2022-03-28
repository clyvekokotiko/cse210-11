import random, time, pygame, sys
from pygame.locals import *
from constants import *
from game.casting.allignment import Allignment
from game.casting.text import Text
from game.scripting.draw import Draw
from game.casting.score import Score


class Director:
    """A person who directs the game."""

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        pass
        
    def start_game(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
        pygame.init()
       
        pygame.display.set_caption('Tetris')
        
        Text.showTextScreen(self,'Tetris')
        while True: # game loop
            if random.randint(0, 1) == 0:
                pygame.mixer.music.load('tetris/assets/sounds/tetrisc.mid')
            else:
                pygame.mixer.music.load('tetris/assets/sounds/tetrisc.mid')
            pygame.mixer.music.play(-1, 0.0)
            self.runGame()
            pygame.mixer.music.stop()
            Text.showTextScreen('Game Over')
    
    def runGame(self):
        # setup variables for the start of the game
        board = Draw.getBlankBoard()
        lastMoveDownTime = time.time()
        lastMoveSidewaysTime = time.time()
        lastFallTime = time.time()
        movingDown = False # note: there is no movingUp variable
        movingLeft = False
        movingRight = False
        score = 0
        level, fallFreq = Score.calculateLevelAndFallFreq(score)
        
        fallingPiece = Draw.getNewPiece()
        nextPiece = Draw.getNewPiece()
        
        while True: # main game loop
            if fallingPiece == None:
                # No falling piece in play, so start a new piece at the top
                fallingPiece = nextPiece
                nextPiece = Draw.getNewPiece()
                lastFallTime = time.time() # reset lastFallTime
                
                if not Allignment.Allignment.isValidPosition(board, fallingPiece):
                    return # can't fit a new piece on the board, so game over
            
            self.checkForQuit()
            for event in pygame.event.get(): # event handling loop
                if event.type == KEYUP:
                    if (event.key == K_p):
                        # Pausing the game
                        DISPLAYSURF.fill(BGCOLOR)
                        pygame.mixer.music.stop()
                        Text.showTextScreen('Paused') # pause until a key press
                        pygame.mixer.music.play(-1, 0.0)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
                    elif (event.key == K_LEFT or event.key == K_a):
                        movingLeft = False
                    elif (event.key == K_RIGHT or event.key == K_d):
                        movingRight = False
                    elif (event.key == K_DOWN or event.key == K_s):
                        movingDown = False
                elif event.type == KEYDOWN:
                    # moving the block sideways
                    if (event.key == K_LEFT or event.key == K_a) and Allignment.isValidPosition(board, fallingPiece, adjX=-1):
                        fallingPiece['x'] -= 1
                        movingLeft = True
                        movingRight = False
                        lastMoveSidewaysTime = time.time()
                    elif (event.key == K_RIGHT or event.key == K_d) and Allignment.isValidPosition(board, fallingPiece, adjX=1):
                        fallingPiece['x'] += 1
                        movingRight = True
                        movingLeft = False
                        lastMoveSidewaysTime = time.time()
                    
                    # rotating the block (if there is room to rotate)
                    elif (event.key == K_UP or event.key == K_w):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])
                        if not Allignment.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])
                    elif (event.key == K_q): # rotate the other direction
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])
                        if not Allignment.isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])
                    
                    # making the block fall faster with the down key
                    elif (event.key == K_DOWN or event.key == K_s):
                        movingDown = True
                        
                        if Allignment.isValidPosition(board, fallingPiece, adjY=1):
                            fallingPiece['y'] += 1
                        lastMoveDownTime = time.time()
                    
                    # move the current block all the way down
                    elif event.key == K_SPACE:
                        movingDown = False
                        movingLeft = False
                        movingRight = False
                        for i in range(1, BOARDHEIGHT):
                            if not Allignment.isValidPosition(board, fallingPiece, adjY=i):
                                break
                        fallingPiece['y'] += i - 1
            
            # handle moving the block because of user input
            if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
                if movingLeft and Allignment.isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                elif movingRight and Allignment.isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                lastMoveSidewaysTime = time.time()
            
            if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and Allignment.isValidPosition(board, fallingPiece, adjY=1):
                fallingPiece['y'] += 1
                lastMoveDownTime = time.time()
            
            # let the piece fall if it is time to fall
            level = 1
            score = 0
            if time.time() - lastFallTime > fallFreq:
                # see if the piece has landed
                if not Allignment.isValidPosition(board, fallingPiece, adjY=1):
                    # falling piece has landed, set it on the board
                    Draw.addToBoard(board, fallingPiece)
                    score += Allignment.removeCompleteLines(board)
                    level = Score.calculateLevelAndFallFreq(score)
                    fallFreq = Score.calculateLevelAndFallFreq(score)

                    fallingPiece = None
                else:
                    # piece did not land, just move the block down
                    fallingPiece['y'] += 1
                    lastFallTime = time.time()
            
            # drawing everything on the screen
            DISPLAYSURF.fill(BGCOLOR)
            Draw.drawBoard(self,board)
            Draw.drawStatus(score, level)
            Draw.drawNextPiece(nextPiece)
            
            if fallingPiece != None:
                Draw.drawPiece(fallingPiece)
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    # def terminate():
    #     pygame.quit()
    #     sys.exit()
    
    def checkForQuit(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            #terminate() # terminate if any QUIT events are present
            pygame.quit()
            sys.exit()
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                #terminate() # terminate if the KEYUP event was for the Esc key
                pygame.quit()
                sys.exit()
            pygame.event.post(event) # put the other KEYUP event objects back
    
    def makeTextObjs(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()