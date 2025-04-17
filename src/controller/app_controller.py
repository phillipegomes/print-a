from src.ui.event_window import EventWindow

class AppController:
    def __init__(self):
        self.current_window = None

    def start(self):
        self.open_event_window()

    def open_event_window(self):
        self.current_window = EventWindow(controller=self)
        self.current_window.show()
