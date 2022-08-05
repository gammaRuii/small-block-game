import kivy
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
#from tenByTengrid import BigGrid
from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from board_logic import BoardLogic
from kivy.uix.screenmanager import Screen,ScreenManager

Window.clearcolor = (.5,.5,.5,0.7)
board_size = 7
default_size = 10

### please think what behavior each widget should have? What callbacks needs to be defined?
### and what data will be updated in each callback?

class BigGrid(GridLayout):
    def __init__(self, size, TwoDArray, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None,None)
        self.size = (dp(800),dp(800))
        if size <= 0:
            size = default_size
        self.cols = size

        self.draw(size, TwoDArray)


    # we need to call the function every time the board status (a new ball placed, or a new game started)
    # please make sure it can redraw 
    def draw(self, size, TwoDArray):
        for i in range(size):
            for j in range(size):
                color = TwoDArray[i][j]
                color = randint(3,4)
                # for each and every button below, we need to find a way to let it send back the column & row number
                if color < 3 or color > 10 :
                    b = Button()
                else :
                    b = Button(background_normal = 'snapshot0{}.png'.format(color), background_down = 'snap0{}d.png'.format(color))
                self.add_widget(b)

# Where the score is displayed
class Scoreboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.3, 0.15)
        self.pos_hint_x = 0.8
        self.pos_hint_y = 0.8
        runScore = BoxLayout()
        runScore.orientation = "vertical"
        scoretext = Label(text = "Score:")
        runScore.add_widget(scoretext)
        actualScore = Label(text = "{}".format(app.score))
        runScore.add_widget(actualScore)
        self.add_widget(runScore)
        highScore = BoxLayout()
        highScore.orientation = "vertical"
        highscoretext = Label(text="Highscore:")
        highScore.add_widget(highscoretext)
        # add high score to format when json/yml file is written
        bestScore = Label(text="1".format())
        highScore.add_widget(bestScore)
        self.add_widget(highScore)
# display three balls for player to place
# once selected and placed, the correspong spot will be disabled. 
class BallPicker:
    pass

# once clicked, the game will be reset, a new game starts
class RestartButton:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PlayingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # we need to return a screen with the board of grids, next-round ball picker, scoreboard, "Start" Button, etc
        print("hi")
        self.add_widget(BigGrid(board_size, app.boardData.GetBoardData()))
        self.add_widget(Scoreboard())

class GameApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.boardData = BoardLogic(board_size)
        self.nextBallColor = 0
        self.nextBallLocation = [0, 0]
        self.score = 0

    def build(self):
        return PlayingScreen()


app = GameApp()

app.run()

