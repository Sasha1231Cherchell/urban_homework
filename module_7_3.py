class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = dict()
        for filename in self.file_names:
            with open(filename, "r", encoding="utf-8") as file:
                file_text = file.read().lower()
                for s in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file_text = file_text.replace(s, "")
                all_words[filename] = file_text.split()

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = dict()
        lower_word = word.lower()
        for key in all_words.keys():
            if lower_word in all_words[key]:
                result[key] = all_words[key].index(lower_word) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = dict()
        lower_word = word.lower()
        for key in all_words.keys():
            if lower_word in all_words[key]:
                result[key] = all_words[key].count(lower_word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('captain')) # 3 слово по счёту
print(finder2.count('captain')) # 4 слова teXT в тексте всего