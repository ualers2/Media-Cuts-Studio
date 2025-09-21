
########################################################################
# IMPORT Custom widgets
from Custom_Widgets.QCustomModals import QCustomModals
########################################################################

def update_custommodals_Warning(description, title="Information",  pos='top-right', parent="self.ui.centralwidget"):

    myModal = QCustomModals.WarningModal(
        title=title, 
        parent=parent,
        position=pos,
        modalIcon=":/web_icons/icons/web_icons/rectangle-3370.png",
        description=description,
        isClosable=False,
        duration=5000
    )
    myModal.show()