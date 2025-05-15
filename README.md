# Extract Liked YouTube Video Titles

This repository contains a lightweight Python script that extracts all video titles from your personal **"Liked videos"** playlist on YouTube — without needing an API key or YouTube login inside the script. All you have to do is **save the playlist page as HTML**, and the script will extract all the titles.

---

## 📌 Why use this?

YouTube does not provide public access to your "Liked videos" playlist via API or URL unless you are logged in, and even then, it's private by default. This script is a simple way to retrieve your liked video titles for:

- Keeping personal archives
- Creating media lists
- Generating watch history or playlists elsewhere
- Reference for educational/research purposes

---

## 📂 How it works

1. You manually log into your YouTube account.
2. You open your "Liked videos" playlist.
3. You scroll all the way down until **all videos are loaded**.
4. You save the HTML page locally.
5. You run this script, and it will parse the file and extract all titles into a `.txt` file.

---

## ✅ Requirements

- Python 3.x installed
- `beautifulsoup4` Python package (see below)
- A saved HTML page of your "Liked videos" playlist

---

## 🖥️ Setup Instructions

### If you **do not have Python** installed:

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version for your OS (Windows/macOS/Linux)
3. During installation, **make sure to check the box**: `Add Python to PATH`
4. Finish the installation and restart your computer (if necessary)

---

## ⚙️ Install dependencies

Open your terminal (or PowerShell on Windows), then run:

```bash
pip install beautifulsoup4
```

If `pip` doesn’t work, try:

```bash
python -m pip install beautifulsoup4
```

---

## 🧠 How to Save Your "Liked Videos" Playlist

1. Go to [https://www.youtube.com/playlist?list=LL](https://www.youtube.com/playlist?list=LL) while logged into your account
2. **Scroll down to the bottom of the page** to load all videos (important!)
3. Right click anywhere on the page → `Save as...`
4. Choose **"Webpage, HTML only"** and save the file (e.g., `liked.html`)

Place this file in the same folder as the script.

---

## ▶️ How to run the script

After saving the HTML page and placing the script in the same folder:

1. Open Terminal or PowerShell
2. Navigate to the folder where the script and HTML file are:
```bash
cd path/to/your/folder
```

3. Run the script:
```bash
python extract_liked.py
```

After completion, you'll find a `liked_titles.txt` file with all the extracted titles.

---

## 📝 Output

- **Input**: `liked.html` (YouTube page saved locally)
- **Output**: `liked_titles.txt` (plain list of video titles)

---

## 📌 Note

This script does **not** collect or send data anywhere. All processing is done locally, and your saved YouTube page is never uploaded.

---

## 📃 License

This project is released under the MIT License.
