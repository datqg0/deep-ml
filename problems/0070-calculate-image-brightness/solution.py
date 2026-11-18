
def calculate_brightness(img):
    # Write your code here
    if(len(img)==0):
        return -1
    isok =True
    cstl = len(img[0])
    sum=0
    for i in range (len(img)):
        if(len(img[i])!=cstl):
            return -1
        for j in range (len(img[0])):
            if(img[i][j]<0 or img[i][j]>255 ):
                return -1
            sum+=img[i][j]
        
    return sum/(len(img)*len(img[0]))
