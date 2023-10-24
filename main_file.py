import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

from database import check_auth, get_user

Builder.load_file('signin.kv')

class EuroplastApp(App):
    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(AuthorizationPage(name='auth_page'))
        sm.add_widget(MainPage(name='main_page'))
        return sm


class AuthorizationPage(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.user = self.ids.username_field
        self.info = self.ids.info


    def validate_user(self):
        login = self.user.text
        if check_auth(login):
            self.info.text = '[color=#00FF00]Вход выполнен[/color]'
            self.manager.current = 'main_page'
        else:
            self.info.text = '[color=#FF0000]Неверный логин или пароль[/color]'


class MainPage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def func_mainpage(self):
        info = self.ids.info
        name, surname = get_user(self.ids.username_field)
        print(name, surname)

        

if __name__ == '__main__':
    EuroplastApp().run()