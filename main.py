import json
import random


class Questions:

    def __init__(self, question, hard_question, answer, is_question=False, ask=None, points=0):
        self.question = question  # – текст вопроса
        self.hard_question = hard_question  # – сложность вопроса
        self.answer = answer  # – верный вариант ответа

        self.is_question = is_question  # – задан ли вопрос (по умолчанию False)
        self.ask = ask  # – ответ пользователя (по умолчанию None)
        self.points = points  # – баллы за вопрос (вычисляется в момент инициализации)

    # def get_points(self):
    #     """Возвращает int, количество баллов. Баллы зависят от сложности:
    #     за 1 дается 10 баллов, за 5 дается 50 баллов.
    #     """
    #     return int(self.hard_question * 10)

    def is_correct(self, answer):
        """Возвращает True, если ответ пользователя совпадает с верным
        ответом иначе False.
        """

        if answer == self.answer:
            self.is_question = True
            self.points = int(self.hard_question) * 10
        return self.is_question

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question}\nСложность: {self.hard_question}/{len(questions)}"

    def build_positive_feedback(self):
        """Возвращает: Ответ верный, получено __ баллов """
        return f"Ответ верный, получено {self.points} баллов"

    def build_negative_feedback(self):
        """Возвращает: Ответ неверный, верный ответ __  """
        return f"Ответ неверный, верный ответ - {self.answer}"


def counts_results(sp):
    """ Подводит итог игры. Сколько верных ответов из общего количества,
    количество набранных баллов"""
    correct_answer = 0
    for s in sp:
        if s.is_question:
            correct_answer += 1

    print("Вот и все!")
    print(f'Отвечено {correct_answer} вопросов из {len(sp)}')
    print(f'Набрано баллов: {points}')


print("Игра начинается!")
# формирование списка вопросов из файла question.json, каждый элемент списка экземпляр класса Questions
questions = []
with open('question.json', 'r', encoding="utf-8") as file:
    list_of_questions = json.load(file)
    for each_question in list_of_questions:
        questions.append(Questions(each_question["q"], each_question["d"], each_question["a"]))

points = 0  # сумма балов за игру
random.shuffle(questions)  # перемешиваем список вопросов

for a in range(len(questions)):
    print(questions[a].build_question())
    user_answer = input()
    questions[a].is_correct(user_answer)  # при правильном ответе переписываем параметр is_correct -  True

    if questions[a].is_question:
        print(questions[a].build_positive_feedback())
        points += questions[a].points  # собираем баллы
    else:
        print(questions[a].build_negative_feedback())

counts_results(questions)
