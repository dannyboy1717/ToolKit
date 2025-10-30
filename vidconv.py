import sys
import cv2

if len(sys.argv) != 3:
    print("Usage: python vidconv.py <source_file> <destination_file>")
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

cap = cv2.VideoCapture(src)
if not cap.isOpened():
    print(f"Error: cannot open source file '{src}'")
    sys.exit(1)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(dst, fourcc, fps, (width, height))
if not out.isOpened():
    print(f"Error: cannot open destination file '{dst}' for writing")
    cap.release()
    sys.exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

cap.release()
out.release()