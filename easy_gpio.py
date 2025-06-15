from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PyQt5.QtCore import QTimer
from easy_gpio_ui import Ui_MainWindow
import sys

class EasyGPIO(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.bank = 0
        self.group = 0
        self.pin = 0
        self.value = 0
        self.banks = [0x10000000, 0x20000000, 0x30000000, 0x40000000, 0x50000000]
        self.changed = True
        self.btgroup_bank = QButtonGroup(self)
        self.btgroup_bank.addButton(self.button_bank0, 0)
        self.btgroup_bank.addButton(self.button_bank1, 1)
        self.btgroup_bank.addButton(self.button_bank2, 2)
        self.btgroup_bank.addButton(self.button_bank3, 3)
        self.btgroup_bank.addButton(self.button_bank4, 4)
        self.btgroup_group = QButtonGroup(self)
        self.btgroup_group.addButton(self.button_groupA, 0)
        self.btgroup_group.addButton(self.button_groupB, 1)
        self.btgroup_group.addButton(self.button_groupC, 2)
        self.btgroup_group.addButton(self.button_groupD, 3)
        self.btgroup_pin = QButtonGroup(self)
        self.btgroup_pin.addButton(self.button_pin0, 0)
        self.btgroup_pin.addButton(self.button_pin1, 1)
        self.btgroup_pin.addButton(self.button_pin2, 2)
        self.btgroup_pin.addButton(self.button_pin3, 3)
        self.btgroup_pin.addButton(self.button_pin4, 4)
        self.btgroup_pin.addButton(self.button_pin5, 5)
        self.btgroup_pin.addButton(self.button_pin6, 6)
        self.btgroup_pin.addButton(self.button_pin7, 7)
        self.btgroup_value = QButtonGroup(self)
        self.btgroup_value.addButton(self.button_value0, 0)
        self.btgroup_value.addButton(self.button_value1, 1)
        self.btgroup_bank.buttonClicked[int].connect(self.slot_bank)
        self.btgroup_group.buttonClicked[int].connect(self.slot_group)
        self.btgroup_pin.buttonClicked[int].connect(self.slot_pin)
        self.btgroup_value.buttonClicked[int].connect(self.slot_value)
        self.button_bank0.setChecked(True)
        self.button_groupA.setChecked(True)
        self.button_pin0.setChecked(True)
        self.button_value0.setChecked(True)
        self.text_out.setReadOnly(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)

    def slot_bank(self, bank):
        # print(f"bank: {bank}")
        self.bank = bank
        self.changed = True

    def slot_group(self, group):
        # print(f"bank: {group}")
        self.group = group
        self.changed = True

    def slot_pin(self, pin):
        # print(f"bank: {pin}")
        self.pin = pin
        self.changed = True

    def slot_value(self, value):
        # print(f"bank: {value}")
        self.value = value
        self.changed = True

    def on_timer(self):
        if not self.changed:
            return
        pin = self.group * 8 + self.pin
        if pin < 16:
            low16 = True
        else:
            low16 = False
            pin = pin - 16
        value = self.value
        text = f"devmem {hex(self.banks[self.bank] + (0x0 if low16 else 0x4))} 32 0x{((value << pin) | 1 << (pin + 16)):08x}"
        self.text_out.setText(text)
        self.changed = False

app = QApplication(sys.argv)
ez = EasyGPIO()
ez.show()
sys.exit(app.exec_())
