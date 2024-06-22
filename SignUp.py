from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class SignUp(App):
    def build(self):
        # why gridlayout
        self.window = GridLayout()

        self.window.cols = 1

        self.window.size_hint = (0.6, 0.7)

        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # adding widgets header
        self.heading = Label(
            text="SIGN UP",
            font_size=38,
            color="#00ffab"
        )
        self.window.add_widget(self.heading)

        # to say hi
        self.greeting = Label(
            text="",
            font_size=38,
            color="#00ffab"
        )
        self.window.add_widget(self.greeting)

        # lable
        self.name_tag = Label(
            text="Name",
            color="#00ffab")
        self.window.add_widget(self.name_tag)

        # input field
        self.name_field = TextInput(
            multiline=False,
            padding_y=(30, 30),
            size_hint=(1, 0.8))
        self.window.add_widget(self.name_field)

        # lable
        self.email_tag = Label(
            text="Email",
            color="#00ffab")
        self.window.add_widget(self.email_tag)

        self.email_field = TextInput(
            multiline=False,
            padding_y=(30, 30),
            size_hint=(1, 0.7)
        )
        self.window.add_widget(self.email_field)

        # lable
        self.password_tag = Label(
            text="Password",
            color="#00ffab"
        )
        self.window.add_widget(self.password_tag)

        self.password_field = TextInput(
            multiline=False,
            padding_y=(30, 30),
            size_hint=(1, 0.7))
        self.window.add_widget(self.password_field)

        self.button = Button(
            text="Sign Up",
            background_color="#00ffab",
            size_hint=(1, 0.5))
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button,)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Welcome " + self.name_field.text + " you have signed up"


if __name__ == "__main__":
    SignUp().run()
