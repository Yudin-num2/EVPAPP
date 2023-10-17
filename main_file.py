import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('signin.kv')

class EuroplastApp(App):
    def build(self):
            return AuthorizationPage()




class AuthorizationPage(Screen):

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == "" or passw == "":
            info.text = '[color=#FF0000]Неверный логин или пароль[/color]'
            return False
        else:
            if uname == "admin" and passw == "admin":
                info.text= '[color=#00FF00]Вход выполнен![/color]'
                return True
            else:
                info.text = '[color=#FF0000]IНеверный логин или пароль[/color]'
                return False


class MainPage(Screen):
    def func_mainpage(self):
        user = self.ids.username_field


if __name__ == '__main__':
    EuroplastApp().run()