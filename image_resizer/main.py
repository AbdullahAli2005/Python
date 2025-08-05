import cv2

# Load the image
image = cv2.imread('babar.jpg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Resizing scales
new_width = 1200
new_height = 800

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('babar_resized.jpg', resized_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()