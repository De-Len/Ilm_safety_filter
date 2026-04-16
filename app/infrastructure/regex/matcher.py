from badwords import ProfanityFilter

class RegexMatcher:
    def __init__(self):
        self.p = ProfanityFilter()
        self.p.init(languages=["en", "ru"])  # загружаем английский и русский

    def is_toxic(self, text):
        return self.p.filter_text(text)

