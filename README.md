# OpenCV Basics: Rotation and Filters

This folder contains simple OpenCV examples demonstrating:
- Image rotation and flipping
- Common image filtering techniques: Gaussian blur, Median blur, and sharpening (via filter2D)

These scripts use a local image file named `sanjay.jpg`. Make sure this image exists relative to where you run the scripts.

## Prerequisites

- Python 3.8+
- OpenCV for Python

Install OpenCV:
```bash
pip install opencv-python
```

## Files Covered

- [rotation.py](https://github.com/sanjaynep/opencv-learning-projects/blob/7df656bd8bdd34186da3f1914702e93dc0f98be6/rotation.py)
- [image_processing/guassian_blur.py](https://github.com/sanjaynep/opencv-learning-projects/blob/7df656bd8bdd34186da3f1914702e93dc0f98be6/image_processing/guassian_blur.py)
- [image_processing/median_blur.py](https://github.com/sanjaynep/opencv-learning-projects/blob/7df656bd8bdd34186da3f1914702e93dc0f98be6/image_processing/median_blur.py)
- [image_processing/sharpen.py](https://github.com/sanjaynep/opencv-learning-projects/blob/7df656bd8bdd34186da3f1914702e93dc0f98be6/image_processing/sharpen.py)

## How to Run

From the repository root:
```bash
python rotation.py
```

From the `image_processing` directory:
```bash
python guassian_blur.py
python median_blur.py
python sharpen.py
```

If you run from a different working directory, ensure `sanjay.jpg` is located where the scripts expect it (same directory as the script).

## What Each Script Does

### rotation.py
- Loads `sanjay.jpg`, resizes to 500x500.
- Creates a rotation matrix with `cv2.getRotationMatrix2D(center, 360, 2.0)` and applies it using `cv2.warpAffine`.
  - Angle: 360° (full rotation)
  - Scale: 2.0 (zooms the image)
- Demonstrates flipping:
  - `cv2.flip(image, 0)`: flip vertically (around x-axis)
  - `cv2.flip(image, 1)`: flip horizontally (around y-axis)
  - `cv2.flip(image, -1)`: flip both axes

Run example:
```bash
python rotation.py
```

### image_processing/guassian_blur.py
- Loads `sanjay.jpg`, resizes to 500x800.
- Applies Gaussian blur with a 3x3 kernel: `cv2.GaussianBlur(resized, (3,3), 0)`
  - Useful for reducing noise with a mild smoothing effect.

Run:
```bash
python image_processing/guassian_blur.py
```

### image_processing/median_blur.py
- Loads `sanjay.jpg`, resizes to 500x800.
- Applies median blur with kernel size 3: `cv2.medianBlur(resized, 3)`
  - Kernel size must be odd.
  - Great for removing “salt-and-pepper” noise while preserving edges better than simple averaging.

Run:
```bash
python image_processing/median_blur.py
```

### image_processing/sharpen.py
- Loads `sanjay.jpg`, resizes to 500x800.
- Applies a sharpening kernel via `cv2.filter2D`:
  - Kernel:
    ```
    [[ 0, -1,  0],
     [-1,  5, -1],
     [ 0, -1,  0]]
    ```
  - Enhances edges and details, making the image appear crisper.

Run:
```bash
python image_processing/sharpen.py
```

## Tips

- If `sanjay.jpg` is not found, the scripts print a message and exit. Ensure the image path is correct.
- You can experiment with different kernel sizes (odd numbers like 3, 5, 7) for blur filters to see how the effect changes.
- For rotation:
  - Try angles like 45, 90, 180 to observe different rotations.
  - Adjust the scale factor (e.g., 0.5 to shrink, 1.0 for original size, >1.0 to zoom).

## Troubleshooting

- “image not found”: Place `sanjay.jpg` in the same directory as the script you’re running or modify the path in the code.
- Windows users may need to press a key in the image window to close it after `cv2.waitKey(0)`.
- If windows do not show, ensure you’re not running in a headless environment (like some remote servers without GUI).

## License

This repository appears to be for learning purposes. If you plan to distribute or reuse, consider adding an explicit license file.

---
To explore more related files in this repository, use GitHub’s code search:
- Rotation/filter-related code search: https://github.com/search?q=repo%3Asanjaynep%2Fopencv-learning-projects+rotate+filter&type=code
