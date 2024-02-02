import os

# Step 1: Create a text file with five lines of a love song on the Desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
source_file_path = os.path.join(desktop_path, 'love_song_1.txt')
destination_file_path = os.path.join(desktop_path, 'love_song_2.txt')

love_song_lyrics = """I love you like a river flows
Gentle, but strong, it always grows
With every beat of my heart
Our love will never depart
Forever and always, you are the one"""

with open(source_file_path, 'w') as source_file:
    source_file.write(love_song_lyrics)

# Step 2: Copy the content to a newly created text file
with open(source_file_path, 'r') as source_file:
    lyrics_content = source_file.read()

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(lyrics_content)

# Display the copied content
with open(destination_file_path, 'r') as copied_file:
    copied_lyrics = copied_file.read()
    print("Content of love_song_2.txt:")
    print(copied_lyrics)
