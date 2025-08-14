from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from PIL import Image, ImageFilter


app = QApplication([])
win = QWidget()
win.resize(700,400)

main_layout = QHBoxLayout()

#file explorer
file_explorer = QVBoxLayout()
btn_dir = QPushButton("Carpeta")
list_files = QListWidget()

file_explorer.addWidget(btn_dir)
file_explorer.addWidget(list_files)

main_layout.addLayout(file_explorer)

#Editor
editor = QVBoxLayout()
lbl_image = QLabel("Image")
lbl_image.setFixedHeight(350)

editor.addWidget(lbl_image)

#Editor -> acciones
actions = QHBoxLayout()
btn_left = QPushButton("Izquierda")
btn_right = QPushButton("Derecha")
btn_mirror = QPushButton("Espejo")
btn_sharp = QPushButton("Nitidez")
btn_bw = QPushButton("BN")

actions.addWidget(btn_left)
actions.addWidget(btn_right)
actions.addWidget(btn_mirror)
actions.addWidget(btn_sharp)
actions.addWidget(btn_bw)

editor.addLayout(actions)

main_layout.addLayout(editor)

win.setLayout(main_layout)

#Variables globales
dir = ""
extensions = [".jpg", ".png"]

#Funcionalidad
def choose_folder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    image_processor.workdir = workdir
    files = os.listdir(workdir)
    filter_files = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                filter_files.append(file)
    list_files.addItems(filter_files)

btn_dir.clicked.connect(choose_folder)

class ImageProcessor():
    def __init__(self):
        self.image_path = ""
        self.image_name = ""
        self.workdir = ""
        self.image = ""

    def show_image(self,filename):
        self.image_name = filename
        self.image_path = os.path.join(self.workdir, filename)
        pixmapImage = QPixmap(self.image_path)
        w,h = lbl_image.width(), lbl_image.height()
        pixmapImage = pixmapImage.scaled(w,h,Qt.KeepAspectRatio)
        lbl_image.setPixmap(pixmapImage)
        self.image = Image.open(self.image_path)
        print(self.workdir)

    def do_bw(self):
        self.image = self.image.convert('L')
        bw_name = self.image_name[:-4] + "_bw" + self.image_name[-4:]
        new_path = self.workdir+ "/" + bw_name
        self.image.save(new_path)
        list_files.addItem(bw_name)
        self.show_image(bw_name)

    def do_rot_right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        bw_name = self.image_name[:-4] + "_rotRight" + self.image_name[-4:]
        new_path = self.workdir+ "/" + bw_name
        self.image.save(new_path)
        list_files.addItem(bw_name)
        self.show_image(bw_name)

    def do_rot_left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        bw_name = self.image_name[:-4] + "_rotLeft" + self.image_name[-4:]
        new_path = self.workdir+ "/" + bw_name
        self.image.save(new_path)
        list_files.addItem(bw_name)
        self.show_image(bw_name)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        bw_name = self.image_name[:-4] + "_blur" + self.image_name[-4:]
        new_path = self.workdir+ "/" + bw_name
        self.image.save(new_path)
        list_files.addItem(bw_name)
        self.show_image(bw_name)

    def do_mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        bw_name = self.image_name[:-4] + "_mirror" + self.image_name[-4:]
        new_path = self.workdir+ "/" + bw_name
        self.image.save(new_path)
        list_files.addItem(bw_name)
        self.show_image(bw_name)

def open_image():
    filename = list_files.currentItem().text()
    image_processor.show_image(filename)

def action_bw():
    image_processor.do_bw()

def action_rot_right():
    image_processor.do_rot_right()

def action_rot_left():
    image_processor.do_rot_left()

def action_blur():
    image_processor.do_blur()

def action_mirror():
    image_processor.do_mirror()

image_processor = ImageProcessor()

list_files.currentRowChanged.connect(open_image)

btn_bw.clicked.connect(action_bw)
btn_right.clicked.connect(action_rot_right)
btn_left.clicked.connect(action_rot_left)
btn_sharp.clicked.connect(action_blur)
btn_mirror.clicked.connect(action_mirror)

win.show()
app.exec()