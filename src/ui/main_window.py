# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(1080, 680))
        self.actionOpenImage = QAction(MainWindow)
        self.actionOpenImage.setObjectName(u"actionOpenImage")
        self.actionOpenOutputFolder = QAction(MainWindow)
        self.actionOpenOutputFolder.setObjectName(u"actionOpenOutputFolder")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionSettings.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionOpenDocs = QAction(MainWindow)
        self.actionOpenDocs.setObjectName(u"actionOpenDocs")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setMenuRole(QAction.MenuRole.AboutRole)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralLayout = QVBoxLayout(self.centralWidget)
        self.centralLayout.setSpacing(0)
        self.centralLayout.setObjectName(u"centralLayout")
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.headerBar = QFrame(self.centralWidget)
        self.headerBar.setObjectName(u"headerBar")
        self.headerBar.setMinimumSize(QSize(0, 48))
        self.headerBar.setMaximumSize(QSize(16777215, 48))
        self.headerLayout = QHBoxLayout(self.headerBar)
        self.headerLayout.setSpacing(12)
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLayout.setContentsMargins(16, 8, 12, 8)
        self.appTitleLabel = QLabel(self.headerBar)
        self.appTitleLabel.setObjectName(u"appTitleLabel")
        self.appTitleLabel.setProperty(u"role", u"appTitle")

        self.headerLayout.addWidget(self.appTitleLabel)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.creditBadgeLabel = QLabel(self.headerBar)
        self.creditBadgeLabel.setObjectName(u"creditBadgeLabel")
        self.creditBadgeLabel.setProperty(u"role", u"creditBadge")

        self.headerLayout.addWidget(self.creditBadgeLabel)

        self.settingsButton = QPushButton(self.headerBar)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setProperty(u"variant", u"ghost")

        self.headerLayout.addWidget(self.settingsButton)


        self.centralLayout.addWidget(self.headerBar)

        self.mainSplitter = QSplitter(self.centralWidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.mainSplitter.setHandleWidth(1)
        self.mainSplitter.setChildrenCollapsible(False)
        self.sidebar = QFrame(self.mainSplitter)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(240, 0))
        self.sidebar.setMaximumSize(QSize(360, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setSpacing(8)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(10, 16, 10, 16)
        self.sidebarHeaderLayout = QHBoxLayout()
        self.sidebarHeaderLayout.setObjectName(u"sidebarHeaderLayout")
        self.sidebarHeaderLayout.setContentsMargins(6, -1, 6, -1)
        self.jobListTitleLabel = QLabel(self.sidebar)
        self.jobListTitleLabel.setObjectName(u"jobListTitleLabel")
        self.jobListTitleLabel.setProperty(u"role", u"sectionTitle")

        self.sidebarHeaderLayout.addWidget(self.jobListTitleLabel)

        self.sidebarHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sidebarHeaderLayout.addItem(self.sidebarHeaderSpacer)

        self.jobCountLabel = QLabel(self.sidebar)
        self.jobCountLabel.setObjectName(u"jobCountLabel")
        self.jobCountLabel.setProperty(u"role", u"muted")

        self.sidebarHeaderLayout.addWidget(self.jobCountLabel)


        self.sidebarLayout.addLayout(self.sidebarHeaderLayout)

        self.newJobButton = QPushButton(self.sidebar)
        self.newJobButton.setObjectName(u"newJobButton")
        self.newJobButton.setProperty(u"variant", u"secondary")

        self.sidebarLayout.addWidget(self.newJobButton)

        self.jobListWidget = QListWidget(self.sidebar)
        self.jobListWidget.setObjectName(u"jobListWidget")
        self.jobListWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.jobListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.jobListWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.jobListWidget.setSpacing(2)
        self.jobListWidget.setUniformItemSizes(True)

        self.sidebarLayout.addWidget(self.jobListWidget)

        self.mainSplitter.addWidget(self.sidebar)
        self.centerPanel = QFrame(self.mainSplitter)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerLayout = QVBoxLayout(self.centerPanel)
        self.centerLayout.setSpacing(16)
        self.centerLayout.setObjectName(u"centerLayout")
        self.centerLayout.setContentsMargins(32, 24, 32, 20)
        self.headingLayout = QVBoxLayout()
        self.headingLayout.setSpacing(4)
        self.headingLayout.setObjectName(u"headingLayout")
        self.pageTitleLabel = QLabel(self.centerPanel)
        self.pageTitleLabel.setObjectName(u"pageTitleLabel")
        self.pageTitleLabel.setProperty(u"role", u"pageTitle")

        self.headingLayout.addWidget(self.pageTitleLabel)

        self.pageSubtitleLabel = QLabel(self.centerPanel)
        self.pageSubtitleLabel.setObjectName(u"pageSubtitleLabel")
        self.pageSubtitleLabel.setWordWrap(True)
        self.pageSubtitleLabel.setProperty(u"role", u"secondary")

        self.headingLayout.addWidget(self.pageSubtitleLabel)


        self.centerLayout.addLayout(self.headingLayout)

        self.dropZone = QFrame(self.centerPanel)
        self.dropZone.setObjectName(u"dropZone")
        self.dropZone.setMinimumSize(QSize(0, 168))
        self.dropZone.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dropZone.setAcceptDrops(True)
        self.dropZoneLayout = QVBoxLayout(self.dropZone)
        self.dropZoneLayout.setObjectName(u"dropZoneLayout")
        self.dropZoneLayout.setContentsMargins(0, 0, 0, 0)
        self.dropZoneStack = QStackedWidget(self.dropZone)
        self.dropZoneStack.setObjectName(u"dropZoneStack")
        self.dropEmptyPage = QWidget()
        self.dropEmptyPage.setObjectName(u"dropEmptyPage")
        self.dropEmptyLayout = QVBoxLayout(self.dropEmptyPage)
        self.dropEmptyLayout.setSpacing(8)
        self.dropEmptyLayout.setObjectName(u"dropEmptyLayout")
        self.dropEmptyTopSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dropEmptyLayout.addItem(self.dropEmptyTopSpacer)

        self.dropIconLabel = QLabel(self.dropEmptyPage)
        self.dropIconLabel.setObjectName(u"dropIconLabel")
        self.dropIconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropIconLabel.setProperty(u"role", u"dropIcon")

        self.dropEmptyLayout.addWidget(self.dropIconLabel)

        self.dropTitleLabel = QLabel(self.dropEmptyPage)
        self.dropTitleLabel.setObjectName(u"dropTitleLabel")
        self.dropTitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropTitleLabel.setProperty(u"role", u"dropTitle")

        self.dropEmptyLayout.addWidget(self.dropTitleLabel)

        self.dropHintLabel = QLabel(self.dropEmptyPage)
        self.dropHintLabel.setObjectName(u"dropHintLabel")
        self.dropHintLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dropHintLabel.setProperty(u"role", u"muted")

        self.dropEmptyLayout.addWidget(self.dropHintLabel)

        self.dropEmptyBottomSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.dropEmptyLayout.addItem(self.dropEmptyBottomSpacer)

        self.dropZoneStack.addWidget(self.dropEmptyPage)
        self.dropPreviewPage = QWidget()
        self.dropPreviewPage.setObjectName(u"dropPreviewPage")
        self.dropPreviewLayout = QHBoxLayout(self.dropPreviewPage)
        self.dropPreviewLayout.setSpacing(16)
        self.dropPreviewLayout.setObjectName(u"dropPreviewLayout")
        self.dropPreviewLayout.setContentsMargins(20, 16, 20, 16)
        self.imagePreviewLabel = QLabel(self.dropPreviewPage)
        self.imagePreviewLabel.setObjectName(u"imagePreviewLabel")
        self.imagePreviewLabel.setMinimumSize(QSize(136, 136))
        self.imagePreviewLabel.setMaximumSize(QSize(136, 136))
        self.imagePreviewLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagePreviewLabel.setProperty(u"role", u"thumbnail")

        self.dropPreviewLayout.addWidget(self.imagePreviewLabel)

        self.selectedFileLayout = QVBoxLayout()
        self.selectedFileLayout.setSpacing(4)
        self.selectedFileLayout.setObjectName(u"selectedFileLayout")
        self.selectedFileTopSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.selectedFileLayout.addItem(self.selectedFileTopSpacer)

        self.selectedFileNameLabel = QLabel(self.dropPreviewPage)
        self.selectedFileNameLabel.setObjectName(u"selectedFileNameLabel")
        self.selectedFileNameLabel.setProperty(u"role", u"dropTitle")

        self.selectedFileLayout.addWidget(self.selectedFileNameLabel)

        self.selectedFileInfoLabel = QLabel(self.dropPreviewPage)
        self.selectedFileInfoLabel.setObjectName(u"selectedFileInfoLabel")
        self.selectedFileInfoLabel.setProperty(u"role", u"muted")

        self.selectedFileLayout.addWidget(self.selectedFileInfoLabel)

        self.selectedFileButtonsLayout = QHBoxLayout()
        self.selectedFileButtonsLayout.setSpacing(8)
        self.selectedFileButtonsLayout.setObjectName(u"selectedFileButtonsLayout")
        self.selectedFileButtonsLayout.setContentsMargins(-1, 8, -1, -1)
        self.changeImageButton = QPushButton(self.dropPreviewPage)
        self.changeImageButton.setObjectName(u"changeImageButton")
        self.changeImageButton.setProperty(u"variant", u"secondary")

        self.selectedFileButtonsLayout.addWidget(self.changeImageButton)

        self.clearImageButton = QPushButton(self.dropPreviewPage)
        self.clearImageButton.setObjectName(u"clearImageButton")
        self.clearImageButton.setProperty(u"variant", u"ghost")

        self.selectedFileButtonsLayout.addWidget(self.clearImageButton)

        self.selectedFileButtonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.selectedFileButtonsLayout.addItem(self.selectedFileButtonsSpacer)


        self.selectedFileLayout.addLayout(self.selectedFileButtonsLayout)

        self.selectedFileBottomSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.selectedFileLayout.addItem(self.selectedFileBottomSpacer)


        self.dropPreviewLayout.addLayout(self.selectedFileLayout)

        self.dropZoneStack.addWidget(self.dropPreviewPage)

        self.dropZoneLayout.addWidget(self.dropZoneStack)


        self.centerLayout.addWidget(self.dropZone)

        self.optionsCard = QFrame(self.centerPanel)
        self.optionsCard.setObjectName(u"optionsCard")
        self.optionsCardLayout = QVBoxLayout(self.optionsCard)
        self.optionsCardLayout.setSpacing(12)
        self.optionsCardLayout.setObjectName(u"optionsCardLayout")
        self.optionsCardLayout.setContentsMargins(20, 16, 20, 16)
        self.optionsTitleLabel = QLabel(self.optionsCard)
        self.optionsTitleLabel.setObjectName(u"optionsTitleLabel")
        self.optionsTitleLabel.setProperty(u"role", u"sectionTitle")

        self.optionsCardLayout.addWidget(self.optionsTitleLabel)

        self.optionsFormLayout = QFormLayout()
        self.optionsFormLayout.setObjectName(u"optionsFormLayout")
        self.optionsFormLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignVCenter)
        self.optionsFormLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignTop)
        self.optionsFormLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        self.optionsFormLayout.setHorizontalSpacing(24)
        self.optionsFormLayout.setVerticalSpacing(14)
        self.aiModelLabel = QLabel(self.optionsCard)
        self.aiModelLabel.setObjectName(u"aiModelLabel")

        self.optionsFormLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.aiModelLabel)

        self.aiModelCombo = QComboBox(self.optionsCard)
        self.aiModelCombo.addItem("")
        self.aiModelCombo.setObjectName(u"aiModelCombo")
        self.aiModelCombo.setMinimumSize(QSize(180, 0))

        self.optionsFormLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.aiModelCombo)

        self.textureLabel = QLabel(self.optionsCard)
        self.textureLabel.setObjectName(u"textureLabel")

        self.optionsFormLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.textureLabel)

        self.textureCheck = QCheckBox(self.optionsCard)
        self.textureCheck.setObjectName(u"textureCheck")
        self.textureCheck.setChecked(True)
        self.textureCheck.setProperty(u"role", u"switch")

        self.optionsFormLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.textureCheck)

        self.pbrLabel = QLabel(self.optionsCard)
        self.pbrLabel.setObjectName(u"pbrLabel")

        self.optionsFormLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pbrLabel)

        self.pbrCheck = QCheckBox(self.optionsCard)
        self.pbrCheck.setObjectName(u"pbrCheck")
        self.pbrCheck.setProperty(u"role", u"switch")

        self.optionsFormLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pbrCheck)

        self.topologyLabel = QLabel(self.optionsCard)
        self.topologyLabel.setObjectName(u"topologyLabel")

        self.optionsFormLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.topologyLabel)

        self.topologySegment = QFrame(self.optionsCard)
        self.topologySegment.setObjectName(u"topologySegment")
        self.topologySegmentLayout = QHBoxLayout(self.topologySegment)
        self.topologySegmentLayout.setSpacing(2)
        self.topologySegmentLayout.setObjectName(u"topologySegmentLayout")
        self.topologySegmentLayout.setContentsMargins(2, 2, 2, 2)
        self.topologyTriangleRadio = QRadioButton(self.topologySegment)
        self.topologyButtonGroup = QButtonGroup(MainWindow)
        self.topologyButtonGroup.setObjectName(u"topologyButtonGroup")
        self.topologyButtonGroup.addButton(self.topologyTriangleRadio)
        self.topologyTriangleRadio.setObjectName(u"topologyTriangleRadio")
        self.topologyTriangleRadio.setChecked(True)
        self.topologyTriangleRadio.setProperty(u"role", u"segment")

        self.topologySegmentLayout.addWidget(self.topologyTriangleRadio)

        self.topologyQuadRadio = QRadioButton(self.topologySegment)
        self.topologyButtonGroup.addButton(self.topologyQuadRadio)
        self.topologyQuadRadio.setObjectName(u"topologyQuadRadio")
        self.topologyQuadRadio.setProperty(u"role", u"segment")

        self.topologySegmentLayout.addWidget(self.topologyQuadRadio)


        self.optionsFormLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.topologySegment)

        self.polycountLabel = QLabel(self.optionsCard)
        self.polycountLabel.setObjectName(u"polycountLabel")

        self.optionsFormLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.polycountLabel)

        self.polycountSpin = QSpinBox(self.optionsCard)
        self.polycountSpin.setObjectName(u"polycountSpin")
        self.polycountSpin.setMinimumSize(QSize(140, 0))
        self.polycountSpin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.polycountSpin.setGroupSeparatorShown(True)
        self.polycountSpin.setMinimum(100)
        self.polycountSpin.setMaximum(300000)
        self.polycountSpin.setSingleStep(1000)
        self.polycountSpin.setValue(30000)

        self.optionsFormLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.polycountSpin)


        self.optionsCardLayout.addLayout(self.optionsFormLayout)


        self.centerLayout.addWidget(self.optionsCard)

        self.centerSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.centerLayout.addItem(self.centerSpacer)

        self.actionBarLayout = QHBoxLayout()
        self.actionBarLayout.setSpacing(12)
        self.actionBarLayout.setObjectName(u"actionBarLayout")
        self.costLayout = QVBoxLayout()
        self.costLayout.setSpacing(2)
        self.costLayout.setObjectName(u"costLayout")
        self.costLabel = QLabel(self.centerPanel)
        self.costLabel.setObjectName(u"costLabel")
        self.costLabel.setTextFormat(Qt.TextFormat.RichText)
        self.costLabel.setProperty(u"role", u"secondary")

        self.costLayout.addWidget(self.costLabel)

        self.refundHintLabel = QLabel(self.centerPanel)
        self.refundHintLabel.setObjectName(u"refundHintLabel")
        self.refundHintLabel.setProperty(u"role", u"muted")

        self.costLayout.addWidget(self.refundHintLabel)


        self.actionBarLayout.addLayout(self.costLayout)

        self.actionBarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.actionBarLayout.addItem(self.actionBarSpacer)

        self.cancelButton = QPushButton(self.centerPanel)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setProperty(u"variant", u"ghost")

        self.actionBarLayout.addWidget(self.cancelButton)

        self.generateButton = QPushButton(self.centerPanel)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setEnabled(False)
        self.generateButton.setProperty(u"variant", u"primary")

        self.actionBarLayout.addWidget(self.generateButton)


        self.centerLayout.addLayout(self.actionBarLayout)

        self.mainSplitter.addWidget(self.centerPanel)
        self.rightPanel = QFrame(self.mainSplitter)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setMinimumSize(QSize(320, 0))
        self.rightPanel.setMaximumSize(QSize(440, 16777215))
        self.rightPanelLayout = QVBoxLayout(self.rightPanel)
        self.rightPanelLayout.setSpacing(16)
        self.rightPanelLayout.setObjectName(u"rightPanelLayout")
        self.rightPanelLayout.setContentsMargins(20, 24, 20, 20)
        self.previewHeaderLayout = QHBoxLayout()
        self.previewHeaderLayout.setObjectName(u"previewHeaderLayout")
        self.previewTitleLabel = QLabel(self.rightPanel)
        self.previewTitleLabel.setObjectName(u"previewTitleLabel")
        self.previewTitleLabel.setProperty(u"role", u"sectionTitle")

        self.previewHeaderLayout.addWidget(self.previewTitleLabel)

        self.previewHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.previewHeaderLayout.addItem(self.previewHeaderSpacer)

        self.currentFileLabel = QLabel(self.rightPanel)
        self.currentFileLabel.setObjectName(u"currentFileLabel")
        self.currentFileLabel.setProperty(u"role", u"muted")

        self.previewHeaderLayout.addWidget(self.currentFileLabel)


        self.rightPanelLayout.addLayout(self.previewHeaderLayout)

        self.viewerContainer = QFrame(self.rightPanel)
        self.viewerContainer.setObjectName(u"viewerContainer")
        self.viewerContainer.setMinimumSize(QSize(0, 260))
        self.viewerLayout = QVBoxLayout(self.viewerContainer)
        self.viewerLayout.setSpacing(0)
        self.viewerLayout.setObjectName(u"viewerLayout")
        self.viewerLayout.setContentsMargins(1, 1, 1, 1)
        self.viewerPlaceholderLabel = QLabel(self.viewerContainer)
        self.viewerPlaceholderLabel.setObjectName(u"viewerPlaceholderLabel")
        self.viewerPlaceholderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.viewerPlaceholderLabel.setProperty(u"role", u"secondary")

        self.viewerLayout.addWidget(self.viewerPlaceholderLabel)


        self.rightPanelLayout.addWidget(self.viewerContainer)

        self.progressSection = QWidget(self.rightPanel)
        self.progressSection.setObjectName(u"progressSection")
        self.progressLayout = QVBoxLayout(self.progressSection)
        self.progressLayout.setSpacing(8)
        self.progressLayout.setObjectName(u"progressLayout")
        self.progressLayout.setContentsMargins(0, 0, 0, 0)
        self.progressHeaderLayout = QHBoxLayout()
        self.progressHeaderLayout.setObjectName(u"progressHeaderLayout")
        self.statusChipLabel = QLabel(self.progressSection)
        self.statusChipLabel.setObjectName(u"statusChipLabel")
        self.statusChipLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statusChipLabel.setProperty(u"role", u"chip")
        self.statusChipLabel.setProperty(u"status", u"pending")

        self.progressHeaderLayout.addWidget(self.statusChipLabel)

        self.progressHeaderSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.progressHeaderLayout.addItem(self.progressHeaderSpacer)

        self.progressPercentLabel = QLabel(self.progressSection)
        self.progressPercentLabel.setObjectName(u"progressPercentLabel")
        self.progressPercentLabel.setProperty(u"role", u"strong")

        self.progressHeaderLayout.addWidget(self.progressPercentLabel)


        self.progressLayout.addLayout(self.progressHeaderLayout)

        self.progressBar = QProgressBar(self.progressSection)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 6))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.progressLayout.addWidget(self.progressBar)

        self.progressMetaLayout = QHBoxLayout()
        self.progressMetaLayout.setObjectName(u"progressMetaLayout")
        self.taskIdLabel = QLabel(self.progressSection)
        self.taskIdLabel.setObjectName(u"taskIdLabel")
        self.taskIdLabel.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.taskIdLabel.setProperty(u"role", u"mono")

        self.progressMetaLayout.addWidget(self.taskIdLabel)

        self.progressMetaSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.progressMetaLayout.addItem(self.progressMetaSpacer)

        self.etaLabel = QLabel(self.progressSection)
        self.etaLabel.setObjectName(u"etaLabel")
        self.etaLabel.setProperty(u"role", u"muted")

        self.progressMetaLayout.addWidget(self.etaLabel)


        self.progressLayout.addLayout(self.progressMetaLayout)


        self.rightPanelLayout.addWidget(self.progressSection)

        self.rightPanelDivider = QFrame(self.rightPanel)
        self.rightPanelDivider.setObjectName(u"rightPanelDivider")
        self.rightPanelDivider.setFrameShape(QFrame.Shape.HLine)
        self.rightPanelDivider.setFrameShadow(QFrame.Shadow.Sunken)

        self.rightPanelLayout.addWidget(self.rightPanelDivider)

        self.downloadSection = QWidget(self.rightPanel)
        self.downloadSection.setObjectName(u"downloadSection")
        self.downloadLayout = QVBoxLayout(self.downloadSection)
        self.downloadLayout.setSpacing(10)
        self.downloadLayout.setObjectName(u"downloadLayout")
        self.downloadLayout.setContentsMargins(0, 0, 0, 0)
        self.downloadTitleLabel = QLabel(self.downloadSection)
        self.downloadTitleLabel.setObjectName(u"downloadTitleLabel")
        self.downloadTitleLabel.setProperty(u"role", u"sectionTitle")

        self.downloadLayout.addWidget(self.downloadTitleLabel)

        self.formatButtonsLayout = QHBoxLayout()
        self.formatButtonsLayout.setSpacing(6)
        self.formatButtonsLayout.setObjectName(u"formatButtonsLayout")
        self.glbButton = QPushButton(self.downloadSection)
        self.glbButton.setObjectName(u"glbButton")
        self.glbButton.setEnabled(False)
        self.glbButton.setProperty(u"variant", u"format")

        self.formatButtonsLayout.addWidget(self.glbButton)

        self.fbxButton = QPushButton(self.downloadSection)
        self.fbxButton.setObjectName(u"fbxButton")
        self.fbxButton.setEnabled(False)
        self.fbxButton.setProperty(u"variant", u"format")

        self.formatButtonsLayout.addWidget(self.fbxButton)

        self.objButton = QPushButton(self.downloadSection)
        self.objButton.setObjectName(u"objButton")
        self.objButton.setEnabled(False)
        self.objButton.setProperty(u"variant", u"format")

        self.formatButtonsLayout.addWidget(self.objButton)

        self.usdzButton = QPushButton(self.downloadSection)
        self.usdzButton.setObjectName(u"usdzButton")
        self.usdzButton.setEnabled(False)
        self.usdzButton.setProperty(u"variant", u"format")

        self.formatButtonsLayout.addWidget(self.usdzButton)

        self.stlButton = QPushButton(self.downloadSection)
        self.stlButton.setObjectName(u"stlButton")
        self.stlButton.setEnabled(False)
        self.stlButton.setProperty(u"variant", u"format")

        self.formatButtonsLayout.addWidget(self.stlButton)

        self.formatButtonsSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.formatButtonsLayout.addItem(self.formatButtonsSpacer)


        self.downloadLayout.addLayout(self.formatButtonsLayout)

        self.openOutputFolderButton = QPushButton(self.downloadSection)
        self.openOutputFolderButton.setObjectName(u"openOutputFolderButton")
        self.openOutputFolderButton.setEnabled(False)
        self.openOutputFolderButton.setProperty(u"variant", u"secondary")

        self.downloadLayout.addWidget(self.openOutputFolderButton)


        self.rightPanelLayout.addWidget(self.downloadSection)

        self.rightPanelSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rightPanelLayout.addItem(self.rightPanelSpacer)

        self.retentionNoteLabel = QLabel(self.rightPanel)
        self.retentionNoteLabel.setObjectName(u"retentionNoteLabel")
        self.retentionNoteLabel.setWordWrap(True)
        self.retentionNoteLabel.setProperty(u"role", u"notice")

        self.rightPanelLayout.addWidget(self.retentionNoteLabel)

        self.mainSplitter.addWidget(self.rightPanel)

        self.centralLayout.addWidget(self.mainSplitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.mainMenuBar = QMenuBar(MainWindow)
        self.mainMenuBar.setObjectName(u"mainMenuBar")
        self.mainMenuBar.setGeometry(QRect(0, 0, 1280, 24))
        self.fileMenu = QMenu(self.mainMenuBar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.helpMenu = QMenu(self.mainMenuBar)
        self.helpMenu.setObjectName(u"helpMenu")
        MainWindow.setMenuBar(self.mainMenuBar)
        self.mainStatusBar = QStatusBar(MainWindow)
        self.mainStatusBar.setObjectName(u"mainStatusBar")
        MainWindow.setStatusBar(self.mainStatusBar)
        QWidget.setTabOrder(self.newJobButton, self.jobListWidget)
        QWidget.setTabOrder(self.jobListWidget, self.changeImageButton)
        QWidget.setTabOrder(self.changeImageButton, self.aiModelCombo)
        QWidget.setTabOrder(self.aiModelCombo, self.textureCheck)
        QWidget.setTabOrder(self.textureCheck, self.pbrCheck)
        QWidget.setTabOrder(self.pbrCheck, self.topologyTriangleRadio)
        QWidget.setTabOrder(self.topologyTriangleRadio, self.topologyQuadRadio)
        QWidget.setTabOrder(self.topologyQuadRadio, self.polycountSpin)
        QWidget.setTabOrder(self.polycountSpin, self.generateButton)
        QWidget.setTabOrder(self.generateButton, self.cancelButton)

        self.mainMenuBar.addAction(self.fileMenu.menuAction())
        self.mainMenuBar.addAction(self.helpMenu.menuAction())
        self.fileMenu.addAction(self.actionOpenImage)
        self.fileMenu.addAction(self.actionOpenOutputFolder)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionSettings)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionQuit)
        self.helpMenu.addAction(self.actionOpenDocs)
        self.helpMenu.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.settingsButton.clicked.connect(self.actionSettings.trigger)
        self.changeImageButton.clicked.connect(self.actionOpenImage.trigger)
        self.openOutputFolderButton.clicked.connect(self.actionOpenOutputFolder.trigger)

        self.dropZoneStack.setCurrentIndex(0)
        self.generateButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image to 3D", None))
        self.actionOpenImage.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc5f4\uae30\u2026", None))
