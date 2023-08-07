import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from adapters.sql_lite.sql_adapter import SqlGateway
from clean_architecture.adapters.presenters.shot import ShotPresenter
from clean_architecture.use_cases.list_post_use_case import ListPostUseCases


def boundary_to_presenter(boundary):
    presenter = ShotPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.description = boundary.description
    presenter.title_size = 'h3'
    presenter.title_is_correct = boundary.title_is_correct
    return presenter


class ListWidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "ListWidget: " + item.text())


if __name__ == '__main__':
    database = SqlGateway()
    app = QApplication(sys.argv)
    listWidget = ListWidget()

    list_post = ListPostUseCases(database)
    posts = list_post.execute()
    list_of_presenters = list()
    for post in posts:
        presenter = boundary_to_presenter(post)
        list_of_presenters.append(presenter)

    font = QFont('arial')

    listWidget.resize(400, 320)
    for post in list_of_presenters:
        item = QListWidgetItem(post.title)
        item.setForeground(QColor(post.title_color))
        font.setPointSize(15)
        item.setFont(font)
        listWidget.addItem(item)


    listWidget.setWindowTitle('QListwidget Example')
    listWidget.itemClicked.connect(listWidget.clicked)

    listWidget.show()
    sys.exit(app.exec_())
