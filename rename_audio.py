import os
files = {
    'music.mp3': 'music_v2.mp3',
    'shine-6-268910.mp3': 'shine_v2.mp3',
    'restoretree-button.mp3': 'restore_v2.mp3',
    'shifting-effect.mp3': 'shifting_v2.mp3',
    'spreading-effect.mp3': 'spreading_v2.mp3'
}
for old, new in files.items():
    if os.path.exists(old):
        if os.path.exists(new):
            os.remove(new) # Ensure target doesn't exist
        os.rename(old, new)
        print(f"Renamed {old} to {new}")
    else:
        print(f"File {old} not found (maybe already renamed)")
