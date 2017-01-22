# writelist
# lines = ["we'll find a way we always have - Interstellar\n",
#         "I'll find you and I'll kill you - Taken\n",
#         "I'll be back - Terminator 2\n"]

# with open('movie_quotes.txt', 'w') as file:
#     for line in lines:
#         file.write(line)

# with open('movie_quotes.txt', 'w') as file:
#     file.writelines(lines)

# with open('movie_quotes.txt', 'r') as file:
#     lines = file.readlines()
#     line = ''
#     for line in lines:
#         print(line, end='')

lines = ['안녕하세요?\n', 
        'こんにちは\n',
        '你好\n']

# with open('greetings_utf8.txt', 'w', encoding='utf-8') as file:
#     for line in lines:
#         file.write(line)

# with open('greetings_utf8.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     line = ''
#     for line in lines:
#         print(line, end='')

with open('greetings_utf8.txt', 'r', encoding='ascii', errors='ignore') as file:
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end='')