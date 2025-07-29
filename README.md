# 🧠 Employee Salary Prediction

This project is a lightweight web-based application that predicts employee salaries based on age, education level, work class, hours per week, and gender. It's built with pure HTML, CSS, and JavaScript and requires **no backend server**.

## 🚀 Features

- Predicts salaries using a simple weighted formula.
- Intuitive and responsive UI.
- Client-side validation with animated error feedback.
- Salary prediction is instantaneous with no data stored.

## 🧠 How It Works

The salary is predicted using the following weighted formula:

salary = base + (age × coef1) + (education level × coef2) + (hours/week × coef3) + (workclass × coef4) + (gender × coef5)

Each feature contributes linearly to the final prediction using hardcoded coefficients. This is just a simulation, not a trained machine learning model.

## 📁 File Structure

salarypredictor.html   # Main HTML file with embedded CSS and JS

## 🛠️ How to Use

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/salarypredictor.git
   cd salarypredictor

2. Open the HTML file in your browser:
   open salarypredictor.html
   or just double-click the file.

3. Enter your details and click **Predict Salary**.

## 📝 License

This project is licensed under the MIT License.

---

⚠️ **Disclaimer**: This is a demo and does not reflect actual salary predictions or real-world models. It's intended for educational purposes only.



