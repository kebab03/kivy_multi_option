from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.graphics import Color, Rectangle
 
class GreenLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 0, 1)  # Green color
            self.rect = Rectangle(pos=self.pos, size=self.size)
 
    def on_size(self, *args):
        self.rect.size = self.size
 
    def on_pos(self, *args):
        self.rect.pos = self.pos
 
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
 
        # List of names and options for input labels
        items = [
            {'name': 'John', 'options': ['Option 1', 'Option 2', 'Option 3']},
            {'name': 'Mary', 'options': ['Option A', 'Option B', 'Option C']},
            {'name': 'Robert', 'options': ['Choice X', 'Choice Y', 'Choice Z']},
            {'name': 'Emily', 'options': ['Alternative 1', 'Alternative 2', 'Alternative 3']}
        ]

        # Dictionary to store references to TextInput widgets
        text_inputs = {}
 
        for item in items:
            # Label for each item
            label = GreenLabel(text=item['name'], font_size='24sp')
            layout.add_widget(label)
            
            # Generate the name for TextInput
            ninpt = "input_" + item['name']
 
            # TextInput for each item
            input_widget = TextInput(multiline=False, font_size='24sp')
            layout.add_widget(input_widget)
 
            # Store the reference to TextInput in the dictionary
            text_inputs[ninpt] = input_widget
 
            # DropDown widget for options
            dropdown = DropDown()
 
            for option in item['options']:
                btn = Button(text=option, size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn, text_input=input_widget, option=option: self.select_item(text_input, option))
                dropdown.add_widget(btn)
 
            # Button to open the dropdown
            dropdown_button = Button(text='Choose Option')
            dropdown_button.background_color = (1, 0, 0, 1)  #
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
