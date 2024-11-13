def custom_write(file_name, strings):
    strings_positions = dict()
    f = open(file_name, "a", encoding="utf-8")
    index = 1
    for s in strings:
        strings_positions[(index, f.tell())] = s
        index += 1
        f.write(s + "\n")
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
