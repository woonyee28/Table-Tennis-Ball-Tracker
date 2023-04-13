# Table Tennis Tracker using OpenCV   
This project aims to track the movement of a table tennis ball in a video using OpenCV, a popular computer vision library. The process involves filtering out the ball, generating a foreground mask, and then adding circles to the original frames to visualize the ball's movement.   
   
## Approach
### First Attempt: Filter out the ball and grab contours
Initially, we attempted to filter out the ball from the video using the inRange function from CV2 by adjusting the lower and upper HSV values.    
![1](/Images/tabletennis1.png)
However, the background and ping pong table's color was too similar to the ball's white color, causing the model to misinterpret. We even tried modifying the video color using Premiere Pro, but it was not effective.     


### Second Attempt: Use Background Subtraction to Track the ball
We then tried using background subtraction to track the ball's movement by generating a foreground mask, which is a binary image containing the pixels belonging to moving objects in the scene, using a static camera. OpenCV provides several functions to subtract the background, and we chose one of them.   
![2](/Images/tabletennis2.png)
This method successfully removed unnecessary white traces, leaving only the ball in the processed frame.

### Adding Circles to the Original Frame
After implementing background subtraction successfully, we identified the white color in the processed frames and added circles to the original frames. The final video output can be found here:   
Final video: [Click Here](https://youtu.be/vu5ulU8vvO4)     
Github Code: [Read Me](https://github.com/woonyee28/tt_tracker)    

## How to run the code?   
To install the dependencies, run:   
``` pip install -r requirements.txt ```   
To run the python file, run:   
``` python tabletennis.py ```   