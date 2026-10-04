import re

path = r"C:\Users\himan\.gemini\antigravity\brain\ca103408-4dc0-4e9c-879d-bb41832b803f\.system_generated\steps\1551\content.md"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

urls = re.findall(r'https://myseoquery\.com/wp-content/uploads/[^\"\'\s\<\>]+', content)
clean = set()
for u in urls:
    if any(u.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
        clean.add(u)

for c in sorted(clean):
    print(c)
