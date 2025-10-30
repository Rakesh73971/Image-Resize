
## 🖼️ Image Resize and Conversion Script

### 🎯 **Objective**

The objective of this project is to **resize and convert multiple images in batch** using **Python** and the **Pillow** library.

---

### 🧰 **Tools & Technologies**

* **Language:** Python
* **Library:** Pillow (PIL Fork)
* **Modules Used:** `os`, `PIL.Image`

---

### 📦 **Setup Instructions**

1. **Install Pillow**

   ```bash
   pip install pillow
   ```

2. **Prepare Folders**

   * Create an **`images`** folder in the same directory as the script.
   * Place all the images you want to resize inside it.

3. **Script Configuration**

   * You can change these values in the script:

     ```python
     input_folder = "images"
     output_folder = "resized_images"
     new_size = (400, 400)
     ```

4. **Run the Script**

   ```bash
   python resize_images.py
   ```

---

### ⚙️ **How It Works**

1. The script loops through all image files in the input folder.
2. Each image is opened using the **Pillow** library.
3. The image is **resized** to the specified dimensions.
4. The resized image is **saved** into the output folder (converted to `.jpg` format).

--

### 💡 **Features**

* Batch resizing of multiple images.
* Automatic conversion to `.jpg` format.
* Creates output folder automatically if it doesn’t exist.
* Easy to modify size and format.

---

### 🚀 **Example Output**

After running the script:

```
 Saved: resized_images/img1.jpg
 Saved: resized_images/img2.jpg
 All images resized successfully!
```

---

### 📚 **Future Improvements**

* Maintain original aspect ratio using `thumbnail()`.
* Add command-line arguments for size and format.
* Add image compression support.

---

