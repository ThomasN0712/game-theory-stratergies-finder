#   Name: Thomas Nguyen
#   Course: CECS 427
#   Assignment: 3
#   Date: 10/14/2023

import numpy as np
import re


def find_dominant(payoff_matrix, dimension_list):
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
            return 0

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
            return 0

    # Find dominating stratergy if no applicable preset matrix
    num_players = len(dimension_list)
    max_payoff = 1
    for dimension in dimension_list:
        max_payoff *= dimension

    for player in range(1, num_players + 1):
        dominant_strategies = []
        if player == 1:
            offset = 1
            next = 2
        if player == 2:
            offset = 2
            next = 1
        i = 0
        while i < max_payoff - player:
            is_dominant = True
            payoff_i = int(payoff_matrix[player][i])
            payoff_j = int(payoff_matrix[player][i + player])
            if payoff_i <= payoff_j:
                i += next
                continue
            if is_dominant:
                dominant_strategies.append(i * offset)
            i += next
        strategy_finder = []
        for payoff_index in dominant_strategies:
            strategy_finder.append(payoff_index % dimension_list[0])
        if (len(strategy_finder) == dimension_list[1]) and all(
            x == strategy_finder[0] for x in strategy_finder
        ):
            print(
                "Player {} has dominant strategy {}".format(
                    player, dominant_strategies[0]
                )
            )
        else:
            print("Player {} has no dominant strategy".format(player))
    return dominant_strategies


def find_dominated(payoff_matrix, dimension_list):
    if len(dimension_list) == 2:
        if dimension_list[0] == 2 and dimension_list[1] == 2:
            # dominated stratergy for p1
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
            # dominated stratergy for p2
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
        return 0
    if len(dimension_list) == 3:
        if dimension_list[0] == 2 and dimension_list[1] == 2 and dimension_list[2] == 2:
            # dominated stratergy for p1
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
            # dominated stratergy for p2
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

            # dominated stratergy for p1
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
            # dominated stratergy for p2
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
            # dominated stratergy for p3
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

        return 0

    # Find dominated stratergy if no applicable preset matrix
    num_players = len(dimension_list)
    max_payoff = 1
    for dimension in dimension_list:
        max_payoff *= dimension

    for player in range(1, num_players + 1):
        dominated_strategies = []
        if player == 1:
            offset = 1
            next = 2
        if player == 2:
            offset = 2
            next = 1
        i = 0
        while i < max_payoff - player:
            is_dominated = True
            payoff_i = int(payoff_matrix[player][i])
            payoff_j = int(payoff_matrix[player][i + player])
            if payoff_i >= payoff_j:
                dominated_strategies.append(i * offset + 1)
                i += next
                continue
            if is_dominated:
                dominated_strategies.append(i)
            i += next
        strategy_finder = []
        for payoff_index in dominated_strategies:
            strategy_finder.append(payoff_index % dimension_list[0])
        if (len(strategy_finder) == dimension_list[1]) and all(
            x == strategy_finder[0] for x in strategy_finder
        ):
            print(
                "Player {} has dominated strategy {}".format(
                    player, dominated_strategies[0]
                )
            )
        else:
            print("Player {} has no dominated strategy".format(player))


def find_strictly_dominant(dominant_strategies):
    # strictly dominant equilibrium
    dominant_strategies = False

    if dominant_strategies:
        print("strictly dominant equilibrium is {}".format(dominant_strategies[0]))
    else:
        print("No strictly dominant equilibrium.")


def is_zero_sum(payoff_list):
    sum = 0
    for i in payoff_list:
        sum += int(i)
    if sum == 0:
        return True
    else:
        return False


def mixed_stratergy(payoff_list):
    x_0 = float(payoff_list[0])
    x_1 = float(payoff_list[2])
    x_2 = float(payoff_list[4])
    x_3 = float(payoff_list[6])
    y_0 = float(payoff_list[1])
    y_1 = float(payoff_list[3])
    y_2 = float(payoff_list[5])
    y_3 = float(payoff_list[7])

    # p & q equation for 2 players zero sum game
    p = (-x_2 + x_3) / (x_0 - x_2 - x_1 + x_3)

    q = (y_3 - y_1) / (y_0 - y_2 - y_1 + y_3)

    print("Mixed stratergy:\n", "p = ", p, "\n", "q = ", q)


def main():
    # Load the game from file
    file = input("Enter the file name: ")
    game = open(file, "r")

    # Read and match with regex
    game_read = game.readlines()

    # construct dimension list
    dimension = re.search("\{\s((\d+)\s)*\}", game_read[1])
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

    # calculate max payoff
    max_payoff = 1
    for dimension in dimension_list:
        max_payoff *= dimension

    # construct payoff matrix list
    payoff_list = game_read[3].split(" ")
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

    # Print number of players:
    print("Number of players:", number_of_players)
    # Print dimension:
    print("Dimension:", dimension_list)
    # Print max payoff:
    print("Max payoff:", max_payoff)
    # Print payoff matrix
    print("Payoff value of each player: ", payoff_matrix)
    # Find dominant & dominated stratergy
    print("\n---Show dominant stratergy---")
    dominant_strategies = find_dominant(payoff_matrix, dimension_list)
    find_dominated(payoff_matrix, dimension_list)
    # Find strictly dominant equilibrium
    print("\n---Show strictly dominant equilibrium---")
    find_strictly_dominant(dominant_strategies)
    # Zero sum game
    if is_zero_sum(payoff_list) and len(dimension_list) == 2:
        print("\n---Zero sum game two players--- ")
        mixed_stratergy(payoff_list)
    else:
        print("\n---Not zero sum game---")


if __name__ == "__main__":
    main()
