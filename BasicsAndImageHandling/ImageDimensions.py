import cv2

img = cv2.imread('../images/cat.jpg')

print(f"Image Shape {img.shape}")
print(f"Width: {img.shape[1]}")
print(f"Height: {img.shape[0]}")
print(f"Color Channels: {img.shape[2]}")