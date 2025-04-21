# 🦴 Bone Fracture Detection – Tkinter + Deep Learning App

<p align="center">
  <img src="trauma.png" alt="App Icon" width="100"/>
</p>

---

## 📌 Overview

This is a desktop GUI application built with **Python** and **Tkinter** to automatically detect bone fractures in X-ray images using a pre-trained deep learning model (TensorFlow/Keras).

---

## 💡 Features

- 🧠 Utilizes a trained **Keras** model to classify X-ray images as:
  - **Fractured**
  - **Not Fractured**
- 📷 Clean and user-friendly **GUI** to load and analyze X-ray images.
- 📊 Displays **prediction confidence** after analysis.
- 🖼️ Shows the **loaded image** in the interface.
- 👨‍💻 "About" window with **developer information**.
- 🎨 Sleek and modern **UI** with soft, calming colors.

---

## 🧪 Requirements

Install the required Python libraries with:

```bash
pip install tensorflow pillow numpy

🗂️ Project Structure

fracture_detection_app/
├── fracture_model.keras        # Pre-trained deep learning model
├── trauma.png                  # Application icon
├── main.py                     # Main application script
└── README.md                   # Project documentation

🚀 How to Run
1.Ensure all the following files are in the same directory:

main.py

fracture_model.keras

trauma.png

2.Launch the application by running:
python main.py

3.Use the GUI to:
📂 Load Image – Select an X-ray image from your system.

🦴 View prediction and confidence score.

👨‍💻 Click About to see developer information.

👨‍💻 Developer:

Name: Bouagal Houssem Eddine

Field: Artificial Intelligence & User Interfaces

Tech Stack: Python (Tkinter + TensorFlow)

📌 Notes
✅ The AI model was trained separately and loaded at runtime.

📦 To convert this app into a standalone executable, use:

pyinstaller

auto-py-to-exe


🧊 Screenshot
<!-- If you want to add a screenshot later: -->
screenshot.png

