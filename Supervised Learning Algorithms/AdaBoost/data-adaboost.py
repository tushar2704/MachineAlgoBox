#© 2023 Tushar Aggarwal. All rights reserved.(github.com/tushar2704)
from sklearn.datasets import make_classification

# Generate a synthetic dataset for classification
X, y = make_classification(
    n_samples=1000,     # Total number of samples
    n_features=10,      # Number of features
    n_informative=5,    # Number of informative features
    n_redundant=2,      # Number of redundant features
    n_classes=2,        # Number of classes
    random_state=42     # Random state for reproducibility
)

# Print the shape of the dataset
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
