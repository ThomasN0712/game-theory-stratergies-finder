import re
from operator import itemgetter


# def find_stratergy(payoff_matrix, dimension_list):
#     # stirctly dominant stratergy
#     player_list = list(payoff_matrix.keys())
#     dominant_stratergies = []
#     # 2 players
#     for player in player_list:
#         # compare each stratergy with other stratergies
#         i = 0  # first pointer, point to current dominant stratergy
#         j = 1  # second pointer, point to other stratergies
#         dominant_stratergy = 0  # 0 means no dominant stratergy
#         while j < (len(payoff_matrix[player]) - dimension_list[player - 1]):
#             print(
#                 "comparing:",
#                 i,
#                 payoff_matrix[player][i],
#                 "with",
#                 j,
#                 payoff_matrix[player][j],
#             )
#             if payoff_matrix[player][i] < payoff_matrix[player][j]:
#                 for i in range(dimension_list[player - 1]):
#                     print(
#                         "comparing 1:",
#                         (i + dimension_list[player - 1]),
#                         payoff_matrix[player][i + dimension_list[player - 1]],
#                         "with",
#                         (j + dimension_list[player - 1]),
#                         payoff_matrix[player][j + dimension_list[player - 1]],
#                     )
#                     if (
#                         payoff_matrix[player][i + dimension_list[player - 1]]
#                         >= payoff_matrix[player][j + dimension_list[player - 1]]
#                     ):
#                         j += 1
#                         break
#                     dominant_stratergy = j + 1
#                     print("statergy found", dominant_stratergy)
#                     i = dominant_stratergy - 1
#                     j = i + 1
#                     print("j: ", j)
#             else:
#                 j += 1
#         if dominant_stratergy == 0:
#             print("There is no dominant stratergy for player " + str(player))
#         else:
#             print(
#                 "Player "
#                 + str(player)
#                 + " has a dominant stratergy "
#                 + str(dominant_stratergy)
#             )
#     # dominant stratergy
#     # all dominated stratergies
#     # Strictly dominant strategy equilibrium, if one exists
#     # All pure strategy Nash Equilibria, if they exist
#     # mixed stratergy
#     return 0


def find_stratergy(payoff_matrix, dimension_list):
    # stirctly dominant stratergy
    player_list = len(dimension_list)
    for player in range(1, player_list):
        if player == 1:
            jump = 2
        else:
            jump = 1
        i = 0
        while i < len(payoff_matrix) - 1:
            print(
                "Comparing: ",
                payoff_matrix[i],
                "and",
                payoff_matrix[i + player],
                player,
            )
            if payoff_matrix[i][player] < payoff_matrix[i + player][player]:
                i += jump
                continue
            i += jump

    # dominant stratergy
    # all dominated stratergies
    # Strictly dominant strategy equilibrium, if one exists
    # All pure strategy Nash Equilibria, if they exist
    # mixed stratergy
    return 0


def main():
    # Load the game from file
    file = "test.nfg"  # input("Enter the file name")
    game = open(file, "r")

    # Read and match with regex
    game_read = game.readlines()

    # player shennanigans --------------
    # players = re.search('\{ "(.*?) \}', x[1])
    # print(players.group())
    # number_of_players = len(players_regex.groups())
    # -----------------------------------

    # construct dimension list
    dimension = re.search("\{\s((\d+)\s)*\}", game_read[1])
    print(dimension)
    dimension_list_temp = dimension.group().split(" ")
    dimension_list_temp.remove("{")
    dimension_list_temp.remove("}")
    dimension_list = [
        eval(i) for i in dimension_list_temp
    ]  # convert string list to int list
    print("Dimension List", dimension_list)

    number_of_players = len(dimension_list)
    print("Number of Players", number_of_players)
    if len(dimension.groups()) == 2:
        x = int(dimension.groups()[0])
        y = int(dimension.groups()[1])

    if len(dimension.groups()) == 3:
        x = int(dimension.groups()[0])
        y = int(dimension.groups()[1])
        z = int(dimension.groups()[2])

    # temp need to make this work with 2 or 3 players
    max_payoff = 1
    for dimension in dimension_list:
        max_payoff *= dimension
    print("Max payoff", max_payoff)

    # construct payoff matrix list
    for i in game_read[2:]:
        payoff = re.fullmatch("\d+(?:\s+\d+)*", i)
    payoff_list = payoff.group().split(" ")
    print(payoff_list)
    payoff_matrix = []
    i = 0
    if dimension_list[2] == None:
        third_dimension = 0
    else:
        third_dimension = dimension_list[2]
    temp_list = []
    for i in range(third_dimension):
        while i < (len(payoff_list) / third_dimension):
            temp_list.append(list(payoff_list[i : i + number_of_players]))
            i += number_of_players
        payoff_matrix.append(temp_list)

    print(payoff_matrix)
    # find_stratergy(payoff_matrix, dimension_list)


if __name__ == "__main__":
    main()
