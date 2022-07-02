from abc import ABC,abstractmethod

class AbstractTextConverter(ABC):
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def convert(self):
        print(self)
        text = self.read_text()
        print('Starting converting the text.', self.read_from(),'Before:', text)
        print('Done! Result:', self.strategy(text))

    @abstractmethod
    def read_text(self):
        pass

    @abstractmethod
    def read_from(self):
        pass

class InputTextConverter(AbstractTextConverter):

    def read_text(self):
        return input('Enter your text...')

    def read_from(self):
        return 'Read from input'

class FileTextConverter(AbstractTextConverter):

    def read_text(self):
        text = ''
        with open('file-text.txt', 'r') as file:
            text = file.read()
        return text

    def read_from(self):
        return 'Read from file'

class UkraineTextConverter(AbstractTextConverter):

    def read_text(self):
        return 'Ukraine'
    
    def read_from(self):
        return 'From Ukraine'

itc = InputTextConverter(lambda s : s.title())
itc.convert()

ftc = FileTextConverter(lambda s : s.upper())
ftc.convert()

utc = UkraineTextConverter(lambda s : s.lower())
utc.convert()