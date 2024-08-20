Overview
The Image Variation Generator is a Python-based desktop application that allows users to upload an image and automatically generate multiple variations by adjusting the image's saturation, contrast, and brightness. This tool is ideal for anyone looking to experiment with different visual effects on images quickly and easily.

Features
User-Friendly Interface:

The application features a simple and intuitive graphical interface using tkinter, making it accessible to users of all skill levels.
Image Uploading:

Users can upload any image file using an easy-to-use upload button that opens a file dialog to select the image.
Automatic Image Variations:

The application automatically generates a variety of image variations by adjusting the saturation, contrast, and brightness of the uploaded image.
Thumbnail Display:

Variations are displayed as thumbnails in a scrollable canvas, allowing users to easily browse through different versions of the image.
Responsive Layout:

The display layout adjusts dynamically based on the window size, ensuring a consistent and user-friendly experience across different screen sizes.
Detailed Image Information:

Each image variation is displayed with its corresponding saturation, contrast, and brightness values, allowing users to understand the adjustments made.
Image Selection and Saving:

Users can select any image variation and save it as a PNG file to their system.

Technologies Used
Python: The main programming language used to develop the application.
Tkinter: The standard Python interface to the Tk GUI toolkit, used for creating the graphical user interface.
Pillow (PIL): A Python Imaging Library that adds image processing capabilities to the application.
Numpy: Used for numerical operations, specifically to create ranges for the saturation, contrast, and brightness adjustments.
