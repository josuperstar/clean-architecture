import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from clean_architecture.frameworks.database.sqllite.sqllite_database import SqlLiteDatabase
from clean_architecture.frameworks.database.mysql.mysql_database import MySqlDatabase
from clean_architecture.adapters.controllers.shot_controller import *


class ListWidget(QListWidget):
    def clicked(self, item):
        shot = item.data(Qt.UserRole)
        print(shot)
        QMessageBox.information(self, "Shot Information",
                                "title: {} \ndescription: {}".format(shot.title, shot.description))


class QtShotApplication(object):
    def __init__(self, database):
        app = QApplication(sys.argv)
        listWidget = ListWidget()

        shot_controller = ShotController(database)
        list_of_presenters = shot_controller.get_shot_list()

        font = QFont('arial')

        listWidget.resize(400, 320)
        for post in list_of_presenters:
            item = QListWidgetItem(post.title)
            item.setForeground(QColor(post.title_color))
            item.setData(Qt.UserRole, post)
            font.setPointSize(15)
            item.setFont(font)
            listWidget.addItem(item)

        listWidget.setWindowTitle('QListwidget Example')
        listWidget.itemClicked.connect(listWidget.clicked)

        listWidget.show()
        sys.exit(app.exec_())


if __name__ == '__main__':

    database = SqlLiteDatabase()
    if len(sys.argv) == 2:
        database_name = sys.argv[1]
        if database_name == 'mysql':
            database = MySqlDatabase()

    qt_application = QtShotApplication(database)




