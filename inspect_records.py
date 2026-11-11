import csv
import io
import re

with open("raw_contacts.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(r'"\s*\n\s*', '"', text)
text = re.sub(r'\s*\n\s*"', '"', text)

reader = csv.reader(io.StringIO(text))
rows = list(reader)

valid_blocks = [
    "Chandrapur", "Bhadrawati", "Warora", "Chimur", "Mul", "Sawali",
    "Nagbhid", "Sindewahi", "Bramhapuri", "Ballarpur", "Rajura",
    "GondPipari", "Pombhurna", "Korpana", "Jiwati"
]

block_map = {b.lower(): b for b in valid_blocks}
block_map["bhadravati"] = "Bhadrawati"
block_map["bhadrawati "] = "Bhadrawati"

contract_keywords = [
    "कंत्राटी", "kantrati", "kantranti", "कंत्राटी ग्रा.प.अ.", "कंत्राटी ग्रा. प. अ", "कंत्राटी ग्रा.पं.अ",
    "कंत्राटी ग्रामपंचायत अधिकारी", "kantrati  gramsevak", "kantranti karmachari", "kantrati g.a."
]

def clean_phone(v):
    digits = re.sub(r'\D', '', str(v or ''))
    if digits.startswith('91') and len(digits) == 12:
        digits = digits[2:]
    return digits

def is_phone(v):
    cp = clean_phone(v)
    return len(cp) >= 10

def is_email(v):
    return '@' in str(v)

records = []
current_block = "Chandrapur"

for idx, r in enumerate(rows):
    cells = [c.strip() for c in r]
    # Skip empty lines
    if not any(cells) or all(c == '' for c in cells):
        continue
    # Skip headers
    if any("Block Name" in c or "Gram Sewak's Full Name" in c for c in cells):
        continue
    
    # Try to find block name
    # Check if a cell exactly or approximately matches a block
    block_candidate = None
    for i in range(min(4, len(cells))):
        c_clean = cells[i].lower().strip()
        if c_clean in block_map:
            block_candidate = block_map[c_clean]
            break
        for b in valid_blocks:
            if b.lower() == c_clean:
                block_candidate = b
                break
    
    if block_candidate:
        current_block = block_candidate

    # Let's inspect the cells to identify fields:
    # We want: block, gram_panchayat, name, sewarth_id, email, phone, designation, remarks
    # Let's see:
    print(f"[{current_block}] row {idx}: {cells}")
