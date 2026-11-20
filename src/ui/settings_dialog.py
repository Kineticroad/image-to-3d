# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(520, 560)
        SettingsDialog.setMinimumSize(QSize(480, 0))
        SettingsDialog.setModal(True)
        self.dialogLayout = QVBoxLayout(SettingsDialog)
        self.dialogLayout.setSpacing(24)
        self.dialogLayout.setObjectName(u"dialogLayout")
        self.dialogLayout.setContentsMargins(24, 20, 24, 20)
        self.apiKeySectionLayout = QVBoxLayout()
        self.apiKeySectionLayout.setSpacing(8)
        self.apiKeySectionLayout.setObjectName(u"apiKeySectionLayout")
        self.apiKeyTitleLabel = QLabel(SettingsDialog)
        self.apiKeyTitleLabel.setObjectName(u"apiKeyTitleLabel")
        self.apiKeyTitleLabel.setProperty(u"role", u"sectionTitle")

        self.apiKeySectionLayout.addWidget(self.apiKeyTitleLabel)

        self.apiKeyHintLabel = QLabel(SettingsDialog)
        self.apiKeyHintLabel.setObjectName(u"apiKeyHintLabel")
        self.apiKeyHintLabel.setWordWrap(True)
        self.apiKeyHintLabel.setProperty(u"role", u"muted")

        self.apiKeySectionLayout.addWidget(self.apiKeyHintLabel)

        self.apiKeyRowLayout = QHBoxLayout()
        self.apiKeyRowLayout.setSpacing(8)
        self.apiKeyRowLayout.setObjectName(u"apiKeyRowLayout")
        self.apiKeyEdit = QLineEdit(SettingsDialog)
        self.apiKeyEdit.setObjectName(u"apiKeyEdit")
        self.apiKeyEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.apiKeyEdit.setClearButtonEnabled(True)
        self.apiKeyEdit.setProperty(u"role", u"mono")

        self.apiKeyRowLayout.addWidget(self.apiKeyEdit)

        self.showApiKeyButton = QPushButton(SettingsDialog)
        self.showApiKeyButton.setObjectName(u"showApiKeyButton")
        self.showApiKeyButton.setCheckable(True)
        self.showApiKeyButton.setProperty(u"variant", u"secondary")

        self.apiKeyRowLayout.addWidget(self.showApiKeyButton)


        self.apiKeySectionLayout.addLayout(self.apiKeyRowLayout)

        self.testConnectionRowLayout = QHBoxLayout()
        self.testConnectionRowLayout.setSpacing(10)
        self.testConnectionRowLayout.setObjectName(u"testConnectionRowLayout")
        self.testConnectionButton = QPushButton(SettingsDialog)
        self.testConnectionButton.setObjectName(u"testConnectionButton")
        self.testConnectionButton.setProperty(u"variant", u"secondary")

        self.testConnectionRowLayout.addWidget(self.testConnectionButton)

        self.connectionStatusLabel = QLabel(SettingsDialog)
        self.connectionStatusLabel.setObjectName(u"connectionStatusLabel")
        self.connectionStatusLabel.setProperty(u"role", u"secondary")

        self.testConnectionRowLayout.addWidget(self.connectionStatusLabel)

        self.testConnectionSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.testConnectionRowLayout.addItem(self.testConnectionSpacer)

        self.apiKeyDocsLinkLabel = QLabel(SettingsDialog)
        self.apiKeyDocsLinkLabel.setObjectName(u"apiKeyDocsLinkLabel")
        self.apiKeyDocsLinkLabel.setTextFormat(Qt.TextFormat.RichText)
        self.apiKeyDocsLinkLabel.setOpenExternalLinks(True)
        self.apiKeyDocsLinkLabel.setProperty(u"role", u"link")

        self.testConnectionRowLayout.addWidget(self.apiKeyDocsLinkLabel)


        self.apiKeySectionLayout.addLayout(self.testConnectionRowLayout)


        self.dialogLayout.addLayout(self.apiKeySectionLayout)

        self.outputSectionLayout = QVBoxLayout()
        self.outputSectionLayout.setSpacing(8)
        self.outputSectionLayout.setObjectName(u"outputSectionLayout")
        self.outputTitleLabel = QLabel(SettingsDialog)
        self.outputTitleLabel.setObjectName(u"outputTitleLabel")
        self.outputTitleLabel.setProperty(u"role", u"sectionTitle")

        self.outputSectionLayout.addWidget(self.outputTitleLabel)

        self.outputHintLabel = QLabel(SettingsDialog)
        self.outputHintLabel.setObjectName(u"outputHintLabel")
        self.outputHintLabel.setWordWrap(True)
        self.outputHintLabel.setProperty(u"role", u"muted")

        self.outputSectionLayout.addWidget(self.outputHintLabel)

        self.outputRowLayout = QHBoxLayout()
        self.outputRowLayout.setSpacing(8)
        self.outputRowLayout.setObjectName(u"outputRowLayout")
        self.outputDirEdit = QLineEdit(SettingsDialog)
        self.outputDirEdit.setObjectName(u"outputDirEdit")
        self.outputDirEdit.setReadOnly(True)
        self.outputDirEdit.setProperty(u"role", u"mono")

        self.outputRowLayout.addWidget(self.outputDirEdit)

        self.browseOutputDirButton = QPushButton(SettingsDialog)
        self.browseOutputDirButton.setObjectName(u"browseOutputDirButton")
        self.browseOutputDirButton.setProperty(u"variant", u"secondary")

        self.outputRowLayout.addWidget(self.browseOutputDirButton)


        self.outputSectionLayout.addLayout(self.outputRowLayout)


        self.dialogLayout.addLayout(self.outputSectionLayout)

        self.formatSectionLayout = QVBoxLayout()
        self.formatSectionLayout.setSpacing(8)
        self.formatSectionLayout.setObjectName(u"formatSectionLayout")
        self.formatTitleLabel = QLabel(SettingsDialog)
        self.formatTitleLabel.setObjectName(u"formatTitleLabel")
        self.formatTitleLabel.setProperty(u"role", u"sectionTitle")

        self.formatSectionLayout.addWidget(self.formatTitleLabel)

        self.formatHintLabel = QLabel(SettingsDialog)
        self.formatHintLabel.setObjectName(u"formatHintLabel")
        self.formatHintLabel.setWordWrap(True)
        self.formatHintLabel.setProperty(u"role", u"muted")

        self.formatSectionLayout.addWidget(self.formatHintLabel)

        self.formatRowLayout = QHBoxLayout()
        self.formatRowLayout.setSpacing(6)
        self.formatRowLayout.setObjectName(u"formatRowLayout")
        self.glbCheck = QCheckBox(SettingsDialog)
        self.glbCheck.setObjectName(u"glbCheck")
        self.glbCheck.setChecked(True)
        self.glbCheck.setProperty(u"role", u"formatToggle")

        self.formatRowLayout.addWidget(self.glbCheck)

        self.fbxCheck = QCheckBox(SettingsDialog)
        self.fbxCheck.setObjectName(u"fbxCheck")
        self.fbxCheck.setProperty(u"role", u"formatToggle")

        self.formatRowLayout.addWidget(self.fbxCheck)

        self.objCheck = QCheckBox(SettingsDialog)
        self.objCheck.setObjectName(u"objCheck")
        self.objCheck.setProperty(u"role", u"formatToggle")

        self.formatRowLayout.addWidget(self.objCheck)

        self.usdzCheck = QCheckBox(SettingsDialog)
        self.usdzCheck.setObjectName(u"usdzCheck")
        self.usdzCheck.setChecked(True)
        self.usdzCheck.setProperty(u"role", u"formatToggle")

        self.formatRowLayout.addWidget(self.usdzCheck)

        self.stlCheck = QCheckBox(SettingsDialog)
        self.stlCheck.setObjectName(u"stlCheck")
        self.stlCheck.setProperty(u"role", u"formatToggle")

        self.formatRowLayout.addWidget(self.stlCheck)

        self.formatRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formatRowLayout.addItem(self.formatRowSpacer)


        self.formatSectionLayout.addLayout(self.formatRowLayout)


        self.dialogLayout.addLayout(self.formatSectionLayout)

        self.notifySectionLayout = QVBoxLayout()
        self.notifySectionLayout.setSpacing(8)
        self.notifySectionLayout.setObjectName(u"notifySectionLayout")
        self.notifyTitleLabel = QLabel(SettingsDialog)
        self.notifyTitleLabel.setObjectName(u"notifyTitleLabel")
        self.notifyTitleLabel.setProperty(u"role", u"sectionTitle")

        self.notifySectionLayout.addWidget(self.notifyTitleLabel)

        self.notifyRowLayout = QHBoxLayout()
        self.notifyRowLayout.setObjectName(u"notifyRowLayout")
        self.notifyLabel = QLabel(SettingsDialog)
        self.notifyLabel.setObjectName(u"notifyLabel")
        self.notifyLabel.setProperty(u"role", u"secondary")

        self.notifyRowLayout.addWidget(self.notifyLabel)

        self.notifyRowSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.notifyRowLayout.addItem(self.notifyRowSpacer)

        self.notifyOnCompleteCheck = QCheckBox(SettingsDialog)
        self.notifyOnCompleteCheck.setObjectName(u"notifyOnCompleteCheck")
        self.notifyOnCompleteCheck.setChecked(True)
        self.notifyOnCompleteCheck.setProperty(u"role", u"switch")

        self.notifyRowLayout.addWidget(self.notifyOnCompleteCheck)


        self.notifySectionLayout.addLayout(self.notifyRowLayout)


        self.dialogLayout.addLayout(self.notifySectionLayout)

        self.dialogSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dialogLayout.addItem(self.dialogSpacer)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.dialogLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.notifyLabel.setBuddy(self.notifyOnCompleteCheck)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.apiKeyEdit, self.showApiKeyButton)
        QWidget.setTabOrder(self.showApiKeyButton, self.testConnectionButton)
        QWidget.setTabOrder(self.testConnectionButton, self.browseOutputDirButton)
        QWidget.setTabOrder(self.browseOutputDirButton, self.glbCheck)
        QWidget.setTabOrder(self.glbCheck, self.fbxCheck)
        QWidget.setTabOrder(self.fbxCheck, self.objCheck)
        QWidget.setTabOrder(self.objCheck, self.usdzCheck)
        QWidget.setTabOrder(self.usdzCheck, self.stlCheck)
        QWidget.setTabOrder(self.stlCheck, self.notifyOnCompleteCheck)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.apiKeyTitleLabel.setText(QCoreApplication.translate("SettingsDialog", u"Meshy API \ud0a4", None))
        self.apiKeyHintLabel.setText(QCoreApplication.translate("SettingsDialog", u"\ud0a4\ub294 OS \ubcf4\uc548 \uc800\uc7a5\uc18c(macOS \ud0a4\uccb4\uc778 / Windows \uc790\uaca9 \uc99d\uba85 \uad00\ub9ac\uc790)\uc5d0 keyring\uc73c\ub85c \ubcf4\uad00\ub418\uba70 \ud30c\uc77c\ub85c \ub0a8\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.", None))
        self.apiKeyEdit.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"msy_\u2026", None))
        self.showApiKeyButton.setText(QCoreApplication.translate("SettingsDialog", u"\ud45c\uc2dc", None))
