# Breast Cancer Classification Model Comparison - Deployment Guide

## Overview
This project implements and compares 5 machine learning classification models on the **Breast Cancer dataset** (569 samples, 30 features, binary classification).

## ✅ What's Included

### Code Files
- **model_training.py** - ML pipeline with 5 classification models
- **streamlit_app.py** - Interactive web application
- **requirements.txt** - Python dependencies

### Launch Scripts
- **run_app.bat** - Windows batch script to launch the app
- **run_app.ps1** - PowerShell script to launch the app

## 🚀 Quick Start

### Option 1: Using Batch Script (Windows)
```batch
run_app.bat
```

### Option 2: Using PowerShell
```powershell
.\run_app.ps1
```

### Option 3: Manual Launch
```bash
cd "d:\BITS_WILP\Sem 1\ML\Assignment 2"
python -m streamlit run streamlit_app.py
```

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 📦 Installation

Dependencies are automatically installed via `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Installed Packages
- **streamlit** >= 1.28.0 - Web framework
- **scikit-learn** >= 1.3.0 - Machine learning library
- **pandas** >= 1.5.0 - Data manipulation
- **numpy** >= 1.24.0 - Numerical computing
- **matplotlib** >= 3.7.0 - Plotting library
- **seaborn** >= 0.12.0 - Statistical visualization
- **joblib** >= 1.3.0 - Model persistence

## 🎯 Features

The Streamlit app provides:

### 1. **Dataset Information**
   - Training/Testing split: 80/20
   - 569 total samples
   - 30 cancer characteristics
   - Binary classification (Malignant vs Benign)

### 2. **Model Performance Metrics**
   - Accuracy
   - AUC Score
   - Precision
   - Recall
   - F1 Score
   - Matthews Correlation Coefficient (MCC)

### 3. **Classification Models**
   1. **Logistic Regression** - Linear model
   2. **Decision Tree** - Tree-based model
   3. **K-Nearest Neighbors** - Instance-based model
   4. **Gaussian Naive Bayes** - Probabilistic model
   5. **Random Forest** - Ensemble model

### 4. **Visualizations**
   - Accuracy vs AUC comparison chart
   - Precision, Recall & F1 Score chart
   - Metrics heatmap
   - Best performing models highlight

### 5. **Model Insights**
   - Detailed observations for each model
   - Performance characteristics
   - Overall recommendations

## 🌐 Accessing the App

Once launched, the app will be available at:
```
http://localhost:8501
```

The browser will open automatically. If not, manually navigate to the URL above.

## 📊 Dataset Information

**Breast Cancer Dataset (from scikit-learn)**
- **Source:** UCI Machine Learning Repository
- **Problem Type:** Binary Classification
- **Samples:** 569
- **Features:** 30 cancer characteristics (measurements of cell nuclei)
- **Classes:** 
  - 0 = Malignant
  - 1 = Benign
- **Train/Test Split:** 80/20 (455 training, 114 testing)

## 🎓 Model Comparison

The application trains and compares 5 different classification algorithms:

| Model | Type | Use Case |
|-------|------|----------|
| Logistic Regression | Linear | Baseline, interpretable |
| Decision Tree | Tree-based | Non-linear, easy to visualize |
| KNN | Instance-based | Local patterns, sensitive to scaling |
| Naive Bayes | Probabilistic | Fast, feature independence |
| Random Forest | Ensemble | Robust, handles interactions |

## 💾 Saved Models

After the first run, trained models are saved to the `model/` directory:
```
model/
├── logistic_regression_model.pkl
├── decision_tree_model.pkl
├── knn_model.pkl
├── naive_bayes_model.pkl
├── random_forest_model.pkl
└── feature_scaler.pkl
```

## 🔧 Configuration

Streamlit configuration is stored in `~/.streamlit/config.toml`:
```toml
[general]
email = ""

[logger]
level = "error"
```

## 📝 Project Structure

```
Assignment 2/
├── streamlit_app.py              # Web application
├── model_training.py             # ML training pipeline
├── requirements.txt              # Dependencies
├── run_app.bat                   # Windows launcher
├── run_app.ps1                   # PowerShell launcher
├── DEPLOYMENT_GUIDE.md           # This file
├── model_evaluation_results.csv  # Results export
├── test_data.csv                 # Dataset export
└── model/                        # Trained models directory
    ├── logistic_regression_model.pkl
    ├── decision_tree_model.pkl
    ├── knn_model.pkl
    ├── naive_bayes_model.pkl
    ├── random_forest_model.pkl
    └── feature_scaler.pkl
```

## 🐛 Troubleshooting

### App won't start
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Try launching manually: `python -m streamlit run streamlit_app.py`

### Port already in use
- The app uses port 8501 by default
- To use a different port: `streamlit run streamlit_app.py --server.port=8502`

### Models not training
- Ensure scikit-learn is properly installed
- Check console for error messages
- Verify 569 samples of breast cancer data are being loaded

### No results displayed
- Wait for model training to complete (first run takes ~30 seconds)
- Check if models are caching properly
- Try clearing Streamlit cache: `streamlit cache clear`

## 📈 Expected Model Performance

Typical accuracy ranges on the Breast Cancer dataset:
- **Random Forest:** 95-97%
- **Logistic Regression:** 95-96%
- **SVM/KNN:** 94-96%
- **Naive Bayes:** 93-95%
- **Decision Tree:** 90-95%

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review model_training.py for implementation details
3. Check Streamlit documentation: https://docs.streamlit.io/

## ✨ Key Updates

- ✅ Dataset changed from Wine (178 samples) to Breast Cancer (569 samples)
- ✅ Meets minimum requirement of 500+ samples
- ✅ Binary classification problem (vs multi-class)
- ✅ 30 features (vs 13 in Wine dataset)
- ✅ All code references updated
- ✅ Deployment scripts created
- ✅ Streamlit app fully configured

---

**Last Updated:** August 13, 2026
**Dataset:** Breast Cancer Classification
**Total Samples:** 569
**Features:** 30
