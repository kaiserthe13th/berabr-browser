import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
import url_utils
from _init import Settings, stgdct
import json
import pyautogui as agui
# import PyQt5.QtWebEngine as WebEngine
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWebSockets import *

cookies = QWebEngineCookieStore

stg = Settings()

__version__ = "0.0.3"
__author__ = "Kerem Göksu"

class MainWindow(QMainWindow):
	def __init__(self):

		# ---

		super(MainWindow, self).__init__()
		self.browser = QWebEngineView()
		self.setWindowIcon(QIcon("img/Berabr-logo.png"))
		self.browser.setUrl(QUrl(stg.starting_page))
		self.setCentralWidget(self.browser)
		self.showMaximized()
		self.setToolButtonStyle(Qt.ToolButtonIconOnly)

		bkgc = self.bkgColor()
		urlbc = self.urlBarColor()
		itemc = self.itemColor()

		# navbar
		self.navbar = QToolBar()
		self.navbar.setStyleSheet(f"background-color: #{bkgc}; color: #{itemc}; padding: 10px;")
		self.navbar.setMovable(False)
		self.addToolBar(self.navbar)

		self.backBtn = QAction(QIcon(self.themeIcon("back")), 'Back', self)
		self.backBtn.triggered.connect(self.browser.back)
		self.navbar.addAction(self.backBtn)

		self.fwdBtn = QAction(QIcon(self.themeIcon("fwd")), 'Forward', self)
		self.fwdBtn.triggered.connect(self.browser.forward)
		self.navbar.addAction(self.fwdBtn)

		self.refreshBtn = QAction(QIcon(self.themeIcon("refresh")), 'Refresh', self)
		self.refreshBtn.triggered.connect(self.browser.reload)
		self.navbar.addAction(self.refreshBtn)

		self.homeBtn = QAction(QIcon(self.themeIcon("home")), 'Home', self)
		self.homeBtn.triggered.connect(self.navHome)
		self.navbar.addAction(self.homeBtn)

		self.urlBar = QLineEdit()
		self.urlBar.setStyleSheet(f"""
		background-color: #{urlbc};
		border-radius: 5px;
		height: 40px;
		padding-top: 0px;
		padding-bottom: 0px;
		""")
		self.urlBar.returnPressed.connect(self.navUrl)
		self.navbar.addWidget(self.urlBar)

		self.settingsBtn = QAction(QIcon(self.themeIcon("settings")), 'Settings', self)
		self.settingsBtn.triggered.connect(self.stgDialog)
		self.navbar.addAction(self.settingsBtn)

		self.browser.urlChanged.connect(self.updateUrl)

		# shortcuts

		self.shortcutbackBtn = QShortcut(QKeySequence("Alt+Left"), self)
		self.shortcutbackBtn.activated.connect(self.browser.back)

		self.shortcutbackBtn = QShortcut(QKeySequence("Alt+Right"), self)
		self.shortcutbackBtn.activated.connect(self.browser.forward)

		self.shortcutrefresh = QShortcut(QKeySequence("Ctrl+R"), self)
		self.shortcutrefresh.activated.connect(self.browser.reload)

	def themeIcon(self, icon):
		if icon == "settings":
			if stg.theme: return "img/settings-dark.png"
			elif not stg.theme: return "img/settings.png"
		elif icon == "refresh":
			if stg.theme: return "img/refresh-dark.png"
			elif not stg.theme: return "img/refresh.png"
		elif icon == "back":
			if stg.theme: return "img/keyboard_arrow_left-dark.png"
			elif not stg.theme: return "img/keyboard_arrow_left.png"
		elif icon == "fwd":
			if stg.theme: return "img/keyboard_arrow_right-dark.png"
			elif not stg.theme: return "img/keyboard_arrow_right.png"
		elif icon == "home":
			if stg.theme: return "img/home-dark.png"
			elif not stg.theme: return "img/home.png"

	def itemColor(self):
		if stg.theme == True:
			return "ffffff"
		return "000000"

	def bkgColor(self):
		if stg.theme == True:
			return "404F4A"
		return "DAE7E3"
	
	def urlBarColor(self):
		if stg.theme == True:
			return "497969"
		return "EBEFEE"

	def navHome(self):
		self.browser.setUrl(QUrl(stg.home))

	def navUrl(self):
		url = self.urlBar.text()
		url = url_utils.confUrl(QUrl(url), url)
		self.browser.setUrl(QUrl(url))

	def updateUrl(self, q):
		self.urlBar.setText(q.toString())
	
	def stgDialog(self, checked):
		def updateTheme():
			stg.theme = self.themechkbox.isChecked()
			stgdct["theme"] = self.themechkbox.isChecked()
			with open("settings.json", "w") as f: f.write(json.dumps(stgdct))
			self.settingsBtn.setIcon(QIcon(self.themeIcon("settings")))
			self.refreshBtn.setIcon(QIcon(self.themeIcon("refresh")))
			self.backBtn.setIcon(QIcon(self.themeIcon("back")))
			self.fwdBtn.setIcon(QIcon(self.themeIcon("fwd")))
			self.homeBtn.setIcon(QIcon(self.themeIcon("home")))
			if stg.theme == False:
				self.urlBar.setStyleSheet(f"""
				background-color: #ebefee;
				border-radius: 5px;
				height: 40px;
				padding-top: 0px;
				padding-bottom: 0px;
				""")
				self.navbar.setStyleSheet(f"background-color: #dae7e3; color: #000000; padding: 10px;")
			elif stg.theme == True:
				self.urlBar.setStyleSheet(f"""
				background-color: #497969;
				border-radius: 5px;
				height: 40px;
				padding-top: 0px;
				padding-bottom: 0px;
				""")
				self.navbar.setStyleSheet(f"background-color: #404f4a; color: #ffffff; padding: 10px;")

		def updateHomePage():
			NEW_HOME = self.homepage.text()
			print(NEW_HOME)
			stg.home = NEW_HOME
			stgdct["home"] = NEW_HOME
			with open("settings.json", "w") as f: f.write(json.dumps(stgdct))

		def updateAll():
			updateHomePage()
			updateTheme()

		self.stgdlg = QWidget()
		self.stgdlg.setWindowIcon(QIcon("img/Berabr-logo.png"))
		self.stgdlg.setWindowTitle("Settings")
		self.stgdlg.setFixedWidth(400)
		self.stgdlg.setMaximumHeight(600)
		header = QLabel("<h1>Settings</h1>")
		self.themechkbox = QCheckBox("Dark Mode")
		self.homepage = QLineEdit()

		self.savebutton = QPushButton(QIcon("img/save.png"), "Save")

		layout = QVBoxLayout()

		layout.addWidget(header)
		layout.addWidget(self.themechkbox)
		
		homebox = QHBoxLayout()

		homebox.addWidget(QLabel("Homepage:"))
		homebox.addWidget(self.homepage)
		layout.addLayout(homebox)

		layout.addWidget(self.savebutton)

		#Config Widgets
		self.themechkbox.setChecked(stg.theme)

		self.themechkbox.toggled.connect(updateTheme)

		self.savebutton.toggled.connect(updateAll)

		self.homepage.setText(stg.home)

		self.stgdlg.setLayout(layout)
		self.stgdlg.show()
		# self.stgdlg.exec_()

	def hello(self):
		print("Hello, World!")

app = QApplication(sys.argv)
QApplication.setApplicationName('Berabr Browser')
QApplication.setApplicationVersion("0.0.3")
app.setWindowIcon(QIcon("img/Berabr-logo.png"))
window = MainWindow()
app.exec_()
