# Challenge Ref: https://twitter.com/learn_byexample/status/1484142816750374916

# read file
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines

# function that takes list of lines and returns list of lines with duplicates removed irrespective of word order
# seperator is a space
# so - hehe haha and haha hehe are the same

def dedupe_lines_words(lines):
    lines = [line.split() for line in lines] # split lines into words
    lines = [sorted(line) for line in lines] # sort words in each line
    lines = [' '.join(line) for line in lines] # join words in each line
    lines = list(set(lines)) # remove duplicates
    return lines

print(read_file('twos.txt'))
print(dedupe_lines_words(read_file('twos.txt')))

# Original
# ['hehe haha', 'door floor', 'haha hehe', '6:8 3-4', 'true blue', 'hehe bebe', 'floor door', '3-4 6:8', 'tru eblue', 'haha hehe']
# Solution
# ['haha hehe', 'door floor', 'bebe hehe', 'eblue tru', '3-4 6:8', 'blue true']
