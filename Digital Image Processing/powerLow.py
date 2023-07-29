import cv2
import numpy as np
import matplotlib.pyplot as plt

def power_law_transform(image, gamma):
    c = 1.0  # Scaling constant (adjust as needed)
    transformed_image = c * np.power(image, gamma)
    return np.clip(transformed_image, 0, 255).astype(np.uint8)

# Load an image
image_path = 'E://New_folder//python//Digital Image Processing//rain.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the gamma value
gamma = 0.5  # Adjust this value to control the transformation

# Apply the Power Law transformation
transformed_image = power_law_transform(image, gamma)

# Display the original and transformed images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Transformed Image')
plt.imshow(transformed_image, cmap='gray')

plt.tight_layout()
plt.show()
