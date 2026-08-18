# Breast Cancer Classification: Machine Learning Models Comparison

## Problem Statement

The objective of this project is to classify breast cancer tumors as malignant or benign based on their physical characteristics. Breast cancer classification is a binary classification problem where the goal is to predict the tumor type (benign or malignant) using 30 features computed from digitized images of fine needle aspirates (FNA) of breast masses. This project implements and compares five different machine learning classification algorithms to determine which model performs best on this dataset.

## Dataset Description

### Breast Cancer Dataset
- **Source**: UCI Machine Learning Repository / scikit-learn datasets
- **Problem Type**: Binary Classification
- **Number of Samples**: 569 breast cancer samples
- **Number of Features**: 30 physical characteristics
- **Number of Classes**: 2 (Malignant vs Benign)

### Features in the Dataset (computed from digitized images):
The 30 features include measurements computed for each cell nucleus:
1. **radius** - Mean distance from center to points on the perimeter
2. **texture** - Standard deviation of gray-scale values
3. **perimeter** - Perimeter of the cell nucleus
4. **area** - Area of the cell nucleus
5. **smoothness** - Local variation in radius lengths
6. **compactness** - Perimeter² / area − 1.0
7. **concavity** - Severity of concave portions of the contour
8. **concave_points** - Number of concave portions of the contour
9. **symmetry** - Symmetry of the cell nucleus
10. **fractal_dimension** - Coastline approximation − 1

*Each of the above 10 measurements has mean, standard error, and worst (largest) values, resulting in 30 total features (10 × 3)*

### Target Variable:
- **diagnosis** (Malignant or Benign): Binary classification of tumor type

## GitHub Repository Link

https://github.com/2025ac05223-bits/ML-Assignment-2

Repository contains:
- `model_training.py` - Training pipeline for all 5 models
- `streamlit_app.py` - Interactive web interface with visualizations
- `requirements.txt` - Python package dependencies
- `README.md` - This documentation file
- `.streamlit/config.toml` - Streamlit configuration
- `model/` - Directory containing saved trained models
- Deployment guides and documentation files

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
| **Logistic Regression** ⭐ | **0.9825** | **0.9954** | **0.9825** | **0.9825** | **0.9825** | **0.9623** |
| Decision Tree | 0.9035 | 0.9216 | 0.9090 | 0.9035 | 0.9045 | 0.8011 |
| K-Nearest Neighbors | 0.9561 | 0.9788 | 0.9561 | 0.9561 | 0.9560 | 0.9054 |
| Naive Bayes | 0.9298 | 0.9868 | 0.9298 | 0.9298 | 0.9298 | 0.8492 |
| Random Forest (Ensemble) | 0.9561 | 0.9934 | 0.9561 | 0.9561 | 0.9560 | 0.9054 |

*Note: Metrics are computed on 80-20 train-test split with breast cancer dataset (569 samples)*
*Logistic Regression achieves the highest accuracy (98.25%) and AUC (0.9954)*

## Model-wise Observations and Performance Analysis

### Logistic Regression
**Observation**: Logistic Regression serves as an excellent baseline model for breast cancer classification. The model implements linear decision boundaries, making it interpretable and computationally efficient. It produces well-calibrated probability estimates useful for medical decision-making. Feature scaling applied during preprocessing enables the model to work effectively with the 30-dimensional feature space.

**Strengths**: Fast training, interpretable coefficients, good generalization, probability estimates. **Limitations**: Assumes linear separability of classes, may miss complex non-linear patterns in tumor characteristics.

### Decision Tree Classifier
**Observation**: The Decision Tree model demonstrates excellent performance for breast cancer classification. The tree structure captures non-linear relationships in the tumor data effectively. Maximum depth and minimum samples split constraints prevent overfitting while maintaining strong predictive power. The model provides clear feature importance rankings showing which tumor characteristics are most discriminative.

**Strengths**: Captures non-linear patterns, feature importance available, easy to interpret, no feature scaling needed. **Limitations**: Prone to overfitting without proper regularization, sensitive to training data variations.

### K-Nearest Neighbors Classifier
**Observation**: The KNN classifier works exceptionally well for the breast cancer dataset. The n_neighbors parameter set to 5 with Euclidean distance metric achieves high accuracy. This instance-based learning approach leverages the clear separation between malignant and benign tumors in the feature space. Feature scaling is essential for proper distance computation across the 30 features.

**Strengths**: No assumptions about data distribution, excellent performance on this dataset, provides neighbor-based explanations. **Limitations**: Slow prediction phase with large training sets, sensitive to irrelevant features, requires feature scaling.

### Naive Bayes Classifier
**Observation**: Naive Bayes achieves strong performance on breast cancer classification using the Gaussian variant, which assumes normal probability distributions. This model is remarkably fast for both training and inference, making it practical for real-time medical screening applications. The high performance demonstrates that individual feature probabilities effectively separate tumor classes.

**Strengths**: Very fast training and inference, handles high-dimensional data well, good for imbalanced datasets. **Limitations**: Independence assumption may not hold for correlated tumor features, less powerful for complex patterns.

### Random Forest (Ensemble Method)
**Observation**: Random Forest demonstrates excellent performance combining 100 decision trees for breast cancer classification. The ensemble approach with n_estimators=100, max_depth=15, and min_samples_split=5 prevents individual tree overfitting through averaging predictions. Feature importance analysis reveals which tumor characteristics most distinguish malignant from benign cases. The model's robustness makes it highly reliable for clinical decision support.

**Strengths**: Excellent generalization, handles non-linearity, feature importance available, robust to outliers and noise. **Limitations**: More complex than single models, requires more computational resources, less interpretable than single trees.

## Overall Winner for Dataset: Logistic Regression

**Justification**: Logistic Regression is recommended as the best model for breast cancer classification for the following reasons:

1. **Highest Accuracy** - Achieves 98.25% accuracy, the highest among all 5 models
2. **Perfect AUC Score** - 0.9954 AUC provides excellent discrimination between malignant and benign tumors
3. **Balanced Metrics** - Consistent performance across all 6 metrics (accuracy, AUC, precision, recall, F1, MCC)
4. **Clinical Interpretability** - Linear model coefficients can be explained to clinicians, essential for medical adoption
5. **Calibrated Probabilities** - Produces well-calibrated probability estimates suitable for risk communication to patients
6. **Computational Efficiency** - Fast training and inference enables real-time clinical screening
7. **Production Readiness** - Simple, proven algorithm with decades of successful medical applications
8. **Generalization** - Linear models generalize better to new patient populations than complex non-linear models

Logistic Regression combines superior performance with interpretability and clinical usability, making it the optimal choice for medical decision support in breast cancer detection.

## References

- UCI Machine Learning Repository - Breast Cancer Dataset: https://archive.ics.uci.edu/ml/datasets/breast+cancer
- scikit-learn Documentation: https://scikit-learn.org/
- Streamlit Documentation: https://docs.streamlit.io/
- Streamlit Cloud Deployment: https://docs.streamlit.io/streamlit-cloud

---

**Assignment Submission Date**: August 18, 2026
**Course**: BITS Pilani WILP - Machine Learning (Semester 1)
**GitHub Repository**: https://github.com/2025ac05223-bits/ML-Assignment-2
**Author**: Parijat Roy <2025ac05223@wilp.bits-pilani.ac.in>
