from abc import ABC,abstractmethod

class Player(ABC):
    def __init__(self, name, fig) -> None:
        self.name = name
        self.fig = fig

    @abstractmethod
    def make_move(self):
        pass

class UserPlayer(Player):

    def make_move(self):
        return input('Твой ход {}:'.format(self.name))


class PlayBoard:
    data = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

    step_count = 0

    def print(self):
        for row in self.data:
            print(*row, sep='|')
            print('-' * (len(self.data) * 2))

    def set(self, row, column, fig):
        self.data[row][column] = fig
        self.step_count += 1

    def rows(self):
        return self.data

    def columns(self):
        copy_arr = [['','',''],['','',''],['','','']]
        for row_i in range(len(self.data)):
            for col_i in range(len(self.data[row_i])):
                copy_arr[row_i][col_i] = self.data[col_i][row_i]
        return copy_arr

    def diagonals(self):
        left_d = [self.data[0][0], self.data[1][1], self.data[2][2]]
        right_d = [self.data[2][0], self.data[1][1], self.data[0][2]]
        return [left_d, right_d]


class Application:
    X = 'X'
    O = 'O'

    MAPPING = {
        '7': {
            'coordinates': [0, 0],
            'used': False
        },
        '8':  {
            'coordinates': [0, 1],
            'used': False
        },
        '9':  {
            'coordinates': [0, 2],
            'used': False
        },
        '4':  {
            'coordinates': [1, 0],
            'used': False
        },
        '5':  {
            'coordinates': [1, 1],
            'used': False
        },
        '6': {
            'coordinates': [1, 2],
            'used': False
        },
        '1': {
            'coordinates': [2, 0],
            'used': False
        },
        '2':  {
            'coordinates': [2, 1],
            'used': False
        },
        '3': {
            'coordinates': [2, 2],
            'used': False
        },
    }

    WIN_POINTS = 3

    def __init__(self) -> None:
        self.board = PlayBoard()
        self.players = []

    def start(self):
        self.__setup_players()
        self.__start_game()


    def __setup_players(self):
        x_player = input('{} играет:'.format(self.X))
        o_player = input('{} играет:'.format(self.O))

        self.players = [UserPlayer(x_player, self.X), UserPlayer(o_player, self.O)]

    def __get_next_player(self, curr_player: Player):
        x_player = self.players[0]
        o_player = self.players[1]
        return o_player if curr_player.fig == self.X else x_player

    def __get_coordinates(self, curr_player: Player):
        cell = None
        while cell is None:
            key = curr_player.make_move()
            if key not in self.MAPPING:
                print('Не корректная клавиша.')
                continue
            if self.MAPPING[key]['used']:
                print('Занято')
            else:
                cell = self.MAPPING[key]
        cell['used'] = True
        return cell['coordinates']

    def __define_winner(self) -> bool:
        has_winner = False
        if self.board.step_count < 5:
            return has_winner
        for p in self.players:
            if self.__is_player_win(p):
                has_winner = True
                print('Победа игрока:', p.name)
                break
        if (self.board.step_count == 9 and not has_winner):
            print('Ничья.')
            return True
        return has_winner

    def __is_player_win(self, player: Player):
        return any(
            [
                self.__all_rows_match_fig(self.board.rows(), player.fig),
                self.__all_rows_match_fig(self.board.columns(), player.fig),
                self.__all_rows_match_fig(self.board.diagonals(), player.fig),
            ])

    def __all_rows_match_fig(self, rows, fig):
        conditions = []
        for row in rows:
            conditions.append(len([r for r in row if r == fig]) == self.WIN_POINTS)
        return any(conditions)

    def __start_game(self):
        self.board.print()
        curr_player = self.players[0]
        game_over = False
        while not game_over:
            row, column = self.__get_coordinates(curr_player)
            self.board.set(row, column, curr_player.fig)
            self.board.print()
            curr_player = self.__get_next_player(curr_player)
            game_over = self.__define_winner()
    