import json
import uuid
from datetime import datetime

def create_note():
    """Crearing note function"""
    title = input("Type header of the note: ")
    text = input("Type the note: ")
    note_id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": note_id, "title": title, "text": text, "created_at": created_at}
    with open("notes.json", "a") as f:
        json.dump(note, f)
        f.write("\n")
    print("Note created successfully")

def list_notes():
    """Showing list of the notes function"""
    with open("notes.json", "r") as f:
        notes = [json.loads(line) for line in f]
    try:
        for note in notes:
            print(f"{note['id']}: {note['title']} ({note['created_at']})")
    except:
        print("Not any note in notebook")

def read_note():
    """Edit note function"""
    note_id = input("Input note ID: ")
    with open("notes.json", "r") as f:
        notes = [json.loads(line) for line in f]
    for note in notes:
        if note["id"] == note_id:
            print(note["text"])
        return
    else:
        print("Error. Note is not found")

def edit_note():
    """Edit note function"""
    note_id = input("Input note ID: ")
    with open("notes.json", "r") as f:
        notes = [json.loads(line) for line in f]
    for note in notes:
        if note["id"] == note_id:
            title = input("Input new header of the note: ")
            text = input("Type new text of the note: ")
            note["title"] = title
            note["text"] = text
            note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
        else:
            print("Error. Note is not found")
        return
    with open("notes.json", "w") as f:
        for note in notes:
            json.dump(note, f)
            f.write("\n")
    print("Note edited successfully.")

def delete_note():
    note_id = input("Input note ID to delete: ")
    with open("notes.json", "r") as f:
        notes = [json.loads(line) for line in f]
    notes = [note for note in notes if note["id"] != note_id]
    with open("notes.json", "w") as f:
        for note in notes:
            json.dump(note, f)
            f.write("\n")
        
    print("Note deleted.")

def show_menu() -> int:
    """Menu function"""
    print("\nPlease input action number:\n"
          "1. Show notes list\n"
          "2. Read the note\n"         
          "3. Create note\n"
          "4. Edit note\n"
          "5. Delete note\n"
          "6. Exit")
    choice = int(input())
    return choice

choice = show_menu()

while (choice != 6):
    if choice == 1:
        list_notes()
    elif choice == 2:
        read_note()        
    elif choice == 3:
        create_note()
    elif choice == 4:
        edit_note()
    elif choice == 5:
        delete_note()
    choice = show_menu()
