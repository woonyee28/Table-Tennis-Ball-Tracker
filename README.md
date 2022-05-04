---
title: "Table Tennis Tracker Using OpenCV"
date: 2022-05-04T22:16:07+08:00
---

## First Attempt: Filter out the ball and grab contours
Initially, I plan to use CV2's inRange function to filter out the ball, by adjusting the lower boundary and higher boundary HSV values.
![1](/Images/tabletennis1.png)
But it seems like my video is not suitable for this method because the background and the ping pong table contain a similar color to the white ball, causing the model to misinterpret. I tried to modify the color of the video using Premiere Pro but the effect doesn't help much too.


## Second Attempt: Use Background Subtraction to Track the ball
This method is purposed to track the movement of the ball by subtracting the previous frame from the current frame. I found this method while googling how to track moving objects using OpenCV. OpenCV provides several functions to subtract the background. I chose one of them and got the below result.
![2](/Images/tabletennis2.png)
As you can see, this method removes the other unnecessary white traces.  Only the ball is left in the processed frame.

## Find corners in the video, add circles and export
After implementing the background subtraction successfully, all left for me is to identify the white color in the processed frames and add circles to the original frames.  
Final video: [Click Here](https://youtu.be/vu5ulU8vvO4)  
Github Code: [Read Me](https://github.com/woonyee28/tt_tracker)
