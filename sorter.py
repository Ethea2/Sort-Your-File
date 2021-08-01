import shutil
import os
from tkinter import *
from tkinter import messagebox

current_dir = os.getcwd()

def choose_dir():
	chosen_dir = dir_box.get("1.0", 'end-1c')
	os.chdir(f'{chosen_dir}')

def sort_dir():
	downloaded_files = os.listdir()
	chosen_dir = str(dir_box.get("1.0", 'end-1c'))
	sure_popup = messagebox.askquestion("Sort This Directory", f"Are you sure you want to {chosen_dir}?")
	if sure_popup == 'yes':	
		for file in downloaded_files:
			if '.' not in file:
				print(f'{file} does not have an extension or is a folder')
			elif '.' in file:	
				for i, letter in enumerate(file):
					if letter == '.':
						file_name, file_extension = os.path.splitext(file)
						file_folder = file_extension[1:]
						if not os.path.isdir(file_folder):
							os.mkdir(file_folder)
						else:
							pass
						shutil.move(file, file_folder)
						print(f"{file} is successfully transferred to {file_folder}")
						break
			else:
				pass


window = Tk()
window.wm_title("File Sorter by Nathan!")

dir_chooser = StringVar()
dir_chooser.set("Choose a directory")
dir_chosen = Label(window, textvariable=dir_chooser, height=2, width=20)
dir_chosen.grid(row=0, column=0)

dir_box = Text(window, height=1)
dir_box.grid(row=0, column=1)
dir_box.insert(END, current_dir)

sort_button = Button(window, text="Sort!", height=1, width=20, command=sort_dir)
sort_button.grid(row=1, column=1)

choose_button = Button(window, text="Choose this directory", height=1, width=20, command=choose_dir)
choose_button.grid(row=0, column=2)

window.mainloop()