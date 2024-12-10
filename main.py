# Author: @cinyc9
# Date: November 20, 2024
# Version: 3
# Purpose: Converts Alaskan CVR into Marks for Rounds 1-5; Corrects error to remove Invalid Contest Ballots (Outstack Condition 7)
# Note: Must Edit 6 C:\\Path\\to\\Files references before running the first time for your file system

import json, csv
#Change these variables for your particular race
race = 'AK-AL' # Race Name to be Saved
version = '1' # Version Number - change if don't want to save over old
cvr_folder = "CVR_Export_20241120180714" # Name of AK CVR Folder
cid = 7 # Your Contest IDs here
candidates = [517, 518, 520, 552, 476]  # Candidate List for AK-AL; Change to your race
ex_list = ['undervote', '476', '552', '520'] # List of candidates in order of elimination, starting with overvote
num_CVR_files = 2000 #number of CVR files in folder


candidates_string = []
for item in candidates:
    candidates_string.append(f'{item}')
candidates2 = candidates_string[:]
candidates2.append('undervote')
candidates2.append('blank')

# Other candidate lists
# [217, 218, '', '', ''] #BM2 (cid 68)
# [219, 220, '', '', ''] #BM2 (cid 69)
# [463, 464, 465, 468, ''] - HD 40
# [548, 538, 553, 539, 502] - HD 36
# [435, 436, 511, '', ''] - HD-27
# [413, 414, 415, 504, ''] - HD-15
# [458, 459, 457, 460, 516] - HD-38 (cid 65)
# [536, 537, 551, 480, ''] - SD L
# [362, 364, 365, 490, ''] - SD-D
# [437, 438, 439, 498, ''] - HD28 (cid 55)
# [391, 392, 393, 493, ''] - HD-6
# [517, 518, 520, 552, 476] - 2024 U.S. House
# ['263, '279', '264', '265', '215'] - November U.S. House
# ['267', '268', '269', '270', '235'] - Gov
# ['215', '217', '218', '214', ''] - Aug Special U.S. House
# ['271', '272', '273', '274', '246'] - Senate

# Other ex_lists
# ['undervote', '516', '460', '457'] - HD-38
# ['undervote', '498', '437', ''] - HD-28
# ['undervote', '493', '393', ''] - HD-6
# ['undervote', '476', '552', '520'] US House 2024 (cid 7)
# ['undervote', '215', '279', '263] - November U.S. House
# ['undervote','235','269','267'] - Gov
# ['undervote', '246', '272', '271'] - Senate
# ['undervote', '214', '215', ''] - August Special House

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

                elif 7 in outstack:
                    print('Invalid Contest!')
                    candidate_count = count_votes("invalid_contest", candidates, candidate_count, level)
                    # rank[level] = 'invalid_contest'
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
            elif 7 in outstack:
                print("Invalid Contest")
                candidate_count= count_votes("invalid_contest", candidates, candidate_count, level)
                rank[level] = 'invalid_contest'
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