#if QT_CONFIG(shortcut)
        self.actionOpenImage.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenOutputFolder.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354 \uc5f4\uae30", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815\u2026", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+,", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenDocs.setText(QCoreApplication.translate("MainWindow", u"Meshy API \ubb38\uc11c", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Image to 3D \uc815\ubcf4", None))
        self.appTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Image to 3D", None))
#if QT_CONFIG(tooltip)
        self.creditBadgeLabel.setToolTip(QCoreApplication.translate("MainWindow", u"\ub0a8\uc740 \ud06c\ub808\ub527 (GET /openapi/v1/balance)", None))
#endif // QT_CONFIG(tooltip)
        self.creditBadgeLabel.setText(QCoreApplication.translate("MainWindow", u"\ud06c\ub808\ub527 \u2013", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.jobListTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\uc791\uc5c5 \ubaa9\ub85d", None))
        self.jobCountLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.newJobButton.setText(QCoreApplication.translate("MainWindow", u"+  \uc0c8 \uc791\uc5c5", None))
        self.pageTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 3D \ubaa8\ub378 \ub9cc\ub4e4\uae30", None))
        self.pageSubtitleLabel.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ud55c \uc7a5\uc744 \uc62c\ub9ac\uba74 Meshy AI Image to 3D\ub85c \ubaa8\ub378\uc744 \ub9cc\ub4e4\uc5b4 \uc90d\ub2c8\ub2e4.", None))
#if QT_CONFIG(tooltip)
        self.dropZone.setToolTip(QCoreApplication.translate("MainWindow", u"JPG \u00b7 PNG \u00b7 WebP, \ucd5c\ub300 20MB", None))
#endif // QT_CONFIG(tooltip)
        self.dropIconLabel.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
        self.dropTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0\ub97c \uc5ec\uae30\ub85c \ub04c\uc5b4\ub2e4 \ub193\uac70\ub098 \ud074\ub9ad\ud574\uc11c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.dropHintLabel.setText(QCoreApplication.translate("MainWindow", u"JPG \u00b7 PNG \u00b7 WebP  \u00b7  \ucd5c\ub300 20MB", None))
        self.selectedFileNameLabel.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc774\ub984.jpg", None))
        self.selectedFileInfoLabel.setText(QCoreApplication.translate("MainWindow", u"1024 \u00d7 1024 \u00b7 2.4MB", None))
        self.changeImageButton.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\ub978 \uc774\ubbf8\uc9c0 \uc120\ud0dd", None))
        self.clearImageButton.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc6b0\uae30", None))
        self.optionsTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\uc0dd\uc131 \uc635\uc158", None))
#if QT_CONFIG(tooltip)
        self.aiModelLabel.setToolTip(QCoreApplication.translate("MainWindow", u"ai_model", None))
#endif // QT_CONFIG(tooltip)
        self.aiModelLabel.setText(QCoreApplication.translate("MainWindow", u"AI \ubaa8\ub378", None))
        self.aiModelCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"latest (\uae30\ubcf8)", None))

