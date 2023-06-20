import getpass
import logging
import os
import platform
import sys
import time

import requests
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from supports import *
from truss import MainPage
from ui_main import Ui_MainWindow
from ui_units import Ui_MainWindow2 

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger('trussify')

date = '<span style="color:#ff002b;">%m/%d/%Y</span> <span style="color:#0800ff;">%I:%M:%S</span> %p'

my_system = platform.uname()
user = getpass.getuser()


class CustomFormatter(logging.Formatter):

    FORMATS = {
        logging.DEBUG: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#d4659d;">[ %(levelname)s ]</span>  %(message)s',
        logging.INFO: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#ff0055;">[ %(levelname)s ]</span>  %(message)s',
        logging.WARNING: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#fd6152;">[ %(levelname)s ]</span>  %(message)s',
        logging.ERROR: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#ff0000;">[ %(levelname)s ]</span>  %(message)s',
        logging.CRITICAL: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#00ffbb;">[ %(levelname)s ]</span>  %(message)s'
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=date)
        return formatter.format(record)


class QTextEditLogger(logging.Handler):

    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

        font = QFont("Terminal Trussify")
        font.setStyleHint(QFont.TypeWriter)
        self.widget.setFont(font)

        self.widget.appendPlainText('#'*80 + '\n')
        self.widget.appendPlainText(f'OS : {my_system.system}')
        self.widget.appendPlainText(f'Nome do computador : {my_system.node}-{user}')
        self.widget.appendPlainText(f'Release : {my_system.release}')
        self.widget.appendPlainText(f'Version : {my_system.version}')
        self.widget.appendPlainText(f'Computador : {my_system.machine}')
        self.widget.appendPlainText(f'Processador : {my_system.processor}')
        self.widget.appendPlainText('#'*80 + '\n')

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendHtml(msg)


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.logTextBox = QTextEditLogger(self)

        formatter = CustomFormatter()
        self.logTextBox.setFormatter(formatter)

        logger.addHandler(self.logTextBox)

        logger.setLevel(logging.DEBUG)

        layout.addWidget(self.logTextBox.widget)

        savebutton = QPushButton('Save logs in a file')
        layout.addWidget(savebutton)
        self.setLayout(layout)

        savebutton.clicked.connect(self.save_log)

    def save_log(self):
        logs = self.logTextBox.widget.toPlainText()
        document = os.path.join(os.path.expanduser('~/Documents'), 'debug')
        filename = QFileDialog.getSaveFileName(
            self, 'Save file', document, "Log files (*.log)")

        with open(filename[0], 'w') as fh:
            fh.writelines(str(logs))


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.window_list = []
        self.name_list = []
        self.path_list = []
        self.count = 0
        self.metric_index = []
        self.imperial_index = [[0, 0, 0]]
        self.metric_unit = [[]]
        self.imperial_unit = [[[0, 0, 0]]]
        self.ui.closeEvent = self.closeEvent

        # Debug Window create
        self.debug = AnotherWindow()
        self.debug.resize(900, 600)
        self.debug.setWindowTitle('Debug')
        icon = QIcon(":/newPrefix/logo@2x.png")
        self.debug.setWindowIcon(icon)
        self.debug.setStyleSheet(u"background-color: rgb(58, 64, 76);\n"
                                "color: rgb(20, 204, 204);\n"
                                "font-size:9.5pt")

        self.APP_NAME = 'trussify'
        self.APP_VERSION = '1.8.0'
        self.APP_UPDATE_TIME = 'Junho 2023'

        self.ui.statusbar.showMessage('')

        logger.info('Sys arguements : %s', str(sys.argv))
        pathname = os.path.dirname(sys.argv[0])

        self.current_directory = os.path.abspath(pathname)
        logger.info('Current Directory : %s', self.current_directory)

        self.ui.pushButton_new.clicked.connect(self.new_file)
        self.ui.pushButton_open.clicked.connect(self.open_file)

        self.ui.pushButton_sendNote.clicked.connect(self.say_thanks)

        self.ui.actionUnits.triggered.connect(self.unit)
        self.ui.actionNew.triggered.connect(
            lambda: self.ui.tabWidget.setCurrentIndex(0))
        self.ui.actionClose.triggered.connect(self.show_dialog)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_as.triggered.connect(self.save_as_file)
        self.ui.actionCheck_for_updates.triggered.connect(self.update_app)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Author.triggered.connect(self.about_author)
        self.ui.actionView_License.triggered.connect(self.open_license)
        self.ui.actionDebug.triggered.connect(self.debug_window)

        self.ui.actionSave.setIcon(
            QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.ui.actionClose.setIcon(
            QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))

        self.ui.plainTextMessage.setPlainText('')
        self.ui.plainTextMessage.setPlaceholderText(
            'Dear Joao Tapparo,\nThank you for ...')
        self.ui.plainTextName.setPlaceholderText(user)
        self.name = user

        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.ui.tabWidget.tabCloseRequested.connect(self.show_dialog)
        self.ui.tabWidget.currentChanged.connect(self.unit_window_set)
        self.ui.tabWidget.setStyleSheet("""
        QTabBar
        {
            font: 63 9pt "Segoe UI Semibold";
            color: black;
        }
        QTabBar::tab::selected {
            font: 63 9pt "Segoe UI Semibold";
            color: red;
        }
        """)

        self.update_app(oninit=True)

        if len(sys.argv) > 1:
            openwith = (sys.argv[1], "")
            self.open_file(demopath=openwith)

    def debug_window(self):
        if self.debug.isVisible():
            self.debug.hide()
        else:
            self.debug.show()

    def open_license(self):
        QDesktopServices.openUrl(
            "https://github.com/johnnyhall/trussify#license")

    def open_donate(self):
        QDesktopServices.openUrl(
            'https://paypal.me/johnnyhall1')

    def open_help(self):
        QDesktopServices.openUrl(
            'https://github.com/johnnyhall/trussify#tutorial')

    def update_app(self, oninit=False):
        """
        Update application from GitHub repository
        """

        self.oninit = oninit
        logger.info('Checking for updates...')
        self.ui.statusbar.showMessage('Checking for updates...')

        if self.oninit:
            self.ui.statusbar.showMessage('Obrigado por utilizar Trussify')
        else:
            self.ui.statusbar.showMessage(
                'Check your internet connections and try again.')
            msgBox = QMessageBox()
            msgBox.setWindowFlags(
                Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            msgBox.setWindowTitle("trussify")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                f"<font color='red' size='5'>Something went wrong. Try again!</font>")
            msgBox.setInformativeText('Check your internet connections.')
            msgBox.exec_()

    def about(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowFlags(
            Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.msgBox.setStyleSheet("background-color: rgb(88, 105, 110);")

        icon = QIcon(os.path.join(self.current_directory, 'logo@4x.png'))
        self.msgBox.setIconPixmap(icon.pixmap(96, 96))
        self.msgBox.setText(
            f"<font color='red' size='4'>Version : {self.APP_VERSION} ({self.APP_UPDATE_TIME})</font>")

        self.msgBox.setInformativeText("""puc campinas</a><br>""")
        self.msgBox.setWindowTitle("Sobre Trussify")
        self.msgBox.exec_()

    def about_author(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowFlags(
            Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.msgBox.setWindowTitle("Sobre Autor")
        self.msgBox.exec_()

    def unit(self, change=True):
        self.window_unit = QMainWindow(parent=self)
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self.window_unit)
        self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial)
        self.window_unit.show()

        self.ui2.metricButton.clicked.connect(
            lambda: self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_metric))
        self.ui2.radioButton_2.clicked.connect(
            lambda: self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial))

        self.cb_length_m = QComboBox()
        self.cb_length_m.addItems(["m", "mm"])
        self.ui2.layout_length_metric.addWidget(self.cb_length_m)
        self.setLayout(self.ui2.layout_length_metric)

        self.cb_load_m = QComboBox()
        self.cb_load_m.addItems(["kN", "N", "kg"])
        self.ui2.layout_load_metric.addWidget(self.cb_load_m)
        self.setLayout(self.ui2.layout_length_metric)

        self.cb_force_m = QComboBox()
        self.cb_force_m.addItems(["kN", "N", "kg"])
        self.ui2.layout_force_metric.addWidget(self.cb_force_m)
        self.setLayout(self.ui2.layout_force_metric)

        self.cb_displacement_m = QComboBox()
        self.cb_displacement_m.addItem("mm")
        self.ui2.layout_displacement_metric.addWidget(self.cb_displacement_m)
        self.setLayout(self.ui2.layout_displacement_metric)
        self.cb_displacement_m.model().item(0).setEnabled(False)

        self.cb_length_i = QComboBox()
        self.cb_length_i.addItems(["ft", "in"])
        self.ui2.layout_length_imperial.addWidget(self.cb_length_i)
        self.setLayout(self.ui2.layout_length_imperial)

        self.cb_load_i = QComboBox()
        self.cb_load_i.addItems(["kip", "lb"])
        self.ui2.layout_load_imperial.addWidget(self.cb_load_i)
        self.setLayout(self.ui2.layout_length_imperial)

        self.cb_force_i = QComboBox()
        self.cb_force_i.addItems(["kip", "lb"])
        self.ui2.layout_force_imperial.addWidget(self.cb_force_i)
        self.setLayout(self.ui2.layout_force_imperial)

        self.cb_displacement_i = QComboBox()
        self.cb_displacement_i.addItem("in")
        self.ui2.layout_displacement_imperial.addWidget(self.cb_displacement_i)
        self.setLayout(self.ui2.layout_displacement_imperial)
        self.cb_displacement_i.model().item(0).setEnabled(False)
        try:
            if len(self.current_metric_index) > 0:
                self.ui2.metricButton.setChecked(True)
                self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_metric)
                self.cb_length_m.setCurrentIndex(
                    self.current_metric_index[0][0])
                self.cb_load_m.setCurrentIndex(self.current_metric_index[0][1])
                self.cb_force_m.setCurrentIndex(
                    self.current_metric_index[0][2])
            elif len(self.current_imperial_index) > 0:
                self.ui2.radioButton_2.setChecked(True)
                self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial)
                self.cb_length_i.setCurrentIndex(
                    self.current_imperial_index[0][0])
                self.cb_load_i.setCurrentIndex(
                    self.current_imperial_index[0][1])
                self.cb_force_i.setCurrentIndex(
                    self.current_imperial_index[0][2])
        except:
            pass

        self.ui2.buttonBox.accepted.connect(self.update_combo)
        self.ui2.buttonBox.accepted.connect(self.unit_per_page)
        self.ui2.buttonBox.accepted.connect(self.unit_window_set)
        self.ui2.buttonBox.accepted.connect(self.unit_send_to_page)
        self.ui2.buttonBox.accepted.connect(self.unit_send_for_converting)
        if change:
            self.ui2.buttonBox.accepted.connect(self.tab_name_change)

    def update_combo(self):
        self.metric_index = []
        self.imperial_index = []
        if self.ui2.stackedWidget.currentIndex() == 0:
            self.metric_index.append([self.cb_length_m.currentIndex(
            ), self.cb_load_m.currentIndex(), self.cb_force_m.currentIndex()])
        else:
            self.imperial_index.append([self.cb_length_i.currentIndex(
            ), self.cb_load_i.currentIndex(), self.cb_force_i.currentIndex()])

    def closeEvent(self, event):
        index = self.ui.tabWidget.count()
        if index == 1:
            self.usedTime = (time.time() - start_time)/60
            logger.info('Total used time : %s minute', self.usedTime)
            event.accept()

        elif index == 2:
            self.returnValue = None
            self.show_dialog(value=1)

            if self.returnValue == QMessageBox.Cancel:
                event.ignore()
            else:
                self.usedTime = (time.time() - start_time)/60
                logger.info('Total used time : %s minute', self.usedTime)
                event.accept()

        else:
            self.msgBox = QMessageBox()
            self.msgBox.setWindowFlags(
                Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText(
                f"""<font color='red' size='5'>Do you want to close all  {index-1} opened <br>projects?</font>""")
            self.msgBox.setInformativeText(
                "Your changes will be lost if you don't save them.")
            self.msgBox.setWindowTitle("trussify")
            self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.msgBox.button(QMessageBox.Yes).setIcon(
                QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))
            self.msgBox.button(QMessageBox.No).setIcon(
                QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
            self.msgBox.setDefaultButton(QMessageBox.Yes)
            self.msgBox.setEscapeButton(QMessageBox.No)
            returnValue = self.msgBox.exec_()
            if returnValue == QMessageBox.Yes:
                self.usedTime = (time.time() - start_time)/60
                logger.info('Total used time : %s minute', self.usedTime)
                event.accept()

            else:
                event.ignore()

    def show_dialog(self, value):
        if value:
            index = value
        else:
            index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.window_list[index-1].change > 0:
                self.msgBox = QMessageBox()
                self.msgBox.setWindowFlags(
                    Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText(
                    f"""<font color='red' size='5'>Deseja salvar suas alterações <br>feitas em {self.ui.tabWidget.tabText(index)}?</font>""")
                self.msgBox.setInformativeText(
                    "Você perdera suas alterações caso não as salve.")
                self.msgBox.setWindowTitle("trussify")
                self.msgBox.setStandardButtons(
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                self.msgBox.button(QMessageBox.Yes).setText("Salvar")
                self.msgBox.button(QMessageBox.Yes).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))

                self.msgBox.button(QMessageBox.No).setText("Não Salvar")
                self.msgBox.button(QMessageBox.No).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
                self.msgBox.button(QMessageBox.Cancel).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))

                self.msgBox.setDefaultButton(QMessageBox.Yes)
                self.msgBox.setEscapeButton(QMessageBox.Cancel)
                self.returnValue = self.msgBox.exec_()
                if self.returnValue == QMessageBox.Yes:
                    self.save_file()
                    self.close_tab(index=index)
                elif self.returnValue == QMessageBox.No:
                    self.close_tab(index=index)
            else:
                self.close_tab(index=index)

    def close_tab(self, index=None):
        index = index
        self.window_list[index-1].closeEvent()
        self.ui.tabWidget.removeTab(index)
        self.window_list.pop(index-1)
        self.name_list.pop(index-1)
        self.path_list.pop(index-1)
        logger.info('Path List after CLOSING tab: %s', self.path_list)
        logger.info('Name List after CLOSING tab: %s', self.name_list)

        self.metric_unit.pop(index)
        self.imperial_unit.pop(index)

    def save_file(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            self.window_list[index-1].save_to_file()
            path = self.window_list[index-1].filename[0]
            name = os.path.basename(path)[:-4]

            self.path_list[index-1] = path
            self.name_list[index-1] = name
            logger.info('Path List after SAVING file: %s', self.path_list)
            logger.info('Name List after SAVING file: %s', self.name_list)
            self.tab_name_change()

    def save_as_file(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            self.window_list[index-1].save_to_file(saveas=True)

    def open_file(self, demopath=None, isdemo=None):
        demopath = demopath
        demo = isdemo
        #demopath= (os.path.join(self.current_directory, 'Demo', 'Example 6.trs'), "")
        self.window = MainPage(
            open=True, filename=demopath, demo=demo, logger=logger)
        path = self.window.filename[0]
        name = os.path.basename(path)[:-4]

        logger.info('Abrir arquivo : %s', name)
        index = self.ui.tabWidget.count()
        self.ui.tabWidget.insertTab(index, self.window, name)
        self.ui.tabWidget.setCurrentIndex(index)
        self.ui.tabWidget.setTabToolTip(index, path)

        self.window_list.append(self.window)
        self.path_list.append(path)
        self.name_list.append(name)
        logger.info('Path List : %s', self.path_list)
        logger.info('Name List : %s', self.name_list)

        self.current_metric_index = self.window.current_metric_index
        self.current_imperial_index = self.window.current_imperial_index
        self.metric_unit.append(self.current_metric_index)
        self.imperial_unit.append(self.current_imperial_index)

        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_nodes.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_members.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_supports.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_loads.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_property.cellChanged.connect(self.tab_name_change)
        self.ui.statusbar.showMessage(
            'Os nós são os pontos nas coordenadas (x,y). Insira os pontos (x,y) na tabela de nós.')
        self.window.ui.pushbutton_nodes.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Os nós são os pontos nas coordenadas (x,y). Insira os pontos (x,y) na tabela de nós.'))
        self.window.ui.pushbutton_members.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina os membros conectando os nós. Não se esqueça de observar o gráfico ao conectar os nós!'))
        self.window.ui.pushbutton_supports.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Existem três tipos de restrições disponíveis. Selecione a adequada nas listas suspensas.'))
        self.window.ui.pushbutton_loads.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina a carga nodal e o ângulo (em graus) de acordo com o número do nó.'))
        self.window.ui.pushbutton_properties.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina o módulo de elasticidade (E) e a área da seção transversal (A) do material.'))
        self.window.ui.pushbutton_displacement.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Use o ampliador de deflexão para visualizar claramente a forma deslocada em azul.'))
        self.window.ui.pushbutton_forces.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'As caixas de seleção no canto superior direito podem ser usadas para modificar os detalhes do gráfico.'))
        self.window.ui.pushbutton_influenceLine.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'A linha de influência é plotada como uma linha vermelha. Use a caixa de membro para navegar pela linha de influência dos membros.'))


    def new_file(self):
        self.count += 1
        self.window = MainPage(logger=logger)
        index = self.ui.tabWidget.count()
        name = f'Projeto Trussify {self.count}'
        self.ui.tabWidget.insertTab(index, self.window, name)
        self.ui.tabWidget.setCurrentIndex(index)
        self.ui.tabWidget.setTabToolTip(index, name)

        self.window_list.append(self.window)
        self.path_list.append(name)
        self.name_list.append(name)
        logger.info('Path List : %s', self.path_list)
        logger.info('Name List : %s', self.name_list)

        self.unit(change=False)

        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_nodes.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_members.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_supports.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_loads.cellChanged.connect(self.tab_name_change)
        self.window_list[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_property.cellChanged.connect(self.tab_name_change)
        self.ui.statusbar.showMessage(
            'Os nós são os pontos nas coordenadas (x,y). Insira os pontos (x,y) na tabela de nós.')
        self.window.ui.pushbutton_nodes.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Os nós são os pontos nas coordenadas (x,y). Insira os pontos (x,y) na tabela de nós.'))
        self.window.ui.pushbutton_members.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina os membros conectando os nós. Não se esqueça de observar o gráfico ao conectar os nós!'))
        self.window.ui.pushbutton_supports.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Três tipos de restrições estão disponíveis. Selecione a opção adequada nas listas suspensas.'))
        self.window.ui.pushbutton_loads.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina a carga nodal e o ângulo (em graus) de acordo com o número do nó.'))
        self.window.ui.pushbutton_properties.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Defina o módulo de elasticidade (E) e a área da seção transversal (A) do material.'))
        self.window.ui.pushbutton_displacement.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Use o ampliador de deflexão para visualizar claramente a forma deslocada em azul.'))
        self.window.ui.pushbutton_forces.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'As caixas de seleção no canto superior direito podem ser usadas para modificar os detalhes do gráfico.'))
        self.window.ui.pushbutton_influenceLine.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'O caminho da carga é plotado como uma linha vermelha. Use a caixa de membros para navegar pela linha de influência dos membros.'))

    def unit_per_page(self):
        index = self.ui.tabWidget.currentIndex()
        try:
            self.metric_unit[index] = self.metric_index
            self.imperial_unit[index] = self.imperial_index
        except:
            self.metric_unit.append(self.metric_index)
            self.imperial_unit.append(self.imperial_index)

    def unit_window_set(self):
        index = self.ui.tabWidget.currentIndex()
        try:
            self.current_metric_index = self.metric_unit[index]
            self.current_imperial_index = self.imperial_unit[index]
        except:
            self.current_metric_index = []
            self.current_imperial_index = [[0, 0, 0]]
        if index == 0:
            self.ui.statusbar.showMessage('Obrigado por utilizar Trussify')

    def unit_send_to_page(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.current_metric_index:
                self.window_list[index-1].change_unit_label(
                    unit=self.current_metric_index, type='metrico')
            else:
                self.window_list[index-1].change_unit_label(
                    unit=self.current_imperial_index, type='imperial')

    def unit_send_for_converting(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.current_metric_index:
                self.window_list[index-1].unit_convert(type='metrico')
            else:
                self.window_list[index-1].unit_convert(type='imperial')

    def tab_name_change(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.window_list[index-1].change > 0:
                self.ui.tabWidget.setTabText(
                    index, self.name_list[index-1]+"*")
                self.ui.tabWidget.setTabToolTip(
                    index, f'{self.path_list[index-1]}')

            elif self.window_list[index-1].change == 0:
                self.ui.tabWidget.setTabText(index, self.name_list[index-1])
                self.ui.tabWidget.setTabToolTip(
                    index, f'{self.path_list[index-1]}')

    def say_thanks(self):
        webhook_id = 'your webhook id'
        webhook_token = 'your webhook token'
        webhook_url = f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}'

        if self.ui.plainTextMessage.toPlainText():
            messeage = self.ui.plainTextMessage.toPlainText()
        else:
            messeage = 'Dear Joao Tapparo, Thank you for...'

        if self.ui.plainTextName.toPlainText():
            user = self.ui.plainTextName.toPlainText()
            note = {
                "content": f'{messeage}',
                "username": f'{user}'
            }
        else:
            note = {
                "content": f'{messeage}',
                "username": f'{self.name}'
            }

        try:
            requests.post(url=webhook_url, json=note, timeout=30)
            self.ui.plainTextMessage.setPlaceholderText(
                'Thank you for sending the notes. Your notes have been sent successfully.')
            logger.info('Notes have been sent successfully')
        except:
            self.ui.plainTextMessage.setPlaceholderText(
                'Oops! Something went wrong. Try again.')

    def example_1(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 1.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)

    def example_2(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 2.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)

    def example_3(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 3.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)

    def example_4(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 4.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)

    def example_5(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 5.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)

    def example_6(self):
        example_path = (os.path.join(self.current_directory,
                        'Demo', 'Example 6.trs'), "")
        logger.info('Example Path : %s', example_path)
        self.open_file(demopath=example_path, isdemo=True)


if __name__ == "__main__":
    start_time = time.time()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()

    screen = app.primaryScreen()
    screensize = (screen.size().width(), screen.size().height())

    logger.info('Screen size : %s', screensize)
    if screensize[0] != 1280:
        window.resize(screensize[0]*.9, screensize[1]*.9)
        x = screensize[0]*0.05
        window.move(x, 3)

    startUpTime = time.time() - start_time
    logger.info('Statup time : %.3f seconds' % startUpTime)
    sys.exit(app.exec_())
