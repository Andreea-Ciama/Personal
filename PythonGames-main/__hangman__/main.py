from repo import FileRepo
from validators import ValidateSentence
from controller import SentenceController
from ui import Console

repoSentences = FileRepo('Hangman.txt')

validateSentence = ValidateSentence()

sentenceController = SentenceController(repoSentences, validateSentence)

console = Console(sentenceController)

console.run()