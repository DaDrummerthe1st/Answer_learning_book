# 9.
print('\n')
print("""
        9.
    a) Genom att använda en f-string med de två variablerna founder
    och language, printa ut texten “Hello Guido, Python is really
    fun to learn!”
    b) Du vill nu skriva ut hela namnet “Guido van Rossum” så texten
    blir “Hello Guido van Rossum, Python is really fun to learn!”.
    Gör det genom att ändra namnet i variabeln founder och exe-
    kvera din f-string på nytt.
    founder = "Guido"
    language = "Python"
""")

class TextAnswer():
    '''
    Takes two argument (founder, language)

    The method print_it() takes these two arguments and prints the sentence:
    Hello {founder}, {language} is really fun to learn!
    '''
    def __init__(self, *, founder, language):
        self.founder = founder
        self.language = language

    def print_it(self):
        whole_sentence = f'Hello {self.founder}, {self.language} is really fun to learn!'
        print(whole_sentence)
        return whole_sentence

nine_a = TextAnswer(founder = "Guido", language = "Python").print_it()
nine_b = TextAnswer(founder = "Guido van Rossum", language = "Python").print_it()
print(TextAnswer.__doc__)