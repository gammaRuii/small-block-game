import kivy
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from tenByTengrid import BigGrid
from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (.5,.5,.5,0.7)

class BigGrid(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None,None)
        self.size = (dp(1200),dp(800))
        self.cols = 10

        print("bess")
        for i in range(100):
            color = randint(3,10)
            b = Button(background_normal = 'snapshot0{}.png'.format(color), background_down = 'snap0{}d.png'.format(color))
            self.add_widget(b)

class GameApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return BigGrid()


app = GameApp()

app.run()