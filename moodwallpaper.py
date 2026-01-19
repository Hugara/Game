import ctypes
import os

# Function to change wallpaper
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, image_path, 3
    )

# Mood to wallpaper mapping
def change_wallpaper_by_mood(mood):
    base_path = os.getcwd()

    wallpapers = {
        "happy": os.path.join(base_path, "happy.jpg"),
        "sad": os.path.join(base_path, "sad.jpg"),
        "calm": os.path.join(base_path, "calm.jpg"),
        "energetic": os.path.join(base_path, "energetic.jpg")
    }

    if mood in wallpapers:
        set_wallpaper(wallpapers[mood])
        print(f"Wallpaper changed for mood: {mood}")
    else:
        print("Invalid mood selected")

# Main program
print("Select your mood:")
print("happy | sad | calm | energetic")

user_mood = input("Enter mood: ").lower()
change_wallpaper_by_mood(user_mood)
