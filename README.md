# 📊 Real A/B Test Evaluation – Statistical Significance Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Testing-8CAAE6?logo=scipy&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Z--Test-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-9cf)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🎯 Project Overview

This project evaluates whether a **new webpage design** leads to a statistically significant improvement in **user conversion rates** compared to the existing page.

Using **real-world A/B test data** with ~300,000 user sessions, I applied rigorous statistical testing to determine whether the observed differences in conversion rates were meaningful — or simply due to chance.

---

## 📁 Project Structure

```
Real-A-B-Test-Evaluation/
├── ab_test_analysis.ipynb       # Main analysis notebook (EDA + hypothesis testing)
├── data_preprocessing.py        # Data loading and cleaning utilities
├── hypothesis_testing.py        # Z-test logic (reusable module)
├── data/
│   └── ab_data.csv              # Raw A/B test dataset (~300k rows)
├── results/
│   └── ab_test_summary.txt      # Saved test results
└── README.md
```

---

## 📊 Dataset

| Column         | Description                                      |
|----------------|--------------------------------------------------|
| `user_id`      | Unique identifier per user                       |
| `timestamp`    | Time of user visit                               |
| `group`        | `control` (old page) or `treatment` (new page)   |
| `landing_page` | `old_page` or `new_page`                         |
| `converted`    | `1` = converted, `0` = did not convert           |

**Raw dataset size:** 294,478 rows × 5 columns

---

## 🧹 Data Cleaning

Before analysis, the dataset was cleaned in two steps:

1. **Removed mismatched rows** — users in the `treatment` group who saw the `old_page`, or `control` users who saw the `new_page` (3,893 rows dropped).
2. **Removed duplicate users** — users who appeared more than once (1 duplicate removed).

**Cleaned dataset size:** 290,584 rows

---

## 📈 Exploratory Data Analysis

### Conversion Rates by Group

| Group      | Conversion Rate |
|------------|-----------------|
| Control    | **12.04%**      |
| Treatment  | **11.88%**      |
| Overall    | **11.96%**      |

The treatment group showed a *slightly lower* conversion rate than control — but is this difference statistically meaningful?

---

## 🔬 Hypothesis Testing

### Hypotheses

- **H₀ (Null):** The new page does **not** perform better than the old page.
- **H₁ (Alternative):** The new page performs **significantly better** than the old page.

### Test Used: **Two-Proportion Z-Test** (one-tailed)

```python
z_stat, p_val = proportions_ztest(convert_counts, n_obs, alternative='larger')
```

### Results

| Metric       | Value     |
|--------------|-----------|
| Z-Statistic  | -1.3109   |
| P-Value      | 0.9051    |
| Alpha (α)    | 0.05      |
| Decision     | ❌ Fail to Reject H₀ |

### ✅ Conclusion

> With a p-value of **0.9051**, far above the significance threshold of 0.05, there is **no statistically significant evidence** that the new page outperforms the old page.
>
> **Business Recommendation:** Do not roll out the new page — the data does not support the claim of improved conversion performance.

---

## 🛠️ Tech Stack

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Python 3.12    | Core language                    |
| Pandas         | Data manipulation & cleaning     |
| NumPy          | Numerical operations             |
| Statsmodels    | Z-test for proportions           |
| SciPy          | Statistical utilities            |
| Seaborn        | Data visualization               |
| Matplotlib     | Plot rendering                   |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/artimistic-afk/Real-A-B-Test-Evaluation.git
cd Real-A-B-Test-Evaluation
```

### 2. Install dependencies
```bash
pip install pandas numpy scipy statsmodels seaborn matplotlib
```

### 3. Run the analysis
Open and run `ab_test_analysis.ipynb` in Jupyter Notebook, or use the modular scripts:

```python
from data_preprocessing import load_data, clean_data
from hypothesis_testing import perform_z_test

df = load_data('data/ab_data.csv')
df_clean = clean_data(df)

# Run Z-test
z, p, conclusion = perform_z_test([treatment_conversions, control_conversions],
                                   [n_treatment, n_control])
print(conclusion)
```

---

## 📌 Key Takeaways

- Analyzed **~300k real user sessions** across two groups in a controlled experiment
- Built a **modular, reusable pipeline** for data cleaning and hypothesis testing
- Applied **two-proportion z-test** to evaluate statistical significance rigorously
- Avoided a **false positive** — correctly identified that the new design showed no meaningful improvement
- Demonstrated ability to translate statistical findings into **clear business recommendations**

---

## 👤 Author

**Abdurrahman Tahir** — Junior Data Scientist / ML Engineer

🌍 Islamabad, Pakistan | Targeting Berlin, Germany 🇩🇪

[![GitHub](https://img.shields.io/badge/GitHub-artimistic--afk-black?logo=github)](https://github.com/artimistic-afk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-abdurrahmantahir79-blue?logo=linkedin)](https://www.linkedin.com/in/abdurrahmantahir79/)
