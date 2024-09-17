import random
import sys


class RPS:
    def __init__(self):
        print('Welcome to RSP 9000!')

        self.moves: dict = {'rock': '🥌', 'paper': '📜', 'scissors': '✂'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('Rock, paper, scissors? >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('----')

    @staticmethod
    def check_moves(user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It\'s a tie!')
        elif ((user_move == 'rock' and ai_move == 'scissors')
              or (user_move == '' and ai_move == 'rock')
              or (user_move == 'scissors' and ai_move == 'paper')):
            print('You Win!')
        else:
            print('AI Wins!')


if __name__ == "__main__":
    rps = RPS()
    while True:
        rps.play_game()
