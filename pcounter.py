import cv2
from tkinter import *
import os
from PIL import ImageTk, Image
from gtts import gTTS #for voice output
import time

from playsound import playsound #for voice output

import mediapipe as mp
sc = 0
timer=30

window = Tk()
window.configure(width=1920, height=1080)
window.title("Push Up Counter")
gFrame = Frame(window, width=1920, height=1080)
gFrame.configure(bg="#651A84")
window.configure(bg="#651A84")
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda e: window.destroy())
window.bind("<Control-Return>", lambda e: e.widget.attributes("-fullscreen", not e.widget.attributes("-fullscreen")))
window.bind("<Return>", lambda e: e.widget.attributes("-topmost", not e.widget.attributes("-topmost")))
canvas = Canvas(gFrame, width = 640, height = 480)

label0 = Label(master=gFrame, text="",fg = "white",bg = "#651A84", font="arial, 100")
label0.grid(row=0, column=0)
label00 = Label(master=gFrame, text="",fg = "white",bg = "#651A84", font="arial, 25")
label00.grid(row=3, column=0)
label1 = Label(master=gFrame, text="Your Score",fg = "white",bg = "#651A84", font="arial, 25")
label1.grid(row=1, column=0, padx=50, sticky="s")
labeltime = Label(master=gFrame, text=f'Time left: {timer:0.2f}',fg = "white",bg = "#651A84", font="arial, 25")
labeltime.grid(row=0, column=8,pady=50, sticky="n")
label2 = Label(master=gFrame, text="High Score",fg = "white",bg = "#651A84", font="arial, 25")
label2.grid(row=1, column=3, padx=50,  sticky="s")
label000 = Label(master=gFrame, text="",fg = "white",bg = "#651A84", font="arial, 25")
label000.grid(row=4, column=0)
score = Label(master=gFrame, text = sc,fg = "white",bg = "#651A84", font="arial, 100")
score.grid(row=2, column=0, padx=50)
gFrame.pack()

# display the final score

fFrame = Frame(window, width=1920, height=1080)
fFrame.configure(bg="#651A84")
start = Button(master=gFrame,fg = "white",bg = "#651A84", font="arial, 25", text = 'START', bd = '5',activebackground='#a66ec4')
start.grid(row=4, column=2)
start.grid_forget()


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
 
high_score=get_high_score()

labelfScore = Label(master=fFrame, text = f'Your score: {sc}',fg = "white",bg = "#651A84", font="arial, 100") 
labelfHighScore = Label(master=fFrame, text = f'High score: {sc}',fg = "white",bg = "#651A84", font="arial, 100") 
labelBeatHighScore = Label(master=fFrame, text = f'Congrats!!! You\'ve beaten the current record.', fg = "white",bg = "#651A84", font="arial, 80")
labelfScore.grid(row=2, column=3, padx=50, )
labelfHighScore.grid(row=3, column=3, padx=50, )
# labelBeatHighScore.grid(row=4, column=3, padx=50, )

canvas.grid(row=1, column=5, columnspan=4, rowspan=4, padx=100, pady=100, )
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
    global high_score
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

def nxt():
    canvas.delete('all')
    start.grid_forget()
    global high
    high = False
    score.configure(text="0")
    label1.configure(text="Your Score")
    window.update()
    starting()
result = 0

def got_name():
    inp = inputName.get(1.0, "end-1c")
    print(inp)
    now_score = result
    print(now_score)
    leader([inp,now_score])
    inputName.grid_forget()
    enter.grid_forget()
    start.configure(command=nxt)
    #start = Button(master=gFrame,fg = "white",bg = "#651A84", font="arial, 25", text = 'START', bd = '5',activebackground='#a66ec4',command = nxt)
    start.grid(row=4, column=2)
inputName = Text(gFrame,height = 1,width = 30,font="arial,50")
inputName.bind("<Return>",got_name)
enter = Button(gFrame,fg="white",bg="#651A84",text="Enter",activebackground='#a66ec4',command=got_name)

with open("lb.txt") as f:
    content_list = f.readlines()

content_list = [x.strip() for x in content_list]
lb=[]
lbb=[]
for i in content_list:
    l=list(map(str,i.split(" ")))
    lb.append(l)

def leader(hs):
    if (int(int(hs[1])) > int(lb[4][1])):
        lb[4] = hs   
        def Sort(sub_li):
            sub_li.sort(key = lambda x: int(x[1]), reverse = True)
            return sub_li
        lbb = Sort(lb)
        print(lbb)
        with open('lb.txt', 'w') as fp:
            for item in lbb:
                for i in item:
                    fp.write("%s " %str(i))
                fp.write("\n")
high_score = int(lb[0][1])
high_score_file = open("high_score.txt", "w")
high_score_file.write(str(high_score))
high_score_file.close()
Hscore = Label(master=gFrame, text=high_score,fg = "white",bg = "#651A84", font="arial, 100")
Hscore.grid(row=2, column=3, padx=50, )
print(high_score)
high = False
def starting():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    stage = None
    create = None
    opname = "output.avi"
    global high_score
    popup = False
    global result

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
    timer = 1
    cap = cv2.VideoCapture(0)
    starttime=time.time()
    
    with mp_pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
     while cap.isOpened() and timer>0:
        gFrame.lift()
        success, image = cap.read()
        curtime = time.time()
        timer = 30 - (curtime-starttime) 
        image = cv2.resize(image, (640,480))
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = pose.process(image)

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
                global result
                global high_score
                result = counter
                score.configure(text = counter,fg = "white",bg = "#651A84", font="arial, 100")
                if counter>high_score:
                    high_score = counter
                    global high
                    high = True
                    Hscore.configure(text=high_score,fg = "white",bg = "#651A84", font="arial, 100")
                    high_score_file = open("high_score.txt", "w")
                    high_score_file.write(str(high_score))
                    high_score_file.close()
                print(counter)
        #text = "{}:{}".format("Push Ups", counter)
        #cv2.putText(image, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # cv2.imshow('MediaPipe Pose', image)
        im = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=im)
        canvas.create_image(0, 0, anchor=NW, image=imgtk)
        labeltime.configure(text=f'Time left: {timer:0.2f}',fg = "white",bg = "#651A84", font="arial, 25")
        window.update()
    
    playsound("timeout.mp3")
    label1.configure(text="Last Score")
    canvas.delete('all')
    cap.release()
    canvas.configure(bg = "#651A84", highlightthickness=0, borderwidth=0)
    labeltime.configure(text="")
    window.update()
    print("this is high")
    print(high)
    def timeUp(result):
        global high
        if result != 0:
            playsound("score.mp3")#for voice output
            playsound(str(result)+".mp3")
            #time.sleep(1)

        if(high):
            #labelBeatHighScore.grid(row=4, column=3, padx=50, )
            playsound("congrats.mp3")#for voice output
            playsound("san-win.mp3")
            #time.sleep(3)

    if timer<=0:
        timeUp(counter)
    last_high = lb[4][1]
    if counter>int(lb[4][1]):
        inputName.grid()
        enter.configure(command=got_name)
        enter.grid()
        window.mainloop()
    else:
        start.configure(command=nxt)
        #start = Button(master=gFrame,fg = "white",bg = "#651A84", font="arial, 25", text = 'START', bd = '5',activebackground='#a66ec4',command = nxt)
        start.grid(row=4, column=2)
        window.mainloop()

    
    
starting()

cv2.destroyAllWindows()

