import cv2

def capture_image():
    # Initialize the camera capture object with the cv2.VideoCapture class.
    count = 0
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Wait for key press
        key = cv2.waitKey(1)

        # if the 'c' key is pressed, capture the frame
        if key == ord('c'):
            cv2.imwrite('captured_frame_' + str(count) + '.jpg', frame)
            print("Image captured and saved as 'captured_frame.jpg'")
            count += 1
            
        # if the 'q' key is pressed, break from the loop
        if key == ord('q'):
            print("Exiting...")
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_image()
