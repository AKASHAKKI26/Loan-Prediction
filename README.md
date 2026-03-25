# 🏠 Loan Prediction App

A simple Machine Learning web application built using **Streamlit** that predicts loan-related values based on user input such as income, age, city, employment type, and loan type.

---

## 🚀 Features

* User-friendly web interface using Streamlit
* Accepts user inputs dynamically
* Uses a trained Machine Learning model (`model.pkl`)
* Handles categorical data using one-hot encoding
* Displays prediction instantly

---

## 📂 Project Structure

```
project/
│
├── app.py              # Main Streamlit application
├── model.pkl           # Trained ML model
├── columns.pkl         # Feature columns used during training
├── requirements.txt    # Required dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository (or download files)

```bash
git clone <your-repo-link>
cd project
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🖥️ Usage

1. Open the app in your browser
2. Enter the required details:

   * City
   * Employment Type
   * Loan Type
   * Income
   * Age
3. Click on **Predict**
4. View the predicted result instantly

---

## 🧠 Model Details

* Algorithm: Machine Learning Regression Model
* Library: Scikit-learn
* Input features:

  * Income
  * Age
  * City (encoded)
  * Employment Type (encoded)
  * Loan Type (encoded)

---

## 📌 Notes

* Ensure `model.pkl` and `columns.pkl` are present in the same directory as `app.py`
* The app automatically handles missing columns using dummy variables
* Predictions are formatted to 2 decimal places

---

## 📸 Future Improvements

* Add more input features for better accuracy
* Improve UI design
* Deploy the app online (Streamlit Cloud / Render)
* Add model evaluation metrics display

---

## 👨‍💻 Author

**Akash**

---

## 📃 License

This project is open-source and free to use.
