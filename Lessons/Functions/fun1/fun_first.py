def team_selection(team):
    """ Функция запрашивает у пользователя хочет ли он выбрать состав
    """

    while True:
        answer = input("Готовы ли вы выбрать состав?: ")
        if answer == 'no' or 'нет':
            break
        myteam = input(f"cегодня в команде {team} в основном сотставе играют: ")
        squad = myteam.split()
        for player in squad:
            print(f"Поздравляю {player}, вы сегодня играете в основном составе!!!")
team_selection('ajax')
