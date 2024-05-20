from PySide6.QtWidgets import QApplication
from charts import Depto2App
import sys

app = QApplication(sys.argv)

window = Depto2App()

window.show()
app.exec()