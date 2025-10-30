import sys
import cv2

if len(sys.argv) != 3:
    print("Usage: python imgconv.py <source_file> <destination_file>")
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

img = cv2.imread(src)
if img is None:
    print(f"Error: cannot read source file '{src}'")
    sys.exit(1)

if not cv2.imwrite(dst, img):
    print(f"Error: cannot write destination file '{dst}'")
    sys.exit(1)