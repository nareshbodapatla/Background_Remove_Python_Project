# Background Removal Python Script

This Python script utilizes the `rembg` and `PIL` modules to remove the background from an image.


## Installation

Make sure you have Python installed on your system. Additionally, install the required modules by running:


```bash
pip install rembg 
pip install Pillow
```

## How to Run
### 1.Clone the Repository: 
Clone this repository to your local machine using Git or download the ZIP file and extract it.

### 2.Navigate to Directory: 
Open a terminal or command prompt and navigate to the directory where you extracted/cloned the repository.

### 3.Set Up Input Image:
Place the image from which you want to remove the background in the same directory as the Python script. Ensure the image is named `carimage.png` or modify the `input_path` variable in the script to match the filename and path of your image.

### 4.Run the Script: 
Execute the following command:

```bash
python background_removal.py
```

### 5.Check Output: 
Once the script has run successfully, you will find the output image named `carimage-removebg.png` in the same directory. This image will have the background removed.

## Notes
- Make sure the input image is in a format supported by the `PIL` module (e.g., PNG, JPEG).
- Depending on the complexity of the image and the system's processing power, the background removal process may take some time.
