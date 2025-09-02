import sys
sys.path.append("../src/pagesizey")

from pagesizey import page_size

print(f"[38;5;38mTEST 1: 24x36.[0m")
size = page_size(24, 36)
print(size)

print(f"[38;5;38mTEST 2: 36x24.[0m")
size = page_size(36, 24)
print(size)

print(f"[38;5;38mTEST 3: 36x22.[0m")
size = page_size(34, 22)
print(size)

print(f"[38;5;38mTEST 4: 14.5x19.5.[0m")
try:
    size = page_size(14.5, 19.5)
    print(size)
except Exception as e:
    print(f"[38;5;196m    {str(e)}[0m")

print(f"[38;5;38mTEST 5: 8.5x11.[0m")
size = page_size(8.5, 11)
print(size)

print(f"[38;5;38mTEST 6: 841x1189 (ISO).[0m")
size = page_size(841, 1189)
print(size)

print(f"[38;5;38mTEST 7: 5.8x8.3 (Cursed ISO).[0m")
size = page_size(5.8, 8.3)
print(size)

print(f"[38;5;38mTEST 8: 33.1x46.8 (Cursed ISO).[0m")
size = page_size(33.1, 46.8)
print(size)

print(f"[38;5;38mTEST 9: 250x176 (ISO).[0m")
size = page_size(250, 176)
print(size)