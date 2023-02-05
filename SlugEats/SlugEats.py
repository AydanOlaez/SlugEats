import pandas as pd
import datetime
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class SlugPointCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.amount_text = TextInput(hint_text='Enter amount of remaining slug points', multiline=False, font_size=60)
        self.add_widget(self.amount_text)
        self.amount_text.bind(on_text_validate=self.calculate_budget)
        self.result_label = Label(size_hint=(1.0, 1.0), halign="left", valign="middle", font_size=60)
        self.add_widget(self.result_label)

    def calculate_budget(self, instance):
        end_date = datetime.datetime(2023, 3, 31)
        current_date = datetime.datetime.now()
        delta = end_date - current_date
        amount = float(self.amount_text.text)
        daily_amount = amount / delta.days
        weekly_amount = daily_amount * 7
        self.result_label.text = 'You must spend {:.2f} slug points per day and {:.2f} slug points per week to run out by March 31st 2023.'.format(daily_amount, weekly_amount)

class PersonInformation(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20

        # name
        self.add_widget(Label(text="Name", font_size=40))
        self.name = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.name)

        # weight
        self.add_widget(Label(text="Weight (lbs)", font_size=40))
        self.weight = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.weight)

        # daily calorie goal
        self.add_widget(Label(text="Daily calorie goal", font_size=40))
        self.daily_calorie_goal = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.daily_calorie_goal)

        # daily protein goal
        self.add_widget(Label(text="Daily protein goal (g)", font_size=40))
        self.daily_protein_goal = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.daily_protein_goal)

        # sex
        self.add_widget(Label(text="Sex", font_size=40))
        self.sex = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.sex)

        # preferred dining hall
        self.add_widget(Label(text="Preferred dining hall", font_size=40))
        self.preferred_dining_hall = TextInput(text="", font_size=50, halign="center", padding_y=30)
        self.add_widget(self.preferred_dining_hall)

class DataFrameSchedule(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (1, 1)
        self.padding = 100

        df = pd.read_csv('indexed_hours.csv')
        col_names = df.columns.tolist()
        
        header = BoxLayout(size_hint=(1, None), height=200)
        for col_name in col_names:
            header.add_widget(Label(text=col_name, size_hint=(1, 1)))
        self.add_widget(header)

        for i in range(len(df)):
            row = BoxLayout(size_hint=(1, None), height=200)
            for j in range(len(df.columns)):
                row.add_widget(Label(text=str(df.iloc[i, j]), size_hint=(1, 1)))
            self.add_widget(row)

class DataFrameNutrition(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint = (1, 1)
        self.padding = 30
        self.spacing = 50

        label = Label(text="Current Menu: ", size_hint=(1, 0.1), font_size=40)
        self.add_widget(label)

        df = pd.read_csv('nutrition_facts.csv')
        col_names = df.columns.tolist()
        
        header = BoxLayout(size_hint=(1, None), height=200, padding=50, spacing=10)
        for col_name in col_names:
            header.add_widget(Label(text=col_name, size_hint=(1, 1)))
        self.add_widget(header)

        for i in range(len(df)):
            row = BoxLayout(size_hint=(1, None), height=200, padding=50, spacing=10)
            for j in range(len(df.columns)):
                row.add_widget(Label(text=str(df.iloc[i, j]), size_hint=(1, 1)))
            self.add_widget(row)


class SlugEatsApp(App):
    def build(self):
        root = TabbedPanel()
        root.add_widget(SlugPointCalculator())
        root.add_widget(PersonInformation())
        return root

if __name__ == '__main__':
    SlugEatsApp().run()
