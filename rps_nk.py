#!/usr/bin/env python3
import random
import pdb


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))


class ReflectPlayer(Player):
    def __init__(self):
        self.reflection = None

    def move(self):
        if self.reflection is None:
            return (random.choice(moves))
        else:
            return (self.reflection)

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)
        self.reflection = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.remember = None

    def move(self):
        if self.remember is None:
            return (random.choice(moves))
        else:
            location = moves.index(self.remember)
            next_location = (location + 1) % 3
            return (moves[next_location])

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)
        self.remember = my_move


class HumanPlayer(Player):
    def move(self):
        while True:
            words = input("Rock, paper, scissors?  >  ")
            if str.lower(words) in moves:
                return (words)
                break
            else:
                print("Oops! Couldn't understand. Try it again!")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nYou played: {move1}.\nOpponent played: {move2}.\n")
        # pdb.set_trace()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # pdb.set_trace()
        if beats(move1, move2):
            self.p1.score += 1
            print("You won!")
        elif beats(move2, move1):
            self.p2.score += 1
            print("Opponent won!")
        elif move1 == move2:
            print("Tied!")
        print(f"Score: You {self.p1.score}, Opponent {self.p2.score}")
        print()

    def play_game(self):
        print("Game start!\n")
        while True:
            customround = input("How many rounds would you like to play? ")
            if customround.isdigit():
                break
            else:
                print("Tell me a number. For example: 1, 2, 3, or 10.\n")
        for round in range(int(customround)):
            print(f"\nRound {round+1} --")
            self.play_round()
        print("Game over!")
        print(f"Final Score: You {self.p1.score} vs Opponent {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("You won!")
        elif self.p2.score > self.p1.score:
            print("Opponent won!")
        elif self.p1.score == self.p2.score:
            print("Tied!")


if __name__ == '__main__':
    c_players = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(c_players))
    game.play_game()
