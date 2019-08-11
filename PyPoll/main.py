import csv


votes = []
candidates = set()

with open('Resources/election_data.csv') as csv_file:
    election_data = csv.reader(csv_file)
    header = next(election_data)
    counter = 0

    for row in election_data:
        counter = counter + 1
        candidates.add(row[2])
        votes.append(row[2])


candidates = list(candidates)
num_of_votes = []

for candidate in candidates:
    num_of_votes.append(votes.count(candidate))

vote_talley = list(zip(candidates,num_of_votes))


print()
print('Election Results')
print('------------')
print('Total Votes: ' + str(counter))
print('------------')
for talley in vote_talley:
    print(str(talley[0]) + ': ' + str(round(((talley[1]/counter)*100),3)) + '% (' + str(talley[1]) + ')')
print('------------')

def takeSecond(elem):
    return elem[1]

vote_talley.sort(key=takeSecond)

print('Winner: ' + str(vote_talley[-1][0]))

print('------------')