import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sun",
             (100,80),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
            )

cv2.putText(img,
            "Mercury",
             (110,180),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Venus",
             (190,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Earth",
             (300,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Mars",
             (400,270),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "Jupiter",
             (500,90),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )            
            
cv2.putText(img,
            "Saturn",
             (720,110),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             ) 

cv2.putText(img,
            "Uranus",
             (950,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.putText(img,
            "Neptune",
             (1080,130),
             cv2.FONT_HERSHEY_COMPLEX,
             0.5,
             (255,255,255)
             )

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)