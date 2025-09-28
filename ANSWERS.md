# 📊 Student Performance Data Analysis - Key Questions & Insights

## Name: Crislane Josh B. Eugenio
## Course and Section: ITD105 - IT4D.1

This document provides detailed answers to critical analytical questions about student academic performance based on the exploratory data analysis performed in our Streamlit dashboard.

## 🎯 Research Questions Addressed

### 1. Which features have the highest correlation with final exam scores (G1, G2, G3)?
### 2. How does study time correlate with exam performance?  
### 3. What insights can you draw from the boxplot?
### 4. How does gender impact the final exam score?

---

## 📈 Question 1: Which features have the highest correlation with final exam scores (G1, G2, G3)?

1. **G1 ↔ G2**: **0.85** correlation
   - First period grades highly predict second period performance
   - Indicates consistent academic performance patterns

2. **G1 ↔ G3**: **0.80** correlation  
   - Early academic performance strongly predicts final outcomes
   - Critical early warning indicator for student success

3. **G2 ↔ G3**: **0.90** correlation
   - Second period grades are the strongest predictor of final grades
   - Demonstrates academic momentum and consistency

4. **Failures ↔ Final Grade**: **-0.35** correlation
   - Past academic failures strongly predict lower performance
   - Early intervention critical for at-risk students


---

## 📚 Question 2: How does study time correlate with exam performance?  

### **Statistical Relationship:**
- **Correlation Coefficient**: **+0.13** (slightly positive)
- **Study Time Scale**: 
  - 1 = <2 hours/week
  - 2 = 2-5 hours/week  
  - 3 = 5-10 hours/week
  - 4 = >10 hours/week

### **Performance Patterns:**
1. **Linear Trend**: Generally positive relationship - more study time → better grades
2. **Diminishing Returns**: Increase from level 3→4 shows smaller performance gains
3. **Individual Variation**: High performers exist at all study time levels
4. **Efficiency Factor**: Some students achieve excellent results with minimal study time

### 📈 **Grade Distribution by Study Time:**
- **Level 1 (<2hrs)**: Average grade **10.25**/20
- **Level 2 (2-5hrs)**: Average grade **10.44**/20  
- **Level 3 (5-10hrs)**: Average grade **11.65**/20
- **Level 4 (>10hrs)**: Average grade **11.73**/20

### 🎯 **Key Insights**
1. **Study time alone doesn't guarantee success** - Despite the significant amount of hours put into studying, minimal improvements 
2. **Quality over quantity** - Effective study methods may matter more than hours spent
3. **Natural ability factor** - Some students perform well regardless of study time
4. **Optimal range** appears to be 5-10 hours per week for most students


---

## 📦 Question 3: What insights can you draw from the boxplot?

### 🔍 **Visualization Analysis**
The normalized boxplot reveals distribution patterns, outliers, and variability across all numeric features.

### 📊 **Key Distribution Insights**

#### **Grade Distributions (G1, G2, G3):**
- **Median Performance**: Around 0.5 on normalized scale (≈12-13/20 actual grades)
- **Quartile Spread**: 
  - Q1: ~0.25 (≈9-10 points)
  - Q3: ~0.75 (≈15-16 points)
- **Outliers**: 
  - **High performers**: Students scoring 18-20/20
  - **At-risk students**: Students scoring <6/20

#### **Age Distribution:**
- **Concentrated Range**: Most students aged 15-17
- **Few Outliers**: Students aged 19-22 (likely grade repeaters)
- **Tight Distribution**: Low variability indicates standard school progression

#### **Study Time Pattern:**
- **Modal Category**: Level 2 (2-5 hours) most common
- **Right Skew**: Few students study >10 hours/week
- **Outliers**: Very high study time students often struggling academically

#### **Absences Distribution:**
- **Highly Skewed**: Most students have 0-10 absences
- **Extreme Outliers**: Students with 50+ absences
- **Risk Identification**: High absence students clearly identifiable

#### **Failures Distribution:**
- **Zero-Inflated**: Majority of students have 0 past failures
- **Discrete Steps**: Clear categories at 0, 1, 2, 3+ failures
- **Early Warning**: Even 1 failure indicates higher risk

### 🎯 **Critical Insights from Boxplots**

#### **Risk Factor Identification:**
1. **Chronic Absenteeism**: Students with >20 absences need immediate intervention
2. **Age Outliers**: Older students (19+) require academic support
3. **Multiple Failures**: Students with 2+ past failures at high risk

#### **Normal Performance Patterns:**
1. **Grade Consistency**: Similar distributions across G1, G2, G3 periods
2. **Expected Spread**: Wide performance range indicates diverse student abilities
3. **Median Performance**: Average student scores around 12-13/20


---

## 👥 Question 4: How does gender impact the final exam score?

