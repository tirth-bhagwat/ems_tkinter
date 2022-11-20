import datetime
import re
import tkinter as tk
from tkinter import ttk, messagebox
from emsdb import Database

FGCOLOR_002 = "#000"
FONTFACE_002 = "Monospace"

db_002 = Database("./employee.db")
root_002 = tk.Tk()

root_002.title("Employee Management System")
root_002.geometry(f"{root_002.winfo_screenwidth()}x{root_002.winfo_screenheight()}")

mode_002 = "View"
selected_employee_id_002 = None


def validate_002():
    global mode_002, selected_employee_id_002
    for i in entry_list_002:
        if type(i) == tk.Entry:
            if i.get().strip() == "":
                messagebox.showerror("Error", "All fields are mandatory")
                i.focus()
                return False
        elif type(i) == tk.Text:
            if i.get(1.0, tk.END).strip() == "":
                messagebox.showerror("Error", "All fields are mandatory")
                i.focus()
                return False

        elif type(i) == ttk.Combobox:
            if i.get().strip() == "":
                messagebox.showerror("Error", "All fields are mandatory")
                i.focus()
                return False

    if re.fullmatch(r"[a-zA-z .]+", txt_name_002.get().strip()) is None:
        messagebox.showerror("Error", "Invalid Name")
        txt_name_002.focus()
        return False

    if not txt_age_002.get().strip().isnumeric():
        messagebox.showerror("Error", "Invalid Age")
        txt_age_002.focus()
        return False

    if (
        re.fullmatch(
            r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+", txt_email_002.get().strip()
        )
        is None
    ):
        messagebox.showerror("Error", "Invalid email")
        txt_email_002.focus()
        return False
    if cmb_designation_002.get().strip().capitalize() not in [
        "Manager",
        "Engineer",
        "Senior engineer",
        "Operator",
    ]:
        messagebox.showerror("Error", "Invalid designation")
        cmb_designation_002.focus()
        return False

    try:
        datetime.datetime.strptime(txt_doj_002.get().strip(), "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date")
        txt_doj_002.focus()
        return False

    if cmb_gender_002.get().strip().capitalize() not in ["Male", "Female"]:
        messagebox.showerror("Error", "Invalid gender")
        cmb_gender_002.focus()
        return False

    if (
        not txt_contact_002.get().strip().isnumeric()
        or len(txt_contact_002.get().strip()) != 10
    ):
        messagebox.showerror("Error", "Invalid contact")
        txt_contact_002.focus()
        return False

    if len(db_002.fetch_by_contact_002(txt_contact_002.get().strip())) > 0:
        if mode_002 == "Add":
            messagebox.showerror("Error", "Contact already exists")
            txt_contact_002.focus()
            return False
        elif mode_002 == "Edit":
            if (
                db_002.fetch_by_contact_002(txt_contact_002.get().strip())[0][0]
                != selected_employee_id_002
            ):
                messagebox.showerror("Error", "Contact already exists")
                txt_contact_002.focus()
                return False

    if len(db_002.fetch_by_email_002(txt_email_002.get().strip())) > 0:
        if mode_002 == "Add":
            messagebox.showerror("Error", "Email already exists")
            txt_email_002.focus()
            return False
        elif mode_002 == "Edit":
            if (
                db_002.fetch_by_email_002(txt_email_002.get().strip())[0][0]
                != selected_employee_id_002
            ):
                messagebox.showerror("Error", "Email already exists")
                txt_email_002.focus()
                return False

    return True


def add_click_002():
    global mode_002, selected_employee_id_002
    for i in entry_list_002:
        i.config(state=tk.NORMAL)
        if type(i) == tk.Entry:
            i.delete(0, tk.END)
        elif type(i) == tk.Text:
            i.delete(1.0, tk.END)
        elif type(i) == ttk.Combobox:
            i.set("")

    mode_002 = "Add"
    btn_save_002.config(state=tk.NORMAL)
    btn_cancel_002.config(state=tk.NORMAL)
    btn_add_002.config(state=tk.DISABLED)
    btn_edit_002.config(state=tk.DISABLED)
    btn_delete_002.config(state=tk.DISABLED)
    selected_employee_id_002 = None

    tree_002.config(selectmode=tk.NONE)
    txt_name_002.focus_set()


