"""
ML Classification Models Training Pipeline
Implements 5 classification models on Breast Cancer dataset with comprehensive evaluation metrics
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Model imports
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

# Evaluation metrics imports
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score,
    f1_score, matthews_corrcoef, roc_curve, auc
)

import joblib
import os


class BreastCancerClassificationPipeline:
    """
    Pipeline to train and evaluate multiple classification models on Breast Cancer dataset
    """

    def __init__(self, test_size=0.2, random_state=42):
        """
        Initialize the pipeline with dataset and parameters

        Args:
            test_size: Proportion of data for testing
            random_state: Seed for reproducibility
        """
        self.test_size = test_size
        self.random_state = random_state
        self.models = {}
        self.results_dataframe = None

    def load_and_prepare_dataset(self):
        """Load Breast Cancer dataset and split into train/test sets"""
        # Load Breast Cancer dataset from sklearn (569 samples)
        cancer_data = load_breast_cancer()
        feature_matrix = pd.DataFrame(
            cancer_data.data,
            columns=cancer_data.feature_names
        )
        target_labels = pd.Series(cancer_data.target, name='cancer_diagnosis')

        # Split dataset
        self.feature_train, self.feature_test, self.target_train, self.target_test = (
            train_test_split(
                feature_matrix, target_labels,
                test_size=self.test_size,
                random_state=self.random_state,
                stratify=target_labels
            )
        )

        # Standardize features for models that benefit from scaling
        self.feature_scaler = StandardScaler()
        self.feature_train_scaled = self.feature_scaler.fit_transform(self.feature_train)
        self.feature_test_scaled = self.feature_scaler.transform(self.feature_test)

        print("Dataset loaded: Breast Cancer Classification (569 samples)")
        print(f"Training samples: {len(self.feature_train)}, Testing samples: {len(self.feature_test)}")
        print(f"Number of features: {self.feature_train.shape[1]}")
        print(f"Number of classes: {len(np.unique(self.target_train))}")

        return self

    def calculate_evaluation_metrics(self, predictions, prediction_probabilities):
        """
        Calculate all required evaluation metrics

        Args:
            predictions: Model predictions
            prediction_probabilities: Probability predictions for AUC calculation

        Returns:
            Dictionary containing all metrics
        """
        accuracy_metric = accuracy_score(self.target_test, predictions)

        # Calculate AUC using one-vs-rest approach for multi-class
        try:
            if len(np.unique(self.target_test)) == 2:
                auc_metric = roc_auc_score(self.target_test, prediction_probabilities[:, 1])
            else:
                auc_metric = roc_auc_score(
                    self.target_test, prediction_probabilities,
                    multi_class='ovr', average='weighted'
                )
        except:
            auc_metric = 0.0

        precision_metric = precision_score(self.target_test, predictions, average='weighted', zero_division=0)
        recall_metric = recall_score(self.target_test, predictions, average='weighted', zero_division=0)
        f1_metric = f1_score(self.target_test, predictions, average='weighted', zero_division=0)
        mcc_metric = matthews_corrcoef(self.target_test, predictions)

        return {
            'accuracy': accuracy_metric,
            'auc': auc_metric,
            'precision': precision_metric,
            'recall': recall_metric,
            'f1': f1_metric,
            'mcc': mcc_metric
        }

    def train_logistic_regression_model(self):
        """Train Logistic Regression model"""
        model_instance = LogisticRegression(
            max_iter=1000, random_state=self.random_state
        )
        model_instance.fit(self.feature_train_scaled, self.target_train)

        predictions = model_instance.predict(self.feature_test_scaled)
        prediction_probabilities = model_instance.predict_proba(self.feature_test_scaled)

        metrics = self.calculate_evaluation_metrics(predictions, prediction_probabilities)
        self.models['logistic_regression'] = {
            'model': model_instance,
            'metrics': metrics
        }

        return metrics

    def train_decision_tree_model(self):
        """Train Decision Tree Classifier model"""
        model_instance = DecisionTreeClassifier(
            max_depth=10, random_state=self.random_state, min_samples_split=5
        )
        model_instance.fit(self.feature_train, self.target_train)

        predictions = model_instance.predict(self.feature_test)
        prediction_probabilities = model_instance.predict_proba(self.feature_test)

        metrics = self.calculate_evaluation_metrics(predictions, prediction_probabilities)
        self.models['decision_tree'] = {
            'model': model_instance,
            'metrics': metrics
        }

        return metrics

    def train_knn_classifier_model(self):
        """Train K-Nearest Neighbors model"""
        model_instance = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
        model_instance.fit(self.feature_train_scaled, self.target_train)

        predictions = model_instance.predict(self.feature_test_scaled)
        prediction_probabilities = model_instance.predict_proba(self.feature_test_scaled)

        metrics = self.calculate_evaluation_metrics(predictions, prediction_probabilities)
        self.models['knn'] = {
            'model': model_instance,
            'metrics': metrics
        }

        return metrics

    def train_gaussian_naive_bayes_model(self):
        """Train Gaussian Naive Bayes model"""
        model_instance = GaussianNB()
        model_instance.fit(self.feature_train_scaled, self.target_train)

        predictions = model_instance.predict(self.feature_test_scaled)
        prediction_probabilities = model_instance.predict_proba(self.feature_test_scaled)

        metrics = self.calculate_evaluation_metrics(predictions, prediction_probabilities)
        self.models['naive_bayes'] = {
            'model': model_instance,
            'metrics': metrics
        }

        return metrics

    def train_random_forest_ensemble_model(self):
        """Train Random Forest Ensemble model"""
        model_instance = RandomForestClassifier(
            n_estimators=100, max_depth=15, random_state=self.random_state,
            min_samples_split=5, min_samples_leaf=2
        )
        model_instance.fit(self.feature_train, self.target_train)

        predictions = model_instance.predict(self.feature_test)
        prediction_probabilities = model_instance.predict_proba(self.feature_test)

        metrics = self.calculate_evaluation_metrics(predictions, prediction_probabilities)
        self.models['random_forest'] = {
            'model': model_instance,
            'metrics': metrics
        }

        return metrics

    def train_all_models(self):
        """Train all classification models"""
        print("\n" + "="*60)
        print("TRAINING ALL MODELS")
        print("="*60)

        print("\n1. Training Logistic Regression...")
        lr_metrics = self.train_logistic_regression_model()
        print(f"   Accuracy: {lr_metrics['accuracy']:.4f}, AUC: {lr_metrics['auc']:.4f}")

        print("\n2. Training Decision Tree...")
        dt_metrics = self.train_decision_tree_model()
        print(f"   Accuracy: {dt_metrics['accuracy']:.4f}, AUC: {dt_metrics['auc']:.4f}")

        print("\n3. Training K-Nearest Neighbors...")
        knn_metrics = self.train_knn_classifier_model()
        print(f"   Accuracy: {knn_metrics['accuracy']:.4f}, AUC: {knn_metrics['auc']:.4f}")

        print("\n4. Training Gaussian Naive Bayes...")
        nb_metrics = self.train_gaussian_naive_bayes_model()
        print(f"   Accuracy: {nb_metrics['accuracy']:.4f}, AUC: {nb_metrics['auc']:.4f}")

        print("\n5. Training Random Forest (Ensemble)...")
        rf_metrics = self.train_random_forest_ensemble_model()
        print(f"   Accuracy: {rf_metrics['accuracy']:.4f}, AUC: {rf_metrics['auc']:.4f}")

        return self

    def generate_comparison_report(self):
        """Generate comparison table of all models"""
        comparison_data = []

        for model_name, model_info in self.models.items():
            metrics = model_info['metrics']
            comparison_data.append({
                'model_name': model_name.replace('_', ' ').title(),
                'accuracy': metrics['accuracy'],
                'auc': metrics['auc'],
                'precision': metrics['precision'],
                'recall': metrics['recall'],
                'f1': metrics['f1'],
                'mcc': metrics['mcc']
            })

        self.results_dataframe = pd.DataFrame(comparison_data)
        return self.results_dataframe

    def save_models_to_disk(self, directory_path='model'):
        """Save all trained models to disk"""
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        for model_name, model_info in self.models.items():
            model_filepath = os.path.join(directory_path, f'{model_name}_model.pkl')
            joblib.dump(model_info['model'], model_filepath)
            print(f"Saved: {model_filepath}")

    def save_scaler_to_disk(self, directory_path='model'):
        """Save the feature scaler for preprocessing"""
        scaler_filepath = os.path.join(directory_path, 'feature_scaler.pkl')
        joblib.dump(self.feature_scaler, scaler_filepath)
        print(f"Saved: {scaler_filepath}")

    def save_models(self, directory_path='model'):
        """Alias for save_models_to_disk and save_scaler_to_disk"""
        self.save_models_to_disk(directory_path)
        self.save_scaler_to_disk(directory_path)

    def generate_results(self):
        """Generate results dataframe if not already generated"""
        if self.results_dataframe is None:
            self.generate_comparison_report()
        return self.results_dataframe


def main():
    """Main execution function"""
    pipeline = BreastCancerClassificationPipeline(test_size=0.2, random_state=42)

    # Load and prepare data
    pipeline.load_and_prepare_dataset()

    # Train all models
    pipeline.train_all_models()

    # Generate comparison report
    comparison_report = pipeline.generate_comparison_report()
    print("\n" + "="*60)
    print("MODEL COMPARISON REPORT")
    print("="*60)
    print(comparison_report.to_string(index=False))

    # Save models and scaler
    pipeline.save_models_to_disk()
    pipeline.save_scaler_to_disk()

    # Save comparison to CSV
    comparison_report.to_csv('model_evaluation_results.csv', index=False)
    print("\nResults saved to model_evaluation_results.csv")


if __name__ == '__main__':
    main()
