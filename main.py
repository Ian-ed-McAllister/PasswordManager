import random
import tkinter
import tkinter.messagebox
import customtkinter
import string
import pyperclip

customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    width = 820
    height = 520
    numberChar = 10
    password = ''


    def __init__(self):
            super().__init__()

            self.title("Password manager")
            self.geometry(f"{App.width}x{App.height}")

            self.grid_columnconfigure(1,weight=1)
            self.grid_columnconfigure((2,3),weight=0)
            self.grid_rowconfigure((0,1,2),weight=1)

            self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Password Manager",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,
                                                            text="generate passowrd")



            self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
            self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
            self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                           values=["Light", "Dark", "System"],
                                                                           command=self.change_appearance_mode_event)
            self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

            self.password_generator_frame = customtkinter.CTkFrame(self)
            self.password_generator_frame.grid(row=0,rowspan=7,column=1,columnspan=3,padx=(20,20),pady=(20,20),sticky="nsew")

            self.slider_1 = customtkinter.CTkSlider(self.password_generator_frame, from_=1, to=25, number_of_steps=25,command=self.update_number_chars)
            self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

            self.number_of_chars_label = customtkinter.CTkLabel(self.password_generator_frame,text=f"Number of characters:{self.numberChar}")
            self.number_of_chars_label.grid(column=1,row=3,padx=(20, 10), pady=(10, 10))


            self.include_numbers_check = customtkinter.CTkCheckBox(self.password_generator_frame,
                                                                   text="Include numbers",
                                                                   command=self.generate_password)
            self.include_numbers_check.grid(column=0,row=4,padx=(20, 10), pady=(10, 10))
            self.include_numbers_check.select()

            self.include_special_check = customtkinter.CTkCheckBox(self.password_generator_frame,
                                                                   text="Include Special Characters",
                                                                   command=self.generate_password)
            self.include_special_check.grid(column=1, row=4, padx=(20, 10), pady=(10, 10))
            self.include_special_check.select()



            self.output_label = customtkinter.CTkLabel(self.password_generator_frame,text=self.password)
            self.output_label.grid(row=5,column=0, padx=(20, 10), pady=(10, 10))

            self.copy_button = customtkinter.CTkButton(self.password_generator_frame,text="copy password", command=self.copy_password)
            self.copy_button.grid(row=5,column=1,padx=(20, 10), pady=(10, 10))
            self.generate_password()




    #will be used later to change the frame to see all passwords
    def sidebar_button_event(self):
        print("sidebar_button click")

    def copy_password(self):
        pyperclip.copy(self.password)
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def generate_password(self):

        mychars = string.ascii_letters
        if self.include_numbers_check.get():
            mychars += string.digits
        if self.include_special_check.get():
            mychars += string.punctuation
        self.password = ''.join(random.choice(mychars) for i in range(self.numberChar))
        self.output_label.configure(text=self.password)


    def update_number_chars(self,value):

        self.numberChar = int(value)
        self.number_of_chars_label.configure(text=f"Number of characters:{self.numberChar}")
        self.generate_password()







if __name__ == "__main__":
    app = App()
    app.mainloop()