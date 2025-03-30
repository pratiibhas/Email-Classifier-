# Email-Classifier

**ADVANCED ANALYSIS AND MODEL DEVELOPMENT TO CLASSIFY A MAIL AS EITHER HAM OR SPAM**

**Workflow**
1. Load the Data – Import and inspect the dataset.
2. Understand the Structure – Analyze the distribution and characteristics of spam vs. ham emails.
3. Check for Data Imbalance – If the dataset is imbalanced, create stratified train-test splits.
4. Create a Test Set – Set aside a test set before conducting any analysis.
5. Perform Exploratory Data Analysis (EDA) – Visualize and analyze word frequency, message length, and other patterns.
6. Advanced Text Analysis – Extract meaningful insights using techniques like n-grams, word clouds, etc.
7. TF-IDF Vectorization – Convert text data into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF).
8. Build Machine Learning Models – Train models such as Naïve Bayes, Logistic Regression, SVM, and more.
9. Train and Evaluate Models – Compare model performance using accuracy, precision, recall, and F1-score.
10. Compare Different Models – Experiment with multiple algorithms and choose the best-performing one.

### Further detailing of listed points:

**1. Introduction**
- Overview of the project
- Objective: Classifying emails as ham (legitimate) or spam
- Importance of spam classification in real-world applications

**2. Dataset Information**
- Source of the dataset (e.g., SMS Spam Collection, Enron Email Dataset)
- Number of emails in the dataset 
total : 3000
ham emails : 500
pam emails : 2500

- Class distribution (ham vs spam)

**3. Data Preprocessing**
- checking datatypes of the given columns
- Handling missing values
- Text cleaning (lowercasing, punctuation removal, stopword removal, lemmatization)
- Tokenization techniques


**4. Exploratory Data Analysis (EDA)**
Distribution of spam vs ham emails

Most frequent words in spam and ham emails

Message length analysis

Special character analysis (e.g., number of links, exclamation marks, etc.)

**5. Feature Engineering**
Creating new features (e.g., word count, special character count)

TF-IDF vectorization

N-grams analysis (unigrams, bigrams, trigrams)

**6. Machine Learning Models**
Baseline model: Naïve Bayes

Other models: Logistic Regression, SVM, Decision Trees, Random Forest, XGBoost

Handling class imbalance using techniques like SMOTE

**7. Model Training and Evaluation**
Splitting the data into train-test sets

Performance metrics (Accuracy, Precision, Recall, F1-score, AUC-ROC)

Hyperparameter tuning using GridSearchCV

**8. Model Comparison and Results**
Comparison of different models using a performance table

Best-performing model and its key insights

9. Deployment (Optional, if applicable)
Deploying the model using Flask/FastAPI

Creating an API for real-time email classification

10. Conclusion
Summary of key findings

Future improvements
