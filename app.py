from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import os
import dill
import pickle
import sqlite3
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# ================= LOAD MODELS =================
with open("model/extension.pckl", "rb") as f:
    model = dill.load(f)

with open("model/pca.pkl", "rb") as f:
    pca = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

labels = ['No-Theft', 'Theft']

# ================= ROUTES =================
@app.route("/predict", methods=["GET", "POST"])
def predict():
    results = None
    columns = None

    if request.method == "POST":
        file = request.files.get("file")

        if file and file.filename.endswith(".csv"):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            df = pd.read_csv(filepath)

            original_df = df.copy()

            data = df.values
            data = pca.transform(data)
            data = scaler.transform(data)

            predictions = model.predict(data)

            # Add Prediction column
            original_df["Prediction"] = [labels[p] for p in predictions]

            # ===== USER FRIENDLY DISPLAY =====
            total_cols = original_df.shape[1]

            if total_cols > 11:   # more than 10 feature columns
                first_cols = original_df.iloc[:, :5]
                last_cols = original_df.iloc[:, -6:-1]  # last 5 feature columns
                display_df = pd.concat([first_cols, last_cols], axis=1)
                display_df.insert(5, "...", ["..."] * len(display_df))
                display_df["Prediction"] = original_df["Prediction"]
            else:
                display_df = original_df

            columns = display_df.columns.tolist()
            results = display_df.values.tolist()

        else:
            results = "Invalid file format"

    return render_template("result.html", results=results, columns=columns)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form.get('user','')
        name = request.form.get('name','')
        email = request.form.get('email','')
        number = request.form.get('mobile','')
        password = request.form.get('password','')

        # Server-side validation
        username_pattern = r'^.{6,}$'
        name_pattern = r'^[A-Za-z ]{3,}$'
        email_pattern = r'^[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$'
        mobile_pattern = r'^[6-9][0-9]{9}$'
        password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'

        if not re.match(username_pattern, username):
            return render_template("signup.html", message="Username must be at least 6 characters.")
        if not re.match(name_pattern, name):
            return render_template("signup.html", message="Full Name must be at least 3 letters, only letters and spaces allowed.")
        if not re.match(email_pattern, email):
            return render_template("signup.html", message="Enter a valid email address.")
        if not re.match(mobile_pattern, number):
            return render_template("signup.html", message="Mobile must start with 6-9 and be 10 digits.")
        if not re.match(password_pattern, password):
            return render_template("signup.html", message="Password must be at least 8 characters, with an uppercase letter, a number, and a lowercase letter.")

        con = sqlite3.connect('signup.db')
        cur = con.cursor()
        cur.execute("SELECT 1 FROM info WHERE user = ?", (username,))
        if cur.fetchone():
            con.close()
            return render_template("signup.html", message="Username already exists. Please choose another.")
        
        cur.execute("insert into `info` (`user`,`name`, `email`,`mobile`,`password`) VALUES (?, ?, ?, ?, ?)",(username,name,email,number,password))
        con.commit()
        con.close()
        return redirect(url_for('login'))

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    else:
        mail1 = request.form.get('user','')
        password1 = request.form.get('password','')
        con = sqlite3.connect('signup.db')
        cur = con.cursor()
        cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
        data = cur.fetchone()

        if data == None:
            return render_template("signin.html", message="Invalid username or password.")    

        elif mail1 == 'admin' and password1 == 'admin':
            return render_template("home.html")

        elif mail1 == str(data[0]) and password1 == str(data[1]):
            return render_template("home.html")
        else:
            return render_template("signin.html", message="Invalid username or password.")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/graphs')
def graphs():
	return render_template('graphs.html')
    
@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')


if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
