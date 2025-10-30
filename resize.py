from PIL import Image
import os


input_folder = "old images"          
output_folder = "new images" 
new_size = (400, 400)            


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        resized_img = img.resize(new_size)
        

        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        resized_img.save(output_path, "JPEG")
        
        print(f"Saved: {output_path}")

print("All images resized successfully!")
