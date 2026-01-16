# 🔐 Password Vulnerability and Generation Scanner using AI

## 📌 Project Description

The **Password Vulnerability and Generation Scanner using AI** is a cybersecurity-focused application that analyzes user passwords to detect security weaknesses and generates strong, secure passwords.
The system uses **Artificial Intelligence (Machine Learning)** along with **entropy analysis, breach detection, and rule-based checks** to provide a complete password security solution.

This project helps users avoid weak or compromised passwords and promotes better cybersecurity practices.

---

## 🎯 Objectives

* Detect weak and vulnerable passwords using AI
* Generate strong and secure passwords automatically
* Check passwords against known breached password lists
* Calculate password entropy and strength score
* Provide improvement suggestions for weak passwords
* Create a user-friendly GUI application

---

## 🧠 Key Features

* ✅ **AI-based Password Vulnerability Scanner**
* 🔐 **Secure Password Generator**
* 📊 **Password Entropy Calculation**
* ⚠️ **Breach Password Detection**
* 💡 **Password Improvement Suggestions**
* 🔢 **Strength Score (0–100)**
* 📋 **Copy Password to Clipboard**
* 👁️ **Show / Hide Password Toggle**
* 🖥️ **Graphical User Interface (Tkinter)**

---

## 🛠 Technologies Used

* **Programming Language:** Python
* **AI / ML:** Random Forest Classifier
* **Libraries:**

  * `numpy`
  * `pandas`
  * `scikit-learn`
  * `tkinter`
  * `re`
  * `secrets`
* **GUI:** Tkinter
* **Dataset:** Common and breached password datasets

---

## ⚙️ How the System Works

1. User enters a password in the GUI
2. Features are extracted from the password
3. AI model classifies password strength
4. Entropy score is calculated
5. Password is checked against breach list
6. Strength score (0–100) is generated
7. Suggestions are displayed if password is weak
8. System can generate a secure password

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install numpy pandas scikit-learn
```

### 2️⃣ Train the AI Model

```bash
python train_model.py
```

### 3️⃣ Run the Application

```bash
python gui.py
```

---

## 🧪 Sample Output

* **Input:** `admin123`

  * Strength: Very Weak
  * Entropy: Low
  * Breach Status: Found in breach list
  * Strength Score: 22 / 100

* **Generated Password:** `A9#fQ@7zL!2`

  * Strength: Strong
  * Entropy: High
  * Breach Status: Safe
  * Strength Score: 95 / 100

---

## ✅ Advantages

* Improves password security awareness
* Combines AI with real-world cybersecurity concepts
* Easy to use GUI
* Practical and industry-relevant
* High scoring final-year diploma project

---

## ⚠️ Limitations

* Offline breach list (limited size)
* Password strength depends on dataset quality
* Generated passwords may be difficult to remember

---

## 🔮 Future Enhancements

* Online breach API integration
* Password vault integration
* Browser extension
* Biometric authentication
* Cloud-based security service

---

## 🎓 Academic Use

This project is suitable for:

* **Final Year Diploma (Computer / IT / AI)**
* Cybersecurity mini-projects
* AI & ML practical demonstrations

---

## 👤 Author

Final Year Diploma – Computer Engineering

---

## 📜 License

This project is for **educational purposes only**.
