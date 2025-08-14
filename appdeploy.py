#Importing libraries
# streamlit_app.py
import streamlit as st
import joblib
import os
import pandas as pd
import joblib
import xgboost

#loading my models
df = joblib.load(r"C:\Users\mitan\Downloads\data.pkl")

clf_model = joblib.load(r"C:\Users\mitan\Downloads\classification_model.pkl")

reg_model = joblib.load(r"C:\Users\mitan\Downloads\regression_model.pkl")




def footer():
    st.markdown("---")
    st.markdown("""
    <small>⚡ Crafted with curiosity & coffee by <b>Gaurvi Maheshwari</b> ⚡ | 
    [Kaggle](https://www.kaggle.com/gaurvimaheshwari) • 
    [GitHub](https://github.com/Gaurvi-1989) • 
    [LinkedIn](www.linkedin.com/in/gaurvi-maheshwari-5a8404263) </small>
    """, unsafe_allow_html=True)




# ===================== Page Functions =====================
def home():
    st.title("🏠 Home")
    st.title("🚀 OpenLearn 1.0 | Machine Learning Capstone")
    st.divider()

    st.subheader("📜 Dataset Overview")
    st.write(
        """
        This dataset comes from the 
        [Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey),
        provided by **OSMI** (*Open Sourcing Mental Illness*).  

        It offers insights into how tech workplace culture, benefits,
        and individual backgrounds relate to mental health conditions.
        """
    )

    st.markdown("### 🔹 Key Data Categories")
    st.markdown(
        """
        1. **Demographics** → Age, Gender, Country  
        2. **Workplace Environment** → Benefits, leave policy clarity  
        3. **Personal Mental Health History** → Previous or ongoing conditions, family history  
        4. **Attitudes & Perceptions** → Comfort in talking about mental health
        """
    )

    st.info(
        "Our mission: Detect patterns, trends, and factors to guide better mental health support strategies in tech."
    )



def eda():
    
    st.title("📊 Data Analysis, Observations & Inferences")
    st.divider()
    st.write(
        "This dataset had many anomalies, null values, outliers, and imbalanced data in columns like `Gender`, `Age`, `Country`, etc. which needed to be cleaned"
        "and standardised."
    )

    # Dynamic row and feature counts
    total_rows, total_features = df.shape
    st.write(f"Total number of values: `{total_rows}`")
    st.write(f"Total number of features: `{total_features}`")

    # Dynamic missing value counts
    missing_counts = df.isnull().sum()
    st.write("Features having NaN values: \n")
    for col, cnt in missing_counts.items():
        if cnt > 0:
            st.write(f"\t`{col}`: {cnt}")

    st.divider()
    st.write("### Dataset Preview:")
    st.dataframe(df.head())

    st.divider()
    removed_features = [
        'Timestamp', 'Country', 'state', 'self_employed', 'phys_health_consequence',
        'mental_health_interview', 'phys_health_interview', 'mental_vs_physical',
        'comments'
    ]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✅ Features Used:")
        for col in df.columns:
            st.markdown(f"- {col}")

    with col2:
        st.markdown("### ❌ Features Removed:")
        for col in removed_features:
            st.markdown(f"- {col}")

    st.divider()
    st.header("Univariate Analysis")
    st.image(r"C:\Users\mitan\Desktop\gm kaggle\u1.png", caption="Univariate Analysis (1)", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ###
        - Mean Age of Respondents: `32.05`
        - Top 5 Countries by Responses: `United States`, `United Kingdom`, `Canada`, `Germany`, `Ireland`
        """)

    with col2:
        st.markdown("""
        ### 
        - Male: `79.6%`
        - Female: `19.0%`
        - Other: `1.4%`
        """)
    
    st.image(r"C:\Users\mitan\Desktop\gm kaggle\u2.png",  caption="Univariate Analysis (2)", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        • The dataset shows a nearly balanced split between those who sought treatment (51.6%) and those who didn’t (48.4%).

        • Around 39% of respondents have a family history of mental illness, suggesting a potential risk factor.

        • Most respondents reported that mental health *sometimes* interferes with work, while fewer experienced frequent interference.
        """)
    with col2:
        st.markdown("""
        • A strong majority feel comfortable discussing mental health with coworkers, which is a positive sign of workplace openness.

        • Many respondents are unsure about mental health leave policies, showing poor communication or unclear HR policies.

        • Although a majority report having benefits, a large proportion either don’t know or lack them, which is a sign of awareness lack.
        """)
    
    st.divider()
    st.header("Bivariate Analysis")
    st.image(r"C:\Users\mitan\Desktop\gm kaggle\b1.png", caption="Bivariate Analysis (1)", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        • Females and Others are more likely to seek treatment compared to Males.

        • Treatment seeking behavior varies globally with countries like France and Germany having notably lower treatment rates.
        """)
    with col2:
        st.markdown("""
        • People in their late 20s to early 30s form the bulk of those seeking treatment.

        • Those who report frequent work interference are far more likely to seek mental health treatment.
        """)

    st.image(r"C:\Users\mitan\Desktop\gm kaggle\b2.png", caption="Bivariate Analysis (2)", use_container_width=False)
    st.markdown("""
    ###   
    Company Mental Health Benefits vs. Treatment Seeking
This chart compares treatment-seeking behavior among employees based on whether their company offers mental health benefits.

Yes (Benefits Provided): Around 64% of employees seek treatment, while 36% do not.

Don't Know: Only 37% seek treatment, while 63% avoid it — indicating awareness gaps.

No (No Benefits): Treatment seeking drops slightly, with 48% seeking help vs. 52% not seeking help.

📊 Key Takeaway:
Providing mental health benefits — and clearly communicating them — significantly boosts the likelihood of employees seeking treatment.
    """)
    st.divider()
    st.header("Multivariate Analysis")
    st.image(r"c:\Users\mitan\Desktop\gm kaggle\m1.png", caption="Multivariate Analysis (1)", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        • Males dominate the dataset and are **less likely** to seek treatment.  
        • A higher proportion of females **do seek** mental health treatment.

        • Most males and females report **"Sometimes"** work interference.  
        • The **"Other"** gender group is minimal but follows similar patterns.
        """)
    with col2:
        st.markdown("""
        • Average age is fairly stable across company sizes (~31–34 years).  
        • People at **large companies** who sought treatment tend to be older.

        • **26–35** is the most common age group for both treated & untreated.  
        • **Significant drop** in treatment observed for respondents **45+**.
        """)

    st.divider()
    st.header("Correlation Heatmap")
    st.image(r"C:\Users\mitan\Desktop\gm kaggle\cm1.png", caption="Correlation Heatmap", use_container_width=True)

