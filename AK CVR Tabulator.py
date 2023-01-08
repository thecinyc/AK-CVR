# Author: @cinyc9
# Date: January 8, 2023
# Version: 1
# Purpose: Parse Alaskan CVR csv

import csv

candidates = ['263', '279', '264', '265', '215']
# ['263, '279', '264', '265', '215'] - November U.S. House
# ['267', '268', '269', '270', '235'] - Gov
# ['215', '217', '218', '214', ''] - Aug Special U.S. House
# ['271', '272', '273', '274', '246'] - Senate
ex_list = ['undervote', '215', '279', '263']
# ['undervote', '215', '279', '263] - November U.S. House
# ['undervote','235','269','267'] - Gov
# ['undervote', '246', '272', '271'] - Senate
# ['undervote', '214', '215', ''] - August Special House
#
candidates2 = [263, 279, 264, 265, 215, 'undervote', 'blank']
total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
the_row = [0, 0, 0, 0, 0, 0, 0]
rank = [0, 0, 0, 0, 0, 0, 0]
rank_row_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
candidate_count_0 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def count_votes(marks, candidate, candidate_count, level=0):
    """Counts votes"""
    if marks == candidate[0]:
        candidate_count[0][level] += 1

    elif marks == candidate[1]:
        candidate_count[1][level] += 1

    elif marks == candidate[2]:
        candidate_count[2][level] += 1

    elif marks == candidate[3]:
        candidate_count[3][level] += 1

    elif marks == candidate[4]:
        candidate_count[4][level] += 1

    elif marks == 'blank':
        candidate_count[5][level] += 1

    elif marks == 'exhausted' or marks == 'undervote' or marks == 'skipped':
        candidate_count[6][level] += 1

    elif marks == 'overvote':
        candidate_count[7][level] += 1
    else:
        candidate_count[8][level] +=1

    return candidate_count


def compute_round(the_row, candidates, candidate_count, ex_list, level=0, ):
    """Computes Round"""
    rank = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    skip_rank = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    rank[0] = the_row[5]
    rank[1] = the_row[0]
    rank[2] = the_row[1]
    rank[3] = the_row[2]
    rank[4] = the_row[3]
    rank[5] = the_row[4]
    rank[7] = the_row[6]

    skip_rank[0] = the_row[5]
    skip_rank[1] = the_row[0]
    skip_rank[2] = the_row[1]
    skip_rank[3] = the_row[2]
    skip_rank[4] = the_row[3]
    skip_rank[5] = the_row[4]
    skip_rank[6] = the_row[6]


    replace_level(skip_rank)

    check_double_skips(rank, skip_rank, ex_list[:1], 0)
    candidate_count = count_votes(rank[1], candidates, candidate_count, 0)



    check_double_skips(rank, skip_rank, ex_list[:2], 1)
    candidate_count = count_votes(rank[2], candidates, candidate_count, 1)

    check_double_skips(rank, skip_rank, ex_list[:3], 2)
    candidate_count = count_votes(rank[3], candidates, candidate_count, 2)

    check_double_skips(rank, skip_rank, ex_list, 3)
    candidate_count = count_votes(rank[4], candidates, candidate_count, 3)

    return rank, candidate_count


def replace_level(skip_rank):
    """Replaces undervotes and duplicate candidate ranks with word skipped"""

    for i in range(4):
        for item in skip_rank[1:i+2]:
            if (skip_rank[i + 2] == item and skip_rank[i + 2] != 'overvote' and
                skip_rank[i + 2] != 'undervote' and skip_rank[i + 2] != 'blank'):
                skip_rank[i + 2] = 'skipped'

    for j in range(5):
        row_to_amend = j + 1
        if skip_rank[row_to_amend] == 'undervote':
            skip_rank[row_to_amend] = 'skipped'

    return skip_rank


def check_double_skips(rank, skip_rank, the_list, level):
    """Checks for double skips"""
    if level == 0:
        initial_level = 1
    else:
        initial_level = level

    if ((skip_rank[1] == skip_rank[2] and skip_rank[1] == 'skipped')
            and (rank[initial_level] in the_list)):
        if initial_level + 1 < 6:
            rank[level + 1] = 'exhausted'
        if initial_level + 2 < 6:
            rank[level + 2] = 'exhausted'
        if initial_level + 3 < 6:
            rank[level + 3] = 'exhausted'
        if initial_level + 4 < 6:
            rank[level + 4] = 'exhausted'

    if ((skip_rank[2] == skip_rank[3] and skip_rank[2] == 'skipped')
            and (rank[initial_level] in the_list)):
        if initial_level + 2 < 6:
            rank[level + 2] = 'exhausted'
        if initial_level + 3 < 6:
            rank[level + 3] = 'exhausted'
        if initial_level + 4 < 6:
            rank[level + 4] = 'exhausted'

        if ((skip_rank[3] == skip_rank[4] and skip_rank[3] == 'skipped')
                and (rank[initial_level] in the_list)):
            if initial_level + 3 < 6:
                rank[level + 3] = 'exhausted'
            if initial_level + 4 < 6:
                rank[level + 4] = 'exhausted'

        if ((skip_rank[4] == skip_rank[5] and skip_rank[4] == 'skipped')
                and (rank[initial_level] in the_list)):
            if initial_level + 4 < 6:
                rank[level + 4] = 'exhausted'

        if ((skip_rank[5] == 'skipped')
                and (rank[initial_level] in the_list)):
            if initial_level + 4 < 6:
                rank[level + 4] = 'exhausted'

    if level == 0:
        remove_initial_skip(skip_rank, the_list)
        change_rank(skip_rank, rank, the_list, 0)

    if level == 1:
        remove_initial_skip(skip_rank, the_list)
        change_rank(skip_rank, rank, the_list, 1)

    if level == 2:
        remove_initial_skip(skip_rank, the_list)
        change_rank(skip_rank, rank, the_list, 2)

    if level == 3:
        remove_initial_skip(skip_rank, the_list)
        change_rank(skip_rank, rank, the_list, 3)

    return rank


