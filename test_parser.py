import csv
import io
import re

with open("raw_contacts.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's clean up multiline quotes like:
# "
# 02ZPEKKKF8702"
# and "02ZPEAJMM8702\n"
text = re.sub(r'"\s*\n\s*', '"', text)
text = re.sub(r'\s*\n\s*"', '"', text)

# Let's inspect rows using csv.reader
reader = csv.reader(io.StringIO(text))
rows = list(reader)
print(f"Total rows read: {len(rows)}")

valid_blocks = [
    "Chandrapur", "Bhadrawati", "Warora", "Chimur", "Mul", "Sawali",
    "Nagbhid", "Sindewahi", "Bramhapuri", "Ballarpur", "Rajura",
    "GondPipari", "Pombhurna", "Korpana", "Jiwati"
]

block_map = {b.lower(): b for b in valid_blocks}
block_map["bhadravati"] = "Bhadrawati"

current_block = ""
parsed = []
skipped = []

for idx, r in enumerate(rows):
    # Strip whitespace from each cell
    cells = [c.strip() for c in r]
    if not any(cells):
        continue
    # Check if header row
    if any("Block Name" in c or "Gram Sewak" in c or "Sewarth ID" in c for c in cells):
        continue
    
    # Analyze row structure
    # Typically: [sr_no, block_name, gp_name, name, sewarth, email, phone, ...]
    # But sometimes sr_no is missing, e.g. ",Chandrapur,Nakoda,Kishor Mahadeo Dhakate,..."
    # Or block is in cell 1, or block is empty and gp_name is in cell 2, etc.
    
    # Let's see if any cell matches a block name
    found_block = None
    for c in cells[:3]:
        clow = c.lower().strip()
        if clow in block_map:
            found_block = block_map[clow]
            break
        for b in valid_blocks:
            if b.lower() in clow:
                found_block = b
                break
        if found_block:
            break
            
    if found_block:
        current_block = found_block
        
    print(f"Row {idx}: found_block={found_block}, cells={cells[:5]}")
