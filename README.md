# Screen Rotator

[English](README_EN.md) | **Русский**

Простая утилита для поворота экрана на 180° через горячие клавиши. Работает в системном трее Windows.

## Возможности

- 🔄 Поворот экрана на 180° и обратно
- ⌨️ Горячие клавиши: **Ctrl+Alt+R**
- 🔽 Минимизация в системный трей
- 📊 Отображение текущего статуса в трее
- 🚪 Выход через меню трея

## Установка

### Готовый exe (Releases)
Скачайте `ScreenRotator.exe` из раздела [Releases](../../releases)

### Из исходников
```bash
git clone https://github.com/yourusername/screen-rotator.git
cd screen-rotator
pip install -r requirements_build.txt
python screen_rotator.py
```

## Сборка в exe

```bash
python build.py
```

Готовый файл появится в `dist/ScreenRotator.exe`

## Требования

- Windows 10/11
- Python 3.7+ (только для запуска из исходников)

## Использование

1. Запустите приложение
2. Оно свернется в трей
3. **Ctrl+Alt+R** - перевернуть экран
4. Клик по иконке в трее - посмотреть статус
5. Правый клик → Выход - закрыть приложение

## Лицензия

MIT