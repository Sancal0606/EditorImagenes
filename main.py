from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QFileDialog
import os

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
    files = os.listdir(workdir)
    filter_files = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                filter_files.append(file)
    list_files.addItems(filter_files)

btn_dir.clicked.connect(choose_folder)

win.show()
app.exec()