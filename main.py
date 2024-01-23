import json
from datetime import datetime

class Notepad:
    def __init__(self):
        self.notes = []
        self.filename = "notes.json"
        try:
            with open(self.filename) as f:
                self.notes = json.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.notes, f)

    def add_note(self, title, body):
        note = {"id": len(self.notes), "title": title, "body": body, "timestamp": datetime.now().isoformat()}
        self.notes.append(note)
        self.save()

    def edit_note(self, note_id, title=None, body=None):
        note = self.get_note(note_id)
        if note:
            if title:
                note["title"] = title
            if body:
                note["body"] = body
            self.save()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note["id"] != note_id]
        self.save()

    def get_note(self, note_id):
        return next((note for note in self.notes if note["id"] == note_id), None)

    def display_notes(self):
        for note in self.notes:
            print(f"{note['id']}: {note['title']} - {note['timestamp']}")

    def display_note(self, note_id):
        note = self.get_note(note_id)
        if note:
            print(f"{note['id']}: {note['title']}\n{note['body']}\n{note['timestamp']}")

    def select_by_date(self):
        print("Enter a date (YYYY-MM-DD):")
        date = input()
        notes_on_date = [note for note in self.notes if datetime.fromisoformat(note["timestamp"]).date() == datetime.fromisoformat(date).date()]
        for note in notes_on_date:
            print(f"{note['id']}: {note['title']} - {note['timestamp']}")

    def exit(self):
        self.save()
        exit()

if __name__ == "__main__":
    notepad = Notepad()
    while True:
        print("\n1. Добавить заметку\n2. Изменить заметку\n3. Удалить заметку\n4. Показать все заметки\n5. Показать примечание\n6. Выбрать по дате\n7. Выход")
        choice = int(input("Введите свой выбор: "))
        if choice == 1:
            title = input("Введите название: ")
            body = input("Введите тело: ")
            notepad.add_note(title, body)
        elif choice == 2:
            note_id = int(input("Enter note id: "))
            title = input("Введите новое название (оставьте пустым, чтобы сохранить актуальность): ")
            body = input("Введите новое тело (оставьте пустым, чтобы сохранить актуальность): ")
            notepad.edit_note(note_id, title, body)
        elif choice == 3:
            note_id = int(input("Введите id: "))
            notepad.delete_note(note_id)
        elif choice == 4:
            notepad.display_notes()
        elif choice == 5:
            note_id = int(input("Введите id: "))
            notepad.display_note(note_id)
        elif choice == 6:
            notepad.select_by_date()
        elif choice == 7:
            notepad.exit()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")