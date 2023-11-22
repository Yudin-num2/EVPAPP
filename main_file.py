import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from database import check_auth, get_user
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file('signin.kv')


class AuthorizationPage(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.username = self.ids.username_field
        self.passw = self.ids.pwd_field
        self.info = self.ids.info

    def validate_user(self):
        if check_auth(self.username.text, self.passw.text):
            self.info.text = '[color=#00FF00]Вход выполнен[/color]'
            self.manager.current = 'main_page'
        else:
            self.info.text = '[color=#FF0000]Неверный логин или пароль[/color]'


class MainPage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class MoldSockets(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def print_testt(self):
        print('Button is pressed')

    
class Application(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        layout = GridLayout(
                spacing=10,
                padding=10,
                cols=4)
        for i in range(48):
            button = Button(
                text=f'{i+1}',
                font_size=15,
                background_normal='Images/Button/BtOn.png'
                )
            layout.add_widget(button)
    def create_widget(self, instance):
        self.remove_widget(instance)
        layout = BoxLayout(
            size_hint=(.5,.5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )    
        layout.canvas.add(Color(1., 1., 0))
        layout.canvas.add(Rectangle(size=layout.size))
        button_1 = Button(
            text='🟨 Облой',
            on_press= self.set_yellow()
        )

    def set_yellow(self, instance):
        original_button = self.children[-2].children[0]
        print(self.children)
        original_button.backgroun_color = (.98, 1, 0, 1)



class SocketsT2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT3(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT4(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT5(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT6(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT7(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)



class EuroplastApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(AuthorizationPage(name='auth_page'))
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(MoldSockets(name='mold_sockets'))
        sm.add_widget(Application(name='application'))
        sm.add_widget(SocketsT1(name='s1'))
        sm.add_widget(SocketsT2(name='s2'))
        sm.add_widget(SocketsT3(name='s3'))
        sm.add_widget(SocketsT4(name='s4'))
        sm.add_widget(SocketsT5(name='s5'))
        sm.add_widget(SocketsT6(name='s6'))
        sm.add_widget(SocketsT7(name='s7'))
        return sm

if __name__ == '__main__':
    EuroplastApp().run()