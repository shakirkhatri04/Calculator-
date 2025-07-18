from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyCalculator(BoxLayout):
    def calculate(self):
        try:
            self.ids.result.text = str(eval(self.ids.input.text))
        except:
            self.ids.result.text = "Error"

class CalculatorApp(App):
    pass

if __name__ == '__main__':
    CalculatorApp().run()
