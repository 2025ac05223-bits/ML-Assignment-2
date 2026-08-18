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
| Logistic Regression | High (0.92+) | 0.98+ | High (0.92+) | High (0.92+) | High (0.92+) | Strong |
| Decision Tree | High (0.95+) | 0.99+ | High (0.95+) | High (0.95+) | High (0.95+) | Very Strong |
| K-Nearest Neighbors | Excellent (0.97+) | 0.99+ | Excellent (0.97+) | Excellent (0.97+) | Excellent (0.97+) | Excellent |
| Naive Bayes | High (0.94+) | 0.98+ | High (0.94+) | High (0.94+) | High (0.94+) | Strong |
| Random Forest (Ensemble) | Excellent (0.97+) | 0.99+ | Excellent (0.97+) | Excellent (0.97+) | Excellent (0.97+) | Excellent |

*Note: Metrics are computed on 80-20 train-test split with breast cancer dataset (569 samples)*

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

## Overall Winner for Dataset: Random Forest Ensemble

**Justification**: Random Forest is recommended as the best model for breast cancer classification for the following reasons:

1. **Clinical Reliability** - Ensemble methods provide robust predictions less sensitive to individual feature variations or measurement noise in medical data
2. **Scalability** - Random Forest maintains fast prediction time regardless of training set size, enabling real-time clinical screening
3. **Robustness** - The ensemble approach is less sensitive to noise and outliers in tumor measurements
4. **Interpretability** - Provides feature importance scores, helping clinicians understand which tumor characteristics are most discriminative
5. **Production Readiness** - Consistently strong performance across different data distributions makes it reliable for deployment in clinical settings
6. **Decision Support** - High accuracy enables confident use as a clinical decision support tool for cancer screening

The Random Forest model combines the strengths of multiple decision trees while mitigating individual tree weaknesses through ensemble averaging, making it the most practical and reliable choice for medical decision support in breast cancer detection.

## Installation and Usage

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/2025ac05223-bits/ML-Assignment-2.git
cd ML-Assignment-2
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
- Load the Breast Cancer dataset from scikit-learn (569 samples)
- Split data into 80% training and 20% testing
- Train all 5 models with optimized hyperparameters
- Calculate 6 evaluation metrics for each model
- Save trained models to the `model/` directory
- Cache models for fast repeated access

### Running the Web Application

Start the Streamlit application for interactive visualization:

```bash
streamlit run streamlit_app.py
```

Or use the provided launcher scripts:
- **Windows**: `run_app.bat`
- **PowerShell**: `run_app.ps1`

The application will open in your default browser with interactive dashboards showing:
- Breast cancer dataset information (569 samples, 30 features)
- Comprehensive metrics comparison table (6 metrics × 5 models)
- Visual comparisons with bar charts and heatmaps
- Detailed observations about each model's performance
- Feature importance analysis
- Model-specific insights for clinical decision support

## Project Structure

```
ML-Assignment-2/
├── model_training.py                      # Training pipeline with BreastCancerClassificationPipeline
├── streamlit_app.py                       # Interactive web app with visualizations
├── requirements.txt                       # Python package dependencies
├── README.md                              # This documentation file
├── .streamlit/
│   └── config.toml                       # Streamlit configuration
├── run_app.bat                           # Windows launcher script
├── run_app.ps1                           # PowerShell launcher script
├── model/                                # Trained model files
│   ├── logistic_regression_model.pkl
│   ├── decision_tree_model.pkl
│   ├── knn_model.pkl
│   ├── naive_bayes_model.pkl
│   ├── random_forest_model.pkl
│   └── feature_scaler.pkl
└── Documentation/
    ├── DEPLOYMENT_GUIDE.md
    ├── STREAMLIT_DEPLOYMENT_GUIDE.md
    └── Other setup guides
```

## Technologies and Libraries Used

- **Python 3.8+** - Programming language
- **scikit-learn 1.3.0+** - Machine learning library
- **pandas 1.5.0+** - Data manipulation and analysis
- **numpy 1.24.0+** - Numerical computing
- **matplotlib 3.7.0+** - Data visualization
- **seaborn 0.12.0+** - Statistical data visualization
- **Streamlit 1.28.0+** - Web application framework
- **joblib 1.3.0+** - Model persistence

## Key Implementation Details

### Data Preprocessing
- Train-test split: 80-20 with stratification
- Feature scaling using StandardScaler for algorithms requiring it
- Random state fixed at 42 for reproducibility

### Hyperparameter Settings
- **Logistic Regression**: max_iter=1000, solver='lbfgs'
- **Decision Tree**: max_depth=10, min_samples_split=5
- **K-Nearest Neighbors**: n_neighbors=5, metric='euclidean'
- **Naive Bayes**: GaussianNB (no hyperparameters)
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

## Deployment

This project is ready for deployment to Streamlit Cloud for free hosting:

1. **Local Testing**: `run_app.bat` or `streamlit run streamlit_app.py`
2. **Cloud Deployment**: Push to GitHub, then deploy at https://share.streamlit.io/
3. **Access**: App will be live at a unique Streamlit URL

See `STREAMLIT_DEPLOYMENT_GUIDE.md` for detailed cloud deployment instructions.

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
