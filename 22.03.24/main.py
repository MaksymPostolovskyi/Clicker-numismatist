from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock

class MenuScreen (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        
class GameScreen (Screen):
    points = NumericProperty(0)
    def __init__(self, **kw):
        super().__init__(**kw)
    def on_enter(self, *args):
        self.ids.coin.new_coin() 
        return super().on_enter(*args)
    
    
#    def on_leave(self, *args):
#            App.get_running_app().coin_count = self.points
#
#    def on_enter(self, *args):
#        self.points = App.get_running_app().coin_count
    
 
        

class ShopScreen(Screen):
    pass
#     autoclicker_price = 10
    
#    def buy_autoclicker(self):
#        print("На даний момент функція не працює, приносимо свої вибачення")
#         game_screen = self.manager.get_screen('game')
#         if game_screen.points >= self.autoclicker_price:
#             game_screen.points -= self.autoclicker_price
#             autoclicker = Autoclicker(game_screen)
#             autoclicker.start_autoclick()
#             print("Автоклікер куплено")
#         else:
#             print("Недостатньо монет для покупки")
    def buy_autoclicker(self):
            print("На даний момент функція не працює, приносимо свої вибачення")
        
class Coin(Image):
    
    LEVELS = ['coin1', 'coin2','coin3']

    COIN = {
    'coin1': {"source": 'assets/images/1.png', 'hp': 30},
    'coin2': {"source": 'assets/images/2.png', 'hp': 40},
    'coin3': {"source": 'assets/images/3.png', 'hp': 50},

        }  
    
    is_anim = False
    hp = None
    coin = None
    coin_index = 0
    
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            
            self.parent.parent.parent.points += 1
            self.hp -= 1
            
            if self.hp <=0:
                   self.new_coin()
            
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y=y-5, duration=0.02) + \
                Animation(x=x, y=y, duration=0.02)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)
    
    
    def new_coin(self):
        self.coin = self.LEVELS[randint(0, len(self.LEVELS)-1)]
        self.source = self.COIN[self.coin]['source']
        self.hp = self.COIN[self.coin]['hp']
        print(self.COIN[self.coin]['source'])
        print(self.COIN[self.coin]['hp'] )

            
        
class MainApp (App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coin_count = 0

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen (name='menu'))
        sm.add_widget(GameScreen (name='game'))

        sm.add_widget(ShopScreen (name='shop'))
        return sm
        
    if platform != 'android':
        Window.size = (400, 600)
        Window.left = +500
        Window.top = 100
        


MainApp().run()

        
