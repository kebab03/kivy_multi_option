
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle

class CustomTextInput(TextInput):
    def __init__(self, background_color=(0, 1, 0.4, 0), foreground_color=(1, 0, 0.5, 1), **kwargs):
        super().__init__(**kwargs)
        self.background_color = background_color
        self.foreground_color = foreground_color


class CustomLabel(Label):
    def __init__(self, color=(1, .4, 0.2, 1), buttons=None, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.buttons = buttons
        if self.buttons:
            for button in self.buttons:
                self.add_widget(button)

    def on_size(self, *args):
        self.rect.size = self.size

    def on_pos(self, *args):
        self.rect.pos = self.pos



class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        items = [
            {'name': 'John', 'options': ['Option 1', 'Option 2', 'Option 3'], 'color': (1, 0, 0, 1)},
            {'name': 'Mary', 'options': ['Option A', 'Option B', 'Option C'], 'color': (0, 1, 0, 1),
             'buttons': [Button(text='Button 1'), Button(text='Button 2')]},
            {'name': 'Robert', 'options': ['Choice X', 'Choice Y', 'Choice Z'], 'color': (0, 0, 1, 1)},
            {'name': 'Emily', 'options': ['Alternative 1', 'Alternative 2', 'Alternative 3'], 'color': (1, 0, 1, 1)}
        ]

        text_inputs = {}

        for item in items:
            label = CustomLabel(text=item['name'], font_size='24sp', color=item['color'], buttons=item.get('buttons'))
            layout.add_widget(label)

            ninpt = "input_" + item['name']
            input_widget = CustomTextInput(multiline=False, font_size='24sp')
            layout.add_widget(input_widget)

            text_inputs[ninpt] = input_widget

            dropdown = DropDown()

            for option in item['options']:
                btn = Button(text=option, size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn, text_input=input_widget, option=option: self.select_item(text_input, option))
                dropdown.add_widget(btn)

            dropdown_button = Button(text='Choose Option')
            dropdown_button.background_color = (1, 0, 0, 1)
            dropdown_button.font_size = '24sp'
            dropdown_button.bind(on_release=dropdown.open)
            dropdown.bind(on_select=lambda instance, x, text_input=input_widget: setattr(dropdown_button, 'text', x) or self.select_item(text_input, x))
            layout.add_widget(dropdown_button)

            dropdown.bind(on_select=lambda instance, x, text_input=input_widget: setattr(text_input, 'text', x))

        return layout

    def select_item(self, input_widget, item_text):
        input_widget.text = item_text

if __name__ == '__main__':
    MyApp().run()
