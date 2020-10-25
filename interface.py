    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 329)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.check_pushButton = QtWidgets.QPushButton(Dialog)
        self.check_pushButton.setGeometry(QtCore.QRect(230, 250, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.check_pushButton.setFont(font)
        self.check_pushButton.setObjectName("check_pushButton")
        self.check_pushButton.clicked.connect(self.check_user)
        self.nomu_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.nomu_lineEdit.setGeometry(QtCore.QRect(200, 99, 211, 21))
        self.nomu_lineEdit.setObjectName("nomu_lineEdit")
        self.pass_lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit_2.setGeometry(QtCore.QRect(200, 180, 211, 21))
        self.pass_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit_2.setObjectName("pass_lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WOF login"))
        self.label.setText(_translate("Dialog", "Welcome to The War Of Words"))
        self.label_2.setText(_translate("Dialog", "Nom d\'utilisateur :"))
        self.label_3.setText(_translate("Dialog", "Mot de passe                  :"))
        self.check_pushButton.setText(_translate("Dialog", "Check"))
