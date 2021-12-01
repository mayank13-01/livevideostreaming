id = cv2.VideoCapture(0)
while (vid.isOpened()): 
    img, frame = vid.read() 
    frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,interpolation = cv2.INTER_CUBIC)
    cv2.imshow('Frame', frame) 
    edge_detect = cv2.Canny(frame, 100, 200) 
    cv2.imshow('Edge_Detect', edge_detect)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
vid.release() 
vid.destroyAllWindows() 
