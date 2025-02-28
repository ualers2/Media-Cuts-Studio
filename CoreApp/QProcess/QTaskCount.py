from firebase_admin import db
from PySide2.QtCore import Signal, QTimer, QThread

# 🚀 Class for accounting and categorizing tasks using QThread
class CountTasks(QThread):
    Tasks_Created_signal = Signal(int)
    Tasks_Running_signal = Signal(int)
    Tasks_Completed_signal = Signal(int)
    def __init__(self, ui, update_custommodals_SuccessModal,  app1, email_user):
        super().__init__()
        self.ui = ui
        self.update_custommodals_SuccessModal = update_custommodals_SuccessModal
        self.app1 = app1
        self.email_user = email_user
        self.ref_tasks = db.reference(f'save_tasks_users/task/{self.email_user}', app=self.app1)
        self.count_task()

    def run(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.count_task)
        self.timer.start(100000) 
        self.exec_() 

    def count_task(self):
        """
        Percorre todas as tarefas e contabiliza os estados "Created", "Running" e "Completed".
        Emite sinais para atualizar os contadores.
        """
        task_counts = {"Created": 0, "Running": 0, "Completed": 0}
        tasks = self.ref_tasks.get()
        if tasks:
            for task_id, task_data in tasks.items():
                status = task_data.get("status")
                if status in task_counts:
                    task_counts[status] += 1
        self.Tasks_Created_signal.emit(task_counts["Created"])
        self.Tasks_Running_signal.emit(task_counts["Running"])
        self.Tasks_Completed_signal.emit(task_counts["Completed"])
