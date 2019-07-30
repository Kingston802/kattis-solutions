musicalNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

n = int(input())
melodyList = input().split()

for note in musicalNotes:
    noteScale = []
    for i in range(len(musicalNotes)):
        