def remove_initial_skip(skip_rank, the_list):
    """Removes First Row of Ranks Skips"""
    skipped = False

    if skip_rank[1] in the_list or skip_rank[1] == 'skipped':
        if skip_rank[1] == 'skipped':
            skipped = True
        skip_rank[1] = skip_rank[2]
        skip_rank[2] = skip_rank[3]
        skip_rank[3] = skip_rank[4]
        skip_rank[4] = skip_rank[5]


        if skip_rank[1] in the_list:
            skipped = False
            skip_rank[1] = skip_rank[2]
            skip_rank[2] = skip_rank[3]
            skip_rank[3] = skip_rank[4]

            if skip_rank[1] in the_list or skip_rank[1] == 'skipped':
                if skip_rank[1] == 'skipped':
                    skipped = True
                skip_rank[1] = skip_rank[2]
                skip_rank[2] = skip_rank[3]

                if skip_rank[1] in the_list:
                    skip_rank[1] = skip_rank[2]

                elif skip_rank[1] == 'skipped' and skipped == True:
                    skip_rank[1] = 'exhausted'

                elif skip_rank[1] == 'skipped' and skipped == False:
                    skip_rank[1] = skip_rank[2]

        elif skip_rank[1] == 'skipped' and skipped == False:
            if skip_rank[1] == 'skipped':
                skipped = True
            skip_rank[1] = skip_rank[2]
            skip_rank[2] = skip_rank[3]
            skip_rank[3] = skip_rank[4]

            if skip_rank[1] in the_list:
                skipped = False
                skip_rank[1] = skip_rank[2]
                skip_rank[2] = skip_rank[3]

                if skip_rank[1] in the_list or skip_rank[1] == 'skipped':
                    skip_rank[1] = skip_rank[2]

            elif skip_rank[1] == 'skipped' and skipped == False:
                skip_rank[1] = skip_rank[2]
                skip_rank[2] = skip_rank[3]

                if skip_rank[1] == 'skipped':
                    skip_rank[1] = 'exhausted'

                elif skip_rank[1] in the_list:
                    skip_rank[1] = skip_rank[2]

            elif skip_rank[1] == 'skipped' and skipped == True:
                skip_rank[1] = 'exhausted'
                skip_rank[2] = 'exhausted'

        elif skip_rank[1] == 'skipped' and skipped == True:
            skip_rank[1] = 'exhausted'
            skip_rank[2] = 'exhausted'
            skip_rank[3] = 'exhausted'

    return skip_rank


def change_rank(skip_rank, rank, the_list, level):
    """Skip Rank level 2 conditionals"""
    if level == 0:
        il = 1
    else:
        il = level

    if rank[il] not in the_list:
        rank[level + 1] = rank[il]

    elif rank[il] in the_list:
        rank[level + 1] = skip_rank[1]

    return rank, skip_rank 


try:
    open('D:\\GISFiles\\Alaska\\2022 AK GE CVR\\Test\\2022_AK_USH_Tab_Test_GE.csv', 'w', newline='')

except:

    print("File is locked for use or folder doesn't exist'!")

