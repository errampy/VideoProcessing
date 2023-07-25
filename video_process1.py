import cv2

cap = cv2.VideoCapture(0)# if you want to read from folder the pass video path
fourcc=cv2.VideoWriter_fourcc(*'XVID')
# creating video writter class
outer = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))
print(cap)
print(cap.isOpened())
while True:
    ret,frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        outer.write(frame)
        
        # if frame avaialbe then True in ret valriable and frame will come in frame variable
        #cv2.imshow('frame',frame)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('You press q button')
            break
    else:
        break
cap.release()
outer.release()
cv2.destroyAllWindows()

