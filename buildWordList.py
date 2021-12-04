from pathlib import Path

with open('word_list.txt', 'w') as f:
    for file in Path('./_posts').glob('*.md'):
        word = ' '.join(file.stem.split('-')[3:])
        f.write(word + '\n')
