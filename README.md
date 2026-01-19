# Game
Mood wallpaper change using python
A mood-based wallpaper system automatically changes your desktop wallpaper based on a detected or selected user mood such as:
Happy 😊
Sad 😔
Calm 😌
Energetic ⚡
Focus 🎯
This improves user experience, motivation, and mental well-being.
2️⃣ How Mood Can Be Detected (Concepts)
There are 3 common approaches:
🔹 1. Manual Mood Input (Beginner – Recommended)
User selects mood:
Copy code
Text
happy / sad / calm / energetic
🔹 2. Time-Based Mood (Intermediate)
Time
Mood
Morning
Energetic
Afternoon
Focus
Evening
Calm
Night
Relax
🔹 3. AI / Emotion Detection (Advanced)
Webcam + OpenCV
NLP sentiment analysis
Wearables (heart rate, etc.)
👉 For clarity and reliability, we’ll implement manual mood selection.
3️⃣ System Architecture
Copy code

User Mood Input
       ↓
Mood-to-Wallpaper Mapping
       ↓
Python Wallpaper Change Function
       ↓
OS Desktop Wallpaper Updated
4️⃣ Requirements
🖥 Software
Python 3.x
Windows OS (code is Windows-specific)
📁 Folder Structure
Copy code

MoodWallpaper/
│
├── happy.jpg
├── sad.jpg
├── calm.jpg
├── energetic.jpg
├── mood_wallpaper.py
5️⃣ How Wallpaper Change Works in Windows
Windows uses a system API:
Copy code
Python
SystemParametersInfoW()
Python accesses it using the ctypes library.
