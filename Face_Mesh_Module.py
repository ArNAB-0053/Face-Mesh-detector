import cv2
import mediapipe as mp
import time

class Fash_Mesh():
    def __init__(
            self,
            static_image_mode=False,
            max_num_faces=2,
            refine_landmarks=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        ):
        self.static_image_mode = static_image_mode
        self.max_num_faces = max_num_faces
        self.refine_landmarks = refine_landmarks
        self.min_detection_confidence = min_detection_confidence   
        self.min_tracking_confidence = min_tracking_confidence

        self.mpFashMesh = mp.solutions.face_mesh
        self.FaceMesh = self.mpFashMesh.FaceMesh(
            self.static_image_mode,
            self.max_num_faces,
            self.refine_landmarks,
            self.min_detection_confidence,  
            self.min_tracking_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 0, color = (0, 255, 0))

    def findFace(self, frame, draw = True):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.FaceMesh.process(frameRGB)

        faces = []
        if self.results.multi_face_landmarks:
            for faceLMS in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, faceLMS, self.mpFashMesh.FACEMESH_TESSELATION,
                                        self.drawSpec, self.drawSpec)
                    
                face = []
                for id, lm in enumerate(faceLMS.landmark):
                    # print(lm)
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w) , int(lm.y*h)
                    face.append([cx, cy])
                    # print(id, cx, cy)   
                faces.append(face)
            return frame, faces