"""Image to 3D 다크 테마 로더

styles/dark.qss 를 읽어 @ICONS@ 자리표시자를 icons 폴더의 절대 경로로 바꾼 뒤
QApplication 에 적용했다.
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QAbstractSpinBox, QApplication, QWidget

UI_DIR = Path(__file__).resolve().parent
QSS_PATH = UI_DIR / "styles" / "dark.qss"
ICONS_DIR = UI_DIR / "icons"


def load_stylesheet() -> str:
    qss = QSS_PATH.read_text(encoding="utf-8")
    return qss.replace("@ICONS@", ICONS_DIR.as_posix())


def apply_theme(app: QApplication) -> None:
    app.setStyle("Fusion")  # 플랫폼마다 다른 기본 스타일 대신 QSS 가 그대로 먹히도록
    app.setStyleSheet(load_stylesheet())


def apply_mono_font(root: QWidget) -> None:
    """role=mono 인 위젯에 시스템 고정폭 글꼴을 적용"""
    mono = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
    for widget in root.findChildren(QWidget):
        if widget.property("role") == "mono":
            current = widget.font()
            font = QFont(mono)
            if current.pixelSize() > 0:  # QSS 가 px 단위로 크기를 지정한 경우
                font.setPixelSize(current.pixelSize())
            elif current.pointSize() > 0:
                font.setPointSize(current.pointSize())
            widget.setFont(font)


def polish(root: QWidget) -> None:
    """.ui 를 로드한 직후 호출: QSS 만으로 안 되는 부분을 코드로 보정"""
    apply_mono_font(root)
    # 버튼 없는 스핀박스는 QSS padding 이 내부 입력칸에 적용되지 않아 여백을 직접 부여한다
    for spin in root.findChildren(QAbstractSpinBox):
        spin.lineEdit().setTextMargins(10, 0, 10, 0)


def refresh_style(widget: QWidget) -> None:
    """status 같은 동적 속성을 바꾼 뒤 QSS 를 다시 적용"""
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    widget.update()
