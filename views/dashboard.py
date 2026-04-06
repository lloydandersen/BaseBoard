import customtkinter as ctk

class DashBoardView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        # Side panel
        side_panel = ctk.CTkFrame(self)

        settings_icon = ctk.CTkButton(side_panel, text="Settings")
        settings_icon.grid(row=0, column=0, sticky="sew")