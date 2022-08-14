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
#from kivymd.app import MDApp
#from kivymd.uix.menu import MDDropdownMenu
#from kivymd.uix.behaviors.backgroundcolor_behavior import BackgroundColorBehavior
from kivy.uix.popup import Popup

Window.clearcolor = (.5,.5,.5,0.7)
board_size = 7
default_size = 10
board_dimension = 800

### please think what behavior each widget should have? What callbacks needs to be defined?
### and what data will be updated in each callback?

class BigGrid(GridLayout):
    def __init__(self, size, TwoDArray, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None,None)
        self.size = (dp(board_dimension ),dp(board_dimension))
        if size <= 0:
            size = default_size
        self.cols = size

        self.draw(size, TwoDArray)


    # we need to call the function every time the board status (a new ball placed, or a new game started)
    # please make sure it can redraw 
    def draw(self, size, TwoDArray):
        self.clear_widgets()
        print(size, TwoDArray )
        for i in range(size):
            for j in range(size):
                color = TwoDArray[i][j]
                # for each and every button below, we need to find a way to let it send back the column & row number
                if color < 2 or color > 9 :
                    b = Button(on_release = app.BoardPlace)
                    b.id = i*board_size + j
                    # b.bind(on_release = app.RemovePickBall)
                else :
                    b = Button(background_normal = 'snapshot0{}.png'.format(color), background_down = 'snap0{}d.png'.format(color), on_release = app.BoardPlace)
                    b.id = i * board_size + j
                self.add_widget(b)

# Where the score is displayed
class Scoreboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (0.3, 0.15)
        self.pos_hint = {"top": 0.8, "right": 0.8}
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
class BallPicker(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = "Ballpicker"
        self.size_hint = (None, None)
        height = int(board_dimension / board_size)
        self.size = (dp(height*3), dp(height))
        for i in range(3):
            ball_color = randint(2,9)
            ball = Button(background_normal = "snapshot0{}.png".format(ball_color), background_down = "snap0{}d.png".format(ball_color), on_release = app.PickerPress, )
            ball.id = "ballpick{}".format(i)
            self.add_widget(ball)
        
        self.pos_hint = {"top": 1, "right": 1}
# once clicked, the game will be reset, a new game starts
class MenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0,0,0,1)
        self.size_hint = (0.05,0.05)
        self.pos_hint = {'top': 1, "right": 1}
        self.background_normal = "pauseButton.png"

class PlayingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # we need to return a screen with the board of grids, next-round ball picker, scoreboard, "Start" Button, etc
        # print("hi")
        self.id = "PlayScreen"
        self.boardGrid = BigGrid(board_size, app.boardData.GetBoardData())
        
        self.add_widget(self.boardGrid)
        self.add_widget(Scoreboard())
        self.add_widget(MenuButton())
        self.add_widget(BallPicker())


class GameApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.boardData = BoardLogic(board_size)
        self.nextBallColor = 0
        self.nextBallLocation = [0, 0]
        self.score = 0
        self.ballColor = 0
        self.placing = False
        self.ballsPlaced = 0

    def PickerPress(self,instance):
        app.BallPressedColor = instance.background_normal
        app.ballColor = instance.background_normal[9]
        app.BallPressedDown = instance.background_down
        instance.disabled = True
        instance.background_disabled_normal = instance.background_down
        print(app.ballColor)

    def BoardPlace(self,instance):
        
        if app.ballColor != 0:
            #instance.background_normal = app.BallPressedColor
            #instance.background_down = app.BallPressedDown
            location = BoardLogic.determineColRow((),instance.id,board_size)
            print("\n~~~~~~~~\n")
            print(location[0], location[1], int(app.BallPressedColor[9]))

            
            self.boardData.putBallInSpot(location[0], location[1], int(app.BallPressedColor[9]))
           
            self.screen.boardGrid.draw(board_size, self.boardData.GetBoardData())
            print(instance.id)
            print(BoardLogic.determineColRow((),instance.id,board_size))
            app.ballColor = 0
            app.ballsPlaced += 1
            if app.ballsPlaced == 3:
                self.boardData.FindEmpty(self.boardData)
                self.boardData.ComputerBalls()
                self.screen.boardGrid.draw(board_size, self.boardData.GetBoardData())

                app.ballsPlaced = 0
        else:
            # popup = Popup(title='Error',
            #     content=Button(text='No ball selected!'),
            #     size_hint=(None, None), size=(300, 200))
            # popup.open()
            # show some error message to user
            pass

            
    # def RemovePickBall(self,instance):
    #     print(app.ball)
    #     self.root.remove_widget(self.root.ids[app.ball])

    def build(self):
        self.screen = PlayingScreen()
        return self.screen


app = GameApp()

app.run()

