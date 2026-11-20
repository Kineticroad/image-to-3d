"""Image to 3D 실행 진입점.

사용법 (프로젝트 루트에서):
    python src/main.py             # 메인 윈도우
    python src/main.py settings    # 설정 다이얼로그만 띄우기
    python src/main.py --sample    # 작업 목록에 샘플 JobItem 을 채워서 띄우기
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PySide6.QtWidgets import QApplication

from ui.theme import apply_theme
from ui.windows import MainWindow, SettingsDialog

SAMPLE_JOBS = [
    ("chair_front.png", "in_progress", "진행 중", "62% · 약 1분 남음"),
    ("sneaker_photo.jpg", "succeeded", "완료", "12분 전"),
    ("ceramic_mug.webp", "succeeded", "완료", "어제"),
    ("lamp_side.jpg", "failed", "실패", "크레딧 환불됨 · 어제"),
]


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Image to 3D")
    apply_theme(app)
    args = sys.argv[1:]

    if "settings" in args:
        return SettingsDialog().exec()

    window = MainWindow()
    if "--sample" in args:
        for job in SAMPLE_JOBS:
            window.add_job(*job)
        window.jobListWidget.setCurrentRow(0)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
