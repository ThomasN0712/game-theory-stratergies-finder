import re
from operator import itemgetter
import numpy as np  

def find_dominant(payoff_matrix, dimension_list):
    num_players = len(dimension_list)
    max_payoff = 1
    for dimension in dimension_list:
        max_payoff *= dimension

    for player in range(1, num_players+1):
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
            strategy_finder.append(payoff_index%dimension_list[0])
        if (len(strategy_finder) == dimension_list[1]) and all(x == strategy_finder[0] for x in strategy_finder):
            print("Player {} has dominant strategy {}".format(player, dominant_strategies[0]))
        else:
            print("Player {} has no dominant strategy".format(player))
        
        # #strictly dominant equilibrium
        # if len(dominant_strategies) == 1:
        #     print("strictly dominant equilibrium is {}".format(dominant_strategies[0]))
        # else:
        #     print("no strictly dominant equilibrium")

        #mixed stratergy nash equilibrium
    

def find_dominated(payoff_matrix, dimension_list):
    num_players = len(dimension_list)
    max_payoff = 1
    
    for dimension in dimension_list:
        max_payoff *= dimension

    for player in range(1, num_players+1):
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
            payoff_j = int(payoff_matrix[player][i+ player])
            if payoff_i >= payoff_j:
                dominated_strategies.append(i * offset + 1)
                i += next
                continue
            if is_dominated:
                dominated_strategies.append(i)
            i += next
        strategy_finder = []
        for payoff_index in dominated_strategies:
            strategy_finder.append(payoff_index%dimension_list[0])
        if (len(strategy_finder) == dimension_list[1]) and all(x == strategy_finder[0] for x in strategy_finder):
            print("Player {} has dominated strategy {}".format(player, dominated_strategies[0]))
        else:
            print("Player {} has no dominated strategy".format(player))


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
    print(payoff_list)

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
    print(payoff_matrix)
    find_dominant(payoff_matrix, dimension_list)
    find_dominated(payoff_matrix, dimension_list)   


if __name__ == "__main__":
    main()