#if QT_CONFIG(tooltip)
        self.textureLabel.setToolTip(QCoreApplication.translate("MainWindow", u"should_texture \u00b7 \ub044\uba74 \ud06c\ub808\ub527\uc774 \uc904\uc5b4\ub4ed\ub2c8\ub2e4", None))
#endif // QT_CONFIG(tooltip)
        self.textureLabel.setText(QCoreApplication.translate("MainWindow", u"\ud14d\uc2a4\ucc98 \uc0dd\uc131", None))
        self.textureCheck.setText("")
#if QT_CONFIG(tooltip)
        self.pbrLabel.setToolTip(QCoreApplication.translate("MainWindow", u"enable_pbr \u00b7 metallic / roughness / normal \ub9f5", None))
#endif // QT_CONFIG(tooltip)
        self.pbrLabel.setText(QCoreApplication.translate("MainWindow", u"PBR \ub9f5", None))
        self.pbrCheck.setText("")
#if QT_CONFIG(tooltip)
        self.topologyLabel.setToolTip(QCoreApplication.translate("MainWindow", u"topology", None))
#endif // QT_CONFIG(tooltip)
        self.topologyLabel.setText(QCoreApplication.translate("MainWindow", u"\ud1a0\ud3f4\ub85c\uc9c0", None))
        self.topologyTriangleRadio.setText(QCoreApplication.translate("MainWindow", u"\uc0bc\uac01\ud615", None))
        self.topologyQuadRadio.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uac01\ud615", None))
