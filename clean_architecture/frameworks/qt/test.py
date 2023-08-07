import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from clean_architecture.adapters.sql_adapter import SqlGateway
from clean_architecture.adapters.presenters.post import PostPresenter
from clean_architecture.use_cases.list_post_use_case import ListPostUseCases

def boundary_to_presenter(boundary):
    presenter = PostPresenter()
    presenter.id = boundary.id
    presenter.title = boundary.title
    presenter.content = boundary.content
    presenter.title_size = 'h3'
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

    listWidget.resize(300, 120)
    for post in list_of_presenters:
        listWidget.addItem(post.title)

    listWidget.setWindowTitle('QListwidget Example')
    listWidget.itemClicked.connect(listWidget.clicked)

    listWidget.show()
    sys.exit(app.exec_())
