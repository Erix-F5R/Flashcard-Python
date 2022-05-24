<h2>Flashcard-Python</h2>

This two part program webscrapes from wiktionary.org to build Anki flashcards that quiz the user on french noun genders.

Using python and the BeautifulSoup4 library, this program first constructs a dictionary from <a href="https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants">a list of common french words.</a>

Then it grabs the gender and english translations for each word from <a href="https://fr.wiktionary.org">fr.wikitionary.org</a> via a request using the Wikimedia API. 

The final flashcards are outputed to deck.txt and formatted in the Anki flashcard standard. You can download the deck to use on your computer or or the mobile AnkiDroid app <a href="https://ankiweb.net/shared/info/195459672">here</a>
