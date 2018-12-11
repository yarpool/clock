import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLCDNumber
from PyQt5.QtCore import QTime, QTimer


class MyWidget(QMainWindow):

    def __init__(self):

        super().__init__()
        uic.loadUi('design.ui', self)
        LIST_OF_TIME_ZONES = ['(UTC−12)',
                              'Ниуэ (UTC−11)',
                              'США(Гавайи) (UTC−10)',
                              'США(Аляска) (UTC−9)',
                              'североамериканское тихоокеанское время\
                              (UTC-8)',
                              'горное время (UTC-7)',
                              'центральноамериканское время (UTC-6)',
                              'североамериканское восточное время\
                              (UTC-5)',
                              'атлантическое время (UTC-4)',
                              'Канада (Ньюфаундленд) (UTC−3:30)',
                              'южноамериканское восточное время (UTC-3)',
                              'среднеатлантическое время (UTC-2)',
                              'Азорские острова (UTC−1)',
                              'западноафриканское время (UTC+0)',
                              'центральноевропейское время (UTC+1)',
                              'восточноевропейское время (UTC+2)',
                              'московское время (UTC+3)',
                              'Иран (UTC+3:30) ',
                              'самарское время (UTC+4)',
                              'Афганистан (UTC+4:30)',
                              'екатеринбургское время (UTC+5)',
                              'Индия (UTC+5:30)',
                              'Непал (UTC+5:45)',
                              'омское время (UTC+6)',
                              'Мьянма (UTC+6:30)',
                              'красноярское время (UTC+7)',
                              'иркутское время (UTC+8)',
                              'Австралия (UTC+8:45)',
                              'якутское время (UTC+9)',
                              'Австралия (UTC+9:30)',
                              'владивостокское время (UTC+10)',
                              'Австралия (UTC+10:30)',
                              'магаданское время (UTC+11)',
                              'камчатское время (UTC+12)',
                              'Новая Зеландия (UTC+12:45)',
                              'Тонга (UTC+13)',
                              'Кирибати (UTC+14)',
                              ]

        self.time_edit_1.move(30, 180)
        self.time_edit_1.resize(190, 20)
        self.time_edit_2.move(280, 180)
        self.time_edit_2.resize(190, 20)
        self.time_edit_3.move(510, 180)
        self.time_edit_3.resize(190, 20)
        self.time_edit_1.addItems(LIST_OF_TIME_ZONES)
        self.time_edit_2.addItems(LIST_OF_TIME_ZONES)
        self.time_edit_3.addItems(LIST_OF_TIME_ZONES)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.Time_1.display(text)
        self.Time_2.display(text)
        self.Time_3.display(text)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
