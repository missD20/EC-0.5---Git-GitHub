
# Adding a comment to commit changes for EC 0.5
import csv 

# Dictionary to store results
stats = {}

# Open and read the CSV file
with open('friend-count.csv', newline='') as file:
    reader = csv.DictReader(file)

    print(reader.fieldnames)

    for row in reader:
        name = row['USER']
        friends = int(row[' FRIENDCOUNT'])

        first_letter = name[0].upper()

        if first_letter not in stats:
            stats[first_letter] = {'users': 0, 'friends': 0}

        stats[first_letter]['users'] += 1
        stats[first_letter]['friends'] += friends

# Print results in alphabetical order
for letter in sorted(stats.keys()):
    users = stats[letter]['users']
    total_friends = stats[letter]['friends']
    print(f"{letter} - {users} users, {total_friends} total friends")