import re
import json
import os

class SpellingConverter:
    def __init__(self):
        self.american_to_british = {}
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # # Path to the JSON file
        # json_file_path = os.path.join(script_dir, 'your_json_file.json')
        # print(f"json_file_path = {json_file_path}")
        
        filenames = ['american_spellings.json', 'additional_american_spellings.json']
        for filename in filenames:
            with open(os.path.join(script_dir, filename), 'r') as f:
                self.american_to_british.update(json.load(f))
        self.british_to_american = {value:key for key, value in self.american_to_british.items()}

    def wordBritishToAmerican(self, word):
        return self.convert(self.british_to_american, word)

    def wordAmericanToBritish(self, word):
        return self.convert(self.american_to_british, word)

    def convert(self, dictionary, word):
        converted = dictionary.get(word)
        if converted:
            return converted
        else:
            return word

    def split(self, sentence):
        # Use findall to get all matches
        return re.findall(r"(\w+|\s+|\W)", sentence)

    def britishToAmerican(self, sentence):
        return "".join(self.wordBritishToAmerican(word) for word in self.split(sentence))

    def americanToBritish(self, sentence):
        return "".join(self.wordAmericanToBritish(word) for word in self.split(sentence))

    def toggle(self, sentence):
        result = []
        for word in self.split(sentence):
            if word in self.american_to_british:
                result.append(self.american_to_british[word])
            elif word in self.british_to_american:
                result.append(self.british_to_american[word])
            else:
                result.append(word)
        return "".join(result)


if __name__ == "__main__":
    spelling_converter = SpellingConverter()
    spelling_converter.britishToAmerican("hello world subsidize")
    spelling_converter.americanToBritish("hello world subsidize")
    spelling_converter.toggle("customiser subsidize")

