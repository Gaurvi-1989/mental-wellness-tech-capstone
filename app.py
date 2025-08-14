#Importing libraries
# streamlit_app.py
import streamlit as st
import joblib
import os
import pandas as pd
import joblib
import xgboost

#loading my models
df = joblib.load("models/data.pkl")

clf_model = joblib.load("models/classification_model.pkl")

reg_model = joblib.load("models/regression_model.pkl")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #ADD8E6;  /* Light Blue */
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)




st.sidebar.title("Navigation")

def footer():
    st.markdown("---")
    st.markdown("""
    <small>⚡ Crafted with curiosity & coffee by <b>Gaurvi Maheshwari</b> ⚡ | 
    [Kaggle](https://www.kaggle.com/gaurvimaheshwari) • 
    [GitHub](https://github.com/Gaurvi-1989) • 
    [LinkedIn](www.linkedin.com/in/gaurvi-maheshwari-5a8404263) </small>
    """, unsafe_allow_html=True)




# ===================== Page Functions =====================
import streamlit as st

def Home():
    st.title(" OpenLearn Capstone Project 🕷️")
    st.markdown(
        "<h4 style='color:#8e44ad;'>Welcome to a data-driven journey into Mental Health in Tech 🚀</h4>",
        unsafe_allow_html=True
    )
    st.divider()

    # Dataset Overview
    st.markdown("## 🌐 Dataset at a Glance")
    st.markdown(
        """
        🗂 **Source:** OSMI *Mental Health in Tech* surveys (2014 & 2016)  
        📍 **Available on:** [Kaggle – Mental Health in Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)  
        📋 **Covers:**  
        - 🧑‍💻 Demographics  
        - 💬 Mental health background & stigma  
        - 🏢 Workplace context  
        - 🩺 Support programs  
        
        💡 **Use it for:** Fun data exploration, neat visualizations, statistical deep dives, and even machine learning magic ✨.
        """,
        unsafe_allow_html=True
    )

    # Project Objectives
    st.markdown("## 🎯 Mission: What’s This Project About?")
    st.markdown(
        """
        We’re diving into the tech world’s mental health landscape to uncover:
        
        1️⃣ **Classification Magic** 🪄 – Can we predict if someone will seek treatment?  
        2️⃣ **Regression Power** 📈 – Guess a person’s age from workplace & personal vibes.  
        3️⃣ **Unsupervised Awesomeness** 🎭 – understand different personas of people about their mental wells
        """,
        unsafe_allow_html=True
    )

    # Project Components
    st.markdown("## 🪜 Game Plan")
    st.markdown(
        """
        - 🔍 **Part 1:** Exploratory Data Analysis (EDA) – Pretty graphs, trends & aha-moments!  
        - 🤖 **Part 2:** Supervised Learning –  
            &nbsp;&nbsp;A. 🛡 Classification Task  
            &nbsp;&nbsp;B. 📊 Regression Task  
        - 🎭 **Part 3:** Unsupervised Learning – Hidden patterns revealed.  
        - 🚀 **Part 4:** Streamlit Deployment – Bring it to life, online!  
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        "<h4 style='text-align:center; color:gray;'>💙 Built with curiosity, code & coffee ☕</h4>",
        unsafe_allow_html=True
    )
    footer()

    



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
    st.image("Images/u1.png", caption="Univariate Analysis (1)", use_container_width=True)

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
    
    st.image("Images/u2.png",  caption="Univariate Analysis (2)", use_container_width=True)

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
    st.image("Images/b1.png", caption="Bivariate Analysis (1)", use_container_width=True)

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

    st.image("Images/b2.png", caption="Bivariate Analysis (2)", use_container_width=False)
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
    st.image("Images/m1.png", caption="Multivariate Analysis (1)", use_container_width=True)

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
    st.image("Images/cm1.png", caption="Correlation Heatmap", use_container_width=True)

# ===============================
# 📉 REGRESSION MODULE - Predict Age
# ===============================
import streamlit as st
import pandas as pd
import joblib  # or pickle depending on how model is saved

import streamlit as st
import pandas as pd
import joblib

def regression():
    st.title("📈 Regression Task")
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
    st.write("A simple yet interpretable model that assumes a direct linear link between predictors and the target variable.")
    st.code(
        "MAE: 5.5234\n"
        "RMSE: 7.1290\n"
        "R² Score: 0.0073"
    )

    # --- Random Forest Regression ---
    st.markdown("#### **Random Forest Regressor**")
    st.write("A tree-ensemble approach that constructs numerous decision trees and averages their outputs "
             "to improve robustness and accuracy.")
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
    st.write("A high-performance gradient boosting algorithm particularly effective for tabular datasets.")
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

    # ================= Prediction Section =================
    st.subheader("📝 Enter Details to Predict Age")

    # Collect user inputs interactively
    family_history = st.selectbox("Family History?", ["Yes", "No"])
    remote_work = st.selectbox("Remote Work?", ["Yes", "No"])
    gender = st.selectbox("Gender", ["Male", "Female", "Others"])
    tech_company = st.selectbox("Works in Tech Company?", ["Yes", "No"])
    obs_consequence = st.selectbox("Observed Consequence?", ["Yes", "No"])
    work_interfere = st.selectbox("Work Interference Frequency", ["Often", "Sometimes", "Rarely", "Never"])
    supervisor = st.selectbox("Supervisor Support", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    coworkers = st.selectbox("Coworker Support", ["Yes", "No", "Some of them", "Unknown/Maybe"])
    benefits = st.selectbox("Benefits", ["Yes", "No", "Unknown/Maybe"])
    wellness_program = st.selectbox("Wellness Program", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    seek_help = st.selectbox("Seek Help", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    anonymity = st.selectbox("Anonymity", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    mental_vs_physical = st.selectbox("Mental vs Physical?", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    care_options = st.selectbox("Care Options Knowledge", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    mental_health_consequence = st.selectbox("Mental Health Consequence", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    phys_health_consequence = st.selectbox("Physical Health Consequence", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    mental_health_interview = st.selectbox("Discuss Mental Health in Interview?", ["Yes", "No", "Maybe", "Unknown/Maybe"])
    phys_health_interview = st.selectbox("Discuss Physical Health in Interview?", ["Yes", "No", "Maybe", "Unknown/Maybe"])

    # Prediction button
    if st.button("Predict Age"):
        try:
            # Load the model file
            reg_model = joblib.load(r"C:\Users\mitan\Downloads\regression_model.pkl")  

            # Prepare user input dict
            user_input = {
                'family_history': family_history,
                'remote_work': remote_work,
                'Gender': gender,
                'tech_company': tech_company,
                'obs_consequence': obs_consequence,
                'work_interfere': work_interfere,
                'supervisor': supervisor,
                'coworkers': coworkers,
                'benefits': benefits,
                'wellness_program': wellness_program,
                'seek_help': seek_help,
                'anonymity': anonymity,
                'mental_vs_physical': mental_vs_physical,
                'care_options': care_options,
                'mental_health_consequence': mental_health_consequence,
                'phys_health_consequence': phys_health_consequence,
                'mental_health_interview': mental_health_interview,
                'phys_health_interview': phys_health_interview
            }

            # Mapping dictionaries
            gender_map = {'Male': 0, 'Female': 1, 'Others': 0.5}
            yn_map = {'Yes': 1, 'No': 0}
            mid_map = {'Yes': 1, 'No': 0, 'Maybe': 0.5, 'Unknown/Maybe': 0.5, 'Some of them': 0.5}
            freq_map = {'Often': 1, 'Sometimes': 0.75, 'Rarely': 0.25, 'Never': 0}

            # Convert to DataFrame
            df_input = pd.DataFrame([user_input])

            # Apply mappings
            df_input['Gender'] = df_input['Gender'].map(gender_map)
            df_input[['family_history', 'remote_work', 'tech_company', 'obs_consequence']] = df_input[
                ['family_history', 'remote_work', 'tech_company', 'obs_consequence']
            ].replace(yn_map)

            df_input['work_interfere'] = df_input['work_interfere'].replace(freq_map)

            mid_cols = [
                'supervisor', 'coworkers', 'benefits', 'wellness_program', 'seek_help', 'anonymity',
                'mental_vs_physical', 'care_options', 'mental_health_consequence', 'phys_health_consequence',
                'mental_health_interview', 'phys_health_interview'
            ]
            df_input[mid_cols] = df_input[mid_cols].replace(mid_map)

            # Make sure all are numeric
            df_input = df_input.apply(pd.to_numeric, errors='coerce').fillna(0)

            # Prediction
            prediction = reg_model.predict(df_input)[0]
            st.success(f"🎯 Estimated Age: **{int(round(prediction))} years**")

        except Exception as e:
            st.error(f"Prediction error: {e}")







# 🧮 CLASSIFICATION MODULE - Seek Treatment Prediction
# ===============================
def classification():
    st.title("🧮 Will You Seek Help? — Prediction Module")
    st.divider()

    st.markdown(
        "This is a **binary classification** challenge — based on your responses about work and personal context, "
        "our model predicts whether you’d likely **seek mental‑health treatment**."
    )

    st.subheader("🔍 Models We Tested")
    st.write("- Logistic Regression — our steady baseline")
    st.write("- Random Forest Classifier — ensemble muscle")
    st.write("- K‑Nearest Neighbors — similarity searcher")
    st.write("- XGBoost Classifier — the speed & accuracy champ")

    # Metrics
    st.markdown("### 📊 Model Performance Snapshot")
    clf_results = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest", "KNN", "XGBoost"],
        "Accuracy": [0.8128, 0.8181, 0.7807, 0.8288],
        "ROC-AUC": [0.8897, 0.9039, 0.8677, 0.9035],
        "F1 Score": [0.84, 0.84, 0.79, 0.86]
    }).sort_values(by="ROC-AUC", ascending=False)
    st.dataframe(
        clf_results.style.format({
            "Accuracy": "{:.4f}",
            "ROC-AUC": "{:.4f}",
            "F1 Score": "{:.4f}"
        }),
        use_container_width=True
    )

    st.image("Images/classification.png",caption="Model ROC Curves — how well we separate Yes vs No seekers.",use_container_width=True)

    st.success("🏆 Best performer: **XGB Classifier** (slightly ahead of Random Forest).")

    # Prediction form
    st.divider()
    st.markdown("## ✏️ Quickfire Questions — Let’s See Your Prediction")
    input_dict_clf = {}

    # Cooler display names
    display_names_clf = {
        "Gender": "👤 Your Gender?",
        "family_history": "🧬 Any family history of mental‑health challenges?",
        "remote_work": "🏡 Work remotely at least half of the time?",
        "tech_company": "💻 Working in a tech/IT company?",
        "obs_consequence": "👀 Have you seen coworkers face backlash over mental‑health issues?",
        "work_interfere": "⚖️ Does mental health interfere with your work?",
        "coworkers": "🤝 Would you openly talk to coworkers about your mental health?",
        "supervisor": "🧑‍💼 Would you discuss mental health with your manager?",
        "benefits": "💳 Does your employer give mental‑health benefits?",
        "seek_help": "📚 Employer provides resources to learn & seek help?",
        "anonymity": "🕵️ Is your privacy protected if you use those resources?",
        "care_options": "🩺 Do you know what mental‑health care options are available at your workplace?",
        "wellness_program": "🏋️ Has your employer covered mental health in wellness programs?",
        "mental_health_consequence": "🚫 Would speaking up about mental health have negative consequences?",
        "phys_health_consequence": "⚠️ Would speaking up about physical health have negative consequences?",
        "mental_vs_physical": "⚖️ Is mental health treated as seriously as physical health?",
        "mental_health_interview": "💬 Would you mention mental health in a job interview?",
        "phys_health_interview": "💬 Would you mention physical health in a job interview?"
    }

    # Only the training columns
    clf_feature_columns = [
        'family_history','Gender','remote_work','tech_company','obs_consequence','work_interfere',
        'supervisor','coworkers','benefits','wellness_program','seek_help','anonymity',
        'mental_vs_physical','care_options','mental_health_consequence','phys_health_consequence',
        'mental_health_interview','phys_health_interview'
    ]

    # Build form
    for col in clf_feature_columns:
        options = df[col].dropna().unique().tolist()
        label = display_names_clf.get(col, col)
        input_dict_clf[col] = st.selectbox(label, options)

    input_df = pd.DataFrame([input_dict_clf])

    # Reverse mapping
    genmap = {'Female': 1, 'Male': 0, 'Others': 0.5}
    input_df['Gender'] = input_df['Gender'].replace(genmap)
    yn_rev = {'Yes': 1, 'No': 0}
    yn50_rev = {'Yes': 1, 'No': 0, 'Some of them': 0.5}
    ynmaybe_rev = {'Yes': 1, 'No': 0, 'Unknown/Maybe': 0.5}

    input_df[['family_history','remote_work','tech_company','obs_consequence']] = \
        input_df[['family_history','remote_work','tech_company','obs_consequence']].replace(yn_rev)
    work_map_rev = {'Often': 1, 'Sometimes': 0.75, 'Rarely': 0.25, 'Never': 0}
    input_df['work_interfere'] = input_df['work_interfere'].replace(work_map_rev)
    input_df[['supervisor','coworkers']] = input_df[['supervisor','coworkers']].replace(yn50_rev)
    othercols = [
        'benefits','wellness_program','seek_help','anonymity','mental_vs_physical',
        'care_options','mental_health_consequence','phys_health_consequence',
        'mental_health_interview','phys_health_interview'
    ]
    input_df[othercols] = input_df[othercols].replace(ynmaybe_rev)

    # Ensure correct format for model
    input_df = input_df[clf_feature_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

    # Predict
    if st.button("🚀 Run Prediction"):
        try:
            prediction = clf_model.predict(input_df)[0]
            if prediction == 1:
                st.success("✅ Our model thinks you’d **likely** seek professional mental‑health treatment.")
            else:
                st.error("❌ Our model predicts you’d **probably not** seek professional mental‑health treatment.")
        except Exception as e:
            st.error(f"⚠️ Prediction failed: {e}")

    footer()

    
# clustering..
def clustering():
    st.title("🌀  Persona Clustering")
    st.markdown("""
        🚀 Discover the hidden 'human clusters' of the tech world!  
        Using advanced AI clustering, we identified distinct mental-health personas that reveal how professionals
        experience, talk about, and seek support for their well-being at work.
    """)
    st.divider()

    # Data prep summary
    st.markdown("#### 🔍 Data Prep in a Nutshell")
    st.info("""
        To focus purely on mindset and workplace experience, we skipped low-impact details like demographics
        and direct benefit listings, so these clusters reflect *attitudes and lived experiences*, not just personal stats.
    """)
    st.divider()
    

    # Techniques used
    st.markdown("#### 🛠️ How We Found These Personas")
    st.write("""
        - **PCA** → Distilled data down to core dimensions  
        - **t-SNE** → Visualized complex relationships  
        - **UMAP** → Best at revealing sharp, well-formed clusters
    """)
    st.image("Images/c1.png", caption="PCA, t‑SNE & UMAP in action", use_container_width=True)
   
    st.divider()
    st.markdown("#### 📊 Who Clustered Best?")
    st.write("""
        We tested multiple algorithms using the silhouette score:  
        - 🏆 **K-Means:** 0.4836 — clear winner  
        - **Agglomerative:** 0.4619  
        - **DBSCAN:** 0.2192 — fragmented with noise/outliers  
        Result? **6 personas** that actually make sense in the real world.
    """)
    st.image("Images/c2.png", caption="Clustering Algorithm Comparison", use_container_width=True)
    

    st.divider()
    st.markdown("#### 🧩 Meet the Personas")

    # New tab names & persona descriptions
    persona_tabs = st.tabs([
        "🌿 Grounded Observers", 
        "🔥 Struggling Communicators", 
        "😎 Unaware Enthusiasts",
        "📢 Aware Advocates", 
        "🚫 Detached Skeptics", 
        "⚖️ Cautious Veterans"
    ])

    with persona_tabs[0]:
        st.markdown("### 🌿 Grounded Observers")
        st.write("""
        Mid-career pros who’ve got their mental game on lock — steady, approachable, and socially in sync.  
        But when it comes to formal mental-health channels (leave, confidentiality, where to even *start*),  
        they’re a little lost. Happy and grounded, but not tapping into structured support yet.
        """)

    with persona_tabs[1]:
        st.markdown("### 🔥 Struggling Communicators")
        st.write("""
        Fighting the good fight against daily stress — some are in therapy, many juggling work disruptions.  
        They speak up, reach out, and *want* to be heard. But… corporate policy mazes and rigid systems slow them down.  
        Courageous in conversation, but often stuck in unsympathetic setups.
        """)

    with persona_tabs[2]:
        st.markdown("### 😎 Unaware Enthusiasts")
        st.write("""
        The “all good here” crew — whether it's true or not.  
        They haven’t sought help, barely know the rules, and their sunny vibe might come more from inexperience  
        or a culture of silence than actual well-being. Fun to hang out with, but totally unplugged from the mental-health loop.
        """)

    with persona_tabs[3]:
        st.markdown("### 📢 Aware Advocates")
        st.write("""
        Sharp to the fact that mental health *matters* for performance — many have sought help before.  
        They thrive with supportive teammates and open leaders.  
        Still, they’re wading through fog around things like anonymity, leave rights, and official processes.  
        Confident, mindful, and subtly shifting workplace culture toward openness.
        """)

    with persona_tabs[4]:
        st.markdown("### 🚫 Detached Skeptics")
        st.write("""
        Often the younger hustlers — unconvinced mental health even *touches* their work life.  
        Not into seeking help, rarely know the policies, and might get minor peer support at best.  
        Keep their distance from the wellness conversation entirely, intentionally or not.
        """)

    with persona_tabs[5]:
        st.markdown("### ⚖️ Cautious Veterans")
        st.write("""
        Been to battle before — many have sought treatment in the past — but now? They hesitate.  
        Burnout, distrust, or policy confusion holds them back.  
        Workplace support is hit-or-miss, depending on who’s around.  
        They’re wise, aware, but playing the game carefully until the system feels safe.
        """)

    st.divider()
    st.caption("✨ Freshly crafted descriptions + names, aligned with our latest insights.")

    footer()

pg = st.navigation([
    st.Page(Home, title="👾 Home"),
    st.Page(eda, title="🎲 Exploratory Data Analysis"),
    st.Page(classification, title=" 🪄Classification Task"),
    st.Page(regression, title="📈 Regression Task"),
    st.Page(clustering, title="🌀  Persona Clustering")
])
pg.run()
