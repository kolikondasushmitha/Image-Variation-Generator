Image Variation Generator

Overview

The Image Variation Generator is a Python-based application that allows users to upload an image from their device and view multiple variations of that image with different levels of saturation, contrast, and brightness. The application provides a user-friendly interface where users can select their desired image variation and save it directly to their device.

This project leverages the power of the Python Imaging Library (PIL) and Seaborn to create visually appealing UI elements and process images efficiently. The application generates 55 unique variations of the uploaded image, giving users a range of choices to select from.

Features

Upload Image: Users can upload any image from their device.
Image Variations: Generates 55 variations of the uploaded image by adjusting the saturation, contrast, and brightness.
Thumbnail Display: Variations are displayed as thumbnails with their respective parameters.
Selection & Save: Users can click on a thumbnail to select a variation and save the chosen variation to their device in PNG format.
Progress Bar: A progress bar provides visual feedback during the image upload process.

Technologies Used

Python: The core programming language used to develop the application.
Tkinter: For building the graphical user interface.
Pillow (PIL): Used for image processing, including adjustments to saturation, contrast, and brightness.
Seaborn: Used for theming UI elements with a pleasant color palette.
NumPy: For generating the range of values used to create the image variations.
