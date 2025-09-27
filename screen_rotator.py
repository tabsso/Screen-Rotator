#!/usr/bin/env python3

import sys
import os
import threading
import keyboard
import rotatescreen
from PIL import Image
import pystray

class ScreenRotator:
    def __init__(self):
        self.screen = rotatescreen.get_primary_display()
        self.is_rotated = False
        self.icon = None
        self.running = True
        
    def get_icon(self):
        """Загрузка иконки"""
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        icon_path = os.path.join(base_path, 'icon.png')
        
        if os.path.exists(icon_path):
            return Image.open(icon_path)
        else:
            # Создаем простую иконку если нет файла
            img = Image.new('RGB', (64, 64), color='blue')
            return img
    
    def rotate_screen(self, icon=None, item=None):
        """Поворот экрана"""
        if not self.is_rotated:
            self.screen.rotate_to(180)
            self.is_rotated = True
        else:
            self.screen.rotate_to(0)
            self.is_rotated = False
    
    def quit_app(self, icon, item):
        """Выход из приложения"""
        self.running = False
        if self.is_rotated:
            self.screen.rotate_to(0)
        self.icon.stop()
        sys.exit(0)
    
    def setup_tray(self):
        """Настройка трея"""
        menu = pystray.Menu(
            pystray.MenuItem(
                lambda text: "Повернут на 180°" if self.is_rotated else "Нормальное положение",
                self.rotate_screen,
                default=True
            ),
            pystray.MenuItem("Выход", self.quit_app)
        )
        
        self.icon = pystray.Icon(
            "ScreenRotator",
            self.get_icon(),
            "Screen Rotator",
            menu
        )
    
    def hotkey_listener(self):
        """Слушатель горячих клавиш"""
        keyboard.add_hotkey('ctrl+alt+r', self.rotate_screen)
        while self.running:
            keyboard.wait('ctrl+alt+q' if self.running else 'esc')
            if self.running:
                self.quit_app(None, None)
    
    def run(self):
        """Запуск приложения"""
        # Запускаем слушатель горячих клавиш в отдельном потоке
        hotkey_thread = threading.Thread(target=self.hotkey_listener, daemon=True)
        hotkey_thread.start()
        
        # Запускаем трей
        self.setup_tray()
        self.icon.run()

if __name__ == "__main__":
    app = ScreenRotator()
    app.run()