# ===============================
# 📉 REGRESSION MODULE - Predict Age
# ===============================
def regression():
    st.title("📈 Regression Task")

    st.title("📉 Predict Employee Age from Workplace Factors")
    st.divider()

    st.markdown(
        "We aim to determine the employee's **Age** based on multiple workplace and health attributes. "
        "Below you can see the algorithms tried, their main parameter settings, and how well they performed."
    )

    # --- Model Inventory ---
    st.subheader("🔍 Models Evaluated")
    st.write("- Ordinary Least Squares (Linear Regression)")
    st.write("- Random Forest Regressor (Ensemble)")
    st.write("- XGBoost Regressor (Boosting)")

    # --- Linear Regression ---
    st.markdown("#### **Linear Regression**")
    st.write(
        "A simple yet interpretable model that assumes a direct linear link between predictors and the target variable."
    )
    st.code(
        "MAE: 5.5234\n"
        "RMSE: 7.1290\n"
        "R² Score: 0.0073"
    )

    # --- Random Forest Regression ---
    st.markdown("#### **Random Forest Regressor**")
    st.write(
        "A tree-ensemble approach that constructs numerous decision trees and averages their outputs "
        "to improve robustness and accuracy."
    )
    st.write("**Tuning Summary:**")
    st.write("- max_depth: 10")
    st.write("- min_samples_leaf: 2")
    st.write("- min_samples_split: 5")
    st.write("- n_estimators: 200")
    st.code(
        "MAE: 5.2341\n"
        "RMSE: 6.8873\n"
        "R² Score: 0.0745"
    )

    # --- XGBoost Regression ---
    st.markdown("#### **XGBoost Regressor**")
    st.write(
        "A high-performance gradient boosting algorithm particularly effective for tabular datasets."
    )
    st.write("**Parameter Highlights:**")
    st.write("- colsample_bytree: 1.0")
    st.write("- learning_rate: 0.01")
    st.write("- max_depth: 3")
    st.write("- n_estimators: 200")
    st.write("- subsample: 0.8")
    st.code(
        "MAE: 5.2612\n"
        "RMSE: 6.8626\n"
        "R² Score: 0.0801"
    )

    # --- Model Comparison ---
    regression_results = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest Regressor", "XGBoost Regressor"],
        "MAE": [5.5234, 5.2341, 5.2612],
        "RMSE": [7.1290, 6.8873, 6.8626],
        "R² Score": [0.0073, 0.0745, 0.0802]
    }).sort_values(by="R² Score", ascending=False)

    st.markdown("### 📊 Performance Summary")
    st.dataframe(
        regression_results.style.format({
            "MAE": "{:.4f}",
            "RMSE": "{:.4f}",
            "R² Score": "{:.4f}"
        }),
        use_container_width=True
    )

    st.success("✅ The model with the highest R² score is the **XGBoost Regressor**, which we will use for predictions.")

