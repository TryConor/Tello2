import cv2
import numpy as np

# Read the image
# img = cv2.imread('eyes.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('circle.jpg', cv2.IMREAD_COLOR)

# Resize the image to reduce its dimensions (e.g., 50% of the original size)
scale_percent = 50  # Adjust this value as needed
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a 3x3 blur to the image
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough Circle Transform
detected_circles = cv2.HoughCircles(
    gray_blurred, cv2.HOUGH_GRADIENT, 1, 20,
    param1=50, param2=30, minRadius=1, maxRadius=40
)

# Draw detected circles
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circle's outline
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw the center point
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

    # Display the result
    cv2.imshow("Detected Circles", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
