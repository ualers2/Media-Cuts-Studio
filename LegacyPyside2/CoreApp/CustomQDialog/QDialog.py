from CoreApp.CustomQDialog.QCustomQDialog import QCustomQDialog
from PySide2 import QtGui

def slot_accepted_button(custom_dialog):
    custom_dialog.accept()

def slot_rejected_button(custom_dialog):
    custom_dialog.reject()

def custom_dialog(yesButtonText, cancelButtonText, myParentWidget, yourNewWidget, handle_accepted, handle_rejected, title="", description=""):

    if title == "" and description == "":
        custom_dialog = QCustomQDialog(
            padding=20,
            margin=60,
            yesButtonIcon=QtGui.QIcon(":/feather/icons/feather/save.png"),
            cancelButtonIcon=QtGui.QIcon(":/material_design/icons/material_design/close.png"),
            yesButtonText=yesButtonText,
            cancelButtonText=cancelButtonText,
            animationDuration=500,
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            parent=myParentWidget,
            addWidget=yourNewWidget #append another widget or widget container to the dialog
        )
    else:
        custom_dialog = QCustomQDialog(
            title=title,
            description=description,
            padding=20,
            margin=60,
            yesButtonIcon=QtGui.QIcon(":/feather/icons/feather/save.png"),
            cancelButtonIcon=QtGui.QIcon(":/material_design/icons/material_design/close.png"),
            yesButtonText=yesButtonText,
            cancelButtonText=cancelButtonText,
            animationDuration=500,
            showYesButton=True,
            showCancelButton=True,
            setModal=True,
            frameless=True,
            windowMovable=True,
            parent=myParentWidget,
            addWidget=yourNewWidget #append another widget or widget container to the dialog
        )
    # alternative:
    # to append another widget or widget container to the dialog
    custom_dialog.addWidget(yourNewWidget)

    custom_dialog.show()
    
    # accepted_button.clicked.connect(lambda: slot_accepted_button(custom_dialog))

    # rejected_button.clicked.connect(lambda: slot_rejected_button(custom_dialog))

    # events
    custom_dialog.accepted.connect(handle_accepted)
    custom_dialog.rejected.connect(handle_rejected)
        