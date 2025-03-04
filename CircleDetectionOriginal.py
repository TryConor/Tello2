# Import the required libraries
import cv2  # OpenCV for image processing
import numpy as np  # NumPy for numerical operations
import os

# Get the current directory
current_directory = os.getcwd()

# List all files in the directory
files = os.listdir(current_directory)

# Filter for image files
image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]

# Define the desired width and height
desired_width = 400  # Example width
desired_height = 400  # Example height

# Read and process each image
for image_file in image_files:
    # Construct full file path
    image_path = os.path.join(current_directory, image_file)
    
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if image was loaded successfully
    if image is not None:
        # Resize the image
        resized_image = cv2.resize(image, (desired_width, desired_height))
        
        # Process the resized image (e.g., display it)
        cv2.imshow('Resized Image', resized_image)
        cv2.waitKey(0)  # Wait until a key is pressed
        cv2.destroyAllWindows()
        
        # Convert resized image to grayscale
        gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian Blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect circles in the image
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=60, param2=40, minRadius=10, maxRadius=50)

        # If circles were found, draw them on the image
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                # Draw the outer circle
                cv2.circle(resized_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # Draw the center of the circle
                cv2.circle(resized_image, (i[0], i[1]), 2, (0, 0, 255), 3)

        # Display the output
        cv2.imshow('Detected Circles', resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Failed to load image: {image_file}")