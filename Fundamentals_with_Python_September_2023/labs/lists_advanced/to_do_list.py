def sort_notes():
    notes = []

    while True:
        note = input()

        if note == "End":
            break
        notes.append(note)

    sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
    return [note.split("-")[1] for note in sorted_notes]


result = sort_notes()
print(result)