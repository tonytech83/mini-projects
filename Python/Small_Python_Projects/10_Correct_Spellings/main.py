from spellchecker import SpellChecker

lang_mapper = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'pt': 'Portuguese',
    'de': 'German',
    'ru': 'Russian',
    'ar': 'Arabic',
    'eu': 'Basque',
    'lv': 'Latvian',
}

lang = input(
    """Chose your language:
    
    en - English        es - Spanish        fr - French 
    pt - Portuguese     de - German         ru - Russian 
    ar - Arabic         eu - Basque         lv - Latvian
    
Your chose is: """)

print()
print(f'You chosen {lang_mapper[lang]} from dictionaries')
print()
spell = SpellChecker(language=lang)

word = input('Enter your word: ')
print()

corrected_word = spell.correction(word)

if corrected_word is None:
    print(f'There no information about {word} into {lang_mapper[lang]} dictionary!')
else:
    # Get the one `most likely` answer
    print(f'The one `most likely` answer is: {corrected_word}')
    # Get a list of `likely` options
    print(f'Here is a list of `likely` options: {spell.candidates(word)}')

