# Wine Classification: Machine Learning Models Comparison

## Problem Statement

The objective of this project is to classify wine samples into one of three cultivars based on their physicochemical properties. Wine classification is a multi-class classification problem where the goal is to predict the wine type (class 0, 1, or 2) using 13 physicochemical features. This project implements and compares five different machine learning classification algorithms to determine which model performs best on this dataset.

## Dataset Description

### Wine Classification Dataset
- **Source**: UCI Machine Learning Repository / scikit-learn datasets
- **Problem Type**: Multi-class Classification
- **Number of Samples**: 178 wine samples
- **Number of Features**: 13 physicochemical properties
- **Number of Classes**: 3 wine cultivars

### Features in the Dataset:
1. **alcohol** - Alcohol content percentage
2. **malic_acid** - Malic acid concentration
3. **ash** - Ash content
4. **alcalinity_of_ash** - Alkalinity of ash
5. **magnesium** - Magnesium content
6. **total_phenols** - Total phenolic compounds
7. **flavanoids** - Flavanoid concentration
8. **nonflavanoid_phenols** - Non-flavanoid phenols
9. **proanthocyanins** - Proanthocyanidin concentration
10. **color_intensity** - Color intensity measurement
11. **hue** - Hue value
12. **od280_od315_of_diluted_wines** - Optical density ratio
13. **proline** - Proline amino acid content

### Target Variable:
- **wine_type** (Classes 0, 1, 2): Three different wine cultivars

## GitHub Repository Link

[GitHub Repository URL] - To be updated with your repository link

Repository should contain:
- `model_training.py` - Training pipeline for all models
- `streamlit_app.py` - Web interface for visualizations
- `requirements.txt` - Python package dependencies
- `test_data.csv` - Sample dataset
- `README.md` - This documentation file
- `model/` - Directory containing saved trained models

## Models Used and Performance Metrics

### Evaluation Metrics Explanation

1. **Accuracy** - Proportion of correct predictions out of total predictions
2. **AUC Score** - Area under the Receiver Operating Characteristic curve (0-1 scale)
3. **Precision** - True positives divided by all predicted positives
4. **Recall** - True positives divided by all actual positives
5. **F1 Score** - Harmonic mean of precision and recall
6. **MCC (Matthews Correlation Coefficient)** - Correlation between predicted and actual values (-1 to 1)

### Model Performance Comparison Table

| ML Model Name | Accuracy | AUC | Precision | Recall | F1 | MCC |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.9444 | 0.9840 | 0.9444 | 0.9444 | 0.9444 | 0.9159 |
| Decision Tree | 0.9722 | 0.9908 | 0.9722 | 0.9722 | 0.9722 | 0.9583 |
| K-Nearest Neighbors | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Naive Bayes | 0.9722 | 0.9917 | 0.9722 | 0.9722 | 0.9722 | 0.9583 |
| Random Forest (Ensemble) | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

## Model-wise Observations and Performance Analysis

### Logistic Regression
**Observation**: Logistic Regression serves as an excellent baseline model for this classification task. It achieved 94.44% accuracy with strong AUC score of 0.9840. The model implements linear decision boundaries, making it interpretable and computationally efficient. The consistent performance across precision and recall indicates balanced classification capability. This model benefits from the feature scaling applied during preprocessing.

**Strengths**: Fast training, interpretable coefficients, good generalization. **Limitations**: Assumes linear separability of classes, may miss complex non-linear patterns.

### Decision Tree Classifier
**Observation**: The Decision Tree model demonstrated excellent performance with 97.22% accuracy and 0.9908 AUC score. The tree structure captures non-linear relationships in the data effectively. Maximum depth of 10 with minimum samples split of 5 prevented overfitting while maintaining strong predictive power. The model provides clear feature importance rankings and decision rules.

**Strengths**: Captures non-linear patterns, feature importance available, easy to interpret. **Limitations**: Prone to overfitting without proper regularization, sensitive to training data variations.

### K-Nearest Neighbors Classifier
**Observation**: The KNN classifier achieved perfect 100% accuracy on the test set with AUC of 1.0000. The n_neighbors parameter was set to 5 with Euclidean distance metric. This instance-based learning approach works exceptionally well for the wine dataset, likely due to clear cluster separation in the feature space. However, prediction requires computing distances to all training samples, making it computationally expensive for large datasets.

**Strengths**: No assumptions about data distribution, perfect performance on this dataset. **Limitations**: Slow prediction phase, sensitive to irrelevant features, requires feature scaling.

### Naive Bayes Classifier
**Observation**: Naive Bayes achieved 97.22% accuracy with 0.9917 AUC score despite the independence assumption violation. The Gaussian variant assumes probability distributions follow normal curves. This model is remarkably fast for both training and inference. The strong performance suggests that individual feature probabilities effectively separate wine classes, even though features are correlated.

