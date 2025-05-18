import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from tensorflow.keras.utils import to_categorical

# Generate a classification dataset
X, y = make_classification(n_samples=1000, n_features=3, n_informative=3, n_redundant=0, n_classes=2, random_state=42)

# Convert labels to categorical format (one-hot encoding)
y_categorical = to_categorical(y, num_classes=2)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# Build the model
model = Sequential([
    Dense(10, activation='relu', input_shape=(3,)),  # First hidden layer
    Dense(2, activation='softmax')  # Output layer (2 classes)
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=16, validation_split=0.1)

# Evaluate the model on the test data
loss, accuracy = model.evaluate(X_test, y_test)

# Print the test accuracy
print(f"Test Accuracy: {accuracy:.2f}")
