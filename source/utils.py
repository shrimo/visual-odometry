import cv2
import numpy as np


# Draws detected and tracked features on a frame (motion vector is drawn as a line).
def drawFrameFeatures(frame, prevPts, currPts, frameIdx):
    currFrameRGB = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
    for i in range(len(currPts) - 1):
        # print(currPts[i])
        cv2.circle(
            currFrameRGB,
            (np.int32(currPts[i][0]), np.int32(currPts[i][1])),
            radius=3,
            color=(0, 255, 0),
        )
        cv2.line(
            currFrameRGB,
            (np.int32(currPts[i][0]), np.int32(currPts[i][1])),
            (np.int32(prevPts[i][0]), np.int32(prevPts[i][1])),
            color=(0, 0, 255),
        )
        cv2.putText(
            currFrameRGB,
            "Frame: {}".format(frameIdx),
            (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 250, 250),
        )
        cv2.putText(
            currFrameRGB,
            "Features: {}".format(len(currPts)),
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 250, 250),
        )
    cv2.imshow("2D Viewer", currFrameRGB)
