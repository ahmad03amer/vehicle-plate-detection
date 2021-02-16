import glob
import os
import cv2
print(cv2.__version__)
def delete_bad_images(dataset_dir):
    anno_dir = "annotation\\"
    images_dir = "images\\"
    with open(dataset_dir + "skipped_images.txt", 'r') as fin:
        data = fin.read().splitlines(False)
        for name in data:
            try:
                os.remove(dataset_dir + anno_dir + name + ".txt")
            except:
                print(name)
                os.remove(dataset_dir + images_dir + name + ".jpg")
    fin.closed()
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def text_to_yolo(file):
    print("test2")
    for file_name in glob.iglob(path, recursive=True):
        name = os.path.splitext(file_name)[0]
        name = os.path.basename(name)
        print(name)
        image = cv2.imread('C:/Users/user/Downloads/PalestinePlateDataSet/images/' + name + '.jpg')
        height, width, channels = image.shape
        with open(file_name, 'r') as f:
            # plateNum = f.readlines()[0]
            data = f.readlines()
        content = data[1].split(' ')
        xmin, ymin, xmax, ymax = content[0], content[1], content[2], content[3]
        w = width
        h = height
        b = (float(xmin), float(xmax), float(ymin), float(ymax))
        bb = convert((w, h), b)

        # print(type(bb))
        newfile = open("C:/Users/user/Downloads/PalestinePlateDataSet/yolo/" + name + ".txt", "w")
        newfile.write('0 ')
        # newfile.write(str(bb))
        for x in bb:
            newfile.write(str(x) + '    ')
        newfile.close()
    print(type(data[1]))


if __name__ == '__main__':
    path = 'C:/Users/user/Downloads/PalestinePlateDataSet/annotation/*.txt'
    dataset_dir = "C:\\Users\\user\\Downloads\\PalestinePlateDataSet\\"
    # to delete a bad quality images
    #delete_bad_images(dataset_dir)
    folder = glob.glob(path)
    text_to_yolo(folder)
    print("Hello World!")

