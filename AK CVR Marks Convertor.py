# Author: @cinyc9
# Date: January 8, 2023
# Version: 1
# Purpose: Converts Alaskan CVR into Marks for Rounds 1-5


import json, csv

candidates = [267, 268, 269, 270, 235]
# ['263, '279', '264', '265', '215'] - November U.S. House
# ['267', '268', '269', '270', '235'] - Gov
# ['215', '217', '218', '214', ''] - Aug Special U.S. House
# ['271', '272', '273', '274', '246'] - Senate
total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
texts = ""
rank_1 = [[]]
the_row = [0, 0, 0, 0, 0, 0]
rank_0 = [0, 0, 0, 0, 0, 0]
first_ranks_added = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    elif marks == 'blank' or marks == 'undervote':
        candidate_count[5][level] += 1

    elif marks == 'exhausted':
        candidate_count[6][level] += 1

    elif marks == 'overvote':
        candidate_count[7][level] += 1
    else:
        candidate_count[8][level] += 1
        print("ambig", marks, level)

    return candidate_count


def compute_round(texts, candidates, candidate_count, rank, level):
    """Computes Round 1"""
    rank = ['undervote', 'undervote', 'undervote', 'undervote', 'undervote']
    overvote = texts["Overvotes"]
    undervote = texts["Undervotes"]
    if overvote == 1:
        candidate_count = count_votes('overvote', candidates, candidate_count, level)
        rank[level] = 'overvote'
    else:
        try:
            texts['Marks'][0]
        except:
            candidate_count = count_votes('undervote', candidates, candidate_count, level)
            rank[level] = 'blank'
        else:
            ranks = texts['Marks'][0]['Rank']
            ambig = texts['Marks'][0]['IsAmbiguous']
            is_vote = texts['Marks'][0]['IsVote']
            outstack = texts['Marks'][0]['OutstackConditionIds']
            marks_1 = texts['Marks'][0]['CandidateId']

            if ranks == 1:
                if is_vote:
                    candidate_count = count_votes(marks_1, candidates, candidate_count, level)
                    rank[level] = marks_1
                else:
                    candidate_count = next_mark_0(texts, candidates, candidate_count, rank, 0, 1)
            else:
                candidate_count = count_votes('undervote', candidates, candidate_count, level)
                rank[level] = 'undervote'

    candidate_count = other_rounds(texts, candidates, candidate_count, rank, 1)
    candidate_count = other_rounds(texts, candidates, candidate_count, rank, 2)
    candidate_count = other_rounds(texts, candidates, candidate_count, rank, 3)
    candidate_count = other_rounds(texts, candidates, candidate_count, rank, 4)


    return candidate_count, rank


def other_rounds(texts, candidates, candidate_count, rank, level):
    """Start for Rounds 2-5"""
    overvote = texts["Overvotes"]
    undervote = texts["Undervotes"]
    temp = []
    if overvote == 1:
        candidate_count = count_votes('overvote', candidates, candidate_count, level)
        rank[level] = 'overvote'
    else:
        try:
            texts['Marks'][0]
        except:
            candidate_count = count_votes('undervote', candidates, candidate_count, level)
            rank[level] = 'blank'
        else:
            ranks = texts['Marks'][0]['Rank']
            ambig = texts['Marks'][0]['IsAmbiguous']
            is_vote = texts['Marks'][0]['IsVote']
            outstack = texts['Marks'][0]['OutstackConditionIds']
            marks_1 = texts['Marks'][0]['CandidateId']
            if ranks == level + 1:
                if 9 in outstack:
                    candidate_count = count_votes('overvote', candidates, candidate_count, level)
                    rank[level] = 'overvote'
                elif not ambig:
                    candidate_count = count_votes(marks_1, candidates, candidate_count, level)
                    rank[level] = marks_1
                else:
                    candidate_count = next_mark(texts, candidates, candidate_count, rank, level, 1, temp)
            else:
                if ranks > level + 1:
                        candidate_count = count_votes('undervote', candidates, candidate_count, level)
                        rank[level] = 'undervote'
                else:
                    candidate_count = next_mark(texts, candidates, candidate_count, rank, level, 1, temp)

    return candidate_count


def next_mark_0(texts, candidates, candidate_count, rank, level, tlevel):
    """Looks for next mark for rank 1"""
    undervote = texts["Undervotes"]
    overvote = texts["Overvotes"]
    try:
        texts['Marks'][tlevel]
    except:
        candidate_count = count_votes('undervote', candidates, candidate_count, level)
        rank[level] = 'undervote'
    else:
        ranks = texts['Marks'][tlevel]['Rank']
        ambig = texts['Marks'][tlevel]['IsAmbiguous']
        is_vote = texts['Marks'][tlevel]['IsVote']
        outstack = texts['Marks'][tlevel]['OutstackConditionIds']
        marks_1 = texts['Marks'][tlevel]['CandidateId']
        if ranks == 1:
            if is_vote:
                candidate_count = count_votes(marks_1, candidates, candidate_count, level)
                rank[level] = marks_1
            else:
                candidate_count = next_mark_0(texts, candidates, candidate_count, rank, level, tlevel + 1)
        else:
            candidate_count = next_mark_0(texts, candidates, candidate_count, rank, level, tlevel + 1)

    return candidate_count