def edit_click_002():
    global mode_002, selected_employee_id_002
    if selected_employee_id_002 is None:
        messagebox.showerror("Error", "No employee selected")
        return

    for i in entry_list_002:
        i.config(state=tk.NORMAL)

    mode_002 = "Edit"
    btn_save_002.config(state=tk.NORMAL)
    btn_cancel_002.config(state=tk.NORMAL)
    btn_add_002.config(state=tk.DISABLED)
    btn_edit_002.config(state=tk.DISABLED)
    btn_delete_002.config(state=tk.DISABLED)

    tree_002.config(selectmode=tk.NONE)
    txt_name_002.focus()


def cancel_click_002():
    global mode_002, selected_employee_id_002
    for i in entry_list_002:
        i.config(state=tk.DISABLED)
        if type(i) == tk.Entry:
            i.config(disabledbackground="white", disabledforeground="black")
            i.delete(0, tk.END)
        elif type(i) == tk.Text:
            i.delete(1.0, tk.END)
        elif type(i) == ttk.Combobox:
            i.set("")

    mode_002 = "View"
    btn_cancel_002.config(state=tk.DISABLED)
    btn_save_002.config(state=tk.DISABLED)
    btn_add_002.config(state=tk.NORMAL)
    btn_edit_002.config(state=tk.NORMAL)
    btn_delete_002.config(state=tk.NORMAL)

    tree_002.config(selectmode=tk.BROWSE)
    tree_002.selection_remove(tree_002.selection())
    selected_employee_id_002 = None


def delete_click_002():
    global selected_employee_id_002
    if selected_employee_id_002 is None:
        messagebox.showerror("Error", "No employee selected")
        return
    if messagebox.askyesno("Delete", "Are you sure you want to delete?"):
        db_002.delete_002(selected_employee_id_002)
        messagebox.showinfo("Success", "Employee deleted successfully")

        for i in entry_list_002:
            i.config(state=tk.DISABLED)
            if type(i) == tk.Entry:
                i.config(disabledbackground="white", disabledforeground="black")
                i.delete(0, tk.END)
                i.delete(0, tk.END)
            elif type(i) == tk.Text:
                i.delete(1.0, tk.END)
            elif type(i) == ttk.Combobox:
                i.set("")

    reload_grid_002()
    selected_employee_id_002 = None
    tree_002.selection_remove(tree_002.selection())
    tree_002.config(selectmode=tk.BROWSE)


def save_click_002():
    global mode_002, selected_employee_id_002

    if not validate_002():
        return

    for i in entry_list_002:
        i.config(state=tk.DISABLED)

    if mode_002 == "Add":
        db_002.insert_002(
            name=txt_name_002.get().strip(),
            age=txt_age_002.get().strip(),
            email=txt_email_002.get().strip(),
            designation=cmb_designation_002.get().strip().capitalize(),
            doj=txt_doj_002.get().strip(),
            gender=cmb_gender_002.get().strip().capitalize(),
            contact=txt_contact_002.get().strip(),
            address=txt_address_002.get(1.0, tk.END).strip(),
        )
        messagebox.showinfo("Success", "Employee added successfully")
        tree_002.selection_remove(tree_002.selection())
        tree_002.config(selectmode=tk.BROWSE)
        selected_employee_id_002 = None

    elif mode_002 == "Edit":
        db_002.update_002(
            id=selected_employee_id_002,
            name=txt_name_002.get().strip(),
            age=txt_age_002.get().strip(),
            email=txt_email_002.get().strip(),
            designation=cmb_designation_002.get().strip().capitalize(),
            doj=txt_doj_002.get().strip(),
            gender=cmb_gender_002.get().strip().capitalize(),
            contact=txt_contact_002.get().strip(),
            address=txt_address_002.get(1.0, tk.END).strip(),
        )
        messagebox.showinfo("Success", "Employee updated successfully")
        tree_002.selection_remove(tree_002.selection())
        tree_002.config(selectmode=tk.BROWSE)
        selected_employee_id_002 = None

    mode_002 = "View"
    btn_cancel_002.config(state=tk.DISABLED)
    btn_save_002.config(state=tk.DISABLED)
    btn_add_002.config(state=tk.NORMAL)
    btn_edit_002.config(state=tk.NORMAL)
    btn_delete_002.config(state=tk.NORMAL)

    reload_grid_002()


