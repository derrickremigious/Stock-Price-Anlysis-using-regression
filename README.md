📊 Analyzing TCS and Accenture Stock Price Using Regression Techniques  

📌 Project Overview  
This project performs **stock price analysis** of **Tata Consultancy Services (TCS) and Accenture** using various **regression techniques**. By leveraging historical stock data, this system identifies key trends, evaluates influencing factors, and predicts future stock prices.  

🔍 **Key Features**  
- 📈 **Multiple Regression Models**: Linear, Polynomial, Decision Tree, Gamma, Poisson, and ARD Regression.  
- 🔄 **Stock Data Preprocessing**: Handling missing values, outliers, and feature engineering.  
- 📊 **Visualization & Insights**: Trend analysis, moving averages, and volatility tracking.  
- 🌐 **Web Application**: Built using Django for real-time stock price predictions.  
- 🛠 **Machine Learning Implementation**: Model training and evaluation with Python (Scikit-Learn, Pandas, NumPy).  

---

🚀 Installation Guide  

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-username/stock-price-analysis.git
cd stock-price-analysis

2️⃣ Create a Virtual Environment

python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate     # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Web Application

python manage.py runserver

⚙️ Technologies Used

Category	Technologies
🖥 Programming	Python (Scikit-Learn, Pandas, NumPy, Matplotlib)
📡 Web Framework	Django
📊 Data Processing	Pandas, Seaborn, Statsmodels
🤖 Machine Learning	Linear Regression, Decision Tree, Poisson Regression, ARD Regression
🗄 Database	SQLite
📉 Visualization	Matplotlib, Seaborn

🛠 Regression Techniques Used

Model	Use Case	Advantage
Linear Regression	Simple stock trends	Fast and interpretable
Polynomial Regression	Non-linear trends	Captures complex trends
Decision Tree Regression	Complex dependencies	Works with numerical & categorical data
Gamma Regression	Skewed stock data	Handles right-skewed distributions
Poisson Regression	Event-based trends	Good for trading volume prediction
ARD Regression	Event impact analysis	Identifies causal effects

📊 Stock Price Data Preprocessing
	•	✅ Handling Missing Values (Forward-fill, mean imputation).
	•	📉 Removing Outliers (IQR method).
	•	🔎 Feature Engineering (Moving Averages, Volatility Index).
	•	🏗 Data Normalization (Min-Max Scaling, Standardization).

🔥 Results & Performance Evaluation
	•	✅ Regression models compared using RMSE, R² Score.
	•	📈 Trend patterns identified for TCS & Accenture stock fluctuations.
	•	🖥 Web dashboard provides real-time stock price predictions.

🛠 Future Enhancements
	•	🔗 Integrating Deep Learning models (LSTMs, GRUs) for better predictions.
	•	🌍 Adding real-time stock API integration (Yahoo Finance, NSE/BSE).
	•	📊 Sentiment Analysis from financial news & social media.
	•	🚀 Expanding to multiple company stocks for broader analysis.

📜 License

This project is open-source and licensed under the MIT License.

🤝 Contributors
	•	👨‍💻 Derrick Remigious G M
	•	👩‍💻 Jenica Rosanne R
	•	📚 Guide: Ms. Saikethana, Assistant Professor

⭐ Support

If you like this project, give it a star ⭐ on GitHub!
For any questions, feel free to open an issue or contact us.

Happy Coding! 🚀
