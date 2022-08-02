import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from tenByTengrid import BigGrid
from random import randint
from kivy.uix.boxlayout import BoxLayout


class BigGrid(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        colorList = [(1, 0, 0, 0.7), (0, 1, 0, 0.7), (0, 0, 1, 0.7)]
        print("bess")
        for i in range(100):
            b = Button(background_normal = '', background_color = colorList[randint(0,2)])
            self.add_widget(b)

class GameApp(App):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def build(self):
        return BigGrid()


app = GameApp()

app.run()