def reload_grid_002():
    for i in tree_002.get_children():
        tree_002.delete(i)
    for row in db_002.fetch_all_002():
        tree_002.insert("", tk.END, values=row)


def load_to_form_002(event: tk.Event):
    global selected_employee_id_002
    for i in entry_list_002:
        i.config(state=tk.NORMAL)
        if type(i) == tk.Entry:
            i.config(disabledbackground="white", disabledforeground="black")
            i.delete(0, tk.END)
        elif type(i) == tk.Text:
            i.delete(1.0, tk.END)
        elif type(i) == ttk.Combobox:
            i.set("")

    row = tree_002.item(tree_002.selection())["values"]
    if len(row) != 9:
        selected_employee_id_002 = None
        for i in entry_list_002:
            i.config(state=tk.DISABLED)
        return
    txt_name_002.insert(0, row[1])
    txt_age_002.insert(0, row[2])
    txt_email_002.insert(0, row[3])
    cmb_designation_002.set(row[4])
    txt_doj_002.insert(0, row[5])
    cmb_gender_002.set(row[6])
    txt_contact_002.insert(0, row[7])
    txt_address_002.insert(1.0, row[8])

    selected_employee_id_002 = int(row[0])

    for i in entry_list_002:
        i.config(state=tk.DISABLED)


form_frame_002 = tk.Frame(root_002)
button_frame_002 = tk.Frame(root_002)
tree_frame_002 = tk.Frame(root_002)


