class Questions:
    """
    Ответы на вопросы.
    """

    def __init__(self, question, hard_question, answer, is_question=False, ask=None, points=0):
        self.question = question  # – текст вопроса
        self.hard_question = hard_question  # – сложность вопроса
        self.answer = answer  # – верный вариант ответа

        self.is_question = is_question  # – задан ли вопрос (по умолчанию False)
        self.ask = ask  # – ответ пользователя (по умолчанию None)
        self.points = points  # – баллы за вопрос (вычисляется в момент инициализации)

    def is_correct(self, answer):
        """Возвращает True, если ответ пользователя совпадает с верным
        ответом иначе False. Устанавливает количество баллов за вопрос
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
        return f"Вопрос: \n{self.question}\nСложность: {self.hard_question}/5"

    def build_positive_feedback(self):
        """Возвращает: Ответ верный, получено __ баллов """
        return f"Ответ верный, получено {self.points} баллов\n"

    def build_negative_feedback(self):
        """Возвращает: Ответ неверный, верный ответ __  """
        return f"Ответ неверный, верный ответ - {self.answer}\n"
