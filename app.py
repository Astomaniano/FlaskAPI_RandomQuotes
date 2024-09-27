from flask import Flask, render_template, request
import requests
from googletrans import Translator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Запрос к публичному API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
    else:
        quote = "Не удалось получить цитату. Попробуйте позже."
        author = ""

    # Создание объекта переводчика
    translator = Translator()

    # Перевод цитаты и автора на русский язык
    translated_quote = translator.translate(quote, dest='ru').text
    translated_author = translator.translate(author, dest='ru').text

    return render_template('index.html', quote=translated_quote, author=translated_author)

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
