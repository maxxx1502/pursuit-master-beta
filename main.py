from kivy.app import App
from kivy.uix.widget import Widget
from random import random as r
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.window import Keyboard
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

W,H = 700, 700
TILE = 45
GAME_RES = W * TILE, H * TILE

class GridGame(Widget):
    # def download_player(self, wid, TILE_W, TILE_H):
    #     with wid.canvas:
    #         img = Image(source = "res/player.png", size_hint = (.5, .5), pos_hint = {"center_x": 50, "center_y": 50})
    #         return img

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(
            BoxLayout())  # Добавление BoxLayout в качестве родительского виджета

        self.img = Image(
            source='res/player.png')  # Замените на путь к вашему изображению

        self.add_widget(self.img)

        self.key_pressed = set()
        self.speed = 10

        self.update_event = Clock.schedule_interval(self.update, 1.0 / 60.0)
        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)

        self.key_codes = {
            Keyboard.keycodes['up']: 'up',
            Keyboard.keycodes['down']: 'down',
            Keyboard.keycodes['left']: 'left',
            Keyboard.keycodes['right']: 'right'
        }

    def update(self, dt):
        if 'up' in self.key_pressed:
            self.img.y += self.speed
        if 'down' in self.key_pressed:
            self.img.y -= self.speed
        if 'left' in self.key_pressed:
            self.img.x -= self.speed
        if 'right' in self.key_pressed:
            self.img.x += self.speed

    def on_key_down(self, window, key, *args):
        self.key_pressed.add(self.key_codes.get(key, ''))

    def on_key_up(self, window, key, *args):
        self.key_pressed.remove(self.key_codes.get(key, ''))


class PursuitGame(Widget):
    my_grid = GridGame()


class PursuitApp(App):
    def build(self):
        Window.bind(on_resize = self.on_window_resize)
        return PursuitGame()
    def on_start(self):
        self._width = self.root.ids["game_layout"].width
        self._height = self.root.ids["game_layout"].height
        self._width_glass = self._width / 20 * 12
        self._height_glass = self._height -40
        TILE_W = self._width_glass / W
        TILE_H = self._height_glass / H


        # self.root.my_grid.download_player(self.root.ids["game_layout_box"], TILE_W, TILE_H)

    def on_window_resize(self, window, width, height):
        self._width = self.root.ids["game_layout"].width
        self._height = self.root.ids["game_layout"].height
        self._width_glass = self._width / 20 * 12
        self._height_glass = self._height - 40
        TILE_W = self._width_glass / W
        TILE_H = self._height_glass / H

        self.root.ids["game_layout_box"].canvas.clear()
        self.root.my_grid.download_player(self.root.ids["game_layout_box"], TILE_W, TILE_H)

if __name__ == "__main__":
    PursuitApp().run()

