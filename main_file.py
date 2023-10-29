import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from database import check_auth, get_user
import kivy.properties

Builder.load_file('signin.kv')


class AuthorizationPage(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user = self.ids.username_field
        self.info = self.ids.info

    def validate_user(self):
        if check_auth(self.login):
            self.info.text = '[color=#00FF00]Вход выполнен[/color]'
            self.manager.current = 'main_page'
        else:
            self.info.text = '[color=#FF0000]Неверный логин или пароль[/color]'

class MainPage(AuthorizationPage):
    def __init__(self, **kw):
        super().__init__(**kw) 


class EuroplastApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AuthorizationPage(name='auth_page'))
        sm.add_widget(MainPage(name='main_page'))
        return sm

if __name__ == '__main__':
    EuroplastApp().run()