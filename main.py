from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class HisabiApp(App):
    def build(self):
        self.title = "حسابي"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        self.layout.add_widget(self.result)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, font_size=24)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.layout.add_widget(h_layout)
            
        return self.layout

    def on_button_press(self, instance):
        text = instance.text
        if text == 'C':
            self.result.text = ""
        elif text == '=':
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = "خطأ"
        else:
            self.result.text += text

if __name__ == '__main__':
    HisabiApp().run()
