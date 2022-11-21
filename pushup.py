import cv2

from gtts import gTTS #for voice output

from playsound import playsound #for voice output

import mediapipe as mp

def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 
 
def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")
 
 
def main(a):
    """ Main program is here. """
    # Get the high score
    high_score = get_high_score()
 
    # Get the score from the current game
    current_score = 0
    try:
        # Ask the user for his/her score
        current_score = int(a)
    except ValueError:
        # Error, can't turn what they typed into a number
        print("I don't understand what you typed.")
 
    # See if we have a new high score
    if current_score > high_score:
        # We do! Save to disk
        print("Yea! New high score!")
        save_high_score(current_score)
    else:
        print("Better luck next time.")
 
# Call the main function, start up the game

mp_drawing = mp.solutions.drawing_utils

mp_pose = mp.solutions.pose

counter = 0

stage = None

create = None

opname = "output.avi"

def findPosition(image, draw=True):

  lmList = []

  if results.pose_landmarks:

      mp_drawing.draw_landmarks(

         image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

      for id, lm in enumerate(results.pose_landmarks.landmark):

          h, w, c = image.shape

          cx, cy = int(lm.x * w), int(lm.y * h)

          lmList.append([id, cx, cy])

          #cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

  return lmList

result = 0

cap = cv2.VideoCapture(0)

with mp_pose.Pose(

    min_detection_confidence=0.7,

    min_tracking_confidence=0.7) as pose:

  while cap.isOpened():

    success, image = cap.read()

    image = cv2.resize(image, (640,480))

    if not success:

      print("Ignoring empty camera frame.")

      # If loading a video, use 'break' instead of 'continue'.

      continue

    # Flip the image horizontally for a later selfie-view display, and convert

    # the BGR image to RGB.

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # To improve performance, optionally mark the image as not writeable to

    # pass by reference.

    results = pose.process(image)

    # Draw the pose annotation on the image.

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    lmList = findPosition(image, draw=True)

    if len(lmList) != 0:

      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)

      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)

      cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 0, 255), cv2.FILLED)

      cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 0, 255), cv2.FILLED)

      if (lmList[12][2] and lmList[11][2] >= lmList[14][2] and lmList[13][2]):

        cv2.circle(image, (lmList[12][1], lmList[12][2]), 20, (0, 255, 0), cv2.FILLED)

        cv2.circle(image, (lmList[11][1], lmList[11][2]), 20, (0, 255, 0), cv2.FILLED)

        stage = "down"

      if (lmList[12][2] and lmList[11][2] <= lmList[14][2] and lmList[13][2]) and stage == "down":

        stage = "up"

        counter += 1

        result = counter

        print(counter)

    text = "{}:{}".format("Push Ups", counter)

    cv2.putText(image, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,

                1, (255, 0, 0), 2)

    cv2.imshow('MediaPipe Pose', image)

    if create is None:

      fourcc = cv2.VideoWriter_fourcc(*'XVID')

      create = cv2.VideoWriter(opname, fourcc, 30, (image.shape[1], image.shape[0]), True)

    create.write(image)

    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop

    if key == ord("r"):

      main(result)
     
      mytext ="Your score is" + str(result)#for voice output

      audio = gTTS(text=mytext, lang="en", slow=False)#for voice output

      audio.save("example.mp3")#for voice output

      playsound("example.mp3")#for voice output
        
      counter = 0

      result = 0

    if key == ord("q"):

      main(result)

      if counter != 0 :
        mytext ="Your score is" + str(result)#for voice output

        audio = gTTS(text=mytext, lang="en", slow=False)#for voice output

        audio.save("example.mp3")#for voice output

        playsound("example.mp3")#for voice output

      break

    # do a bit of cleanup
  


cv2.destroyAllWindows()
