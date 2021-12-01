id = cv2.VideoCapture(0) 
while (vid.isOpened()): 
    img, frame = vid.read()
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,interpolation = cv2.INTER_CUBIC)
    cv2.imshow(‘Frame', frame) 
    gaussianblur = cv2.GaussianBlur(frame, (5, 5), 0) 
    cv2.imshow('gblur', gaussianblur)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vid.release()
vid.destroyAllWindows() 
