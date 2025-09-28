    

# 🎓 Student Performance Analysis Dashboard

A comprehensive web-based dashboard built with Streamlit for analyzing student academic performance data. This project was developed as part of the ITD105 course requirements, demonstrating exploratory data analysis techniques and interactive data visualization.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset Information](#dataset-information)
- [Dashboard Structure](#dashboard-structure)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Academic Context](#academic-context)
- [License](#license)

## 🔍 Overview

This interactive dashboard provides comprehensive analysis of student performance data from Portuguese secondary schools. It enables educators, administrators, and researchers to explore relationships between various factors (demographic, social, and academic) and student outcomes through dynamic visualizations and statistical analysis.

The dashboard implements all core activities required for exploratory data analysis:

- Data loading and preview
- Dataset information analysis
- Statistical summaries
- Correlation analysis
- Distribution exploration
- Interactive visualizations

## ✨ Features

### 🎛️ Interactive Filtering System

- **School Selection**: Filter by Gabriel Pereira (GP) or Mousinho da Silveira (MS)
- **Demographics**: Age range and gender filtering
- **Geographic**: Urban vs Rural address filtering
- **Academic**: Study time, failures, and absences range filtering
- **Real-time Updates**: All visualizations update dynamically with filter changes

### 📊 Comprehensive Visualizations

- **Grade Progression Analysis**: Interactive scatter plots showing G1 → G2 → G3 progression
- **Performance Correlations**: Heatmap revealing relationships between variables
- **Distribution Analysis**: Normalized boxplots for outlier detection
- **Comparative Analysis**: School vs performance, study habits vs outcomes
- **Attendance Impact**: Absences vs academic performance visualization

### 📈 Statistical Insights

- Dynamic correlation calculations
- Performance metrics and comparisons
- Data completeness analysis
- Outlier identification and explanation

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone or Download the Project**

   ```bash
   git clone <repository-url>
   cd student-performance-dashboard
   ```
2. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:

   ```bash
   pip install streamlit pandas numpy matplotlib seaborn scipy plotly
   ```
3. **Run the Dashboard**

   ```bash
   streamlit run student_performance.py
   ```
4. **Access the Dashboard**

   - Open your web browser
   - Navigate to `http://localhost:8501`
   - Upload the `student-mat.csv` file to begin analysis

## 📖 Usage

### Getting Started

1. **Launch the Application**: Run `streamlit run student_performance.py`
2. **Upload Dataset**: Use the file uploader to load `student-mat.csv`
3. **Apply Filters**: Use the sidebar to filter data by various criteria
4. **Explore Tabs**: Navigate through different analysis sections
5. **Interact**: Hover over visualizations for detailed information

### Navigation Guide

- **Sidebar**: Contains all filtering options and displays filtered record count
- **Tab Navigation**: Four main sections for different types of analysis
- **Interactive Charts**: Click, zoom, and hover for detailed insights
- **Dynamic Updates**: All charts update automatically when filters change

## 📊 Dataset Information

### Source

Student Performance Dataset from Portuguese secondary schools, containing information about student academic performance in Mathematics.

### Key Features

- **Demographics**: Age, sex, address type
- **Family Background**: Parental education, jobs, family size
- **Academic History**: Past failures, study time, extra support
- **Social Factors**: Free time, going out, romantic relationships
- **Behavioral**: Alcohol consumption, health status
- **Performance Metrics**: G1 (first period), G2 (second period), G3 (final grade)

### Dataset Statistics

- **Total Records**: 395 students
- **Features**: 33 variables
- **Grade Scale**: 0-20 points
- **Data Quality**: Complete dataset with no missing values

## 🗂️ Dashboard Structure

### Tab 1: 📊 Overview

**Activities B, C, D - Fundamental Data Analysis**

- Data preview and structure analysis
- Missing values assessment
- Comprehensive statistical summaries
- Key performance metrics display

### Tab 2: 📈 Performance Analysis

**Activity G - Interactive Visualizations**

- Grade progression scatter plots (G1 vs G2 vs G3)
- Study time vs performance analysis
- School performance comparisons
- Attendance impact on academic outcomes

### Tab 3: 🔍 Detailed Insights

**Activity E - Correlation Analysis**

- Comprehensive correlation heatmap
- Statistical relationship identification
- Family factor analysis
- Behavioral pattern insights

### Tab 4: 📋 Data Exploration

**Activity F - Distribution Analysis**

- Normalized boxplot visualizations
- Outlier detection and explanation
- Distribution pattern analysis
- Risk factor identification

## 💡 Key Insights

### 🎯 Academic Performance Patterns

- Strong correlation between G1, G2, and G3 grades (0.8+ correlation)
- Early academic performance (G1) is highly predictive of final outcomes
- Study time shows moderate positive correlation with grades

### 👨‍👩‍👧‍👦 Family Influence

- Parental education levels strongly correlate with student performance
- Mother's and father's education show high correlation (0.6+)
- Family educational support impacts student outcomes

### 🚨 Risk Factors

- High absence rates negatively correlate with academic performance
- Alcohol consumption patterns show negative correlation with grades
- Past failures significantly predict future academic struggles

### 🏫 School Differences

- Minimal performance gap between the two schools
- Individual student factors more influential than school choice
- Wide performance distribution within both institutions

## 🛠️ Technologies Used

### Core Framework

- **Streamlit**: Web application framework for Python
- **Python 3.7+**: Primary programming language

### Data Analysis

- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **SciPy**: Statistical analysis

### Visualization

- **Plotly Express**: Interactive plotting library
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical data visualization

### Additional Libraries

- **io**: Input/output operations
- **stats**: Statistical functions

## 📱 Screenshots

### Dashboard Overview

The main interface features a clean, professional layout with:

- Sidebar filtering system
- Tabbed navigation structure
- Real-time data metrics
- Interactive visualizations

### Key Visualizations

- **Correlation Heatmap**: Shows relationships between all numeric variables
- **Grade Progression**: Interactive scatter plots with hover details
- **Distribution Analysis**: Normalized boxplots for comparison
- **Performance Metrics**: Dynamic statistical summaries

## 📋 Requirements

```txt
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
seaborn>=0.11.0
scipy>=1.10.0
plotly>=5.15.0
```

## 🎓 Academic Context

### Course Information

- **Course**: ITD105 - Big Data Analytics
- **Institution**: Mindanao State University - Iligan institute of Technology
- **Academic Year**: 2025-2026, 4th Year 1st Semester

### Learning Objectives Demonstrated

- **Data Loading**: CSV file handling and data preprocessing
- **Exploratory Data Analysis**: Statistical summaries and data profiling
- **Data Visualization**: Multiple chart types and interactive dashboards
- **Statistical Analysis**: Correlation analysis and distribution exploration
- **Web Development**: Interactive dashboard creation using Streamlit

### Project Activities Completed

- ✅ **Activity A**: Dataset loading implementation
- ✅ **Activity B**: Data preview and exploration
- ✅ **Activity C**: Dataset information and missing value analysis
- ✅ **Activity D**: Statistical summary generation
- ✅ **Activity E**: Correlation heatmap visualization
- ✅ **Activity F**: Boxplot distribution analysis
- ✅ **Activity G**: Interactive scatter plot implementation

## 📞 Contact

For questions about this project or academic inquiries:

- **Student**: Crislane Josh B. Eugenio
- **Course**: ITD105 - Big Data Analytics
- **Email**:
  - [josheugenio65@gmail.com](mailto:josheugenio65@gmail.com)
  - [crislanejosh.eugenio@g.msuiit.edu.ph](mailto:crislanejosh.eugenio@g.msuiit.edu.ph)
- **Institution**: Mindanao State University - Iligan Institute of Technology

## 📄 License

This project is created for academic purposes as part of the ITD105 course requirements. The dataset used is publicly available for educational and research purposes.

---

**Note**: This dashboard demonstrates fundamental concepts in data analysis and visualization. It serves as a comprehensive example of interactive dashboard development using modern Python libraries and frameworks.

## 🚀 Future Enhancements

Potential improvements for future versions:

- Machine learning prediction models
- Advanced filtering capabilities
- Export functionality for reports
- Additional visualization types
- Mobile responsiveness optimization
- Database integration capabilities

---

*Built with ❤️ using Streamlit and Python for ITD105 Course Requirements*
