from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class ToDoListApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=5, padding=10)

        # Title
        self.title_label = Label(text="To-Do List", font_size=24, size_hint=(1, 0.1))
        self.layout.add_widget(self.title_label)

        # Task Input
        self.task_input = TextInput(hint_text="Enter task...", size_hint=(1, 0.1))
        self.layout.add_widget(self.task_input)

        # Add Task Button
        self.add_button = Button(text="Add Task", size_hint=(1, 0.1), background_color=(0, 0.5, 1, 1))
        self.add_button.bind(on_press=self.add_task)
        self.layout.add_widget(self.add_button)

        # Task List
        self.task_list_layout = BoxLayout(orientation='vertical', spacing=2)
        self.scroll = ScrollView(size_hint=(1, 0.7))
        self.scroll.add_widget(self.task_list_layout)
        self.layout.add_widget(self.scroll)

        return self.layout

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task_label = Label(text=task_text, font_size=18, size_hint=(1, None), height=40)
            self.task_list_layout.add_widget(task_label)
            self.task_input.text = ""


ToDoListApp().run()
