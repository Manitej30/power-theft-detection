# ⚡ Power Theft Detection in Smart Grids

## Overview

This project detects electricity theft using machine learning models by analyzing energy consumption patterns. It identifies abnormal usage behavior in smart grid environments.

## Features

* Machine learning-based fraud detection
* Web application using Flask
* CSV data upload support
* Real-time prediction
* Visualization of results

## Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas, NumPy
* HTML, CSS, JavaScript

## Project Structure

```
power-theft-detection/
│
├── app.py
├── model/
├── static/
├── templates/
├── dataset/
└── notebook/
```

## Installation

Clone repository:

```
git clone https://github.com/YOUR_USERNAME/power-theft-detection.git
cd power-theft-detection
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run Application

```
python app.py
```

Open:

```
http://127.0.0.1:5000/
```

## Model Details

* Algorithms used: XGBoost, LightGBM, Custom Model
* Accuracy: ~85%+

## Future Improvements

* Deploy on AWS
* Add real-time streaming (Kafka + Spark)
* Improve anomaly detection models

## Author

Manitej Narendula
