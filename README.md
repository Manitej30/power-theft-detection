# ⚡ Power Theft Detection in Smart Grids using Quantum Machine Learning (QML)

## 📌 Overview

Electricity theft in modern smart grids is a major challenge, especially with the integration of photovoltaic (PV) systems and distributed energy generation. Traditional machine learning models struggle with high-dimensional, noisy, and imbalanced smart meter data.

This project proposes a **Quantum Machine Learning (QML)** based approach using a hybrid quantum-classical architecture to accurately detect power theft from both **consumption and generation domains**.

---

## 🚀 Key Features

* Detects electricity theft from **smart meter and PV generation data**
* Uses **Quantum Variational Circuit (QVC)** for feature encoding
* Implements **Data Re-uploading Circuit (DRC)** for enhanced learning
* Introduces **Entanglement layer** for improved classification
* Compares performance with classical models:

  * XGBoost
  * LightGBM
* Achieves up to **91% accuracy**

---

## 🧠 Methodology

### 🔹 Data Processing

* Dataset: Smart Grid Theft Detection (Kaggle)
* Steps:

  * Feature extraction
  * Data normalization
  * Shuffling
  * Train-test split (80/20)

---

### 🔹 Model Architecture

1. **Classical Preprocessing Layer**

   * Prepares input features

2. **Quantum Variational Circuit (QVC)**

   * Angle embedding
   * Rotation gates
   * CNOT gates

3. **Data Re-uploading Circuit (DRC)**

   * Iterative data encoding
   * Improves representation

4. **Entanglement Layer**

   * Enhances feature interaction
   * Improves classification accuracy

---

## 📊 Results

| Model                    | Accuracy |
| ------------------------ | -------- |
| XGBoost                  | 86%      |
| LightGBM                 | 73%      |
| QVC + DRC                | 88%      |
| QVC + DRC + Entanglement | **91%**  |

---

## 🏗️ Project Structure

```
Power-Theft-Detection/
│
├── dataset/
│   └── smart_grid_data.csv
│
├── models/
│   ├── qvc_model.py
│   ├── drc_model.py
│   └── entanglement_layer.py
│
├── notebooks/
│   └── training.ipynb
│
├── app/
│   └── flask_app.py
│
├── static/
├── templates/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

### Hardware

* Processor: i5 or above
* RAM: 8GB+
* OS: Windows

### Software

* Python 3.x
* Anaconda
* Jupyter Notebook
* Flask
* SQLite3

---

## 📦 Installation

```bash
git clone https://github.com/your-username/power-theft-detection.git
cd power-theft-detection

pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run Notebook

```bash
jupyter notebook
```

### Run Flask App

```bash
python app/flask_app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📈 Advantages

* Handles **high-dimensional and noisy data**
* Works on both **consumption and generation domains**
* Reduces manual feature engineering
* Better generalization than classical ML models
* Utilizes **quantum parallelism and entanglement**

---

## 🔬 Novelty

* Hybrid **Quantum Deep Learning architecture**
* Integration of:

  * QVC
  * DRC
  * Entanglement layer
* Improved classification for smart grid fraud detection

---

## 📌 Future Work

* Deploy on real smart grid systems
* Integrate real-time data streams
* Use quantum hardware for execution
* Extend to cyber-attack detection

---

## 👨‍💻 Author

**Narendula Manitej**
B.Tech AIML | Data Engineering Aspirant

---

## ⭐ Conclusion

This project demonstrates how **Quantum Machine Learning** can outperform traditional models in detecting electricity theft by leveraging quantum properties like **superposition, entanglement, and interference**, making it a powerful solution for next-generation smart grids.

---
