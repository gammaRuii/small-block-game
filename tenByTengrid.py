from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from random import randint

class BigGrid(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 10
        colorList = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 0, 1)]
        for i in range(100):
            b = Button(background_color = colorList[randint(0,2)])