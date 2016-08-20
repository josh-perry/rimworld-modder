import sys
from PySide import QtGui, QtCore


class BodyDef:
    def __init__(self):
        self.name = "Body Part"


class BodyPartEditor:
    def __init__(self):
        self.vbox = QtGui.QVBoxLayout()

        self.name_input = QtGui.QLineEdit()
        self.name_input.setPlaceholderText('Name')
        self.inside_checkbox = QtGui.QCheckBox('Is inside?')
        self.coverage_slider = QtGui.QSlider()
        self.coverage_slider.setOrientation(QtCore.Qt.Horizontal)

        self.vbox.addWidget(self.name_input)
        self.vbox.addWidget(self.inside_checkbox)
        self.vbox.addWidget(self.coverage_slider)


class BodyDefCreatorUi(QtGui.QWidget):
    def __init__(self):
        super(BodyDefCreatorUi, self).__init__()

        self.body_defs = []

        for x in xrange(0, 4):
            self.body_defs.append(BodyDef())

        self.init()

    def init(self):
        self.setGeometry(300, 300, 825, 550)
        self.setWindowTitle('Rimworld BodyDef Creator')

        self.bodypart_editor = BodyPartEditor()

        self.hbox = QtGui.QHBoxLayout()

        self.body_treeview_model = QtGui.QStandardItemModel()
        self.body_treeview = QtGui.QTreeView()
        self.body_treeview.setModel(self.body_treeview_model)

        for body in self.body_defs:
            item = QtGui.QStandardItem(body.name)
            self.body_treeview_model.appendRow([item])

            item.appendRow(QtGui.QStandardItem("hey"))

        self.hbox.addWidget(self.body_treeview)
        self.editor_vbox = self.bodypart_editor.vbox
        self.hbox.addLayout(self.editor_vbox)

        self.setLayout(self.hbox)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ui = BodyDefCreatorUi()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
