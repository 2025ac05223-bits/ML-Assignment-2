"""
Streamlit Web Application for Breast Cancer Classification Model Comparison
Displays model performance metrics and visualizations
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from model_training import BreastCancerClassificationPipeline
import os

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
def initialize_training_pipeline():
    """Initialize and train all models (cached for performance)"""
    import os
    from pathlib import Path

    # Check if pre-trained models exist
    model_dir = Path("model")
    models_exist = all([
        (model_dir / "logistic_regression_model.pkl").exists(),
        (model_dir / "decision_tree_model.pkl").exists(),
        (model_dir / "knn_model.pkl").exists(),
        (model_dir / "naive_bayes_model.pkl").exists(),
        (model_dir / "random_forest_model.pkl").exists(),
        (model_dir / "feature_scaler.pkl").exists(),
    ])

    pipeline = BreastCancerClassificationPipeline(test_size=0.2, random_state=42)
    pipeline.load_and_prepare_dataset()

    if models_exist:
        # Load pre-trained models
        import joblib
        from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef

        pipeline.feature_scaler = joblib.load(model_dir / "feature_scaler.pkl")
        pipeline.feature_train_scaled = pipeline.feature_scaler.fit_transform(pipeline.feature_train)
        pipeline.feature_test_scaled = pipeline.feature_scaler.transform(pipeline.feature_test)

        # Load models
        models_loaded = {
            'logistic_regression': joblib.load(model_dir / "logistic_regression_model.pkl"),
            'decision_tree': joblib.load(model_dir / "decision_tree_model.pkl"),
            'knn': joblib.load(model_dir / "knn_model.pkl"),
            'naive_bayes': joblib.load(model_dir / "naive_bayes_model.pkl"),
            'random_forest': joblib.load(model_dir / "random_forest_model.pkl"),
        }

        # Store models in pipeline
        pipeline.models = {
            'logistic_regression': {'model': models_loaded['logistic_regression'], 'metrics': {}},
            'decision_tree': {'model': models_loaded['decision_tree'], 'metrics': {}},
            'knn': {'model': models_loaded['knn'], 'metrics': {}},
            'naive_bayes': {'model': models_loaded['naive_bayes'], 'metrics': {}},
            'random_forest': {'model': models_loaded['random_forest'], 'metrics': {}},
        }

        # Generate metrics for each model
        comparison_data = []
        for model_name, model_info in pipeline.models.items():
            model = model_info['model']

            # Use scaled features for scaled models, raw features for tree-based
            if model_name in ['logistic_regression', 'knn', 'naive_bayes']:
                test_features = pipeline.feature_test_scaled
            else:
                test_features = pipeline.feature_test

            predictions = model.predict(test_features)
            prediction_probabilities = model.predict_proba(test_features)

            accuracy = accuracy_score(pipeline.target_test, predictions)
            try:
                if len(np.unique(pipeline.target_test)) == 2:
                    auc = roc_auc_score(pipeline.target_test, prediction_probabilities[:, 1])
                else:
                    auc = roc_auc_score(pipeline.target_test, prediction_probabilities, multi_class='ovr', average='weighted')
            except:
                auc = 0.0

            precision = precision_score(pipeline.target_test, predictions, average='weighted', zero_division=0)
            recall = recall_score(pipeline.target_test, predictions, average='weighted', zero_division=0)
            f1 = f1_score(pipeline.target_test, predictions, average='weighted', zero_division=0)
            mcc = matthews_corrcoef(pipeline.target_test, predictions)

            metrics = {
                'accuracy': accuracy,
                'auc': auc,
                'precision': precision,
                'recall': recall,
                'f1': f1,
                'mcc': mcc
            }
            pipeline.models[model_name]['metrics'] = metrics

            comparison_data.append({
                'model_name': model_name.replace('_', ' ').title(),
                'accuracy': accuracy,
                'auc': auc,
                'precision': precision,
                'recall': recall,
                'f1': f1,
                'mcc': mcc
            })

        pipeline.results_dataframe = pd.DataFrame(comparison_data)
    else:
        # Train models if not pre-trained
        pipeline.train_all_models()
        pipeline.generate_comparison_report()
        pipeline.save_models()

    return pipeline


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
    - **Features**: 30 cancer characteristics
    - **Classes**: 2 (Malignant vs Benign)
    - **Total Samples**: 569
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
        st.metric(
            "Best Accuracy",
            comparison_numeric.iloc[best_accuracy_idx]['model_name'],
            f"{comparison_numeric.iloc[best_accuracy_idx]['accuracy']:.4f}"
        )

    with col2:
        best_f1_idx = comparison_numeric['f1'].idxmax()
        st.metric(
            "Best F1 Score",
            comparison_numeric.iloc[best_f1_idx]['model_name'],
            f"{comparison_numeric.iloc[best_f1_idx]['f1']:.4f}"
        )

    with col3:
        best_auc_idx = comparison_numeric['auc'].idxmax()
        st.metric(
            "Best AUC Score",
            comparison_numeric.iloc[best_auc_idx]['model_name'],
            f"{comparison_numeric.iloc[best_auc_idx]['auc']:.4f}"
        )


def plot_metrics_comparison(comparison_df):
    """Create and display metrics comparison visualizations"""
    st.header("📊 Visual Comparison of Metrics")

    # Prepare data for plotting
    metrics_to_plot = ['accuracy', 'auc', 'precision', 'recall', 'f1', 'mcc']
    models_list = comparison_df['model_name'].tolist()

    # Create a more informative visualization
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Accuracy & AUC Comparison")
        fig, axis = plt.subplots(figsize=(10, 6))

        x_position = np.arange(len(models_list))
        bar_width = 0.35

        accuracy_bars = axis.bar(
            x_position - bar_width/2, comparison_df['accuracy'],
            bar_width, label='Accuracy', color='#3498db', alpha=0.8
        )
        auc_bars = axis.bar(
            x_position + bar_width/2, comparison_df['auc'],
            bar_width, label='AUC Score', color='#e74c3c', alpha=0.8
        )

        axis.set_xlabel('Models', fontsize=11, fontweight='bold')
        axis.set_ylabel('Score', fontsize=11, fontweight='bold')
        axis.set_title('Accuracy vs AUC Score', fontsize=13, fontweight='bold')
        axis.set_xticks(x_position)
        axis.set_xticklabels(models_list, rotation=45, ha='right')
        axis.legend()
        axis.grid(axis='y', alpha=0.3)

        # Add value labels on bars
        for bars in [accuracy_bars, auc_bars]:
            for bar in bars:
                height = bar.get_height()
                axis.text(bar.get_x() + bar.get_width()/2., height,
                         f'{height:.3f}', ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        st.subheader("Precision, Recall & F1 Score")
        fig, axis = plt.subplots(figsize=(10, 6))

        x_position = np.arange(len(models_list))
        bar_width = 0.25

        precision_bars = axis.bar(
            x_position - bar_width, comparison_df['precision'],
            bar_width, label='Precision', color='#2ecc71', alpha=0.8
        )
        recall_bars = axis.bar(
            x_position, comparison_df['recall'],
            bar_width, label='Recall', color='#f39c12', alpha=0.8
        )
        f1_bars = axis.bar(
            x_position + bar_width, comparison_df['f1'],
            bar_width, label='F1 Score', color='#9b59b6', alpha=0.8
        )

        axis.set_xlabel('Models', fontsize=11, fontweight='bold')
        axis.set_ylabel('Score', fontsize=11, fontweight='bold')
        axis.set_title('Precision, Recall & F1 Score Comparison', fontsize=13, fontweight='bold')
        axis.set_xticks(x_position)
        axis.set_xticklabels(models_list, rotation=45, ha='right')
        axis.legend()
        axis.grid(axis='y', alpha=0.3)

        plt.tight_layout()
        st.pyplot(fig)

    # Heatmap of all metrics
    st.subheader("Metrics Heatmap")
    fig, axis = plt.subplots(figsize=(10, 4))

    heatmap_data = comparison_df[metrics_to_plot].T
    heatmap_data.columns = models_list

    sns.heatmap(
        heatmap_data, annot=True, fmt='.3f', cmap='RdYlGn',
        cbar_kws={'label': 'Score'}, ax=axis, vmin=0, vmax=1
    )

    axis.set_title('All Metrics Heatmap', fontsize=13, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)


def display_model_observations():
    """Display observations about model performance"""
    st.header("💡 Model Performance Observations")

    observations_dict = {
        "Logistic Regression": """
        - Linear decision boundaries, works well for linearly separable data
        - Fast training and inference
        - Excellent baseline model with good generalization
        - Weights provide interpretability for feature importance
        """,

        "Decision Tree": """
        - Non-linear model that captures complex patterns
        - Prone to overfitting without depth regularization
        - Computationally efficient but may require pruning
        - Easy to interpret with tree structure visualization
        """,

        "K-Nearest Neighbors": """
        - Instance-based learning with local decision boundaries
        - Performance depends heavily on feature scaling and k value
        - Computationally expensive during prediction phase
        - Sensitive to irrelevant features and class imbalance
        """,

        "Naive Bayes": """
        - Probabilistic model assuming feature independence
        - Very fast training and prediction
        - Works surprisingly well despite independence assumption
        - Good baseline for high-dimensional data
        """,

        "Random Forest (Ensemble)": """
        - Combines multiple decision trees for robust predictions
        - Handles feature interactions and non-linearity effectively
        - Provides feature importance rankings
        - Less prone to overfitting than single decision tree
        - Often the most reliable performer across datasets
        """
    }

    for model_name, observation in observations_dict.items():
        with st.expander(f"🔍 {model_name}"):
            st.markdown(observation)

    st.subheader("🎯 Overall Winner Recommendation")
    st.info(
        """
        **Random Forest Ensemble** typically performs best because:
        - Combines strengths of multiple models through ensemble approach
        - Robust to overfitting with proper hyperparameter tuning
        - Handles both linear and non-linear relationships
        - Provides feature importance for interpretability
        - Consistent performance across various dataset types
        """
    )


def display_about_section():
    """Display about and footer information"""
    st.header("ℹ️ About This Project")

    st.markdown("""
    ### Assignment Details
    - **Subject**: Machine Learning Classification
    - **Dataset**: Breast Cancer Classification (UCI Machine Learning Repository)
    - **Models Implemented**: 5 classifiers with comprehensive evaluation
    - **Evaluation Metrics**: 6 standard metrics per model

    ### Technologies Used
    - Python 3.8+
    - scikit-learn for machine learning models
    - Streamlit for web interface
    - pandas & numpy for data manipulation
    - matplotlib & seaborn for visualizations

    ### Repository Structure
    ```
    project-folder/
    ├── streamlit_app.py (main web application)
    ├── model_training.py (training pipeline)
    ├── requirements.txt (dependencies)
    ├── README.md (documentation)
    ├── test_data.csv (dataset export)
    └── model/ (trained models directory)
        ├── logistic_regression_model.pkl
        ├── decision_tree_model.pkl
        ├── knn_model.pkl
        ├── naive_bayes_model.pkl
        ├── random_forest_model.pkl
        └── feature_scaler.pkl
    ```
    """)


def main():
    """Main application entry point"""
    display_header()

    # Initialize pipeline
    with st.spinner("Loading and training models..."):
        pipeline = initialize_training_pipeline()

    # Generate comparison report
    comparison_report = pipeline.generate_comparison_report()

    # Create sidebar navigation
    sidebar_option = st.sidebar.radio(
        "Navigation",
        ["Overview", "Metrics Comparison", "Visualizations", "Model Details", "About"]
    )

    if sidebar_option == "Overview":
        display_dataset_info(pipeline)

    elif sidebar_option == "Metrics Comparison":
        display_metrics_comparison_table(comparison_report)

    elif sidebar_option == "Visualizations":
        plot_metrics_comparison(comparison_report)

    elif sidebar_option == "Model Details":
        display_model_observations()

    elif sidebar_option == "About":
        display_about_section()

    # Save models
    if not os.path.exists('model'):
        pipeline.save_models_to_disk()
        pipeline.save_scaler_to_disk()


if __name__ == '__main__':
    main()
