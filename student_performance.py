import io
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="ITD105: Student Performance Analysis Dashboard", page_icon=":chart_with_upwards_trend:", layout="wide")

# Title of the app
st.markdown('# 🎓 Exploratory Data Analysis with Streamlit')
st.write("Welcome to the Student Performance Analysis Dashboard. This project was made as fulfillment for my requirements in my ITD105 Course. This dashboard was made using Streamlit, a Python library for creating custom web applications.")

st.markdown("---")
st.markdown("## Comprehensive Data Analysis of Student Performance")

# File uploader
st.subheader("Activity A: Load the dataset into the Streamlit app")
uploaded_file = st.file_uploader("Upload CSV file here", type="csv")

if uploaded_file is not None:

    st.sidebar.header("🔍 Filter Options")

    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Performance Analysis", "🔍 Detailed Insights", "📋 Data Exploration"])

    # Activity Tasks

    # a. Load the dataset into the Streamlit app.
    df = pd.read_csv(uploaded_file, delimiter=';')

    # Create Average Performance Column, for later analysis
    df['Average_Grade'] = ((df['G1'] + df['G2'] + df['G3']) / 3).round(2)

    # School Filter
    school_filter = st.sidebar.multiselect(
        "Select School:",
        options=df['school'].unique(),
        default=df['school'].unique()
    )

    # Sex Filter
    sex_filter = st.sidebar.multiselect(
        "Select Sex:",
        options=df['sex'].unique(),
        default=df['sex'].unique()
    )
    
    # Age Filter
    age_filter = st.sidebar.slider(
        "Select Age:",
        min_value=df['age'].min(),
        max_value=df['age'].max(),
        value=(df['age'].min(), df['age'].max())
    )
    
    # Address Filter
    address_filter = st.sidebar.multiselect(
        "Select Address:",
        options=df['address'].unique(),
        default=df['address'].unique()
    )

    # Study Time Filter
    studytime_filter = st.sidebar.slider(
        "Select Study Time:",
        min_value=df['studytime'].min(),
        max_value=df['studytime'].max(),
        value=(df['studytime'].min(), df['studytime'].max())
    )
    
    # Failures Filter
    failures_filter = st.sidebar.slider(
        "Select Failures:",
        min_value=df['failures'].min(),
        max_value=df['failures'].max(),
        value=(df['failures'].min(), df['failures'].max())
    )

    # Absences Filter
    absences_filter = st.sidebar.slider(
        "Select Absences:",
        min_value=df['absences'].min(),
        max_value=df['absences'].max(),
        value=(df['absences'].min(), df['absences'].max())
    )

    # Apply Filters
    filtered_df = df[
        (df['school'].isin(school_filter)) &
        (df['sex'].isin(sex_filter)) &
        (df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1]) &
        (df['address'].isin(address_filter)) &
        (df['studytime'] >= studytime_filter[0]) & (df['studytime'] <= studytime_filter[1]) &
        (df['failures'] >= failures_filter[0]) & (df['failures'] <= failures_filter[1]) &
        (df['absences'] >= absences_filter[0]) & (df['absences'] <= absences_filter[1])
    ]

    st.sidebar.markdown(f"**Filtered Data Information:** {len(filtered_df)} out of {len(df)} records remain")



    with tab1:
        st.header("📊 Dataset Overview")

        # Key Metrics 
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Students", f"{len(filtered_df)} / {len(df)}")
        with col2:
            st.metric("Average Grade", f"{filtered_df['Average_Grade'].mean():.2f} / {df[['G1', 'G2', 'G3']].max().max():.2f}")
        with col3:
            st.metric("School Split Ratio", f"{(filtered_df['school'] == 'GP').sum()} : {(filtered_df['school'] == 'MS').sum()}")


        # b. Display the first few rows of the dataset.
        st.subheader('Activity B: Data Preview')
        st.write(filtered_df.head())

        # Explanation for Data Preview
        st.markdown("""
        **📋 Dataset Insights:**
        - Each row represents a **unique student** with their academic and personal characteristics
        - Key features include **demographic information** (age, sex, address), **family background** (parental education, jobs), and **academic performance** (G1, G2, G3 grades)
        - The data provides a comprehensive view of factors that may influence student success
        """)

        col1, col2 = st.columns(2)

        with col1:
            # c. Show dataset information (e.g., data types, missing values).
            st.subheader('Activity C.1: Dataset Information')

            # Show columns, rows, and data types
            st.write("Dataset Information (Columns, Rows, Data Types)")
            buffer = io.StringIO()
            filtered_df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text(info_str)

            st.markdown("""
            **🔍 Data Structure Analysis:**
            - **Mixed data types**: Combination of numerical and categorical variables
            - **Categorical features**: School, gender, family status, parental jobs
            - **Numerical features**: Grades, age, study time, absences
            - **Data quality**: Check for appropriate data types and memory usage
            """)

        with col2:
            st.subheader('Activity C.2: Missing Values')
            # Show missing values
            st.write("Missing Values")
            st.write(filtered_df.isnull().sum())

            # Explanation for Missing Values
            missing_count = filtered_df.isnull().sum().sum()
            st.markdown(f"""
            **✅ Data Completeness Analysis:**
            - **Total missing values**: {missing_count}
            - **Data quality**: {"Excellent - No missing values!" if missing_count == 0 else "Some missing values detected"}
            - **Reliability**: {"High data integrity for analysis" if missing_count == 0 else "May need data cleaning"}
            """)


            # d. Generate summary statistics for the dataset.
            st.subheader('Activity D: Summary Statistics for the dataset')
            st.write(filtered_df.describe())

             # Explanation for Summary Statistics
            st.markdown(f"""
            **📈 Statistical Overview:**
            - **Grade Range**: Students scored between {filtered_df['G3'].min():.1f} and {filtered_df['G3'].max():.1f} (final grade)
            - **Average Performance**: Mean final grade is {filtered_df['G3'].mean():.2f}/20
            - **Age Distribution**: Students aged {filtered_df['age'].min()}-{filtered_df['age'].max()} years
            - **Study Patterns**: Average study time is {filtered_df['studytime'].mean():.1f}/4 scale
            """)


    with tab2:
        st.header("📈 Performance Analysis")

        # Activity g: Use Plotly to create an interactive scatter plot of student performance.
        st.subheader('Activity G: Interactive Scatter Plot of Student Performance')

        # G1 vs G2 vs G3
        st.write("**Grade Progression: G1 vs G2 vs G3**")
        fig_grades = px.scatter(filtered_df, 
            x='G1', y='G2', color='G3', 
            title='Grade Progression: G1 vs G2 vs G3',
            hover_data=['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences'],
            labels={
                'G1': 'First Period Grade', 
                'G2': 'Second Period Grade', 
                'G3': 'Final Grade'
            }
        )
        fig_grades.update_layout(width=800, height=600)
        st.plotly_chart(fig_grades)

        # Explanation for Grade Progression
        st.markdown("""
        **🎯 Grade Progression Analysis:**
        - **Positive Correlation**: Clear positive relationship between G1, G2, and G3 grades
        - **Consistent Performance**: Students who perform well in G1 tend to maintain performance in G2 and G3
        - **Early Warning**: Poor G1 scores often predict lower final grades (G3)
        - **Improvement Patterns**: Some students show upward trends from G1 to G3 (points above diagonal)
        - **Risk Identification**: Students below the trend line may need additional support
        """)

        

        # Study Time vs. Average Performance
        st.write("**Study Time vs. Average Performance**")
        fig_study = px.scatter(filtered_df, 
            x='studytime', 
            y='Average_Grade',
            title='Study Time vs. Average Performance',
            hover_data=['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences'],
            labels={
                'studytime': 'Study Time', 
                'Average_Grade': 'Average Grade'
            }
        )
        fig_study.update_layout(width=800, height=600)
        st.plotly_chart(fig_study)

        # Explanation for Study Time
        correlation_study_grade = filtered_df['studytime'].corr(filtered_df['Average_Grade'])
        st.markdown(f"""
        **📚 Study Habits Impact:**
        - **Correlation Strength**: {abs(correlation_study_grade):.3f} correlation between study time and grades
        - **Study Time Scale**: 1 = <2hrs, 2 = 2-5hrs, 3 = 5-10hrs, 4 = >10hrs per week
        - **Performance Trend**: {"Positive" if correlation_study_grade > 0 else "Negative"} relationship - more study time generally leads to {"better" if correlation_study_grade > 0 else "worse"} grades
        - **Individual Variation**: Some students achieve high grades with minimal study time (natural ability)
        - **Efficiency Matters**: Quality of study time may be more important than quantity alone
        """)


        # School vs. Average Performance
        st.write("**School vs. Average Performance**")
        fig_school = px.scatter(filtered_df, 
            x='school', y='Average_Grade', color='school', 
            title='School vs. Average Performance',
            hover_data=['sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences'],
            labels={
                'school': 'School', 
                'Average_Grade': 'Average Grade'
            }
        )
        fig_school.update_layout(width=800, height=600)
        st.plotly_chart(fig_school)

        # Explanation for School Performance
        gp_avg = filtered_df[filtered_df['school'] == 'GP']['Average_Grade'].mean()
        ms_avg = filtered_df[filtered_df['school'] == 'MS']['Average_Grade'].mean()
        st.markdown(f"""
        **🏫 School Performance Comparison:**
        - **Gabriel Pereira (GP)**: Average grade of {gp_avg:.2f}
        - **Mousinho da Silveira (MS)**: Average grade of {ms_avg:.2f}
        - **Performance Gap**: {abs(gp_avg - ms_avg):.2f} points difference between schools
        - **Distribution**: Wide spread in both schools indicates individual student factors matter more than school
        - **School Effect**: {"Minimal" if abs(gp_avg - ms_avg) < 1 else "Moderate"} school-level differences in student outcomes
        """)


        # Absences vs. Average Performance
        st.write("**Absences vs. Average Performance**")
        fig_absences = px.scatter(filtered_df,
            x='absences', y='Average_Grade', color='absences',
            title='Absences vs. Average Performance',
            hover_data=['sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences'],
            labels={
                'absences': 'Absences',
                'Average_Grade': 'Average Grade'
            }
        )
        fig_absences.update_layout(width=800, height=600)
        st.plotly_chart(fig_absences)

        # Explanation for Absences
        correlation_absence_grade = filtered_df['absences'].corr(filtered_df['Average_Grade'])
        high_absence_threshold = filtered_df['absences'].quantile(0.75)
        st.markdown(f"""
        **📅 Attendance Impact Analysis:**
        - **Correlation**: {correlation_absence_grade:.3f} correlation between absences and grades
        - **Attendance Pattern**: Students with >{high_absence_threshold:.0f} absences show {"lower" if correlation_absence_grade < 0 else "higher"} average performance
        - **Critical Threshold**: Excessive absences (>20) often correlate with academic struggles
        - **Engagement Indicator**: Regular attendance reflects student engagement and commitment
        - **Intervention Opportunity**: High absence rates can signal need for student support
        """)


        with tab3:
            st.header("🔍 Detailed Insights")

            # Activity e: Create a heatmap to visualize correlations between features.
            st.subheader("Activity E: Heatmap to Visualize Correlations between Features")

            numeric_df = filtered_df.select_dtypes(include=[np.number])
            corr = numeric_df.corr()
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax, annot_kws={"size": 5})
            ax.set_title('Correlation Heatmap of Numeric Features')
            st.pyplot(fig)

            # Enhanced explanation for correlation heatmap
            strong_corr_pairs = []
            for i in range(len(corr.columns)):
                for j in range(i+1, len(corr.columns)):
                    corr_val = abs(corr.iloc[i, j])
                    if corr_val > 0.5:
                        strong_corr_pairs.append((corr.columns[i], corr.columns[j], corr.iloc[i, j]))

            st.markdown("""
            ### 🔍 **Correlation Analysis Insights:**
            
            **📊 Key Findings:**
            """)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                **🎯 Strong Positive Correlations:**
                - **G1 ↔ G2 ↔ G3**: Academic consistency across periods
                - **Medu ↔ Fedu**: Parental education alignment  
                - **Dalc ↔ Walc**: Daily and weekend alcohol consumption patterns
                """)

            with col2:
                st.markdown("""
                **📈 Moderate Correlations:**
                - **Parent Education ↔ Student Grades**: Family background influence
                - **Study Time ↔ Academic Performance**: Effort-outcome relationship
                """)
            
            with col3:
                st.markdown("""
                **💡 Insights:**
                - **Family factors** significantly influence student outcomes
                - **Behavioral patterns** (alcohol, absences) predict academic risk
                """)



        with tab4:
            st.header("📋 Data Exploration")

            # Activity f: Display a boxplot for exploratory visualization of numeric features.
            st.subheader("Activity F: Boxplot for Exploratory Visualization of Numeric Features")
            
            fig, ax = plt.subplots(figsize=(12, 8))

            # Normalize and bring to same scale for better visualization
            normalized_data = []
            labels = []

            for col in numeric_df.columns:
                if filtered_df[col].max() != filtered_df[col].min():  # Avoid division by zero
                    normalized_values = (filtered_df[col] - filtered_df[col].min()) / (filtered_df[col].max() - filtered_df[col].min())
                else:
                    normalized_values = filtered_df[col] * 0  # All same value
                normalized_data.append(normalized_values)
                labels.append(col)

            ax.boxplot(normalized_data, labels=labels)
            ax.set_title('Boxplot for Exploratory Visualization of Numeric Features')
            ax.set_xlabel('Features')
            ax.set_ylabel('Normalized Values')
            ax.set_xticklabels(labels, rotation=45, ha='right')
            st.pyplot(fig)

            # Explanation for Boxplot
            st.markdown("""
            ### 📦 **Boxplot Distribution Analysis:**
            
            **🔍 What the Boxplot Shows:**
            """)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("""
                - **Box**: Interquartile range (25th to 75th percentile)
                - **Line in Box**: Median (50th percentile)  
                """)

            with col2:
                st.markdown("""
                - **Whiskers**: Data range within 1.5 × IQR
                - **Dots**: Outliers beyond whiskers
                """)
            
            st.markdown("""
            **📊 Key Insights:**
            """)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                **🎯 Grade Distributions (G1, G2, G3):**
                - **Median Performance**: Around 0.5 on normalized scale
                - **Spread**: Wide distribution indicates diverse student abilities
                - **Outliers**: Students with exceptionally high/low performance
                """)
            
            with col2:
                st.markdown("""
                **📈 Other Feature Patterns:**
                - **Age**: Concentrated around median age with few outliers
                - **Study Time**: Most students study 2-5 hours weekly  
                - **Absences**: Right-skewed distribution (few students with many absences)
                - **Failures**: Most students have 0 failures, few with multiple
                """)
            
            st.markdown("""
            **💡 Practical Implications:**
            - **Normal Distribution**: Grades follow expected bell curve pattern
            - **Risk Identification**: Outliers in absences/failures need attention
            - **Resource Allocation**: Understanding typical ranges helps in planning interventions
            """)
