# large 1600x900
for f in assets/originals/*.{jpg,png}; do
  magick "$f" -resize 1600x900^ -gravity center -extent 1600x900 -quality 85 "assets/large/$(basename "$f")"
done

# medium 800x450
for f in assets/originals/*.{jpg,png}; do
  magick "$f" -resize 800x450^ -gravity center -extent 800x450 -quality 82 "assets/medium/$(basename "$f")"
done

# thumb 420x236
for f in assets/originals/*.{jpg,png}; do
  magick "$f" -resize 420x236^ -gravity center -extent 420x236 -quality 80 "assets/thumbs/$(basename "$f")"
done