### 📊 **Statistical Analysis Results**

#### **Performance Comparison:**
- **Male Students**: Mean Average Grade = **11.07** (n=187, σ=3.76, Median=11.0)
- **Female Students**: Mean Average Grade = **10.32** (n=208, σ=3.61, Median=10.0)
- **Performance Gap**: **+0.75 points** in favor of male students
- **Sample Distribution**: Relatively balanced (47.3% male, 52.7% female)

### 🔍 **Key Findings**

#### **Modest Gender Difference:**
- **Small Effect Size**: The 0.75-point difference represents approximately **7.5%** improvement on a 20-point scale
- **Practical Significance**: While statistically observable, the difference is relatively small in educational terms
- **Consistent Medians**: Both groups show identical patterns (11 vs 10 median scores align with means)

#### **Similar Variability Patterns:**
- **Standard Deviations**: Nearly identical spread (Male: 3.76, Female: 3.61)
- **Performance Range**: Both groups show **similar distribution patterns** with comparable variability
- **Individual Differences**: Within-group variation (±3.7 points) is **much larger** than between-group difference (0.75 points)

### 💡 **Interpretation and Implications**

#### **Statistical Context:**
- **Overlapping Distributions**: The high standard deviations indicate substantial overlap between male and female performance ranges
- **Individual Factors Dominate**: Personal characteristics, study habits, and family background likely matter more than gender
- **Balanced Representation**: Sample sizes are adequate for both groups (187 vs 208 students)

#### **Educational Insights:**
1. **Gender is not a strong predictor** of academic performance in this dataset
2. **Individual variation** within each gender group far exceeds the difference between groups  
3. **Both groups perform similarly** around the 10-11 average grade range
4. **Teaching and intervention strategies** should focus on individual needs rather than gender-based approaches

### 🎯 **Professional Conclusions**

#### **Primary Finding:**
While male students show a slightly higher average grade (+0.75 points), the **practical significance is limited** given the substantial overlap in performance distributions and similar variability patterns between groups.

#### **Recommendations:**
- **Avoid Gender-Based Assumptions**: The small difference doesn't justify differential treatment
- **Focus on Individual Assessment**: Personal factors are far more predictive than gender
- **Inclusive Strategies**: Design educational interventions that address individual learning needs regardless of gender
- **Continued Monitoring**: Track these patterns over time to ensure equitable educational outcomes

#### **Data-Driven Conclusion:**
The analysis reveals that **individual student characteristics and circumstances are substantially more influential than gender** in determining academic performance, supporting the need for personalized rather than gender-based educational approaches.


---


## 🎯 Overall Conclusions and Recommendations

### 🔑 **Key Takeaways from Real Data Analysis**

1. **Academic Consistency is Paramount**: Strong correlations between G1, G2, and G3 (0.80-0.90) demonstrate that consistent performance across periods is the strongest predictor of success

2. **Early Warning Systems Work**: G1 scores provide an 80% correlation with final outcomes, making first-period intervention crucial for at-risk students

3. **Study Time Paradox**: Despite conventional wisdom, study time shows minimal correlation with performance (+0.13), suggesting that study **effectiveness** matters far more than study **duration**

4. **Past Failures are Strong Predictors**: The -0.35 correlation between previous failures and current performance highlights the importance of preventing academic setbacks

5. **Gender Differences are Negligible**: With only 0.75 points difference (11.07 vs 10.32) and high variability (±3.7 points), individual factors vastly outweigh gender considerations

6. **Distribution Patterns Reveal Risk Profiles**: Boxplot analysis clearly identifies outliers in absences, age, and failures as primary intervention targets

### 💡 **Strategic Implications**

#### **Data-Driven Decision Making:**
This analysis demonstrates that **statistical evidence should override conventional assumptions**. The weak study time correlation challenges traditional "more hours = better grades" thinking, while strong grade progression correlations support early intervention strategies.

#### **Personalized vs. Demographic Approaches:**
With gender explaining minimal performance variance but individual variation being substantial, educational strategies must be **individually tailored** rather than based on demographic categories.

#### **Prevention vs. Remediation:**
The strong negative correlation with past failures (-0.35) suggests that **preventing the first failure** is more effective than remediating after multiple failures occur.


---

*This analysis demonstrates the power of exploratory data analysis in understanding educational outcomes and informing evidence-based decision making in academic settings.*

## 📚 References

- Dataset: Student Performance Data Set
- Analysis Tool: Custom Streamlit Dashboard for Interactive EDA
- Visualization: Interactive Plotly charts, Seaborn heatmaps, Matplotlib boxplots

---

**Academic Context:** ITD105 - Big Data Analytics
**Analysis Date:** Academic Year 2025-2026
**Tools Used:** Python, Streamlit, Pandas, NumPy, Plotly, Seaborn, Matplotlib