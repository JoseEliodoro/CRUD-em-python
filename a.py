from customtkinter import *
from tkcalendar import DateEntry
from PIL import Image, ImageTk


color_text_toplevel = 'purple'
color_bg_toplevel = 'yellow'
color_bg_entry_toplevel = 'blue'
color_border_entry_top = 'white'
color_text_button_toplevel = 'pink'
color_bg_button_toplevel = 'red'
color_border_button_toplevel = 'green'
color_hover_button_toplevel = 'black'


self.window_edit = CTkToplevel(self.janela)
self.window_edit.title('clear')
self.window_edit.geometry('270x450')
self.window_edit.maxsize(width=300, height=500)
self.window_edit.minsize(width=270, height=400)
self.window_edit.config(background=color_bg_toplevel)


self.img = Image.open('logo2.png')
self.img = ImageTk.PhotoImage(self.img)
self.lb_img = CTkLabel(self.window_edit, image=self.img)
self.lb_img.place(relx=.15, rely=0.1)

self.specie_entry_edit = CTkEntry(self.window_edit, placeholder_text='Espécie',  text_color=color_text_toplevel,
                                fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                text_font='Arial 15')
self.specie_entry_edit.place(relx=0.05, rely=0.4, relwidth=0.9)


self.order_entry_edit = CTkEntry(self.window_edit, placeholder_text='Order',  text_color=color_text_toplevel,
                                fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                text_font='Arial 15')
self.order_entry_edit.place(relx=0.05, rely=0.5, relwidth=0.9)


self.location_entry_edit = CTkEntry(self.window_edit, placeholder_text='Local da coleta', text_color=color_text_toplevel,
                                fg_color=color_bg_entry_toplevel, border_color=color_border_entry_top,
                                text_font='Arial 15')
self.location_entry_edit.place(relx=0.05, rely=0.6, relwidth=0.9)

date_entry_edit = DateEntry(self.window_edit, font='Arial 15')
date_entry_edit.place(relx=0.05, rely=0.7, relwidth=0.9)

btn_add_edit = CTkButton(self.window_edit, text='Editar', text_font='Arial 15', cursor='hand2',
                    text_color=color_text_button_toplevel, fg_color=color_bg_button_toplevel,
                    border_color=color_border_button_toplevel, hover_color=color_hover_button_toplevel)
btn_add_edit.place(relx=0.35, rely=0.85, relwidth=0.45, height=35)



self.window_edit.grab_set()
self.window_edit.mainloop()