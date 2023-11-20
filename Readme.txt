# Image Multiplication and Download

This simple Python program provides a graphical user interface for selecting an image, multiplying it to fit a predefined SRA3 page size, and saving the resulting image to a file.

## Requirements

- Python 3.x
- Tkinter (included in most Python installations)
- Pillow (PIL) library (install using `pip install Pillow`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/image-multiplication.git
    ```

2. Open the project in PyCharm:

   - Launch PyCharm.
   - Choose "Open" and select the project directory.

3. Set up a Python interpreter:

   - Open the "File" menu.
   - Select "Settings."
   - Under "Project," choose "Python Interpreter."
   - Ensure the Project Interpreter points to your Python interpreter.

4. Install required libraries:

    - Open the terminal in PyCharm.
    - Run the following command:

        ```bash
        pip install Pillow
        ```

5. Run the program:

    - Open the main Python file (`main.py`) in the project.
    - Right-click on the file in the editor.
    - Select "Run 'main.'"

6. Follow the on-screen instructions to:

   - Click "Select Image" to choose an image file.
   - Click "Image replication and Download" to multiply the image to fit the SRA3 page and save the result.

6. Arhitecture Diagram (In textual representation)


The Image Multiplication and Download application architecture is a simple GUI-based Python program. The key components include:

    User Interface (UI):
        Developed using the Tkinter library.
        Three buttons: "Select Image," "Send," and "Download Image."
        A label to display messages and status updates.

    Image Processing:
        Utilizes the Pillow (PIL) library for image manipulation.
        Loading, resizing, and pasting the image onto the SRA3 page.

    File Handling:
        Uses the filedialog module for selecting and saving files.

7. Flow Diagram
Select Image Flow:

    User clicks the "Select Image" button.
    File dialog opens for image selection.
    User selects an image file.
    Selected image is loaded and displayed in the UI.

Image replication and Download Flow:

    User clicks the "Image replication and Download" button.
    If an image is selected:
        Image is multiplied to completely fit the SRA3 page.
        Resulting image is displayed in a pop-up window.
    If no image is selected, an appropriate message is displayed.
    If an image is replicated and displayed:
        File dialog opens for choosing a save location.
        User specifies a file name and clicks "Save."
        Replicated image is saved to the specified location.
    If no image is replicated, an appropriate message is displayed.