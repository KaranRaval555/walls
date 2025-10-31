
import os

# --- CONFIG ---
ROOT_DIR = "."  # repo root (where this script is)
OUTPUT_FILE = "README.md"
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

# --- HEADER TEMPLATE ---
README_HEADER = """# 🖼️ Wallpaper Collection

A curated collection of wallpapers organized by categories.  
Click any thumbnail below to view the full-resolution image!

---

"""

def generate_markdown():
    lines = [README_HEADER]
    
    for folder, _, files in sorted(os.walk(ROOT_DIR)):
        # Skip hidden folders or git stuff
        if folder.startswith("./.") or folder == ".":
            continue
        
        # Get only image files
        images = [f for f in sorted(files) if f.lower().endswith(IMAGE_EXTENSIONS)]
        if not images:
            continue
        
        # Folder title
        folder_name = os.path.basename(folder)
        lines.append(f"## 📁 {folder_name}\n")
        
        # Add each image as clickable thumbnail (HTML for consistent sizing)
        for img in images:
            img_path = os.path.join(folder, img).replace("\\", "/")
            lines.append(f'<a href="{img_path}"><img src="{img_path}" width="200"/></a> ')
        
        lines.append("\n---\n")
    
    return "\n".join(lines)


def main():
    md_content = generate_markdown()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ README.md generated with wallpaper thumbnails!")


if __name__ == "__main__":
    main()
