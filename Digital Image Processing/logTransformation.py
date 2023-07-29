import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'E://New_folder//python//Digital Image Processing//rain.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

log_transformed_image = np.log1p(original_image)
log_transformed_image = (log_transformed_image - np.min(log_transformed_image)) / (np.max(log_transformed_image) - np.min(log_transformed_image)) * 255
log_transformed_image = log_transformed_image.astype(np.uint8)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_image, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Log-Transformed Image')
plt.imshow(log_transformed_image, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
