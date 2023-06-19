from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        MainWindow.resize(1200, 630)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))

        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/newPrefix/logo@2x.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/add-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionUnits = QAction(MainWindow)
        self.actionUnits.setObjectName(u"actionUnits")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/unit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnits.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionWindows = QAction(MainWindow)
        self.actionWindows.setObjectName(u"actionWindows")
        self.actionAbout_Author = QAction(MainWindow)
        self.actionAbout_Author.setObjectName(u"actionAbout_Author")
        self.actionCheck_for_updates = QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionDebig = QAction(MainWindow)
        self.actionDebig.setObjectName(u"actionDebig")
        self.actionDebug = QAction(MainWindow)
        self.actionDebug.setObjectName(u"actionDebug")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/console.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDebug.setIcon(icon4)
        self.actionView_License = QAction(MainWindow)
        self.actionView_License.setObjectName(u"actionView_License")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1198, 577))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.tab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_intro = QWidget()
        self.page_intro.setObjectName(u"page_intro")
        self.gridLayout_4 = QGridLayout(self.page_intro)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(self.page_intro)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.pushButton_new = QPushButton(self.splitter)
        self.pushButton_new.setObjectName(u"pushButton_new")
        self.pushButton_new.setMinimumSize(QSize(174, 0))
        self.pushButton_new.setMaximumSize(QSize(150, 50))
        self.pushButton_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_new.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(222, 49, 92);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(218, 0, 55);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/new-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_new.setIcon(icon5)
        self.splitter.addWidget(self.pushButton_new)
        self.pushButton_open = QPushButton(self.splitter)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMinimumSize(QSize(174, 0))
        self.pushButton_open.setMaximumSize(QSize(150, 50))
        self.pushButton_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_open.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(61, 69, 79);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(138, 147, 158);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/open-envelope.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open.setIcon(icon6)
        self.splitter.addWidget(self.pushButton_open)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)

        self.plainTextName = QPlainTextEdit(self.page_intro)
        self.plainTextName.setObjectName(u"plainTextName")
        self.plainTextName.setMinimumSize(QSize(0, 37))
        self.plainTextName.setMaximumSize(QSize(250, 35))
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(9)
        self.plainTextName.setFont(font)
        self.plainTextName.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.plainTextName, 5, 0, 1, 1)

        self.label_4 = QLabel(self.page_intro)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.pushButton_sendNote = QPushButton(self.page_intro)
        self.pushButton_sendNote.setObjectName(u"pushButton_sendNote")
        self.pushButton_sendNote.setMaximumSize(QSize(190, 45))
        self.pushButton_sendNote.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(58, 192, 37);\n"
"	color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 165, 32);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/message.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_sendNote.setIcon(icon7)

        self.gridLayout_4.addWidget(self.pushButton_sendNote, 6, 0, 1, 1)

        self.label_2 = QLabel(self.page_intro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 100))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        self.label_2.setFont(font1)

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_intro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 9, 1)

        self.plainTextMessage = QPlainTextEdit(self.page_intro)
        self.plainTextMessage.setObjectName(u"plainTextMessage")
        self.plainTextMessage.setMinimumSize(QSize(290, 0))
        self.plainTextMessage.setMaximumSize(QSize(350, 300))
        font3 = QFont()
        font3.setFamily(u"Segoe Print")
        font3.setPointSize(10)
        self.plainTextMessage.setFont(font3)

        self.gridLayout_4.addWidget(self.plainTextMessage, 3, 0, 1, 1)

        self.label = QLabel(self.page_intro)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(300, 0))
        self.label.setMaximumSize(QSize(16777215, 27))
        font4 = QFont()
        font4.setFamily(u"Old English Text MT")
        font4.setPointSize(18)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(85, 85, 255);")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_4.addWidget(self.label, 8, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_intro)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.stackedWidget.addWidget(self.page_main)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon8, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        self.menuNew = QMenu(self.menubar)
        self.menuNew.setObjectName(u"menuNew")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionSave_as)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionClose)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionUnits)
        self.menuSettings.addAction(self.actionDebug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionView_License)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Author)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Trussify", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"Novo Projeto", None))
#if QT_CONFIG(statustip)
        self.actionNew.setStatusTip(QCoreApplication.translate("MainWindow", u"Criar projeto", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Salve seu projeto", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Salvar como", None))
#if QT_CONFIG(statustip)
        self.actionSave_as.setStatusTip(QCoreApplication.translate("MainWindow", u"Salve seu projeto como quiser", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionSave_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(statustip)
        self.actionOpen.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir um projeto existente", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
#if QT_CONFIG(statustip)
        self.actionQuit.setStatusTip(QCoreApplication.translate("MainWindow", u"Sair do projeto", None))
#endif // QT_CONFIG(statustip)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
#if QT_CONFIG(statustip)
        self.actionClose.setStatusTip(QCoreApplication.translate("MainWindow", u"Fechar o projeto atual", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F4", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnits.setText(QCoreApplication.translate("MainWindow", u"Unidades", None))
#if QT_CONFIG(statustip)
        self.actionUnits.setStatusTip(QCoreApplication.translate("MainWindow", u"Mudar unidades", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionUnits.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"Sobre Trussify", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionWindows.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.actionAbout_Author.setText(QCoreApplication.translate("MainWindow", u"About Author", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for updates...", None))
#endif // QT_CONFIG(shortcut)
        self.actionDebig.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
#if QT_CONFIG(statustip)
        self.actionDebug.setStatusTip(QCoreApplication.translate("MainWindow", u"Open debug console", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionDebug.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionView_License.setText(QCoreApplication.translate("MainWindow", u"Ver licença", None))
#if QT_CONFIG(tooltip)
        self.pushButton_new.setToolTip(QCoreApplication.translate("MainWindow", u"Crie um novo projeto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_new.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.pushButton_new.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_new.setText(QCoreApplication.translate("MainWindow", u"\n"
"  New\n"
"", None))
#if QT_CONFIG(tooltip)
        self.pushButton_open.setToolTip(QCoreApplication.translate("MainWindow", u"Abra um projeto existente", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\n"
"  Procurar projeto\n"
"", None))
        
        #menu in the top bar
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Configurações", None))


