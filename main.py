import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = cv2.imread("Task_1.jpg")
image_copy = image.copy()

# Create a list to store the coordinates of the rectangle
rectangle_coordinates = []

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global rectangle_coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        rectangle_coordinates = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        rectangle_coordinates.append((x, y))
        cv2.rectangle(image_copy, rectangle_coordinates[0], rectangle_coordinates[1], (0, 255, 0), 2)
        cv2.imshow('Task_1', image_copy)

# Create a window and set the callback function
cv2.namedWindow('Task_1')
cv2.setMouseCallback('Task_1', draw_rectangle)

# Display the image
cv2.imshow('Task_1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Crop the image based on the selected rectangle
top_left = rectangle_coordinates[0]
bottom_right = rectangle_coordinates[1]
cropped_image = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

# Save the cropped image
cv2.imwrite('Task_1_cropped.jpg', cropped_image)

# Draw the rectangle on a copy of the original image
cv2.rectangle(image_copy, top_left, bottom_right, (0, 255, 0), 2)

# Display the coordinates of the cropped image
crop_coordinates_text = f'Top Left: {top_left}, Bottom Right: {bottom_right}'
cv2.putText(image_copy, crop_coordinates_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Save the annotated image with coordinates
cv2.imwrite('Task_1_insights.jpg', image_copy)

# Display the original image with the selected rectangle and coordinates using Matplotlib
plt.imshow(cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB))
plt.title('Task_1_insights.jpg')
plt.show()
