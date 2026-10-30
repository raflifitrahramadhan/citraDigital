"""
Tugas Pengolahan Citra Digital - Transformasi Geometri
Translation, Scaling, Rotation, Horizontal Flip, Vertical Flip

Library: OpenCV, NumPy, Matplotlib
Install: pip install opencv-python numpy matplotlib
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



img_bgr = cv2.imread("gambar.jpg")
if img_bgr is None:
    raise FileNotFoundError(f"Gambar '{IMAGE_PATH}' tidak ditemukan.")
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  
h, w = img.shape[:2]
def translation(image, tx, ty):
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))



def scaling(image, sx, sy):
    new_w = int(image.shape[1] * sx)
    new_h = int(image.shape[0] * sy)
    M = np.float32([[sx, 0, 0],
                    [0, sy, 0]])
    return cv2.warpAffine(image, M, (new_w, new_h), flags=cv2.INTER_LINEAR)



def rotation(image, angle):
    (hh, ww) = image.shape[:2]
    center = (ww / 2, hh / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos, sin = abs(M[0, 0]), abs(M[0, 1])
    new_w = int(hh * sin + ww * cos)
    new_h = int(hh * cos + ww * sin)

   
    M[0, 2] += new_w / 2 - center[0]
    M[1, 2] += new_h / 2 - center[1]
    return cv2.warpAffine(image, M, (new_w, new_h))


def horizontal_flip(image):
    M = np.float32([[-1, 0, image.shape[1] - 1],
                    [0, 1, 0]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))


def vertical_flip(image):
    M = np.float32([[1, 0, 0],
                    [0, -1, image.shape[0] - 1]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))


hasil = {
    "Citra Asli": img,
    f"Translation (tx={w // 4}, ty={h // 4})": translation(img, w // 4, h // 4),
    "Scaling 0,5x": scaling(img, 0.5, 0.5),
    "Scaling 2x": scaling(img, 2, 2),
    "Rotation 45°": rotation(img, 45),
    "Rotation 90°": rotation(img, 90),
    "Rotation 180°": rotation(img, 180),
    "Horizontal Flip": horizontal_flip(img),
    "Vertical Flip": vertical_flip(img),
}

fig, axes = plt.subplots(3, 3, figsize=(14, 12))
for ax, (judul, gambar) in zip(axes.ravel(), hasil.items()):
    ax.imshow(gambar)
    ax.set_title(f"{judul}\n{gambar.shape[1]}x{gambar.shape[0]} px", fontsize=10)
    ax.axis("off")

plt.tight_layout()
plt.savefig("hasil_transformasi.png", dpi=150) 
plt.show()