# --- Input Form ---
    st.divider()
    st.markdown("### 🔮 Try it yourself – predict an employee's age:")

    # SAME mapping from notebook for Gender
    gender_map = {'Male': 0, 'Female': 1, 'Others': 0.5}

    reg_user_input = {}
    # Features used during model training (num_cols from notebook)
    num_cols = [
        'family_history', 'remote_work', 'Gender', 'tech_company', 'obs_consequence',
        'work_interfere', 'supervisor', 'coworkers', 'benefits', 'wellness_program',
        'seek_help', 'anonymity', 'mental_vs_physical', 'care_options',
        'mental_health_consequence', 'phys_health_consequence',
        'mental_health_interview', 'phys_health_interview'
    ]

    reg_labels = {
        "self_employed": "Self-employed?",
        "Gender": "Gender",
        "family_history": "Family history of mental illness?",
        "treatment": "Sought mental health treatment?",
        "work_interfere": "Does mental health interfere with work?",
        "no_employees": "Company size (number of employees)",
        "remote_work": "Work remotely ≥50% of the time?",
        "benefits": "Employer provides mental health benefits?",
        "care_options": "Aware of care options from employer?",
        "wellness_program": "Employer wellness program includes mental health?",
        "seek_help": "Resources provided to seek help?",
        "anonymity": "Anonymity assured if using treatment resources?",
        "leave": "Ease of taking leave for mental health?",
        "mental_health_consequence": "Fear of negative consequences if disclosing?",
        "coworkers": "Willingness to discuss with coworkers?",
        "supervisor": "Willingness to discuss with supervisor?",
        "obs_consequence": "Heard/seen negative consequences for others?",
        "mental_vs_physical": "Perception of mental vs physical health?",
        "phys_health_consequence": "Physical health consequence",
        "mental_health_interview": "Mental health discussed in interview?",
        "phys_health_interview": "Physical health discussed in interview?"
    }

    # Collect inputs exactly as in model features
    for col in num_cols:
        opts = df[col].dropna().unique().tolist()
        label = reg_labels.get(col, col)
        reg_user_input[col] = st.selectbox(label, opts)

    # Create DataFrame and apply preprocessing
    reg_input_df = pd.DataFrame([reg_user_input])

    # Map Gender to numeric
    if "Gender" in reg_input_df.columns:
        reg_input_df["Gender"] = reg_input_df["Gender"].map(gender_map)

    # Ensure numeric data types
    reg_input_df = reg_input_df.astype(float)

    if st.button("Predict Age"):
        try:
            prediction = reg_model.predict(reg_input_df[num_cols])  # exact column order
            st.success(f"🎯 Estimated Age: **{int(round(prediction[0]))} years**")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
    footer()

