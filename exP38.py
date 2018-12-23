import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array(
    [
        [-1,-1,-1],
        [-1,8,-1],  #8+(-1)*8 = 0
        [-1,-1,-1],
    ]
)

kernel_5x5 = np.array(
    [
        [-1,-1,-1,-1,-1],
        [-1, 1, 2, 1,-1],
        [-1, 2, 4, 2,-1], #同理　，　之和为 0
        [-1, 1, 2, 1,-1],
        [-1,-1,-1,-1,-1],
    ]
)

img = cv2.imread('./buzz.jpg',0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (11,11) , 0 )
g_hpf = img - blurred

while True:
    key = input("""
    ----------
    k3
    k5
    g_hpf
    ----------

    please input one of the above words >:""")

    if key == "k3":
        cv2.imshow("3x3",k3)
        cv2.waitKey()
    
    elif key == "k5":
        cv2.imshow("5x5",k5)
        cv2.waitKey()

    elif key == "g_hpf":
        cv2.imshow("g_hpf",g_hpf)
        cv2.waitKey()
        
    else:
        print("""
                     你真是太调皮了！
                        /´ ¯/)
                       /´ ¯/)
                      /´ ¯/)
                     /´ ¯/) 
                    /¯ ../ 
                   /     / 
             /´. ¯/'    '/´¯.`·¸ 
         /'/     /     /     /     ¯\ 
        (  /  ')    ')  ')  ')  ')  ')
         \                          / 
          \                 _.·´   /
            \     　嘻嘻         ( /   
             \      D:)         （   
              \                  （
        
        """)


