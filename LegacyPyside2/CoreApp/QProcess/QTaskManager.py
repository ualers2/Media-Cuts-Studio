import platform
from PySide2.QtGui import QStandardItem, QStandardItemModel, QIcon, QPixmap
from firebase_admin import db
import hashlib
from PySide2.QtCore import QTimer, QThread, Signal
from PySide2.QtWidgets import QPushButton 
import requests

# 🚀 Class to Manage Tasks in Task Control Panel using QThread
class TaskManager(QThread):
    tasks_fetched = Signal(dict)
    new_tasks = Signal(dict)

    def __init__(self, ref_tasks):
        super().__init__()
        self.ref_tasks = ref_tasks
        
    def run(self):
        self.load_tasks_from_firebase()
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_tasks_from_firebase)
        self.timer.start(100000) 

        self.exec_() 

    def add_new_task(self, data):
        self.new_tasks.emit(data)

    def load_tasks_from_firebase(self):
        """
        Busca as tarefas do usuário armazenadas no Firebase e popula a TreeView.
        Cada tarefa pode ter uma lista de datas/horários e o canal do YouTube.
        """
        try:
            tasks_data = self.ref_tasks.get()
        except:
            pass
        
        self.tasks_fetched.emit(tasks_data)
       