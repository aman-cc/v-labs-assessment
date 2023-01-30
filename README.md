# V-Labs Assessment

## Assignment 1
Given a folder with image and text files, segregate images and text files into two different folders.

Solution: Iterate through the files in the given folder and check if the extension is image file or text file. Then write to two different folders.

Steps:

```
python assignment-1.py
```

Output is stored in `Assignment_1/output_folder`.

## Assignment 2
Write a program for calculating statistics from given excel files.

Solution: \
a) Accuracy: Accuracy  = 100 - character level error rate \
b) Number of lines in GT column = len(gt_df["GT"])  \
c) Number of characters in ground truth file = Concatenate strings in the column and calculate length of string

Steps:

```
python assignment-2.py Assignment_2/gt.xlsx Assignment_2/pred.xlsx
```

## Assigment 3
Develop a solution for detecting a face in a live web camera feed.

Solution:
Used open-cv based face detector to detect faces and draw bounding box and save the video to disk with name 'vid_face_detect.mp4'.

Steps:
```
python assignment-3.py
```
Press 'Q' to quit.