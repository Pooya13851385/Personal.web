# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 07:05:35 2025

@author: PC
"""

import tkinter as tk
from tkinter import messagebox

tasks = []

def add_KarHa():
    def add_KarHa_winow():
        work = task_e.get()
        if work:
            tasks.append({"title": work, "status": "Anjam Nashodeh"})
            messagebox.showinfo("Success", f"work '{work}' added!")
            update_list_KarHa()
            win.destroy()
        else:
            messagebox.showerror("Error", "Enter a work!")
    win = tk.Toplevel(root)
    win.title("Add")
    tk.Label(win, text="Enter work:").grid(row=0, column=0, padx=5, pady=5)
    task_e = tk.Entry(win)
    task_e.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(win, text="Add work", command=add_KarHa_winow).grid(row=1, column=0, columnspan=2, pady=10)

def list_KarHa():
    update_list_KarHa()

def delete_KarHa():
    def delete_KarHa_winow():
        Entekhab_work = work_list_del.curselection()
        if Entekhab_work:
            task_del = Entekhab_work[0]
            deleted_task = tasks.pop(task_del)
            messagebox.showinfo("Success", f"work '{deleted_task['title']}' delete!")
            update_list_KarHa()
            del_window.destroy()
        else:
            messagebox.showerror("Error", "selec a work!")

    del_window = tk.Toplevel(root)
    del_window.title("delete work")
    
    tk.Label(del_window, text="select work to delete:").grid(row=0, column=0, padx=5, pady=5)
    
    work_list_del = tk.Listbox(del_window, width=40, height=10)
    work_list_del.grid(row=1, column=0, padx=5, pady=5)
    
    for index, task in enumerate(tasks):
        work_list_del.insert(tk.END, f"work #{index}: {task['title']} - {task['status']}")

    tk.Button(del_window, text="delete", command=delete_KarHa_winow).grid(row=2, column=0, pady=10)

def KarHaye_Anjam_Shode():
    def Anjam_Shode_win():
          Entekhab_work = work_list_mark.curselection()
          if Entekhab_work:
              task_mark = Entekhab_work[0]
              tasks[task_mark]["status"] = "Anjam Shode"
              messagebox.showinfo("Success", f"work #{task_mark} ('{tasks[task_mark]['title']}') completed!")
              update_list_KarHa()
              mark_window.destroy()
          else:
              messagebox.showerror("Error", "Select a work!")
    mark_window = tk.Toplevel(root)
    mark_window.title("work Completed")
    tk.Label(mark_window, text="Select work to completed:").grid(row=0, column=0, padx=5, pady=5)
    work_list_mark = tk.Listbox(mark_window, width =40, height= 10)
    work_list_mark.grid(row=1, column=0, padx=5, pady=5)
    for index, task in enumerate(tasks):
            work_list_mark.insert(tk.END, f"work #{index}: {task['title']} - Status: {task['status']}")
    tk.Button(mark_window, text="work Completed", command=Anjam_Shode_win).grid(row=2, column=0, pady=10)

def update_list_KarHa():
    work_list.delete(0,tk.END)
    for index, task in enumerate(tasks):
        work_list.insert(tk.END, f"work #{index}: {task['title']} - Status: {task['status']}")

def Quit_Barname():
    if messagebox.askyesno("Quit", "Quit the program?"):
        root.destroy()

if __name__=="__main__":
    root = tk.Tk()
    root.title("Mahdi Golbang To Do List App")
    root.geometry("600x400")

    add_button = tk.Button(root, text="Add New Work", command= add_KarHa)
    add_button.pack(pady=10)

    delete_button = tk.Button(root, text="Delete Work ", command=delete_KarHa)
    delete_button.pack(pady=10)

    mark_Anjam_Shode_button = tk.Button(root, text=" Completed Works", command=KarHaye_Anjam_Shode)
    mark_Anjam_Shode_button.pack(pady=10)

    tk.Label(root, text="Works:").pack()
    work_list = tk.Listbox(root, width = 70, height=10)
    work_list.pack(pady=10)
    update_list_KarHa()

    quit_button = tk.Button(root, text="Quit", command=Quit_Barname)
    quit_button.pack(pady=10)

    root.mainloop()
  