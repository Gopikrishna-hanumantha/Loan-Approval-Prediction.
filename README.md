#Loan Approval Prediction System
### A Machine Learning and Deep Learning Approach Using Python and Streamlit
About the Project
Getting a loan approved depends on several factors, such as an applicant's income, credit history, education, loan amount and other personal details. Understanding how these factors influence loan approval can help make the decision-making process more efficient.
With this idea in mind, I developed a **Loan Approval Prediction System** using Machine Learning and Deep Learning techniques.
The main purpose of this project is to predict whether a loan application is likely to be approved or rejected based on the information provided by the applicant.
To explore different approaches, I implemented and compared two methods: traditional Machine Learning algorithms and a CNN-based Deep Learning model. I also developed a Streamlit application to make the prediction process simple and interactive.
##Project Objectives
The major objectives of this project are:
- To understand the factors that influence loan approval.
- To prepare and process the dataset before training the models.
- To implement different Machine Learning algorithms for loan prediction.
- To experiment with CNN and explore its performance on the dataset.
- To compare the performance of the implemented models.
- To build a user-friendly application using Streamlit.

Dataset Information
For this project, I used the **Loan Prediction Dataset from Analytics Vidhya**.
The dataset contains information about loan applicants, including their income, education, credit history and property area.
Training Dataset
- Number of records: 614
- Number of columns: 13
  Testing Dataset
- Number of records: 367
- Number of columns: 12
#Important Features
- Gender – Applicant's gender.
- Married – Marital status.
- Dependents – Number of financial dependents.
- Education – Applicant's education level.
- Self_Employed – Employment status.
- ApplicantIncome – Applicant's income.
- CoapplicantIncome – Co-applicant's income.
- LoanAmount – Requested loan amount.
- Loan_Amount_Term – Loan repayment period.
- Credit_History – Credit history indicator.
- Property_Area – Location category of the property.
Target Variable: `Loan_Status`
- Y – Loan Approved
- N – Loan Not Approved
##Tools and Technologies
The following tools and libraries were used during the development of this project:
- Python – Main programming language.
- Jupyter Notebook – For writing and executing Python code.
- Anaconda Navigator – For managing the development environment.
- Pandas and NumPy – For data handling and numerical operations.
- Matplotlib and Seaborn – For data visualization.
- Scikit-learn – For preprocessing and Machine Learning algorithms.
- TensorFlow and Keras – For building and training the CNN model.
- Streamlit – For developing the interactive application.
- Joblib – For saving and loading trained models.
##Models and Approaches
I explored two different approaches to understand how different algorithms perform on the loan prediction dataset.

### 1. Machine Learning Approach (Without CNN)
In this approach, I implemented three Machine Learning algorithms:
- Logistic Regression: Used to predict whether a loan application is likely to be approved or rejected.
- Decision Tree: Makes predictions by following a series of decision-based rules.
- Random Forest: Combines multiple decision trees to improve prediction performance.
### 2. Deep Learning Approach (With CNN)
I also experimented with a Convolutional Neural Network (CNN) to explore its performance on the loan prediction dataset.
The CNN architecture includes:
- Conv1D
- MaxPooling1D
- Flatten
- Dense
- Dropout
This approach helped me compare a Deep Learning model with the traditional Machine Learning algorithms used in the project.
##Model Performance
After training and evaluating the models, I obtained the following results:
| Model | Accuracy |
| Logistic Regression | 86.18% |
| Decision Tree | 75.61% |
| Random Forest | 82.11% |
| CNN | 82.11% |
Among the four models, **Logistic Regression achieved the highest accuracy of 86.18%**.
Based on this comparison, I selected Logistic Regression for the Streamlit application.
##Streamlit Web Application
To make the project easier to use, I developed an interactive application using Streamlit.
Instead of manually running prediction code, users can enter applicant details through the application.
The application processes the entered information using the saved preprocessing pipeline and passes it to the trained Logistic Regression model.
It then displays the predicted loan approval status along with the estimated approval probability.
This makes the project easier to demonstrate and understand.
##How to Run the Project
Follow these steps to run the application on your computer.
  Step 1: Download or clone the repository.
```bash
git clone https://github.com/YOUR-USERNAME/Loan-Approval-Prediction.git
```
step 2: Open the project folder.
```bash
cd Loan-Approval-Prediction
```
Step 3: Install the required
 Author
 Maddireddy G K N Hanumantha Siva Durga

Enrollment Number: 240160226177

Department: CSE (AI & ML)

Institution: GD Goenka University
 
