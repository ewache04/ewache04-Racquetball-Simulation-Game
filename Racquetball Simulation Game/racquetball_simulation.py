'''
Author: Jeremiah E. Ochepo
Last Edited: 2/15/2020 (7 PM)
Description: Racquetball Simulation
'''

import time
from random import random


class RacquetballSimulation:
    def __init__(self, *args, **kwargs):
        self.active_flag = True
        self.service = 'A'
        self.serve_A = 0
        self.serve_B = 0
        self.score_A = 0
        self.score_B = 0
        self.win_A = 0
        self.win_B = 0

    @staticmethod
    def print_intro():
        txt = 'Racquetball Simulation Game'
        print(txt)

    def get_inputs(self):
        # Returns the three simulation parameters probA, probB and n
        self.prob_A = float(input('Enter probability Player A wins a serve: '))
        self.prob_B = float(input('Enter probability Player B wins a serve: '))
        self.num_games = int(input('Enter number of games to be simulated: '))

    def sim_n_games(self):
        self.start_time = time.time()
        print('Game Summary')

        while self.active_flag:
            if self.service == 'A':
                self.serve_A += 1

                if random() < self.prob_A:
                    self.score_A += 1
                else:
                    self.service = 'B'
            else:
                self.serve_B += 1

                if random() < self.prob_B:
                    self.score_B += 1
                else:
                    self.service = 'A'

                if self.score_A == 15:
                    self.win_A += 1
                elif self.score_B == 15:
                    self.win_B += 1

                self.print_game_summary()

                if self.score_A == 15 or self.score_B == 15:
                    self.num_games -= 1

                    if self.num_games == 0:
                        print('Game Over\n\n')
                        self.active_flag = False
                    else:
                        self.serve_A = self.serve_B = 0
                        self.score_A = self.score_B = 0
                        print('New Game\n')

    def print_game_summary(self):
        print(f'Service A: {self.serve_A} service B: {self.serve_B}')
        print(f'Score A: {self.score_A} Score B: {self.score_B}')
        print(f'Win A: {self.win_A} Win B: {self.win_B}\n\n')


# Main execution
game_info = RacquetballSimulation()
game_info.print_intro()
game_info.get_inputs()
game_info.sim_n_games()
