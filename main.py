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
from kivy.uix.popup import Popup

__version__ = '0.0.1'

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
    
class Application(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SocketsT1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT3(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT4(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT5(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT6(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

    def open_popup(self, widget):
        popup = ColorPopup(widget)
        popup.open()

class SocketsT7(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.button = kw

class ColorPopup(Popup):
    def __init__(self, button, **kwargs):
        super().__init__(**kwargs)
        self.button = button

        layout = BoxLayout(orientation='vertical')
        red_button = Button(text='Поломка', on_release=self.change_color, background_color=(1, 0, 0, 1))
        blue_button = Button(text='Облой', on_release=self.change_color, background_color=(0, 0, 1, 1))
        yellow_button = Button(text='Недолив', on_release=self.change_color, background_color=(1, 1, 0, 1))

        layout.add_widget(red_button)
        layout.add_widget(blue_button)
        layout.add_widget(yellow_button)

        self.content = layout

    def change_color(self, instance):
        button_text = instance.text
        self.button.background_color = (1, 0, 0, 1) if button_text == 'Поломка' else \
                                        (0, 0, 1, 1) if button_text == 'Облой' else \
                                        (1, 1, 0, 1) if button_text == 'Недолив' else \
                                        (1, 1, 1, 1)
        self.dismiss()

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