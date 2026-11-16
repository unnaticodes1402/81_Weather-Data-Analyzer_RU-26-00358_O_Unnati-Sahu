# Weather Data Analyzer

## 1. Project Information

- **Project Title:** Weather Data Analyzer
- **PS Number:** 81
- **Course:** Bachelor of Technology (B.Tech)
- **Programming Language:** Python 3
- **Semester:** First Semester

## 2. Project Description

Weather Data Analyzer is a Python-based project that reads daily weather data from a CSV file and performs data analysis.

It analyzes temperature, humidity and rainfall data, cleans missing values and duplicate records, calculates statistical information and displays graphical representations of weather trends.

## 3. Objectives

- To load weather data from a CSV file.
- To clean missing values and duplicate records.
- To calculate average, maximum and minimum temperature.
- To calculate standard deviation and total rainfall.
- To visualize weather information using charts.

## 4. Technologies and Libraries Used

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| Pandas | Data loading and cleaning |
| NumPy | Mathematical calculations |
| Matplotlib | Data visualization |

## 5. Input Data Format

The CSV file contains the following columns:

- Date
- Temp
- Humidity
- Rainfall

Example:

```csv
Date,Temp,Humidity,Rainfall
2026-08-01,32,70,0
2026-08-02,34,65,0
2026-08-03,30,80,12
```

## 6. Features

1. CSV File Loading
2. Weather Data Summary
3. Missing Value Handling
4. Duplicate Record Removal
5. Statistical Analysis
6. Temperature Trend Line Chart
7. Rainfall Bar Chart
8. Invalid File Handling

## 7. Data Analysis

The program calculates:

- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Standard Deviation
- Total Rainfall

Missing numerical values are filled using the column mean, and duplicate rows are removed.

## 8. How to Run the Project

**Step 1:** Install Python 3.

**Step 2:** Install the required libraries.

```bash
pip install pandas numpy matplotlib
```

**Step 3:** Open the project folder in VS Code.

**Step 4:** Run the Python file.

```bash
python weather_analyzer.py
```

**Step 5:** Enter the CSV filename.

```text
weather.csv
```

**Step 6:** Select an option from the menu.

- Option 1: Summary
- Option 2: Clean & Plot
- Option 3: Exit

## 9. Test Cases

The project is tested using four test scenarios:

1. Normal Input
2. Boundary / Minimum Input
3. Invalid Input
4. Different Valid Scenario (Missing Values and Duplicates)

Test case screenshots are available in the Testcases folder.

## 10. Project Folder Structure

```text
Weather_Data_Analyzer/
│
├── Testcases/
│   ├── test1_normal.png
│   ├── test2_boundary.png
│   ├── test3_invalid.png
│   ├── test4_cleaning.png
│   ├── test4_line_chart.png
│   └── test4_bar_chart.png
│
└── Codebase/
    ├── weather_analyzer.py
    ├── weather.csv
    └── README.md
```

## 11. Conclusion

The Weather Data Analyzer project demonstrates how Python libraries such as Pandas, NumPy and Matplotlib can be used for data cleaning, statistical analysis and visualization.

It provides a simple way to analyze weather information and understand temperature and rainfall trends.

## 12. Author

**Name:** Unnati Sahu

**Project:** Weather Data Analyzer

**PS Number:** 81