with open(f'C:\\Path\\to\\Files\\{race} Marks {version}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerow(['Rank 1', 'Rank 2', 'Rank 3', 'Rank 4', 'Rank 5','Precinct','Json Number','Record Number'])

    for i in range(num_CVR_files):
        try:
            with open(f'C:\\Path\\to\\Files\\{cvr_folder}\\CvrExport_{i}.json', 'r') as file:
                contents = json.load(file)
                sessions = len(contents['Sessions'])
                for session in range(sessions):
                    try:
                        contents['Sessions'][session]['Modified']['Cards'][0]['Contests']
                        contests = len(contents['Sessions'][session]['Modified']['Cards'][0]['Contests'])
                        for contest in range(contests):
                            contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][contest]
                    except:
                        try:
                            cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests']
                            contests = len(cards)
                            for contest in range(contests):
                                if contents['Sessions'][session]['Original']['Cards'][0]['Contests'][contest]['Id'] == cid:
                                    cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests'][contest]
                        except:
                            pass
                        else:
                            cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests']
                            contests = len(cards)
                            for contest in range(contests):
                                if contents['Sessions'][session]['Original']['Cards'][0]['Contests'][contest]['Id'] == cid:
                                    cards = contents['Sessions'][session]['Original']['Cards'][0]['Contests'][contest]
                                    precinct = contents['Sessions'][session]['Original']["PrecinctPortionId"]
                                    recordId = contents['Sessions'][session]['RecordId']

                                    candidate_count, row_to_write = compute_round(cards, candidates, candidate_count_0, rank_0, 0)
                                    row_to_write.append(precinct)
                                    row_to_write.append(f"{i}-{session}")
                                    row_to_write.append(recordId)
                                    writer.writerow(row_to_write)
                                    candidate_count[0][5] += 1

                    else:
                        cards = contents['Sessions'][session]['Modified']['Cards'][0]['Contests']
                        contests = len(cards)
                        for contest in range(contests):
                            if contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][contest]['Id'] == cid:
                                cards = contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][contest]
                                precinct = contents['Sessions'][session]['Modified']["PrecinctPortionId"]
                                recordId = contents['Sessions'][session]['RecordId']

                                candidate_count, row_to_write = compute_round(cards, candidates, candidate_count_0,
                                                                              rank_0, 0)
                                row_to_write.append(precinct)
                                row_to_write.append(f"{i}-{session}")
                                row_to_write.append(recordId + "Modified")
                                writer.writerow(row_to_write)
                                candidate_count[0][5] += 1
                        else:
                            cards = contents['Sessions'][session]['Modified']['Cards'][0]['Contests'][contest]
                            precinct = contents['Sessions'][session]['Modified']["PrecinctPortionId"]
                            recordId = contents['Sessions'][session]['RecordId']
                            candidate_count, row_to_write = compute_round(cards, candidates, candidate_count_0, rank_0, 0)
                            row_to_write.append(precinct)
                            row_to_write.append(f"{i}-{session}")
                            row_to_write.append(recordId + "Modified")
                            writer.writerow(row_to_write)
                            candidate_count[1][5] += 1
        except:
            print(f"File {i} Missing!")

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
      f"Peltola: {candidate_count[1][i]}\n"
      f"Howe: {candidate_count[2][i]}\n"
      f"Hafner: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )

i = 5
print(f"\nRound {i + 1} Votes:\n"
      f"Begich: {candidate_count[0][i]}\n"
      f"Peltola: {candidate_count[1][i]}\n"
      f"Howe: {candidate_count[2][i]}\n"
      f"Hafner: {candidate_count[3][i]}\n"
      f"WI: {candidate_count[4][i]}\n"
      f"Blank: {candidate_count[5][i]}\n"
      f"Exhausted: {candidate_count[6][i]}\n"
      f"Overvotes: {candidate_count[7][i]}\n"
      f"Total = {total[i]}\n"
      )

candidates = candidates_string
# ['465', '463', '464', '468', ''] - HD-40
# ['539', '538', '548', '553', '502'] - HD-36
# ['435', '436', '511', '', ''] - HD-27
# ['413', '414', '415', '504', ''] - HD-15
# ['459', '458', '457', '460', '516'] - HD-38
# ['536', '537', '551', '480', ''] - SD-L
# ['365', '362', '364', '490', ''] - SD-D
# ['439', '438', '437', '498', ''] - HD-28
# ['391', '392', '393', '493', ''] - HD-6
# ['517', '518', '520', '552', '476'] - U.S. House 2024
# candidates = ['476', '552', '520', '518', '517']
# ['263, '279', '264', '265', '215'] - November U.S. House
# ['267', '268', '269', '270', '235'] - Gov
# ['215', '217', '218', '214', ''] - Aug Special U.S. House
# ['271', '272', '273', '274', '246'] - Senate
#

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
    open(f'C:\\Path\\to\\Files\\{race} Computation {version}.csv', 'w', newline='')

except:

    print("File is locked for use or folder doesn't exist'!")

else:
    with open(f'C:\\Path\\to\\Files\\{race} Computation {version}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerow(['Precinct','Round 1', 'Round 2', 'Round 3', 'Round 4','ID'])

        try:
            open(f'C:\\Path\\to\\Files\\{race} Marks {version}.csv', 'r')

        except:
            print("File not found! Please check path!")

        else:
            print("Computing ranks...")
            with open(f'C:\\Path\\to\\Files\\{race} Marks {version}.csv', 'r') as file:
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

            total[2] = candidate_count_1[1][2] + candidate_count_1[2][2] + candidate_count_1[3][2] + candidate_count_1[4][2] + \
                       candidate_count_1[5][2] + candidate_count_1[0][2] + candidate_count_1[6][2] + candidate_count_1[7][2]

            i = 2
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

            total[3] = candidate_count_1[1][3] + candidate_count_1[2][3] + candidate_count_1[3][3] + candidate_count_1[4][3] + \
                       candidate_count_1[5][3] + candidate_count_1[0][3] + candidate_count_1[6][3] + candidate_count_1[7][3]

            i = 3
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
