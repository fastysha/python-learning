import emoji
from termcolor import colored

STONE = emoji.emojize(':punch:', language='alias')
CUT = emoji.emojize(':v:',  language='alias')
SHEET = emoji.emojize(':hand:',  language='alias')

WIN = 1
LOSS = -1
DRAW = 0

class GameShape:
    def __init__(self, name) -> None:
        self.name = name

    def compare(self, other):
        pass
###

class Stone(GameShape):
    def __init__(self) -> None:
        super().__init__(STONE)

    def compare(self, other: GameShape):
        if other.name == CUT:
            return WIN
        elif other.name == SHEET:
            return LOSS
        return DRAW
###


class Cut(GameShape):
    def __init__(self) -> None:
        super().__init__(CUT)

    def compare(self, other: GameShape):
        if other.name == SHEET:
            return WIN
        elif other.name == STONE:
            return LOSS
        return DRAW
###


class Sheet(GameShape):
    def __init__(self) -> None:
        super().__init__(SHEET)

    def compare(self, other: GameShape):
        if other.name == STONE:
            return WIN
        elif other.name == CUT:
            return LOSS
        return DRAW

from abc import ABC,abstractmethod
class Player(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.win_count = 0
    
    def increment_win_count(self):
        self.win_count += 1

    @abstractmethod
    def get_key(self):
        pass

class UserPlayer(Player):
    def __init__(self) -> None:
        super().__init__('Человек')

    def get_key(self):
        return int(input('1 2 3\nк н б\n')) - 1


class BotPlayer(Player):
    def __init__(self) -> None:
        super().__init__('Бот')

    def get_key(self):
        import random
        return random.randint(0, 2)

data = [Stone(), Cut(), Sheet()]

def get_shape_by_key(key) -> GameShape:
    return data[key]

user = UserPlayer()
bot = BotPlayer()

print("""Hello! This is "Камень Ножницы Бумага"
1 - Камень
2 - Ножницы
3 - Бумага
""")

while True:

    user_shape = get_shape_by_key(user.get_key())
    bot_shape = get_shape_by_key(bot.get_key())

    print("{} vs {}".format(user_shape.name, bot_shape.name))

    res = user_shape.compare(bot_shape)

    if (res == 1):
        print(colored('Победа!', color='green', attrs=['bold']))
        user.increment_win_count()
    elif (res == -1):
        print(colored('Поражение...', color='red', attrs=['bold']))
        bot.increment_win_count()
    else:
        print(colored('Ничья.', attrs=['bold']))
    print('Счет: {} = {}'.format(user.win_count, bot.win_count))
    print('#' * 20)