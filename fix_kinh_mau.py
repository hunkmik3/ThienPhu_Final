import os

source_dir = "source/images/products"
old_name = "kinh-mau_257325068975.webp"
new_name = "kinh-mau.webp"

old_path = os.path.join(source_dir, old_name)
new_path = os.path.join(source_dir, new_name)

if os.path.exists(old_path):
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    except Exception as e:
        print(f"Error renaming {old_name}: {e}")
else:
    print(f"File not found: {old_name}")
    # Check if maybe it was already renamed or I missed it
    files = os.listdir(source_dir)
    print("Files in directory:")
    for f in files:
        if "mau" in f:
            print(f)
