"""
Streamlit Web Application for Breast Cancer Classification Model Comparison
Cloud-optimized version with pre-trained models for Streamlit Cloud deployment
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import joblib
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Breast Cancer Classification Models",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_models_and_data():
    """Load pre-trained models from the model/ directory"""
    model_dir = Path("model")

    # Check if models exist
    models_exist = all([
        (model_dir / "logistic_regression_model.pkl").exists(),
        (model_dir / "decision_tree_model.pkl").exists(),
        (model_dir / "knn_model.pkl").exists(),
        (model_dir / "naive_bayes_model.pkl").exists(),
        (model_dir / "random_forest_model.pkl").exists(),
        (model_dir / "feature_scaler.pkl").exists(),
    ])

    if not models_exist:
        # If models don't exist, train them
        from model_training import BreastCancerClassificationPipeline
        pipeline = BreastCancerClassificationPipeline(test_size=0.2, random_state=42)
        pipeline.load_and_prepare_dataset()
        pipeline.train_all_models()
        pipeline.save_models()
        return pipeline, True
    else:
        # Load pre-trained models
        from model_training import BreastCancerClassificationPipeline
        from sklearn.datasets import load_breast_cancer
        from sklearn.model_selection import train_test_split
        import pandas as pd

        pipeline = BreastCancerClassificationPipeline(test_size=0.2, random_state=42)

        # Load dataset
        cancer_data = load_breast_cancer()
        feature_matrix = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
        target_labels = pd.Series(cancer_data.target, name='cancer_diagnosis')

        # Split dataset
        pipeline.feature_train, pipeline.feature_test, pipeline.target_train, pipeline.target_test = (
            train_test_split(
                feature_matrix, target_labels,
                test_size=0.2,
                random_state=42,
                stratify=target_labels
            )
        )

        # Load scaler
        pipeline.feature_scaler = joblib.load(model_dir / "feature_scaler.pkl")
        pipeline.feature_train_scaled = pipeline.feature_scaler.fit_transform(pipeline.feature_train)
        pipeline.feature_test_scaled = pipeline.feature_scaler.transform(pipeline.feature_test)

        # Load models
        pipeline.models = {
            'Logistic Regression': joblib.load(model_dir / "logistic_regression_model.pkl"),
            'Decision Tree': joblib.load(model_dir / "decision_tree_model.pkl"),
            'K-Nearest Neighbors': joblib.load(model_dir / "knn_model.pkl"),
            'Naive Bayes': joblib.load(model_dir / "naive_bayes_model.pkl"),
            'Random Forest': joblib.load(model_dir / "random_forest_model.pkl"),
        }

        # Generate predictions and results
        pipeline.generate_results()

        return pipeline, False


def display_header():
    """Display application header"""
    st.title("🏥 Breast Cancer Classification Model Comparison")
    st.markdown("""
    This application demonstrates the implementation and evaluation of 5 machine learning
    classification models on the Breast Cancer dataset. Each model is evaluated using 6 key metrics.
    """)


def display_dataset_info(pipeline):
    """Display dataset information"""
    st.header("📊 Dataset Information")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Training Samples", len(pipeline.feature_train))
    with col2:
        st.metric("Testing Samples", len(pipeline.feature_test))
    with col3:
        st.metric("Number of Features", pipeline.feature_train.shape[1])
    with col4:
        st.metric("Number of Classes", len(np.unique(pipeline.target_train)))

    st.markdown("""
    **Dataset**: Breast Cancer Classification Dataset from scikit-learn
    - **Problem Type**: Binary Classification
    - **Features**: 30 cancer characteristics (computed from digitized FNA images)
    - **Classes**: 2 (Malignant vs Benign)
    - **Total Samples**: 569 (training: ~455, testing: ~114)
    """)


def display_metrics_comparison_table(comparison_df):
    """Display detailed comparison table"""
    st.header("📈 Model Performance Metrics Comparison")

    # Format the dataframe for display
    display_df = comparison_df.copy()
    numeric_columns = ['accuracy', 'auc', 'precision', 'recall', 'f1', 'mcc']

    for col in numeric_columns:
        display_df[col] = display_df[col].apply(lambda x: f"{x:.4f}")

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    # Find and display the best model for each metric
    st.subheader("🏆 Best Performing Models")
    comparison_numeric = comparison_df.copy()

    col1, col2, col3 = st.columns(3)

    with col1:
        best_accuracy_idx = comparison_numeric['accuracy'].idxmax()
        st.metric("Best Accuracy", f"{comparison_numeric['accuracy'].max():.4f}",
                  f"{comparison_numeric.index[best_accuracy_idx]}")

    with col2:
        best_auc_idx = comparison_numeric['auc'].idxmax()
        st.metric("Best AUC Score", f"{comparison_numeric['auc'].max():.4f}",
                  f"{comparison_numeric.index[best_auc_idx]}")

    with col3:
        best_f1_idx = comparison_numeric['f1'].idxmax()
        st.metric("Best F1 Score", f"{comparison_numeric['f1'].max():.4f}",
                  f"{comparison_numeric.index[best_f1_idx]}")


def display_visualizations(comparison_df):
    """Display visualization charts"""
    st.header("📊 Model Performance Visualizations")

    # Bar chart for all metrics
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Accuracy Comparison")
        fig, ax = plt.subplots(figsize=(10, 6))
        comparison_df['accuracy'].plot(kind='bar', ax=ax, color='steelblue')
        ax.set_ylabel('Accuracy')
        ax.set_xlabel('Model')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)

    with col2:
        st.subheader("AUC Score Comparison")
        fig, ax = plt.subplots(figsize=(10, 6))
        comparison_df['auc'].plot(kind='bar', ax=ax, color='seagreen')
        ax.set_ylabel('AUC Score')
        ax.set_xlabel('Model')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)

    # Metrics heatmap
    st.subheader("Metrics Heatmap")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(comparison_df[['accuracy', 'auc', 'precision', 'recall', 'f1', 'mcc']],
                annot=True, fmt='.4f', cmap='RdYlGn', ax=ax, cbar_kws={'label': 'Score'})
    ax.set_ylabel('Model')
    st.pyplot(fig)


def display_model_observations():
    """Display detailed model observations"""
    st.header("🔍 Model-wise Observations")

    observations = {
        "Logistic Regression": """
        **Observation**: Serves as an excellent baseline model for binary breast cancer classification.
        Implements linear decision boundaries, making it highly interpretable and computationally efficient.
        The model benefits from feature scaling, which is applied during preprocessing.

        **Strengths**:
        - Fast training and inference
        - Interpretable coefficients
        - Good generalization to new data
        - Produces well-calibrated probability estimates

        **Limitations**:
        - Assumes linear separability of classes
        - May miss complex non-linear patterns in tumor characteristics
        """,

        "Decision Tree": """
        **Observation**: The tree-based model effectively captures non-linear relationships in tumor data.
        Maximum depth and minimum samples constraints prevent overfitting while maintaining strong predictive power.
        Provides clear feature importance rankings showing which tumor characteristics are most discriminative.

        **Strengths**:
        - Captures non-linear patterns
        - Feature importance available for clinical interpretation
        - Easy to understand decision rules
        - No feature scaling required

        **Limitations**:
        - Prone to overfitting without proper regularization
        - Sensitive to small variations in training data
        """,

        "K-Nearest Neighbors": """
        **Observation**: Achieves excellent performance on the breast cancer dataset using instance-based learning.
        The n_neighbors parameter set to 5 with Euclidean distance metric works well. Clear separation between
        malignant and benign tumors in the feature space enables high accuracy.

        **Strengths**:
        - No assumptions about data distribution
        - Excellent performance on this dataset
        - Can provide neighbor-based explanations
        - Performs well with binary classification

        **Limitations**:
        - Slow prediction phase with large training sets
        - Sensitive to irrelevant features
        - Requires feature scaling for proper distance computation
        """,

        "Naive Bayes": """
        **Observation**: Achieves strong performance using the Gaussian variant, which assumes probability
        distributions follow normal curves. Remarkably fast for both training and inference, making it practical
        for real-time medical screening applications. The strong performance demonstrates that individual feature
        probabilities effectively separate tumor classes.

        **Strengths**:
        - Very fast training and inference (good for clinical use)
        - Handles high-dimensional data well
        - Good for imbalanced datasets
        - Produces probability estimates

        **Limitations**:
        - Independence assumption may not hold for correlated tumor features
        - Less powerful for capturing complex patterns
        """,

        "Random Forest": """
        **Observation**: Demonstrates excellent performance combining 100 decision trees for cancer classification.
        The ensemble approach prevents individual tree overfitting through averaging. Feature importance analysis
        reveals which tumor characteristics most distinguish malignant from benign cases. High reliability for
        clinical decision support.

        **Strengths**:
        - Excellent generalization capability
        - Handles non-linearity effectively
        - Feature importance available for clinical interpretation
        - Robust to noise and outliers
        - Less sensitive to training data variations

        **Limitations**:
        - More complex than single models
        - Requires more computational resources
        - Less interpretable than single decision trees
        """
    }

    for model_name, obs_text in observations.items():
        with st.expander(f"📌 {model_name}", expanded=False):
            st.markdown(obs_text)


def display_winner_recommendation():
    """Display overall winner recommendation"""
    st.header("🏆 Overall Recommended Model: Random Forest")

    st.markdown("""
    **Justification**: Random Forest is recommended as the best model for breast cancer classification:

    1. **Clinical Reliability**
       - Ensemble methods provide robust predictions less sensitive to measurement variations
       - Excellent generalization to new patient data

    2. **Scalability**
       - Maintains fast prediction time for real-time clinical screening
       - Handles large patient databases efficiently

    3. **Robustness**
       - Less sensitive to noise in tumor measurements
       - Handles outliers well (important in medical data)

    4. **Interpretability**
       - Provides feature importance scores showing which tumor characteristics matter most
       - Helps clinicians understand the decision basis

    5. **Production Readiness**
       - Consistently strong performance across different data distributions
       - Reliable for deployment in clinical settings

    6. **Decision Support**
       - High accuracy enables confident use as a clinical decision support tool
       - Helps in early cancer detection and diagnosis

    The Random Forest model combines the strengths of multiple decision trees while mitigating
    individual tree weaknesses through ensemble averaging, making it the most practical and
    reliable choice for medical decision support in breast cancer detection.
    """)


def display_about():
    """Display about section"""
    st.header("ℹ️ About This Application")

    st.markdown("""
    ### Project Information
    - **Course**: BITS Pilani WILP - Machine Learning (Semester 1)
    - **Assignment**: ML Classification Models Comparison
    - **Dataset**: Breast Cancer Dataset (UCI ML Repository / scikit-learn)
    - **GitHub**: https://github.com/2025ac05223-bits/ML-Assignment-2

    ### Models Implemented
    1. Logistic Regression
    2. Decision Tree Classifier
    3. K-Nearest Neighbors
    4. Gaussian Naive Bayes
    5. Random Forest Ensemble (100 trees)

    ### Evaluation Metrics
    - **Accuracy**: Classification accuracy on test set
    - **AUC**: Area Under the ROC Curve
    - **Precision**: True Positive Rate among predicted positives
    - **Recall**: True Positive Rate among actual positives
    - **F1 Score**: Harmonic mean of Precision and Recall
    - **MCC**: Matthews Correlation Coefficient

    ### Dataset Details
    - **Samples**: 569 breast cancer observations
    - **Features**: 30 computed characteristics from FNA images
    - **Classes**: 2 (Malignant or Benign)
    - **Train-Test Split**: 80-20 with stratification

    ### Feature Scaling
    - StandardScaler applied to normalize features
    - Essential for distance-based and gradient-based models
    - Improves model convergence and performance

    **Author**: Parijat Roy
    **Email**: 2025ac05223@wilp.bits-pilani.ac.in
    **Date**: August 2026
    """)


def main():
    """Main application logic"""
    try:
        # Load models and data
        with st.spinner("Loading models and data..."):
            pipeline, was_trained = load_models_and_data()

        if was_trained:
            st.success("✅ Models trained and ready!")
        else:
            st.success("✅ Pre-trained models loaded successfully!")

        # Display sections
        display_header()
        display_dataset_info(pipeline)
        display_metrics_comparison_table(pipeline.results_dataframe)
        display_visualizations(pipeline.results_dataframe)
        display_model_observations()
        display_winner_recommendation()
        display_about()

    except Exception as e:
        st.error(f"❌ Error loading application: {str(e)}")
        st.info("Please check that all model files are present in the `model/` directory")

        # Offer to train models
        if st.button("Train Models Now"):
            with st.spinner("Training models... this may take a few minutes"):
                try:
                    from model_training import BreastCancerClassificationPipeline
                    pipeline = BreastCancerClassificationPipeline(test_size=0.2, random_state=42)
                    pipeline.load_and_prepare_dataset()
                    pipeline.train_all_models()
                    pipeline.save_models()
                    st.success("✅ Models trained successfully! Please refresh the page.")
                except Exception as train_error:
                    st.error(f"Error during training: {str(train_error)}")


if __name__ == "__main__":
    main()
