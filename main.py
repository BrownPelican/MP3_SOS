from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader

class Mp3SOS(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "SOS"

    def build(self):
        self.title = "SOS"
        self.img = Image(source='./images/SOS.png')
        self.btn = Button(background_normal='./images/SOS.png')
        self.btn.bind(on_press=self.callback)

        superBox = BoxLayout(orientation='vertical')

        BL = BoxLayout(orientation='horizontal')
        BL.add_widget(self.btn)

        superBox.add_widget(BL)

        self.playSound()

        return superBox

    def callback(self, event):
        self.playSound()

    def playSound(self):
        self.soundFile = './sounds/SOS.mp3'
        self.soundLoader = SoundLoader.load(self.soundFile)

        i = 0
        run = True
        while run:
            if i < 10:
                self.soundLoader.play()
            else:
                run = False
            i += 1

if __name__ == '__main__':
    Mp3SOS().run()
