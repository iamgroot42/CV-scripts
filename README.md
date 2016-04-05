## openCV examples (Python)
A set of functions (useful for CV) implemented using openCV for Python.

### Requirements:
- <a href="http://www.pyimagesearch.com/opencv-tutorials-resources-guides/"> opencv_contrib package (for SIFT,SURF) </a>

### Running it:
- `python face_track.py <Y/N>` , to use HAAR to track faces in frames and dump them into a .json
- `python face_track_manual.py`, to manually track features (marking them frame-by-frame)
- `python Graphs/face_diff.py <input .json>`, to see "difference" plots, in case two features were used
- `python Graphs/face_track.py <input .json>`, to plot faces across frames (correspondences established via sorting)

## Note
You may have to run the following commands (if `import cv2` throws any errors):

 * `  sudo ldconfig /usr/local/cuda/lib64 `
 * add `export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH` to .bashrc