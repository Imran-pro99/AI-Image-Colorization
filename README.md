#  AI Image Colorization

Automatically convert black-and-white images into realistic color images using **OpenCV's Deep Neural Network (DNN)** module and a pre-trained **Caffe** model.

> This project demonstrates the integration of Deep Learning with Computer Vision to colorize grayscale images.

---

##  Preview

### Image (Black & White)

### Result (Black & White - Colorized)

<p align="center">
  <img src="results/output_colorized.jpg" width="350">
</p>

---

##  Features

- Convert grayscale images into color images
- Uses a pre-trained Deep Learning model
- Built using Python and OpenCV
- Simple and beginner-friendly code
- Easy to customize for your own images

---

##  Tech Stack

- Python
- OpenCV
- NumPy
- OpenCV DNN Module
- Caffe (Pre-trained Model)

---

##  Project Structure

```text
AI-Image-Colorization/
│
├── images/
├── Model/
│   └── README.md
├── results/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/Imran-pro99/AI-Image-Colorization.git
```

### 2. Move into the project folder

```bash
cd AI-Image-Colorization
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the pre-trained model

The model files are **not included** in this repository.

Please follow the instructions inside:

```
Model/README.md
```

After downloading the files, place them inside the **Model/** folder.

---

##  Run

```bash
python main.py
```

---

##  Model Credits

This project uses a **pre-trained image colorization model** developed by:

Richard Zhang  
Phillip Isola  
Alexei A. Efros

Paper:

**Colorful Image Colorization (ECCV 2016)**

Official Repository:

https://github.com/richzhang/colorization

---

##  Future Improvements

- Web Interface using Flask
- React Frontend
- Drag & Drop Image Upload
- Batch Image Colorization
- GPU Acceleration

---

##  Author

**Imran Farhat**

GitHub:
https://github.com/Imran-pro99

---

##  Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
