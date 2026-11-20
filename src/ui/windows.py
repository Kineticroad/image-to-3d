"""pyside6-uic 로 변환한 Ui_* 클래스를 실제 창(위젯)으로 감싸는 모듈

main_window.py / settings_dialog.py / job_item.py 는 .ui 를 다시 변환하면 덮어써지므로
직접 수정하지 않고, 여기서 상속해 화면 동작을 구현
"""

from __future__ import annotations

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QListWidgetItem,
    QMainWindow,
    QWidget,
)

from ui.job_item import Ui_JobItem
from ui.main_window import Ui_MainWindow
from ui.settings_dialog import Ui_SettingsDialog
from ui.theme import polish, refresh_style


def set_chip(label: QLabel, status: str, text: str) -> None:
    """상태 칩 문구와 status 속성(pending | in_progress | succeeded | failed)을 바꿉니다"""
    label.setText(text)
    label.setProperty("status", status)
    refresh_style(label)


class JobItemWidget(QWidget, Ui_JobItem):
    """작업 목록(jobListWidget)의 한 줄"""

    ROW_HEIGHT = 60

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        polish(self)

    def set_job(self, name: str, status: str, chip_text: str, detail: str) -> None:
        self.nameLabel.setText(name)
        self.detailLabel.setText(detail)
        set_chip(self.statusChipLabel, status, chip_text)


class SettingsDialog(QDialog, Ui_SettingsDialog):
    """설정 다이얼로그"""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        # 표준 버튼 문구는 Qt 번역(qtbase_ko)을 로드하지 않으면 영어로 나오므로 직접 지정합니다.
        save = self.buttonBox.button(QDialogButtonBox.StandardButton.Save)
        cancel = self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel)
        save.setText("저장")
        cancel.setText("취소")
        save.setProperty("variant", "primary")
        refresh_style(save)

        self.showApiKeyButton.toggled.connect(self._toggle_api_key_visible)
        polish(self)

    def _toggle_api_key_visible(self, visible: bool) -> None:
        mode = QLineEdit.EchoMode.Normal if visible else QLineEdit.EchoMode.Password
        self.apiKeyEdit.setEchoMode(mode)


class MainWindow(QMainWindow, Ui_MainWindow):
    """메인 윈도우"""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.mainSplitter.setSizes([264, 656, 360])

        self.actionSettings.triggered.connect(self.open_settings)
        self.settingsButton.clicked.connect(self.open_settings)
        self.actionQuit.triggered.connect(self.close)

        polish(self)

    def open_settings(self) -> None:
        SettingsDialog(self).exec()

    def add_job(self, name: str, status: str, chip_text: str, detail: str) -> JobItemWidget:
        """작업 목록에 JobItemWidget 한 줄을 추가"""
        row = JobItemWidget()
        row.set_job(name, status, chip_text, detail)
        item = QListWidgetItem(self.jobListWidget)
        item.setSizeHint(QSize(0, JobItemWidget.ROW_HEIGHT))
        self.jobListWidget.setItemWidget(item, row)
        self.jobCountLabel.setText(str(self.jobListWidget.count()))
        return row
