# rutube_comments

**rutube_comments** — это Python - оконное приложение для автоматического оставления комментариев и ответов под одним видео на определенной платформе. Бот также отслеживает время отправки комментариев и записывает это в тексте комментария. Программа позволяет гибко управлять списком видео и режимами работы.

## Основные возможности

- **Оставление комментариев**: Оставляет комментарий под видео, а затем отвечает на этот же комментарий по истечении времени, равному длительности видео.
- **Управление списком видео**: Возможность загрузки пользовательского списка видео, добавления или удаления видео вручную.
- **Режимы работы**:
  - Поочередная обработка видео.
  - Одновременное оставление пар комментариев под всеми видео из списка.
- **Отслеживание времени**: Программа добавляет в текст комментария текущие дату и время, указывая, когда было отправлено сообщение.
## Скриншот
![Image](https://github.com/user-attachments/assets/ea9e1dc3-9144-4368-8c14-858b1fc1fcec)
## Как это работает

1. **Загрузка видео**:
   - Пользователь может указать ссылки на видео вручную или загрузить их из заранее подготовленного файла.
   
2. **Выбор режима работы**:
   - По порядку: бот обрабатывает видео одно за другим.
   - Одновременный запуск: бот начинает работу со всеми видео сразу.

3. **Указание комментариев**:
   - Бот оставляет начальный комментарий и со временем отвечает под ним, синхронизируясь с длительностью видео.

4. **Добавление времени**:
   - Программа автоматически включает в каждый комментарий отметку времени, чтобы отслеживать, когда именно комментарий был опубликован.

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/Yambai/rutube_comments.git
   cd rutube_comments
   ```

2. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Настройте параметры программы в конфигурационном файле `config.yaml` (если он имеется).

## Запуск

Запустите программу, выполнив:

```bash
python main.py
```

Далее следуйте инструкциям для настройки списка видео, выбора режима работы и других параметров.

## Требования

- Python 3.10+
- Необходимые модули указаны в файле `requirements.txt`.

## Пример использования

Пример комментария, публикуемого программой:
Первый комментарий:
```
21:07 07.02.2023
```
И ответ на первый комментарий:
```
21:47 07.02.2023
```
