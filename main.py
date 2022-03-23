"""
Simple whatsapp UI clone with Python, kivy and 
it's material design framework KivyMD
"""

#modules imports
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
from kivy.core.window import Window
from kivy.lang import Builder
#resize window
Window.size = (310,510)
#'/home/chidera/Videos/Rumble (2021)@Betty Tv.mp4'
#tab class
class Tab(FloatLayout, MDTabsBase):
    pass

#app classs
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        return Builder.load_file("main.kv")
    def on_start(self):
        # Set colors
        self.theme_cls.primary_palette = 'Green'

        # add messages
        self.new_message("Chidera Onwurah", "Hello bro", "avatar.png")
        self.new_message("Mum", "Am fine", "avatar.png")
        self.new_message("Emmanuel O", "Lol", "avatar.png")
        self.new_message("Kelvin", "Amazing", "avatar.png")
        self.new_message("Coder", "Gee", "avatar.png")
        self.new_message("Jane", "really ??", "avatar.png")
        self.new_message("Franklin", "Still trashing the keyboards", "avatar.png")

    def new_message(self, name, message, image_name):
        new_message = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_message.add_widget(ImageLeftWidget(source=image_name))
        self.root.ids.list.add_widget(new_message)


    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        pass

if __name__ == "__main__":
    MainApp().run()



