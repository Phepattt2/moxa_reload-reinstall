from datetime import datetime

def getDatetimeFromImageName(imageName):
    imageName = imageName.split('_')[3]
    datetime_object = datetime.strptime(imageName, '%Y-%m-%d-%H-%M-%S-%f')
    return datetime_object
