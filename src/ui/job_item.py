# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_item.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_JobItem(object):
    def setupUi(self, JobItem):
        if not JobItem.objectName():
            JobItem.setObjectName(u"JobItem")
        JobItem.resize(244, 60)
        JobItem.setMinimumSize(QSize(0, 60))
        JobItem.setMaximumSize(QSize(16777215, 60))
        self.jobItemLayout = QHBoxLayout(JobItem)
        self.jobItemLayout.setSpacing(10)
        self.jobItemLayout.setObjectName(u"jobItemLayout")
        self.jobItemLayout.setContentsMargins(10, 8, 10, 8)
        self.thumbnailLabel = QLabel(JobItem)
        self.thumbnailLabel.setObjectName(u"thumbnailLabel")
        self.thumbnailLabel.setMinimumSize(QSize(40, 40))
        self.thumbnailLabel.setMaximumSize(QSize(40, 40))
        self.thumbnailLabel.setScaledContents(True)
        self.thumbnailLabel.setProperty(u"role", u"thumbnail")

        self.jobItemLayout.addWidget(self.thumbnailLabel)

        self.jobMetaLayout = QVBoxLayout()
        self.jobMetaLayout.setSpacing(4)
        self.jobMetaLayout.setObjectName(u"jobMetaLayout")
        self.nameLabel = QLabel(JobItem)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setProperty(u"role", u"itemTitle")

        self.jobMetaLayout.addWidget(self.nameLabel)

        self.jobSubLayout = QHBoxLayout()
        self.jobSubLayout.setSpacing(8)
        self.jobSubLayout.setObjectName(u"jobSubLayout")
        self.statusChipLabel = QLabel(JobItem)
        self.statusChipLabel.setObjectName(u"statusChipLabel")
        self.statusChipLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statusChipLabel.setProperty(u"role", u"chip")
        self.statusChipLabel.setProperty(u"status", u"succeeded")

        self.jobSubLayout.addWidget(self.statusChipLabel)

        self.detailLabel = QLabel(JobItem)
        self.detailLabel.setObjectName(u"detailLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailLabel.sizePolicy().hasHeightForWidth())
        self.detailLabel.setSizePolicy(sizePolicy)
        self.detailLabel.setProperty(u"role", u"muted")

        self.jobSubLayout.addWidget(self.detailLabel)


        self.jobMetaLayout.addLayout(self.jobSubLayout)


        self.jobItemLayout.addLayout(self.jobMetaLayout)


        self.retranslateUi(JobItem)

        QMetaObject.connectSlotsByName(JobItem)
    # setupUi

    def retranslateUi(self, JobItem):
        JobItem.setWindowTitle(QCoreApplication.translate("JobItem", u"Job Item", None))
        self.nameLabel.setText(QCoreApplication.translate("JobItem", u"sneaker_photo.jpg", None))
        self.statusChipLabel.setText(QCoreApplication.translate("JobItem", u"\uc644\ub8cc", None))
        self.detailLabel.setText(QCoreApplication.translate("JobItem", u"12\ubd84 \uc804", None))
    # retranslateUi