else:
    with open('D:\\GISFiles\\Alaska\\2022 AK GE CVR\\Test\\2022_AK_USH_Tab_Test_GE.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerow(['Precinct','Round 1', 'Round 2', 'Round 3', 'Round 4','ID'])

        try:
            open('D:\\GISFiles\\Alaska\\2022 AK GE CVR\\Test\\2022_AK_USH4_GE.csv', 'r')

        except:
            print("File not found! Please check path!")

        else:
            print("Computing ranks...")
            with open('D:\\GISFiles\\Alaska\\2022 AK GE CVR\\Test\\2022_AK_USH4_GE.csv', 'r') as file:
                contents = csv.reader(file)
                for row in contents:
                    rank_row = row
                    if rank_row[0] == "Rank 1":
                        pass
                    else:
                        rank_2, candidate_count_1 = compute_round(rank_row, candidates, candidate_count_0, ex_list, 0)
                        writer.writerow(rank_2)
            total[0] = (candidate_count_1[1][0] + candidate_count_1[2][0] + candidate_count_1[3][0] + candidate_count_1[4][0] +
                        candidate_count_1[5][0] + candidate_count_1[0][0] + candidate_count_1[6][0] + candidate_count_1[7][0])
            total[1] = candidate_count_1[1][1] + candidate_count_1[2][1] + candidate_count_1[3][1] + candidate_count_1[4][1] + \
                       candidate_count_1[5][1] + candidate_count_1[0][1] + candidate_count_1[6][1] + candidate_count_1[7][1]
            total[2] = candidate_count_1[1][2] + candidate_count_1[2][2] + candidate_count_1[3][2] + candidate_count_1[4][2] + \
                       candidate_count_1[5][2] + candidate_count_1[0][2] + candidate_count_1[6][2] + candidate_count_1[7][2]
            total[3] = candidate_count_1[1][3] + candidate_count_1[2][3] + candidate_count_1[3][3] + candidate_count_1[4][3] + \
                       candidate_count_1[5][3] + candidate_count_1[0][3] + candidate_count_1[6][3] + candidate_count_1[7][3]
            total[4] = candidate_count_1[1][4] + candidate_count_1[2][4] + candidate_count_1[3][4] + candidate_count_1[4][4] + \
                       candidate_count_1[5][4] + candidate_count_1[0][4] + candidate_count_1[6][4] + candidate_count_1[7][4]

            i = 0
            print(f"\nRound {i + 1} Votes:\n"
                  f"Candidate {candidates[0]}: {candidate_count_1[0][i]}\n"
                  f"Candidate {candidates[1]}: {candidate_count_1[1][i]}\n"
                  f"Candidate {candidates[2]}: {candidate_count_1[2][i]}\n"
                  f"Candidate {candidates[3]}: {candidate_count_1[3][i]}\n"
                  f"WI: {candidate_count_1[4][i]}\n"
                  f"Blank: {candidate_count_1[5][i]}\n"
                  f"Exhausted: {candidate_count_1[6][i]}\n"
                  f"Overvotes: {candidate_count_1[7][i]}\n"
                  f"Total = {total[i]}\n"
                  )

            print("Allocating Write_ins...")

            total[1] = candidate_count_1[1][1] + candidate_count_1[2][1] + candidate_count_1[3][1] + candidate_count_1[4][1] + \
                       candidate_count_1[5][1] + candidate_count_1[0][1] + candidate_count_1[6][1] + candidate_count_1[7][1]

            i = 1
            print(f"\nRound {i + 1} Votes:\n"
                  f"Begich: {candidate_count_1[0][i]}\n"
                  f"Bye: {candidate_count_1[1][i]}\n"
                  f"Palin: {candidate_count_1[2][i]}\n"
                  f"Peltola: {candidate_count_1[3][i]}\n"
                  f"WI: {candidate_count_1[4][i]}\n"
                  f"Blank: {candidate_count_1[5][i]}\n"
                  f"Exhausted: {candidate_count_1[6][i]}\n"
                  f"Overvotes: {candidate_count_1[7][i]}\n"
                  f"Total = {total[i]}\n"
                  )

            total[2] = candidate_count_1[1][2] + candidate_count_1[2][2] + candidate_count_1[3][2] + candidate_count_1[4][2] + \
                       candidate_count_1[5][2] + candidate_count_1[0][2] + candidate_count_1[6][2] + candidate_count_1[7][2]

            i = 2
            print(f"\nRound {i + 1} Votes:\n"
                  f"Begich: {candidate_count_1[0][i]}\n"
                  f"Bye: {candidate_count_1[1][i]}\n"
                  f"Palin: {candidate_count_1[2][i]}\n"
                  f"Peltola: {candidate_count_1[3][i]}\n"
                  f"WI: {candidate_count_1[4][i]}\n"
                  f"Blank: {candidate_count_1[5][i]}\n"
                  f"Exhausted: {candidate_count_1[6][i]}\n"
                  f"Overvotes: {candidate_count_1[7][i]}\n"
                  f"Total = {total[i]}\n"
                  )

            total[3] = candidate_count_1[1][3] + candidate_count_1[2][3] + candidate_count_1[3][3] + candidate_count_1[4][3] + \
                       candidate_count_1[5][3] + candidate_count_1[0][3] + candidate_count_1[6][3] + candidate_count_1[7][3]

            i = 3
            print(f"\nRound {i + 1} Votes:\n"
                  f"Begich: {candidate_count_1[0][i]}\n"
                  f"Bye: {candidate_count_1[1][i]}\n"
                  f"Palin: {candidate_count_1[2][i]}\n"
                  f"Peltola: {candidate_count_1[3][i]}\n"
                  f"WI: {candidate_count_1[4][i]}\n"
                  f"Blank: {candidate_count_1[5][i]}\n"
                  f"Exhausted: {candidate_count_1[6][i]}\n"
                  f"Overvotes: {candidate_count_1[7][i]}\n"
                  f"Total = {total[i]}\n"
                  )