import cv2
import numpy


def getimg(name_of_movi, jump_in_second):
    """
        Récupère des images à partir d'une vidéo et retourne une liste de ces images 
    """

    videocap = cv2.VideoCapture(name_of_movi)
    jump_in_frame = videocap.get(cv2.CAP_PROP_FPS)*jump_in_second
    tab_of_image = []

    last_mille_frame = 0

    success, image = videocap.read()
    pos_frame = videocap.get(cv2.CAP_PROP_POS_FRAMES)

    while pos_frame == videocap.get(cv2.CAP_PROP_POS_FRAMES):
        success, image = videocap.read()
        if success:
            pos_frame = videocap.get(cv2.CAP_PROP_POS_FRAMES)
            tab_of_image.append(image)

            if pos_frame // 1000 != last_mille_frame:
                print (str(pos_frame)+" frame")
                last_mille_frame = pos_frame // 1000
            
            pos_frame += jump_in_frame
            videocap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame)

        else:
            pos_frame +=1.0
            videocap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame)
            print ("frame is fail")
    
    return tab_of_image


def resize_tad_of_imge(tab_of_image, width, height):
    """
        Redimensionne les images d'une liste et retourne une liste d'images
    """

    resize_tab = []
    dim = (width, height)

    for image in tab_of_image:
        resize_tab.append(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    
    return resize_tab


def stack_image(tab_of_image):
    """
        Crée une image qui est un empilement d'une liste d'images
    """
    
    stack = tab_of_image[0]
    tab_of_image.pop(0)

    for image in tab_of_image:
        stack = numpy.concatenate((stack, image), axis=1)
    
    return stack


if __name__ == "__main__":
    
    import sys
    import time

    if len(sys.argv) < 5:
        print("Error missing argument \nLes arguments attendus son: \nNom du fichier video \nIntervale entre 2 échantillons \nLargeur des échantillons \nHauteur des echantillons")
    
    else:
        print('Start')
        start = time.time()

        tab_of_image = []

        print('Start get image')
        tab_of_image = getimg(sys.argv[1], float(sys.argv[2]))
        print('Fin get image')

        print('Start resize')
        tab_of_image = resize_tad_of_imge(tab_of_image, int(sys.argv[3]), int(sys.argv[4]))
        print('Fin resize')
        
        print('Start stack')
        image = stack_image(tab_of_image)
        print('Fin stack')

        name = sys.argv[1].split(".")
        cv2.imwrite(name[0]+".jpeg", image)
        
        end = time.time()
        print("Fin", end - start)