#!/usr/bin/env python3
"""
Скрипт для сборки ScreenRotator в exe файл
"""

import os
import sys
import subprocess

def build():
    print("=" * 40)
    print("  Screen Rotator Build Script")
    print("=" * 40)
    print()
    
    # Установка зависимостей
    print("[1] Установка зависимостей...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print()
    print("[2] Создание EXE файла...")
    
    # Параметры сборки
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",           # Один файл
        "--windowed",          # Без консоли
        "--name", "ScreenRotator",
        "--add-data", "icon.png;." if os.name == 'nt' else "icon.png:.",
    ]
    
    # Добавляем иконку если есть
    if os.path.exists("icon.ico"):
        cmd.extend(["--icon", "icon.ico"])
    
    cmd.append("screen_rotator.py")
    
    # Запускаем сборку
    subprocess.run(cmd)
    
    print()
    print("=" * 40)
    print("  Сборка завершена!")
    print("  EXE файл: dist/ScreenRotator.exe")
    print("=" * 40)

if __name__ == "__main__":
    build()