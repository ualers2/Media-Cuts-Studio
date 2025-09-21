
########################################################################
# IMPORT Libs 

try:

    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings, QWebEngineScript

except ImportError as e:
    print(f"Erro ao importar bibliotecas: {e}")
    
########################################################################


class PreviewWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.original_pixmap = QPixmap(image_path)
        self.setMinimumSize(200, 200)
    
    def setImage(self, image_path):
        """Atualiza a imagem e redesenha o widget."""
        self.original_pixmap = QPixmap(image_path)
        self.update()  # Solicita o redesenho do widget
    
    def paintEvent(self, event):
        painter = QPainter(self)
        # Redimensiona a imagem para caber no widget mantendo a proporção
        scaled_pixmap = self.original_pixmap.scaled(
            self.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        # Centraliza a imagem
        x = (self.width() - scaled_pixmap.width()) // 2
        y = (self.height() - scaled_pixmap.height()) // 2
        painter.drawPixmap(x, y, scaled_pixmap)
