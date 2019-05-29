import csv
import os

# create file path and save as file
file = os.path.join('..', 'Resources', 'election_data.csv')

#read csv and parse data into lists
#profit list will be list of integers
with open(file, 'r') as csvfile:
    
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    candidate = []
    
    for row in csvread:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]

    votes = []
    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]

total_votes = len(candidate)

correy_total = candidate.count('Correy')
correy_percent = (correy_total) / (total_votes)

otooley_total = candidate.count("O'Tooley")
otooley_percent = otooley_total / total_votes

li_total = candidate.count('Li')
li_percent = li_total / total_votes

khan_total = candidate.count('Khan')
khan_percent = khan_total / total_votes

print(f'***ELECTION RESULTS***')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_percent:.3%} ({khan_total})')
print(f'Correy: {correy_percent:.3%} ({correy_total})')
print(f'Li: {li_percent:.3%} ({li_total})')
print(f"O'Tooley: {otooley_percent:.3%} ({otooley_total})")
print(f'-------------------------')
print(f'Winner: {winner_name}')
print(f'-------------------------')

output_path = os.path.join('..', 'Output', 'results.csv')

# opens the output destination in write mode and prints the summary
with open(output_path, 'w') as text_file:
    print(f'***ELECTION RESULTS***', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Khan: {khan_percent:.3%} ({khan_total})', file=text_file)
    print(f'Correy: {correy_percent:.3%} ({correy_total})', file=text_file)
    print(f'Li: {li_percent:.3%} ({li_total})', file=text_file)
    print(f"O'Tooley: {otooley_percent:.3%} ({otooley_total})", file=text_file)
    print(f'-------------------------', file=text_file)
    print(f'Winner: {winner_name}', file=text_file)
    print(f'-------------------------', file=text_file)