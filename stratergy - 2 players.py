import re
from operator import itemgetter
import numpy as np  

def find_stratergy(payoff_matrix, dimension_list):
    if len(dimension_list) == 2:
        if dimension_list[0] == 2 and dimension_list[1] == 2:
            # dominant stratergy for p1
            if (
                payoff_matrix[1][0] >= payoff_matrix[1][1]
                and payoff_matrix[1][2] >= payoff_matrix[1][3]
            ):
                print("p1 has dominant stratergy 1")
            elif (
                payoff_matrix[1][1] >= payoff_matrix[1][0]
                and payoff_matrix[1][3] >= payoff_matrix[1][2]
            ):
                print("p1 has dominant stratergy 2")
            else:
                print("p1 has no dominant stratergy")
            # dominant stratergy for p2
            if (
                payoff_matrix[2][0] >= payoff_matrix[2][2]
                and payoff_matrix[2][1] >= payoff_matrix[2][3]
            ):
                print("p2 has dominant stratergy 1")
            elif (
                payoff_matrix[2][2] >= payoff_matrix[2][0]
                and payoff_matrix[2][3] >= payoff_matrix[2][1]
            ):
                print("p2 has dominant stratergy 2")
            else:
                print("p2 has no dominant stratergy")
            
            #dominated stratergy for p1
            if (
                payoff_matrix[1][0] <= payoff_matrix[1][1]
                and payoff_matrix[1][2] <= payoff_matrix[1][3]
            ):
                print("p1 has dominated stratergy 1")
            elif (
                payoff_matrix[1][1] <= payoff_matrix[1][0]
                and payoff_matrix[1][3] <= payoff_matrix[1][2]
            ):
                print("p1 has dominated stratergy 2")
            else:
                print("p1 has no dominated stratergy")
            #dominated stratergy for p2
            if (
                payoff_matrix[2][0] <= payoff_matrix[2][2]
                and payoff_matrix[2][1] <= payoff_matrix[2][3]
            ):
                print("p2 has dominated stratergy 1")
            elif (
                payoff_matrix[2][2] <= payoff_matrix[2][0]
                and payoff_matrix[2][3] <= payoff_matrix[2][1]
            ):
                print("p2 has dominated stratergy 2")
            else:
                print("p2 has no dominated stratergy")

    if len(dimension_list) == 3:
        if dimension_list[0] == 2 and dimension_list[1] == 2 and dimension_list[2]:
            # dominant stratergy for p1
            if (
                payoff_matrix[1][0] >= payoff_matrix[1][1]
                and payoff_matrix[1][2] >= payoff_matrix[1][3]
                and payoff_matrix[1][4] >= payoff_matrix[1][5]
                and payoff_matrix[1][6] >= payoff_matrix[1][7]
            ):
                print("p1 has dominant stratergy 1")
            elif (
                payoff_matrix[1][1] > payoff_matrix[1][0]
                and payoff_matrix[1][3] > payoff_matrix[1][2]
                and payoff_matrix[1][5] > payoff_matrix[1][4]
                and payoff_matrix[1][7] > payoff_matrix[1][6]
            ):
                print("p1 has dominant stratergy 2")
            else:
                print("p1 has no dominant stratergy")
            # dominant stratergy for p2
            if (
                payoff_matrix[2][0] > payoff_matrix[2][2]
                and payoff_matrix[2][1] > payoff_matrix[2][3]
                and payoff_matrix[2][4] > payoff_matrix[2][6]
                and payoff_matrix[2][5] > payoff_matrix[2][7]
            ):
                print("p2 has dominant stratergy 1")
            elif (
                payoff_matrix[2][2] > payoff_matrix[2][0]
                and payoff_matrix[2][3] > payoff_matrix[2][1]
                and payoff_matrix[2][6] > payoff_matrix[2][4]
                and payoff_matrix[2][7] > payoff_matrix[2][5]
            ):
                print("p2 has dominant stratergy 2")
            else:
                print("p2 has no dominant stratergy")
            # dominant stratergy for p3
            if (
                payoff_matrix[3][0] > payoff_matrix[3][4]
                and payoff_matrix[3][1] > payoff_matrix[3][5]
                and payoff_matrix[3][2] > payoff_matrix[3][6]
                and payoff_matrix[3][3] > payoff_matrix[3][7]
            ):
                print("p3 has dominant stratergy 1")
            elif (
                payoff_matrix[3][4] > payoff_matrix[3][0]
                and payoff_matrix[3][5] > payoff_matrix[3][1]
                and payoff_matrix[3][6] > payoff_matrix[3][2]
                and payoff_matrix[3][7] > payoff_matrix[3][3]
            ):
                print("p3 has dominant stratergy 2")
            else:    
                print("p3 has no dominant stratergy")

            #dominated stratergy for p1
            if (
                payoff_matrix[1][0] <= payoff_matrix[1][1]
                and payoff_matrix[1][2] <= payoff_matrix[1][3]
                and payoff_matrix[1][4] <= payoff_matrix[1][5]
                and payoff_matrix[1][6] <= payoff_matrix[1][7]
            ):
                print("p1 has dominated stratergy 1")
            elif (
                payoff_matrix[1][1] <= payoff_matrix[1][0]
                and payoff_matrix[1][3] <= payoff_matrix[1][2]
                and payoff_matrix[1][5] <= payoff_matrix[1][4]
                and payoff_matrix[1][7] <= payoff_matrix[1][6]
            ):
                print("p1 has dominated stratergy 2")
            else:
                print("p1 has no dominated stratergy")
            #dominated stratergy for p2
            if (
                payoff_matrix[2][0] <= payoff_matrix[2][2]
                and payoff_matrix[2][1] <= payoff_matrix[2][3]
                and payoff_matrix[2][4] <= payoff_matrix[2][6]
                and payoff_matrix[2][5] <= payoff_matrix[2][7]
            ):
                print("p2 has dominated stratergy 1")
            elif (
                payoff_matrix[2][2] <= payoff_matrix[2][0]
                and payoff_matrix[2][3] <= payoff_matrix[2][1]
                and payoff_matrix[2][6] <= payoff_matrix[2][4]
                and payoff_matrix[2][7] <= payoff_matrix[2][5]
            ):
                print("p2 has dominated stratergy 2")
            else:
                print("p2 has no dominated stratergy")
            #dominated stratergy for p3
            if (
                payoff_matrix[3][0] <= payoff_matrix[3][4]
                and payoff_matrix[3][1] <= payoff_matrix[3][5]
                and payoff_matrix[3][2] <= payoff_matrix[3][6]
                and payoff_matrix[3][3] <= payoff_matrix[3][7]
            ):
                print("p3 has dominated stratergy 1")
            elif (
                payoff_matrix[3][4] <= payoff_matrix[3][0]
                and payoff_matrix[3][5] <= payoff_matrix[3][1]
                and payoff_matrix[3][6] <= payoff_matrix[3][2]
                and payoff_matrix[3][7] <= payoff_matrix[3][3]
            ):
                print("p3 has dominated stratergy 2")
            else:
                print("p3 has no dominated stratergy")
        

def main():
    # Load the game from file
    file = "test.nfg"  # input("Enter the file name")
    game = open(file, "r")

    # Read and match with regex
    game_read = game.readlines()

    dimension = re.search("\{\s((\d+)\s)*\}", game_read[1])
    print(dimension)
    dimension_list_temp = dimension.group().split(" ")
    dimension_list_temp.remove("{")
    dimension_list_temp.remove("}")
    dimension_list = [
        eval(i) for i in dimension_list_temp
    ]  # convert string list to int list

    number_of_players = len(dimension_list)

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

    # construct payoff matrix list
    payoff = re.fullmatch("\d+(?:\s+\d+)*", game_read[3])
    payoff_list = payoff.group().split(" ")

    payoff_matrix = {}
    for player in range(number_of_players):
        i = 0 + player
        j = 0
        player += 1
        payoff_matrix[player] = []
        while j < max_payoff:
            payoff_matrix[player].append(payoff_list[i])
            i += number_of_players
            j += 1
    find_stratergy(payoff_matrix, dimension_list)

if __name__ == "__main__":
    main()
