import os
import shutil

source_dir = "source/images/products"

# Define mappings from current (potentially problematic) name to new safe name
# Using exact strings from provided list + observation
renames = {
    "Kính Điện (Smart Film).jpeg": "kinh-dien-smart-film.jpeg",
    "kính ghép vải.jpg": "kinh-ghep-vai.jpg",
    "kính gương.jpg": "kinh-guong.jpg",
    "kinh in men.jpg": "kinh-in-men.jpg",
    "kính lowe.jpg": "kinh-low-e.jpg",
    "kinh phan quang.jpg": "kinh-phan-quang.jpg",
    "kinh phu nano.jpg": "kinh-phu-nano.jpg",
    "kinh sieu trong.webp": "kinh-sieu-trong.webp",
    "kính-hộp-solar.png": "kinh-hop-solar.png",
    # Including these just in case users want consistent naming, though they are fine
    # "kinh-in-hoa-van-mo-3.jpg" -> keep
    # "kinh-mau_257325068975.webp" -> keep
    # "kinh-moi-phun-cat.jpg" -> keep
    # "kinh-mo-nhung-axit.jpg" -> keep
    # "kinhuongcong.jpg" -> keep
    # "kinhcuongluc.jpg" -> keep
    # "kinh-cuong-luc-2-lop-3.jpg" -> keep
    # "kinh-hop-an-toan.jpg" -> keep
}

# Also handle the solar one carefully due to unicode decomposition
# I'll try to find the file via listing if exact match fails
files = os.listdir(source_dir)

for old_name, new_name in renames.items():
    old_path = os.path.join(source_dir, old_name)
    new_path = os.path.join(source_dir, new_name)
    
    if os.path.exists(old_path):
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")
    else:
        # fuzzy match check for solar file specifically or others
        # Check if file exists with different normalization
        found = False
        for f in files:
            # simple normalization check by encoding (rough)
            if f == old_name: 
                # Should have been caught by exists, but maybe some other issue
                pass
            # Try to match manually for the solar file if exact string failed
            if "solar" in old_name and "solar" in f:
                 # assume this is it if it's the only solar file
                 print(f"Potential match for {old_name}: {f}")
                 try:
                     os.rename(os.path.join(source_dir, f), new_path)
                     print(f"Renamed (fuzzy): {f} -> {new_name}")
                     found = True
                 except Exception as e:
                     print(f"Error renaming {f}: {e}")
        
        if not found:
            print(f"File not found: {old_name}")

print("Renaming complete.")
