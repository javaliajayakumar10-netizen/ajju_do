# 🚀 AJJU – YT Downloader PRO

**A powerful command-line YouTube downloader built with Python, powered by yt-dlp, and enhanced with a beautiful terminal UI using rich.**

# AJJU allows you to download:

**🎥 Videos in multiple resolutions (1080p, 720p, 480p)
🎵 Audio-only (MP3 format)
📂 Full playlists
📊 Real-time download progress bar
📁 Automatic save to your Downloads folder**

# 📌 Features:

**✅ Automatic dependency installation
✅ Playlist detection
✅ Resolution selector
✅ MP3 audio extraction (requires FFmpeg)
✅ Clean progress UI with speed & time remaining
✅ Saves files automatically to Downloads/**

# 🛠 Requirements:
```
Python 3.8+
pip
FFmpeg (required for MP3 conversion and merging)
```

# 📦 Installation:
**Option 1 — Install Globally (Recommended):**

```bash
git clone https://github.com/Ajay-do/ajju.git
cd ajju
pip install .
```
### Run from anywhere:
`ajju`

**Option 2 — Run Directly:**
```bash
git clone https://github.com/your-username/ajju.git
cd ajju
python -m ajju_do.py
```

### 2️⃣ Install Python (if not installed)

**Download from:**
`https://www.python.org/downloads/`

**Verify installation:**
```bash
python --version
```

**▶️ How to Run**
```bash
python ajju_do.py
```

**Or (if renamed to ajju.py):**
```bash
python ajju.py
```

**🔎 Check Version:**
```bash
python ajju_do.py --version
```

# 🎯 How to Use:
- **Run the script**
- **Paste the YouTube link**
- **If playlist is detected → choose:**
- **y → download full playlist**
- **n → download single video**

### Select quality:
- Option	Quality
1	Best (Auto)
2	1080p
3	720p
4	480p
5	Audio Only (MP3)

**Wait for download to complete**

Files will be saved in:
`C:\Users\YourName\Downloads`

Playlists will be saved in:
`Downloads/Playlist_Name/`

# 🎵 FFmpeg Installation (Important for MP3)
# Windows:
Download FFmpeg from:
`https://ffmpeg.org/download.html`

# Extract the folder
**Add bin folder to `System Environment Variables` → `PATH`
Restart terminal
Verify installation:
```bash
ffmpeg -version
```

# 📂 Project Structure:
```
Ajju-do/
│
├── ajju_do.py
|__ setup.py
|__ ajju.bat
└── README.md
```

# ⚙️ Built With:
- yt-dlp – YouTube downloading engine
- rich – Beautiful terminal UI
- argparse – CLI argument parsing
- FFmpeg – Audio extraction and merging

# 🛡 Notes:
**The script automatically installs missing Python dependencies.
Internet connection required.
FFmpeg must be installed separately for audio conversion.**

# 🎯 Recommended for GitHub Users:**
# Global CLI Setup (Windows)
# Clone repo
```bash
git clone https://github.com/your-username/Ajju-do.git
```

# Move to project folder
```bash
cd Ajju-do**
```

# Install locally
```python
pip install .**
```

# Run
```bash
ajju
```

After installation, you can run the tool globally from any directory using:
`ajju`

# 📜 License:
**Developed By `Javali Ajayakumar`** | © 2026 AJJU YT Downloader. All rights reserved.
