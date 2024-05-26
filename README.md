## Installation

1. Clone the repository:

```bash
git clone https://github.com/RayGman/face-swapper
cd face-swapper
```

2. Install the required dependencies:

```pip
pip install -r requirements.txt
```

3. Execution

```python
 python main.py
```

## Usage

### There are three main functions available for face swapping:

- swap_n_show(img1_fn, img2_fn, app, swapper, plot_before=True, plot_after=True): This function swaps faces between two input images.

- swap_n_show_same_img(img1_fn, app, swapper, plot_before=True, plot_after=True): This function swaps faces within the same image.

- swap_face_single(img1_fn, img2_fn, app, swapper): This function adds face from the source image to the target image and saves in output/ folder.

- fine_face_swap(img1_fn, img2_fn, app, swapper): This function has ability to finely select faces from image with multiple faces.

You can use these functions in your Python scripts or Jupyter notebooks.

## Example

```python
import cv2
import matplotlib.pyplot as plt
from faceswap import swap_n_show, swap_n_show_same_img, swap_face_single

# Load images
img1_fn = 'images/bramhi.jpg'
img2_fn = 'images/modi.jpg'

# Swap faces between two images
swap_n_show(img1_fn, img2_fn, app, swapper, enhance=True, enhancer='REAL-ESRGAN 2x')

# Swap faces within the same image
swap_n_show_same_img(img1_fn, app, swapper, enhance=True, enhancer='REAL-ESRGAN 2x')

# Add face to an image
swap_face_single(img1_fn, img2_fn, app, swapper, enhance=True, enhancer='REAL-ESRGAN 2x', device="cpu")

# Swap faces in images with multiple faces
fine_face_swap(img1_fn, img2_fn, app, swapper, enhance=True, enhancer='REAL-ESRGAN 2x')
```

## Available Enhancers

- GFPGAN
- REAL-ESRGAN 2x
- REAL-ESRGAN 4x
- REAL-ESRGAN 8x

## GPU Support

- cuda
  **_(set 'device=cuda' to run with gpu)_**