# ===============================
# 🧮 CLASSIFICATION MODULE - Seek Treatment Prediction
# ===============================
def classification():
    st.title("🧮 Classification Task")

    st.title("🧮 Predict Need for Mental Health Treatment")
    st.divider()

    st.markdown(
        "This task is a **binary classification** problem: given certain demographic and workplace responses, "
        "predict whether the employee would seek mental health treatment."
    )

    st.subheader("🔍 Models Tested")
    st.write("- Logistic Regression")
    st.write("- Random Forest Classifier")
    st.write("- K-Nearest Neighbors")
    st.write("- XGBoost Classifier")

    # Logistic Regression
    st.markdown("#### **Logistic Regression**")
    st.write("A baseline linear model estimating log-odds; parameters tuned for reduced overfitting.")
    st.write("- C: 1")
    st.write("- penalty: l2")
    st.write("- solver: lbfgs")
    st.code("Accuracy: 0.8128\nROC-AUC: 0.8897\nF1 Score: 0.84")

    # Random Forest
    st.markdown("#### **Random Forest Classifier**")
    st.write("Ensemble of decision trees, tuned via grid search.")
    st.write("- max_depth: 5")
    st.write("- max_features: log2")
    st.write("- n_estimators: 100")
    st.code("Accuracy: 0.8181\nROC-AUC: 0.9039\nF1 Score: 0.84")

    # KNN
    st.markdown("#### **K-Nearest Neighbors**")
    st.write("Classifies based on the closest labeled examples in the dataset.")
    st.write("- metric: manhattan")
    st.write("- n_neighbors: 10")
    st.write("- weights: distance")
    st.code("Accuracy: 0.7807\nROC-AUC: 0.8677\nF1 Score: 0.79")

    # XGBoost Classifier
    st.markdown("#### **XGBoost Classifier**")
    st.write("A gradient boosting method optimized for speed and accuracy.")
    st.write("- learning_rate: 0.01")
    st.write("- max_depth: 3")
    st.write("- n_estimators: 300")
    st.code("Accuracy: 0.8288\nROC-AUC: 0.9035\nF1 Score: 0.86")

    # Model comparison table
    clf_results = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest", "KNN", "XGBoost"],
        "Accuracy": [0.8128, 0.8181, 0.7807, 0.8288],
        "ROC-AUC": [0.8897, 0.9039, 0.8677, 0.9035],
        "F1 Score": [0.84, 0.84, 0.79, 0.86]
    }).sort_values(by="ROC-AUC", ascending=False)

    st.markdown("### 📊 Classification Model Metrics")
    st.dataframe(
        clf_results.style.format({
            "Accuracy": "{:.4f}",
            "ROC-AUC": "{:.4f}",
            "F1 Score": "{:.4f}"
        }),
        use_container_width=True
    )

    st.image(r"C:\Users\mitan\Desktop\gm kaggle\classification.png", caption="ROC Curves for the evaluated models", use_container_width=True)

    st.success("✅ Best performer: **XGB Classifier**, narrowly ahead of Random Forest.")

    # Prediction form
    st.divider()
    st.markdown("### 🔮 Will this person seek treatment?")
    clf_inputs = {}
    clf_labels = {
        "self_employed": "Self-employed?",
        "Gender": "Gender",
        "family_history": "Family history of mental illness?",
        "work_interfere": "Mental health interferes with work?",
        "no_employees": "Company size (# employees)",
        "remote_work": "Works remotely ≥50% of time?",
        "benefits": "Employer offers mental health benefits?",
        "care_options": "Knows mental care options available?",
        "wellness_program": "Wellness program includes mental health?",
        "seek_help": "Resources to seek help available?",
        "anonymity": "Anonymity protected for treatment use?",
        "leave": "How easy to take leave for mental health?",
        "mental_health_consequence": "Fear of consequence if disclosing?",
        "coworkers": "Would discuss mental health with coworkers?",
        "supervisor": "Would discuss with supervisor?",
        "obs_consequence": "Observed negative consequences for others?"
    }

    for col in df.columns:
        if col in ["age_group", "treatment"]:
            continue
        if col == "Age":
            clf_inputs[col] = st.number_input("Age", min_value=19, max_value=100, step=1)
        else:
            opts = df[col].dropna().unique().tolist()
            label = clf_labels.get(col, col)
            clf_inputs[col] = st.selectbox(label, opts)

    clf_input_df = pd.DataFrame([clf_inputs])

    if st.button("Classify Treatment Likelihood"):
        try:
            pred = clf_model.predict(clf_input_df)[0]
            st.success("✅ Likely to seek treatment!" if pred == 1 else "❌ Likely not to seek treatment.")
        except Exception as e:
            st.error(f"Classification failed: {e}")

    footer()
    

pg = st.navigation([
    st.Page(home, title="🏠 Home"),
    st.Page(eda, title="📊 Exploratory Data Analysis"),
    st.Page(classification, title="🧮 Classification Task"),
    st.Page(regression, title="📈 Regression Task"),
    # st.Page(clustering, title="📊 Persona Clustering")
])
pg.run()
