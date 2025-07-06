import random
from dataclasses import dataclass

@dataclass
class TicTacToe:

    @staticmethod
    def start_game():
        plateau = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]

        return plateau, True

    @staticmethod
    def select_player(turns: int, list_moves):
        # Si la partie commence prendre un joueur au hasard
        random_number = random.random()
        if turns == 0:
            if random_number > 0.5:
                print("Player 1 starts")
                player = "Player 1"
                list_moves.append(player)
            else:
                print("Player 2 starts")
                player = "Player 2"
                list_moves.append(player)
        else:
            # vérifier le premier joueur et en fonction de si la position est pair ou pas alterner entre chaque joueur
            first_player = list_moves[0]
            if first_player == "Player 1":
                if turns % 2 == 0:
                    list_moves.append("Player 1")
                else:
                    list_moves.append("Player 2")
            else:
                if turns % 2 == 0:
                    list_moves.append("Player 2")
                else:
                    list_moves.append("Player 1")
            player = list_moves[-1]
        return player

        # Vérifier qui est le dernier à avoir joué et donner la main au suivant

    @staticmethod
    def make_move(plateau, player):
        # Penser aux cas limites, i.e un utilisateur mets une valeur qui dépasse les bounds du tableau
        # try except de la valeur rentrée par l'utilisateur
        try:
            x, y = input("Veuillez rentrer la position de votre choix: " ).split()
            if plateau[int(x)][int(y)] != 0:
                print("Cette position est déjà prise")
            else:
                if player == "Player 1":
                    plateau[int(x)][int(y)] = "X"
                else:
                    plateau[int(x)][int(y)] = "O"
            print(plateau)
        except IndexError as e:
            print(f'Les positions ne sont pas valides {e}')
        return plateau

    @staticmethod
    def check_board(plateau):
        # dernier cas celui en diagonale
        c, r = 0, 0
        end = False
        for row in plateau:
            if row == ["X", "X", "X"] or row == ["O", "O", "O"]:
                print("la partie est terminée")
                end = True

        buffer = []
        while c < 3:
            for i in range(len(plateau)):
                buffer.append(plateau[i][c])
            if buffer == ["X", "X", "X"] or buffer == ["O", "O", "O"]:
                print("La partie est terminée")
                end = True
            else:
                buffer = []
                c += 1
        return end

    @staticmethod
    def end_game():
        # Une fois que le plateau est actualisé, vérifier qu'aucun des joueurs ait gagné
        # Si un joueur gagne terminer la partie et si le tableau est rempli terminer aussi
        # condition pour terminer une partie de renvoyer un booléen.
        return False

    def restart_game(self):
        reset = input("Voulez vous rejouer? : ")
        if reset == "oui":
            output = self.start_game()[1]
            plateau = self.start_game()[0]
        else:
            output = self.end_game()
            plateau = None
        return output, plateau