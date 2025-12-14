from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        layout.add_widget(Label(text="Willkommen in meiner Kivy App!", font_size=30))
        layout.add_widget(TextInput(hint_text="Gib etwas ein...", font_size=20, size_hint=(1, 0.4)))
        layout.add_widget(Button(text="Klick mich!", font_size=24))
        return layout

if __name__ == "__main__":
    MyApp().run()
