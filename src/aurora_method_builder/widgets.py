from PySide6.QtGui import QWheelEvent
from PySide6.QtWidgets import QComboBox


class NoScrollComboBox(QComboBox):
    """Prevent accidental value changes while scrolling a form."""

    def wheelEvent(self, event: QWheelEvent) -> None:
        event.ignore()