#if QT_CONFIG(tooltip)
        self.testConnectionButton.setToolTip(QCoreApplication.translate("SettingsDialog", u"\uc794\uc561 \uc870\ud68c(GET /openapi/v1/balance)\ub85c \ud0a4\ub97c \ud655\uc778\ud569\ub2c8\ub2e4. \ud06c\ub808\ub527\uc774 \ub4e4\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.testConnectionButton.setText(QCoreApplication.translate("SettingsDialog", u"\uc5f0\uacb0 \ud14c\uc2a4\ud2b8", None))
        self.connectionStatusLabel.setText("")
        self.apiKeyDocsLinkLabel.setText(QCoreApplication.translate("SettingsDialog", u"<a href=\"https://docs.meshy.ai/api/authentication\" style=\"color:#9D85FF; text-decoration:none;\">API \ud0a4 \uc548\ub0b4 \u2197</a>", None))
        self.outputTitleLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc800\uc7a5 \uc704\uce58", None))
        self.outputHintLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc644\ub8cc\ub41c \ubaa8\ub378\uc740 \uc791\uc5c5\ubcc4 \ud3f4\ub354\uc5d0 \uc790\ub3d9\uc73c\ub85c \uc800\uc7a5\ub429\ub2c8\ub2e4.", None))
        self.outputDirEdit.setText(QCoreApplication.translate("SettingsDialog", u"~/Documents/MeshyDesktop", None))
        self.browseOutputDirButton.setText(QCoreApplication.translate("SettingsDialog", u"\ubcc0\uacbd\u2026", None))
        self.formatTitleLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc790\ub3d9 \ub2e4\uc6b4\ub85c\ub4dc \ud615\uc2dd", None))
        self.formatHintLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud55c \ud615\uc2dd\uacfc \uc378\ub124\uc77c\uc744 \uc644\ub8cc \uc989\uc2dc \ub0b4\ub824\ubc1b\uc2b5\ub2c8\ub2e4. (\uc11c\ubc84 \ubcf4\uad00 3\uc77c)", None))
        self.glbCheck.setText(QCoreApplication.translate("SettingsDialog", u"GLB", None))
        self.fbxCheck.setText(QCoreApplication.translate("SettingsDialog", u"FBX", None))
        self.objCheck.setText(QCoreApplication.translate("SettingsDialog", u"OBJ", None))
        self.usdzCheck.setText(QCoreApplication.translate("SettingsDialog", u"USDZ", None))
        self.stlCheck.setText(QCoreApplication.translate("SettingsDialog", u"STL", None))
        self.notifyTitleLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc54c\ub9bc", None))
        self.notifyLabel.setText(QCoreApplication.translate("SettingsDialog", u"\uc791\uc5c5\uc774 \ub05d\ub098\uba74 \uc2dc\uc2a4\ud15c \uc54c\ub9bc \ubcf4\ub0b4\uae30", None))
        self.notifyOnCompleteCheck.setText("")
    # retranslateUi

