import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
clean_text = re.sub(r'http\S+|@\S+|#[^\s]+|[^\w\s]', '', raw_text).lower()
print("Tīrs teksts:", clean_text)
