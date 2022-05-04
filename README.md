---
title: "Table Tennis Tracker Using OpenCV"
date: 2022-05-04T22:16:07+08:00
---
## Inspiration
Hello people! You know life is getting great again when you have ample time to execute your personal projects. (I just finished my Year 1’s final!!!) Anyway, this table tennis tracker thingy has been lying on my project list for quite a long time. It was a fortuitous coincidence for me to be piqued by this computer vision topic. There are mainly two reasons for me doing this:
1. I accidentally knew someone from Linkedin who did this project before
2. I found out that XX company’s employees are doing this as a fun after-work project in a company visit

These two things coupled together make me want to give this project a shot.

## Videography
Before creating a tracking OpenCV model for a table tennis ball, I first need to record a video of me playing table tennis. In the recording process, I tried to take the videos from several angles, filter out the unwanted parts, and compile the usable parts altogether. In the end, I got two short videos. One acts as a training video while the other acts as a testing video.

## First Attempt: Filter out the ball and grab contours
Initially, I plan to use CV2's inRange function to filter out the ball, by adjusting the lower boundary and higher boundary color values.
![1](/img/tabletennis1.png)
But it seems like my video is not suitable for this method because the background and the ping pong table contain a similar color to the white ball, causing the model to misinterpret. I tried to modify the color of the video using premier pro but the effect doesn't help much too.


## Second Attempt: Use Background Subtraction to Track the ball
This method is purposed to track the movement of the ball by subtracting the previous frame from the current frame. I found this method while googling how to track moving objects using OpenCV. OpenCV provides several functions to subtract the background. I chose one of them and got the below result.
![2](/img/tabletennis2.png)
As you can see, this method removes the other unnecessary white traces.  Only the ball is left in the processed frame.

## Find corners in the video, add circles and export
After implementing the background subtraction successfully, all left for me is to identify the white color in the processed frames and add circles to the original frames.  
Final video: [Click Here](https://youtu.be/vu5ulU8vvO4)  
Github Code: [Read Me](https://github.com/woonyee28/tt_tracker)