#if QT_CONFIG(tooltip)
        self.polycountLabel.setToolTip(QCoreApplication.translate("MainWindow", u"target_polycount", None))
#endif // QT_CONFIG(tooltip)
        self.polycountLabel.setText(QCoreApplication.translate("MainWindow", u"\ubaa9\ud45c \ud3f4\ub9ac\uace4 \uc218", None))
        self.costLabel.setText(QCoreApplication.translate("MainWindow", u"\uc608\uc0c1 \ube44\uc6a9 <b>30 \ud06c\ub808\ub527</b>", None))
        self.refundHintLabel.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud328(FAILED) \uc2dc\uc5d0\ub9cc \ud658\ubd88\ub429\ub2c8\ub2e4", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"\ucde8\uc18c", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"3D \ubaa8\ub378 \uc0dd\uc131", None))
        self.previewTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\ub9ac\ubcf4\uae30", None))
        self.currentFileLabel.setText("")
        self.viewerPlaceholderLabel.setText(QCoreApplication.translate("MainWindow", u"3D \ubdf0\uc5b4 \uc601\uc5ed", None))
        self.statusChipLabel.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30", None))
        self.progressPercentLabel.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.taskIdLabel.setText(QCoreApplication.translate("MainWindow", u"task \u2013", None))
        self.etaLabel.setText("")
        self.downloadTitleLabel.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.glbButton.setText(QCoreApplication.translate("MainWindow", u"GLB", None))
        self.fbxButton.setText(QCoreApplication.translate("MainWindow", u"FBX", None))
        self.objButton.setText(QCoreApplication.translate("MainWindow", u"OBJ", None))
        self.usdzButton.setText(QCoreApplication.translate("MainWindow", u"USDZ", None))
        self.stlButton.setText(QCoreApplication.translate("MainWindow", u"STL", None))
        self.openOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \ud3f4\ub354 \uc5f4\uae30", None))
        self.retentionNoteLabel.setText(QCoreApplication.translate("MainWindow", u"Meshy \uc11c\ubc84\ub294 \uacb0\uacfc\ubb3c\uc744 3\uc77c\ub9cc \ubcf4\uad00\ud569\ub2c8\ub2e4. \uc644\ub8cc\ub418\uba74 \uc571\uc774 \uc790\ub3d9\uc73c\ub85c \ub0b4\ub824\ubc1b\uc2b5\ub2c8\ub2e4.", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
    # retranslateUi

