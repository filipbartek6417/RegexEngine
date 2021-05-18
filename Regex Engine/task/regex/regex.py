pair = input().split('|')
match = 'True'
for index, item in enumerate(pair[0]):
    try:
        if item != pair[1][index] and item != '.':
            match = 'False'
            break
    except IndexError:
        match = 'False'
        break
print(match)
