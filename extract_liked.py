from bs4 import BeautifulSoup

with open("liked.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

titles = [a.get("title") for a in soup.find_all("a", {"id": "video-title"}) if a.get("title")]

with open("liked_titles.txt", "w", encoding="utf-8") as out:
    for title in titles:
        out.write(title + "\n")

print(f"Am extras {len(titles)} titluri.")
