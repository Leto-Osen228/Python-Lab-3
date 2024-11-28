import imageio
from PIL import Image
import os

input_gif = "animation.gif"
output_folder = "frames"
size = (500, 300)

gif = imageio.mimread(input_gif)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i, frame in enumerate(gif):
    img = Image.fromarray(frame)
    img_resized = img.resize(size)
    img_resized.save(os.path.join(output_folder, f"frame_{i}.png"))
    print(f"Frame {i} saved as frame_{i}.png")

print(f"All frames have been saved to {output_folder}")