lbl_name_002 = tk.Label(
    form_frame_002, text="Name", fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
txt_name_002 = tk.Entry(
    form_frame_002, fg=FGCOLOR_002, font=(FONTFACE_002, 12), width=30
)
lbl_name_002.grid(row=0, column=0, padx=15, pady=5, sticky=tk.E)
txt_name_002.grid(row=0, column=1, padx=15, pady=5, sticky=tk.W)

lbl_age_002 = tk.Label(
    form_frame_002, text="Age", fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
txt_age_002 = tk.Entry(form_frame_002, fg=FGCOLOR_002, font=(FONTFACE_002, 12))
lbl_age_002.grid(row=0, column=2, padx=15, pady=5, sticky=tk.E)
txt_age_002.grid(row=0, column=3, padx=15, pady=5, sticky=tk.W)

lbl_email_002 = tk.Label(
    form_frame_002,
    text="Email",
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
txt_email_002 = tk.Entry(
    form_frame_002, fg=FGCOLOR_002, font=(FONTFACE_002, 12), width=30
)
lbl_email_002.grid(row=1, column=0, padx=15, pady=5, sticky=tk.E)
txt_email_002.grid(row=1, column=1, padx=15, pady=5, sticky=tk.W)

lbl_designation_002 = tk.Label(
    form_frame_002, text="Designation", fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
cmb_designation_002 = ttk.Combobox(
    form_frame_002,
    values=["Manager", "Engineer", "Senior engineer", "Operator"],
    foreground=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
lbl_designation_002.grid(row=1, column=2, padx=15, pady=5, sticky=tk.E)
cmb_designation_002.grid(row=1, column=3, padx=15, pady=5, sticky=tk.W)

lbl_contact_002 = tk.Label(
    form_frame_002,
    text="Contact",
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
txt_contact_002 = tk.Entry(
    form_frame_002, fg=FGCOLOR_002, font=(FONTFACE_002, 12), width=30
)
lbl_contact_002.grid(row=2, column=0, padx=15, pady=5, sticky=tk.E)
txt_contact_002.grid(row=2, column=1, padx=15, pady=5, sticky=tk.W)

lbl_gender_002 = tk.Label(
    form_frame_002, text="Gender", fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
cmb_gender_002 = ttk.Combobox(
    form_frame_002,
    values=["Male", "Female"],
    foreground=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
lbl_gender_002.grid(row=2, column=2, padx=15, pady=5, sticky=tk.E)
cmb_gender_002.grid(row=2, column=3, padx=15, pady=5, sticky=tk.W)

lbl_address_002 = tk.Label(
    form_frame_002, text="Address", fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
txt_address_002 = tk.Text(
    form_frame_002, height=5, width=30, fg=FGCOLOR_002, font=(FONTFACE_002, 12)
)
lbl_address_002.grid(row=3, column=0, padx=15, pady=5, sticky=tk.NE)
txt_address_002.grid(row=3, column=1, padx=15, pady=5, sticky=tk.NW)

lbl_doj_002 = tk.Label(
    form_frame_002,
    text="Date of Joining",
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
txt_doj_002 = tk.Entry(form_frame_002, fg=FGCOLOR_002, font=(FONTFACE_002, 12))
lbl_doj_002.grid(row=3, column=2, padx=15, pady=5, sticky=tk.NE)
txt_doj_002.grid(row=3, column=3, padx=15, pady=5, sticky=tk.NW)

btn_add_002 = tk.Button(
    button_frame_002,
    text="Add",
    command=add_click_002,
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
btn_add_002.grid(row=8, column=0, padx=5, pady=5)


btn_edit_002 = tk.Button(
    button_frame_002,
    text="Edit",
    command=edit_click_002,
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
btn_edit_002.grid(row=8, column=1, padx=5, pady=5)


btn_save_002 = tk.Button(
    button_frame_002,
    text="Save",
    command=save_click_002,
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
btn_save_002.grid(row=8, column=2, padx=5, pady=5)


btn_delete_002 = tk.Button(
    button_frame_002,
    text="Delete",
    command=delete_click_002,
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
btn_delete_002.grid(row=8, column=3, padx=5, pady=5)


btn_cancel_002 = tk.Button(
    button_frame_002,
    text="Cancel",
    command=cancel_click_002,
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
)
btn_cancel_002.grid(row=8, column=4, padx=5, pady=5)


tree_002 = ttk.Treeview(
    tree_frame_002,
    columns=(1, 2, 3, 4, 5, 6, 7, 8, 9),
)

tree_002.heading("#1", text="ID")
tree_002.heading("#2", text="Name")
tree_002.heading("#3", text="Age")
tree_002.heading("#4", text="Email")
tree_002.heading("#5", text="Designation")
tree_002.heading("#6", text="Date of Joining")
tree_002.heading("#7", text="Gender")
tree_002.heading("#8", text="Contact")
tree_002.heading("#9", text="Address")

tree_002.column("#1", minwidth=50, width=50, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#2", anchor=tk.CENTER, stretch=tk.YES)
tree_002.column("#3", minwidth=75, width=75, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#4", anchor=tk.CENTER, stretch=tk.YES)
tree_002.column("#5", minwidth=125, width=125, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#6", minwidth=100, width=100, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#7", minwidth=75, width=75, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#8", minwidth=100, width=100, anchor=tk.CENTER, stretch=tk.NO)
tree_002.column("#9", anchor=tk.CENTER, stretch=tk.YES)

tree_002["show"] = "headings"
# tree_002.bind("<ButtonRelease-1>", load_to_form)
tree_002.bind("<<TreeviewSelect>>", load_to_form_002)
tree_002.pack(expand=True, fill="both")


entry_list_002 = [
    txt_name_002,
    txt_age_002,
    txt_email_002,
    cmb_designation_002,
    txt_doj_002,
    cmb_gender_002,
    txt_contact_002,
    txt_address_002,
]


form_frame_002.pack()
button_frame_002.pack()
tree_frame_002.pack(fill="both", expand=True)

footer_frame_002 = tk.Frame(root_002)
lbl_footer_name_002 = tk.Label(
    footer_frame_002,
    text="Created by : Tirth Bhagwat - 21C22002",
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
    anchor=tk.W,
)
lbl_footer_name_002.pack(fill=tk.X, anchor=tk.W, side=tk.LEFT)
lbl_footer_branch_002 = tk.Label(
    footer_frame_002,
    text="B.Tech CSE (AI) Sem-3",
    fg=FGCOLOR_002,
    font=(FONTFACE_002, 12),
    anchor=tk.W,
)
lbl_footer_branch_002.pack(fill=tk.X, anchor=tk.W, side=tk.RIGHT)
footer_frame_002.pack(fill=tk.X, pady=5)

btn_cancel_002.config(state=tk.DISABLED)
btn_save_002.config(state=tk.DISABLED)

for i in entry_list_002:
    i.config(state=tk.DISABLED)
    if type(i) == tk.Entry:
        i.config(disabledbackground="white", disabledforeground="black")
        i.delete(0, tk.END)
    elif type(i) == tk.Text:
        i.delete(1.0, tk.END)
    elif type(i) == ttk.Combobox:
        i.set("")

reload_grid_002()

root_002.mainloop()
