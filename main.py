import json
import random
from questions import Questions


def main():

    def forms_questions(file):
        """Формирование списка вопросов из файла question.json, каждый элемент списка
        экземпляр класса Questions """
        questions = []  # заготовка вопросов
        with open(file, 'r', encoding="utf-8") as file:
            list_of_questions = json.load(file)
            for each_question in list_of_questions:
                questions.append(Questions(each_question["q"], each_question["d"], each_question["a"]))
        random.shuffle(questions)  # перемешиваем список вопросов
        return questions

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
    print('**-------------**')

    points = 0  # сумма балов за игру

    questions = forms_questions('question.json')

    for attempt in range(len(questions)):
        print(questions[attempt].build_question())
        user_answer = input()
        questions[attempt].is_correct(user_answer)  # при правильном ответе переписываем параметр is_correct -  True

        if questions[attempt].is_question:
            print(questions[attempt].build_positive_feedback())
            points += questions[attempt].points  # собираем баллы
        else:
            print(questions[attempt].build_negative_feedback())

    counts_results(questions)


if __name__ == '__main__':
    main()
