# Create class that in your opinion can perfectly represent the book
# You can create more than 1 class if you want
# Your fields should be with the corresponding type [str,int,bool,list,etc]
# Create an object of your class

class Book:
    def __init__(self, name: str, autor: str, genre: str, punlishing_house: str, year: int, pages: int, language: str):
        self.name = name # +
        self.autor=autor # -
        self.genre=genre # +
        self.punlishing_house=punlishing_house # +
        self.year=year # +
        self.pages=pages 
        self.language=language # +
    def __init__(self,foreword:str,chapter_number:int,chapter_name:str,) :
            self.foreword=foreword
            self.chapter_number=chapter_number
            self.chapter_name=chapter_name
book1=Book("Тайный клуб психопатов"," Вера Куриан","Детектив","Эксмо",2022,460,"Russian")
book1=Book("Для всех Хлоя Севр – отличница-первокурсница, красотка, обожающая фитнес и студенческие вечеринки… Но еще она – диагностированная психопатка. И прямо сейчас замышляет убийство давнего знакомого – этого придурка, посмевшего очень жестоко ее унизить. Хлоя – одна из семи студентов колледжа, участвующих в необычном эксперименте: клиническом исследовании психопатов – людей, не способных к эмпатии, никогда не испытывающих чувства вины, стыда или страха. Она согласилась на это, чтобы подобраться ближе к будущей жертве",1,"Обратный отсчёт")
