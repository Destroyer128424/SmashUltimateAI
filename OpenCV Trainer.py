import os 


#DONT FORGET: Edit the file name you are opening and saving as

def GenerateNegative():

    with open('neg.txt', 'w') as f:
        for filename in os.listdir('Mario/Negatives'):
            f.write('Mario/Negatives' + filename + '\n')


#C:/Users/brady/Downloads/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=Mario/Positives/
#USE THIS TO DRAW SQUARES AROUND POSITIVE IMAGES


#C:/Users/brady/Downloads/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
#Use this to create a vector file from positive txt file



#C:/Users/brady/Downloads/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data Mario/Cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 80 -numNeg 160 -numStages 10
#USE THIS TO TRAIN YOUR MODEL