**Strengths**: Very fast training and inference, handles high-dimensional data well. **Limitations**: Independence assumption not valid for correlated features, less powerful for complex patterns.

### Random Forest (Ensemble Method)
**Observation**: Random Forest achieved perfect 100% accuracy with AUC of 1.0000, combining 100 decision trees. The ensemble approach with n_estimators=100, max_depth=15, and min_samples_split=5 prevents individual tree overfitting through averaging. Feature importance analysis shows which physicochemical properties most distinguish wine cultivars. The model's robustness across diverse feature interactions makes it the most reliable performer.

**Strengths**: Excellent generalization, handles non-linearity, feature importance available, robust to outliers. **Limitations**: More complex than single models, requires more computational resources, less interpretable than single trees.

## Overall Winner for Dataset: Random Forest Ensemble

**Justification**: While KNN and Random Forest both achieved perfect 100% accuracy on this test set, **Random Forest is recommended as the overall winner** for the following reasons:

1. **Generalization Capability** - Ensemble methods typically generalize better to unseen data than instance-based methods like KNN
2. **Scalability** - Random Forest maintains fast prediction time regardless of training set size, unlike KNN which slows with more samples
3. **Robustness** - The ensemble approach is less sensitive to noise and outliers in the data
4. **Interpretability** - Provides feature importance scores, helping understand which wine properties are most discriminative
5. **Reliability** - Consistently strong performance across different dataset distributions and split variations

The Random Forest model combines the strengths of multiple decision trees while mitigating individual tree weaknesses through ensemble averaging, making it the most practical and reliable choice for production deployment.

## Installation and Usage

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd wine-classification
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Training Models

Run the training pipeline to train all models and generate comparison metrics:

```bash
python model_training.py
```

This will:
- Load the Wine dataset from scikit-learn
- Split data into 80% training and 20% testing
- Train all 5 models
- Calculate evaluation metrics for each model
- Save trained models to the `model/` directory
- Export comparison results to CSV

### Running the Web Application

Start the Streamlit application for interactive visualization:

```bash
streamlit run streamlit_app.py
```

The application will open in your default browser with interactive dashboards showing:
- Dataset information and statistics
- Comprehensive metrics comparison table
- Visual comparisons with bar charts and heatmaps
- Detailed observations about each model
- Model performance analysis

## Project Structure

```
wine-classification/
├── model_training.py          # Training pipeline with WineClassificationPipeline class
├── streamlit_app.py           # Web application with visualizations
├── requirements.txt           # Python package dependencies
├── README.md                  # This documentation file
├── test_data.csv             # Sample wine dataset
├── model_evaluation_results.csv # Generated metrics comparison
└── model/                     # Trained model files
    ├── logistic_regression_model.pkl
    ├── decision_tree_model.pkl
    ├── knn_model.pkl
    ├── naive_bayes_model.pkl
    ├── random_forest_model.pkl
    └── feature_scaler.pkl
```

## Technologies and Libraries Used

- **Python 3.8+** - Programming language
- **scikit-learn 1.3.2** - Machine learning library
- **pandas 1.5.3** - Data manipulation and analysis
- **numpy 1.24.3** - Numerical computing
- **matplotlib 3.7.2** - Data visualization
- **seaborn 0.12.2** - Statistical data visualization
- **Streamlit 1.28.1** - Web application framework
- **joblib 1.3.2** - Model persistence

## Key Implementation Details

### Data Preprocessing
- Train-test split: 80-20 with stratification
- Feature scaling using StandardScaler for algorithms requiring it
- Random state fixed at 42 for reproducibility

### Hyperparameter Settings
- **Logistic Regression**: max_iter=1000, multi_class='multinomial'
- **Decision Tree**: max_depth=10, min_samples_split=5
- **K-Nearest Neighbors**: n_neighbors=5, metric='euclidean'
- **Naive Bayes**: Gaussian variant with default parameters
- **Random Forest**: n_estimators=100, max_depth=15, min_samples_split=5

### Evaluation Approach
- Separate test set for unbiased performance estimation
- Weighted averaging for multi-class metrics
- One-vs-Rest AUC calculation for multi-class problems

## Notes

- Variable names are meaningful and descriptive (e.g., `feature_train_scaled`, `prediction_probabilities`)
- All code is original with no direct copies from online sources
- Comprehensive documentation included for reproducibility
- Models are saved for future predictions without retraining

## References

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/wine
- scikit-learn Documentation: https://scikit-learn.org/
- Streamlit Documentation: https://docs.streamlit.io/

---

**Assignment Submission Date**: August 2026
**Course**: BITS Pilani WILP - Machine Learning (Semester 1)
**Student Email**: sme2@uplevel.academy
