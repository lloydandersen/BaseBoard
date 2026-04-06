import customtkinter as ctk
from views.dashboard import DashBoardView

class BaseBoard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BaseBoard")
        self.minsize(width=700, height=700)

        self.current_view = None

        self.show_view(DashBoardView)

    def show_view(self, ViewClass):
        """Destroy current view if it exists and show new view"""
        if self.current_view is not None:
            self.current_view.destroy()

        self.current_view = ViewClass(self, self) # parent + controller
        self.current_view.grid(row=0, column=0, sticky="swen")



