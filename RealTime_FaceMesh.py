import cv2
import Face_Mesh_Module as fm
import time

cap = cv2.VideoCapture('ResizeVdos/ResizeV8.mp4')
pre_time = 0
detector = fm.Fash_Mesh()
while True:
    succes, frame = cap.read()
    frame, faces = detector.findFace(frame)
    if len(faces) != 0:
        print(len(faces))

    current_time = time.time()
    fps = 1 / (current_time-pre_time)
    pre_time = current_time

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

    # FPS Box
    start_point = (0, 0)
    end_point = (102, 32)
    color = (255, 255, 255)
    thickness = -1

    FPS_Box = cv2.rectangle(
        frame, start_point, end_point, color, thickness)

    cv2.putText(
        FPS_Box,
        str(int(fps)),
        (31, 26),
        font, 1,
        (255, 200, 0),
        2
    )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(10) == ord('0'):
        break

cap.release()
cv2.destroyAllWindows()
