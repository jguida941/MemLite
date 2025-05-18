#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MemLite v1.0.0 – Apple-style floating memory monitor for macOS

import os
import psutil
import time
import platform
from datetime import datetime
import threading

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QMenu, QFrame, QHBoxLayout
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QStackedLayout
from PyQt6.QtCore import (
    Qt, QTimer, QPoint, QUrl
)
from PyQt6.QtMultimedia import QSoundEffect

LOG_FILE = os.path.expanduser("~/Desktop/memory_log.txt")

def log_sys_info():
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")

        mem = psutil.virtual_memory()
        f.write(f"Total RAM: {mem.total / 1e9:.2f} GB\n")
        f.write(f"Used RAM: {mem.used / 1e9:.2f} GB ({mem.percent}%)\n")
        f.write(f"Available RAM: {mem.available / 1e9:.2f} GB\n")

        swap = psutil.swap_memory()
        f.write(f"Swap Used: {swap.used / 1e9:.2f} GB ({swap.percent}%)\n")

        f.write(f"CPU Usage: {psutil.cpu_percent()}%\n")
        f.write(f"Load Avg (1/5/15 min): {os.getloadavg()}\n")

        if platform.system() == "Darwin":
            gpu_info = os.popen("system_profiler SPDisplaysDataType | grep 'VRAM'").read()
            f.write(f"GPU VRAM Info: {gpu_info.strip()}\n")

        f.write(f"Captured on: {datetime.now()} | macOS {platform.mac_ver()[0]} | CPU: {platform.processor()}\n")
        f.flush()

def start_monitor():
    while True:
        log_sys_info()
        time.sleep(10)

threading.Thread(target=start_monitor, daemon=True).start()

class MemLiteWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.container = QFrame(self)
        self.container.setObjectName("MainFrame")
        container_layout = QVBoxLayout(self.container)

        self.setWindowTitle("MemLite v1.0.0")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("""
            QFrame#MainFrame {
                background-color: rgba(35, 35, 35, 210);
                border-radius: 24px;
                border: 2px solid rgba(255, 120, 30, 0.9);
            }

            QLabel {
                font-family: -apple-system, "Helvetica Neue", sans-serif;
                font-size: 17px;
                font-weight: 600;
                color: white;
                padding: 8px 20px;
                background-color: rgba(45, 45, 45, 180);
                border-radius: 12px;
                margin: 4px 8px;
                letter-spacing: 0.4px;
            }

            QPushButton {
                background-color: rgba(255, 120, 30, 0.6);
                color: white;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-radius: 10px;
                padding: 4px 10px;
                min-width: 22px;
            }

            QPushButton:hover {
                background-color: rgba(255, 180, 0, 0.9);
            }
        """)
        self.setWindowOpacity(0.93)
        self.resize(360, 260)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(255, 149, 0, 160))
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        self.setGraphicsEffect(shadow)

        layout = QVBoxLayout()
        container_layout.addLayout(layout)

        self.offset = QPoint()
        self.mouse_pressed = False
        self.alert_counter = 0

        # Button row (Apple-style: exit, minimize, settings)
        self.minimize_btn = QPushButton("")
        self.minimize_btn.setFixedSize(14, 14)
        # Remove per-button style, let stylesheet apply unified theme
        self.minimize_btn.clicked.connect(self.showMinimized)

        self.exit_btn = QPushButton("")
        self.exit_btn.setFixedSize(14, 14)
        self.exit_btn.clicked.connect(QApplication.quit)

        self.settings_btn = QPushButton("")
        self.settings_btn.setFixedSize(14, 14)
        self.settings_btn.clicked.connect(self.toggle_zoom)

        self.close_btn = QPushButton("–")
        self.close_btn.setFixedSize(20, 20)

        self.click_sound = QSoundEffect()
        self.click_sound.setSource(QUrl.fromLocalFile("click.wav"))
        self.click_sound.setVolume(0.25)
        self.close_btn.clicked.connect(lambda: (self.hide(), self.click_sound.play()))

        # Mac-style traffic light buttons (top left)
        self.exit_btn.setStyleSheet("background-color: #FF5F57; border: none; border-radius: 7px;")
        self.minimize_btn.setStyleSheet("background-color: #FFBD2E; border: none; border-radius: 7px;")
        self.settings_btn.setStyleSheet("background-color: #28C840; border: none; border-radius: 7px;")

        traffic_layout = QHBoxLayout()
        traffic_layout.setContentsMargins(10, 10, 10, 0)
        traffic_layout.setSpacing(6)
        traffic_layout.addWidget(self.exit_btn)
        traffic_layout.addWidget(self.minimize_btn)
        traffic_layout.addWidget(self.settings_btn)

        traffic_container = QWidget()
        traffic_container.setLayout(traffic_layout)

        container_layout.insertWidget(0, traffic_container, alignment=Qt.AlignmentFlag.AlignLeft)

        self.labels = {
            "ram": QLabel("RAM: --"),
            "cpu": QLabel("CPU: --"),
            "swap": QLabel("Swap: --"),
            "load": QLabel("Load: --")
        }

        for lbl in self.labels.values():
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(lbl)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_metrics)
        self.update_timer.start(3000)
        self.update_metrics()

        self.back_widget = QWidget()
        self.back_widget.setStyleSheet("background-color: rgba(30, 30, 30, 230); border-radius: 24px;")
        self.back_layout = QVBoxLayout(self.back_widget)
        self.back_layout.setContentsMargins(12, 12, 12, 12)

        self.return_btn = QPushButton("← Return")
        self.return_btn.setFixedSize(80, 28)
        self.return_btn.clicked.connect(self.flip_card)
        self.back_layout.addWidget(self.return_btn, alignment=Qt.AlignmentFlag.AlignTop)

        self.back_layout.addWidget(QLabel("Settings (coming soon)"))

        self.stack_layout = QStackedLayout(self)
        self.stack_layout.addWidget(self.container)
        self.stack_layout.addWidget(self.back_widget)
        self.stack_layout.setCurrentWidget(self.container)

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        always_on_top_action = menu.addAction("Toggle Always on Top")
        refresh_action = menu.addAction("Refresh Metrics")
        close_action = menu.addAction("Close Widget")
        action = menu.exec(event.globalPos())

        if action == always_on_top_action:
            current_flags = self.windowFlags()
            if current_flags & Qt.WindowType.WindowStaysOnTopHint:
                self.setWindowFlags(current_flags & ~Qt.WindowType.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(current_flags | Qt.WindowType.WindowStaysOnTopHint)
            self.show()
        elif action == refresh_action:
            self.update_metrics()
        elif action == close_action:
            self.close()

    def closeEvent(self, event):
        QApplication.quit()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.mouse_pressed = True
            event.accept()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False
        event.accept()

    def update_metrics(self):
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        cpu = psutil.cpu_percent()
        load = os.getloadavg()

        self.labels["ram"].setText(f"RAM Used: {mem.percent}% ({mem.used // 1e6:.0f} MB)")
        self.labels["cpu"].setText(f"CPU Usage: {cpu:.1f}%")
        self.labels["swap"].setText(f"Swap Used: {swap.percent}%")
        self.labels["load"].setText(f"Load Avg: {load[0]:.2f}, {load[1]:.2f}, {load[2]:.2f}")

        if swap.percent > 5 or cpu > 85:
            self.alert_counter += 1
        else:
            self.alert_counter = 0

        if self.alert_counter >= 5:  # ~15 seconds at 3s intervals
            print("⚠️ High system usage detected!")
            os.system("say 'System warning: memory or CPU is under pressure'")
            self.alert_counter = 0

    def flip_card(self):
        if self.stack_layout.currentWidget() == self.container:
            self.stack_layout.setCurrentWidget(self.back_widget)
        else:
            self.stack_layout.setCurrentWidget(self.container)

    def mouseDoubleClickEvent(self, event):
        self.flip_card()

    def toggle_zoom(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MemLiteWindow()
    win.show()
    sys.exit(app.exec())
