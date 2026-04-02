class Note:
    def __init__(self,text):
        self.text = text
    
    def __str__(self):
        return self.text  

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self,text):
        self.notes.append(Note(text))  
        return "Заметка добавлена"
    
    def show_notes(self):
        if not self.notes:
            print("Нет заметок")
            return 
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}. {note}")
    
    def delete_note(self,index):
        if 0 < index <= len(self.notes):
            del self.notes[index - 1]
            return "Заметка удалена"
        else:
            return "Номер заметки введен неправильно"
        
    def search_notes(self,keyword):
        found_notes = []
        for note in self.notes:
          if keyword.lower() in note.text.lower():
            found_notes.append(note)
        if found_notes:
            print("Найдены заметки:")
            for note in found_notes:
                print(note)
        else:
            print('Заметки не найдены')
    
    def save_to_file(self):
       with open("notes.txt", "w") as f:
          for note in self.notes:
              f.write(note.text + '\n')

    def load_from_file(self):    
        try:
            with open("notes.txt", "r") as f:
                for line in f:
                    self.notes.append(Note(line.strip()))
        except FileNotFoundError:
            print("Файл заметок не найден, начнем с пустого списка заметок")
    
manager = NotesManager()
manager.load_from_file()

while True:
    print("1 - Добавить заметку")
    print("2 - Показать заметки")
    print("3 - Удалить заметку")
    print("4 - Поиск заметок")
    print("5 - Выйти")

    choice = input('Выберите действие: ')

    if choice == "1":
        text = input('Введите текст заметки:')
        print(manager.add_note(text))

    elif choice == "2":
        manager.show_notes()
    
    elif choice == "3":
        try:
            index = int(input("Введите номер заметки для удаления: "))
            print(manager.delete_note(index))
        except ValueError:
            print("Нужно ввести число")
    
    elif choice == "4":
        keyword = input("Введите ключевое слово для поиска: ")
        manager.search_notes(keyword)
    
    elif choice == "5":
        manager.save_to_file()
        print("Заметки сохранены. До свидания!")
        break
    else:
        print("Нверный выбор, попробуйте снова")



