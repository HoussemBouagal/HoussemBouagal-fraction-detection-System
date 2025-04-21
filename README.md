🦴 Bone Fracture Detection – Tkinter + Deep Learning App
<p align="center"> <img src="trauma.png" alt="App Icon" width="100"/> </p>
📌 Overview
This is a desktop GUI application built with Python and Tkinter to automatically detect bone fractures in X-ray images using a pre-trained deep learning model (TensorFlow/Keras).
💡 Features
🧠 Utilizes a trained Keras model to classify images as:

Fractured

Not Fractured

📷 Clean and user-friendly GUI to load and analyze X-ray images.

📊 Displays prediction confidence.

🖼️ Shows the loaded image in the interface.

👨‍💻 "About" window with developer information.

🎨 Sleek modern UI with soft colors.

🧪 Requirements
Make sure the following Python libraries are installed:
pip install tensorflow pillow numpy

🗂️ Project Structure
📁 fracture_detection_app/
├── fracture_model.keras        # Pre-trained model
├── trauma.png                  # App icon
├── main.py                     # Main application script
└── README.md                   # This file

🚀 How to Run:
Make sure all files (main.py, fracture_model.keras, trauma.png) are in the same directory.

Run the app using:
python main.py

Click 📂 Load Image to select an X-ray image.

The app will display:

The result: Fractured / Not Fractured

Prediction confidence

Click 👨‍💻 About to view developer info.

👨‍💻 Developer
Name: Bouagal Houssem Eddine

Field: Artificial Intelligence & User Interfaces

Language: Python (Tkinter + TensorFlow)

📌 Notes:

✅ The AI model was trained separately and loaded at runtime.
📦 You can convert the project into an executable using pyinstaller or auto-py-to-exe.

🧊 Screenshot:
![App Screenshot](screenshot.png)