def next_mark(texts, candidates, candidate_count, rank, level, tlevel, temp=[]):
    """Looks for next Mark for rank 2-5"""
    try:
        texts['Marks'][tlevel]
    except:
      candidate_count = count_votes('undervote', candidates, candidate_count, level)
      rank[level] = 'undervote'
    else:
        ranks = texts['Marks'][tlevel]['Rank']
        ambig = texts['Marks'][tlevel]['IsAmbiguous']
        is_vote = texts['Marks'][tlevel]['IsVote']
        outstack = texts['Marks'][tlevel]['OutstackConditionIds']
        marks_1 = texts['Marks'][tlevel]['CandidateId']

        if ranks == level + 1:
            if 9 in outstack:
                candidate_count = count_votes('overvote', candidates, candidate_count, level)
                rank[level] = 'overvote'
            elif not ambig:
                candidate_count = count_votes(marks_1, candidates, candidate_count, level)
                rank[level] = marks_1
            else:
                candidate_count = next_mark(texts, candidates, candidate_count, rank, level, tlevel + 1)
        else:
            if ranks > level + 1:
                candidate_count = count_votes('undervote', candidates, candidate_count, level)
                rank[level] = 'undervote'
            else:
                candidate_count = next_mark(texts, candidates, candidate_count, rank, level, tlevel + 1)

    return candidate_count

with open('C:\\Path\\to\\your\\csv\\file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerow(['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5', 'Precinct'])

    for i in range(1887):
        with open(f'C:\\Path\\to\\json\\CvrExport_{i}.json', 'r') as file:
            contents = json.load(file)
            sessions = len(contents['Sessions'])
            for session in range(sessions):
                try:
                    contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][2]
                except:
                    try:
                        cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests'][2]
                    except:
                        pass
                    else:
                        cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests'][2]
                        precinct = contents['Sessions'][session]['Original']["PrecinctPortionId"]

                        candidate_count, row_to_write = compute_round(cards, candidates, candidate_count_0, rank_0, 0)
                        row_to_write.append(precinct)
                        row_to_write.append(f"{i}-{session}")
                        writer.writerow(row_to_write)
                        candidate_count[0][5] += 1

                else:
                    cards = contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][2]
                    precinct = contents['Sessions'][session]['Modified']["PrecinctPortionId"]
                    candidate_count, row_to_write = compute_round(cards, candidates, candidate_count_0, rank_0, 0)
                    row_to_write.append(precinct)
                    row_to_write.append(f"{i}-{session}")
                    writer.writerow(row_to_write)
                    candidate_count[1][5] += 1
                    if precinct == 380:
                        print("Ambler")

total[0] = candidate_count[1][0] + candidate_count[2][0] + candidate_count[3][0] + candidate_count[4][0] + \
           candidate_count[5][0] + candidate_count[0][0] + candidate_count[6][0] + candidate_count[7][0]

for i in range(1):
    print(f"\nRound {i + 1} Votes:\n"
          f"Begich: {candidate_count[0][i]}\n"
          f"Bye: {candidate_count[1][i]}\n"
          f"Palin: {candidate_count[2][i]}\n"
          f"Peltola: {candidate_count[3][i]}\n"
          f"WI: {candidate_count[4][i]}\n"
          f"Blank: {candidate_count[5][i]}\n"
          f"Exhausted: {candidate_count[6][i]}\n"
          f"Overvotes: {candidate_count[7][i]}\n"
          f"Total = {total[i]}\n"
          )

print("Allocating Write_ins...")

total[1] = candidate_count[1][1] + candidate_count[2][1] + candidate_count[3][1] + candidate_count[4][1] + \
           candidate_count[5][1] + candidate_count[0][1] + candidate_count[6][1] + candidate_count[7][1]

i = 1
print(f"\nRound {i + 1} Votes:\n"
      f"Begich: {candidate_count[0][i]}\n"
      f"Bye: {candidate_count[1][i]}\n"
      f"Palin: {candidate_count[2][i]}\n"
      f"Peltola: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )

total[2] = candidate_count[1][2] + candidate_count[2][2] + candidate_count[3][2] + candidate_count[4][2] + \
           candidate_count[5][2] + candidate_count[0][2] + candidate_count[6][2] + candidate_count[7][2]

i = 2
print(f"\nRound {i + 1} Votes:\n"
      f"Begich: {candidate_count[0][i]}\n"
      f"Bye: {candidate_count[1][i]}\n"
      f"Palin: {candidate_count[2][i]}\n"
      f"Peltola: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )

total[3] = candidate_count[1][3] + candidate_count[2][3] + candidate_count[3][3] + candidate_count[4][3] + \
           candidate_count[5][3] + candidate_count[0][3] + candidate_count[6][3] + candidate_count[7][3]

i = 3
print(f"\nRound {i + 1} Votes:\n"
      f"Begich: {candidate_count[0][i]}\n"
      f"Bye: {candidate_count[1][i]}\n"
      f"Palin: {candidate_count[2][i]}\n"
      f"Peltola: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )

i = 5
print(f"\nRound {i + 1} Votes:\n"
      f"Begich: {candidate_count[0][i]}\n"
      f"Bye: {candidate_count[1][i]}\n"
      f"Palin: {candidate_count[2][i]}\n"
      f"Peltola: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )