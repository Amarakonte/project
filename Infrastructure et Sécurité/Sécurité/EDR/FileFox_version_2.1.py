import os
import pwd
import grp
import logging 
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from multiprocessing import Process

path_list = []
path_file = ""
user_list = []
group_list = []
now = datetime.now()
current_time = now.strftime("%Y%m%d_%H%M%S")
log_file = f"/tmp/filefox_{current_time}.log"
script_path = __file__
script_dir = os.path.dirname(__file__)

# Initiation du fichier de journalisation ainsi que du style des logs
logging.basicConfig(filename=log_file,
                    filemode='a',
                    level=logging.INFO,
                    format="\n%(asctime)s - %(message)s",
                    datefmt='%Y-%m-%d %H:%M:%S')

logging.info(f"Lancement en cours ...")

# Fonctionalites de detection des evenements systeme (creation, suppression, modification et deplacement)
class CustomLoggingEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.directories = {}
        super().__init__()
    
    def on_created(self, event):
        src_path = event.src_path
        username = get_username(src_path)
        if os.path.isfile(event.src_path):
            filename = os.path.basename(event.src_path)
            dirname = os.path.dirname(event.src_path)
            logging.info(f"L'utilisateur - {username} - a creer le fichier - {filename} - dans le dossier - {dirname}")
        
        if os.path.isdir(event.src_path):
            dirname = os.path.dirname(event.src_path)
            logging.info(f"L'utilisateur - {username} - a creer le dossier - {dirname}")

    def on_moved(self, event):
        src_path = event.src_path
        dest_path = event.dest_path
        username = get_username(dest_path)
        if os.path.isfile(event.dest_path):
            logging.info(f"L'utilisateur - {username} - a deplacer le fichier - {event.src_path} - vers - {event.dest_path}")
        
        if os.path.isdir(event.dest_path):
            logging.info(f"L'utilisateur - {username} - a deplacer le dossier - {event.src_path} - vers - {event.dest_path}")
	
    def on_deleted(self, event):
        filename = os.path.basename(event.src_path)
        dirname = os.path.dirname(event.src_path)
        logging.info(f"L'element - {filename} - a ete supprimer du dossier - {dirname}")

    def on_modified(self, event):
        src_path = event.src_path
        username = get_username(src_path)
        groupname = get_groupname(src_path)
        elem_name = os.path.basename(src_path)
        user_perm = get_permissions(src_path, "user")
        group_perm = get_permissions(src_path, "group")
        other_perm = get_permissions(src_path, "other")
        file_size_str = ""

        if os.path.isfile(src_path):
            elem = "fichier"
            file_size = human_size(os.stat(src_path).st_size)
            file_size_str = str(f"\n - Taille du fichier \"{elem_name}\" : {file_size}")
        if os.path.isdir(src_path):
            elem = "dossier"
        
        owner_str = str(f"\n - Le  proprietaire du {elem} \"{elem_name}\" est :  Utilisateur -> {username} | Groupe -> {groupname}")
        user_perm_str = str(f"\n - Droits de l'utilisateur \"{username}\" : {user_perm}")
        group_perm_str = str(f"\n - Droits du groupe \"{groupname}\" : {group_perm}")
        other_perm_str = str(f"\n - Droits des autres : {other_perm}")
        all_perm_str = str(f"\n - Les droits sur le {elem} \"{elem_name}\" sont : Utilisateur -> {user_perm} | Groupe -> {group_perm} | Autre -> {other_perm}")

        # elem_create = os.stat(path).st_ctime
        # elem_create = datetime.fromtimestamp(elem_create)
        # elem_create_str = str(f"\n - Date de creation du {elem} : {elem_create}")

        elem_modif = os.stat(src_path).st_ctime
        elem_modif = datetime.fromtimestamp(elem_modif)
        elem_modif_str = str(f"\n - Date de la derniere modification du {elem} \"{elem_name}\" : {elem_modif}")

        elem_access = os.stat(src_path).st_ctime
        elem_access = datetime.fromtimestamp(elem_access)
        elem_access_str = str(f"\n - Date du dernier acces au {elem} \"{elem_name}\" : {elem_access}")

        elem_alter_str = str(f"\n - Derniere modification : {elem_modif} | Derniere acces : {elem_access}")

        logging.info(f"Les proprietes du {elem} - {src_path} - ont ete modifier : {owner_str} {all_perm_str} {elem_alter_str} {file_size_str}")
    
# Fonction pour obtenire le nom de l'utilisateur proprietaire d'un fichier ou dossier
def get_username(path):
    if os.path.exists(path):
        uid = os.stat(path).st_uid
        try:
            username = pwd.getpwuid(uid).pw_name
        except KeyError:
            username = "System"
        return username
    else:
        return "System"

# Fonction pour obtenire le nom du groupe proprietaire d'un fichier ou dossier
def get_groupname(path):
    if os.path.exists(path):
        gid = os.stat(path).st_gid
        try:
            groupname = pwd.getpwuid(gid).pw_name
        except KeyError:
            groupname = "System"
        return groupname
    else:
        return "System"
    
# Fonction les permissions d'un fichier ou dossier pour chacun de l'utilisateur, le groupe et les autres
def get_permissions(path, who):
    mask = oct(os.stat(path).st_mode)[-4:]
    special = str()
    
    if who == "user":
        index = 1
    if who == "group":
        index = 2
    if who == "other":
        index = 3

    if mask[index] == "0":
        permissions = "Aucun droit"
    if mask[index] == "1":
        permissions = "Executer"
    if mask[index] == "2":
        permissions = "Ecriture"
    if mask[index] == "3":
        permissions = "Ecriture, execution"
    if mask[index] == "4":
        permissions = "Lecture"
    if mask[index] == "5":
        permissions = "Lecture, execution"
    if mask[index] == "6":
        permissions = "Lecture, ecriture"
    if mask[index] == "7":
        permissions = "Lecture, ecriture, execution"

    if mask[0] == "0":
        special = ""
    if mask[0] == "1":
        if index == 3:
            special = "[Sticky]"
    if mask[0] == "2":
        if index == 2:
            special = "[SGID]"
    if mask[0] == "3":
        if index == 2:
            special = "[SGID]"
        if index == 3:
            special = "[Sticky]"
    if mask[0] == "4":
        if index == 1:
            special = "[SUID]"
    if mask[0] == "5":
        if index == "1":
            special = "[SUID]"
        if index == 3:
            special = "[Sticky]"
    if mask[0] == "6":
        if index == 1:
            special = "[SUID]"
        if index == 2:
            special = "[SGID]"
    if mask[0] == "7":
        if index == 1:
            special = "[SUID]"
        if index == 2:
            special = "[SGID]"
        if index == 3:
            special = "[Sticky]"

    if permissions == "Aucun droit":
        if special != "":
            all_perm = special
        else:
            all_perm = permissions
    
    if special != "":
        all_perm = permissions + ", " + special
    else:
        all_perm = permissions
    
    return (all_perm)

# Fonction pour obtenire la taille d'un fichier
def human_size(bytes, units=[' bytes',' KB',' MB',' GB',' TB', ' PB', ' EB']):
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])

# Fonction pour ajouter un chemin a la surveillance
def add_directory(path):
    global event_handler
    global tracked

    observer = Observer()
    observer.schedule(event_handler, path, recursive = True)
    observer.start()
    tracked[path] = observer

    event_handler.directories[path] = os.stat(path).st_ino
    logging.info(f"***** Le dossier {path} est actuellement sous surveillance *****")

# Fonction pour enlever un chemin de la surveillance
def remove_directory(path):
    global event_handler
    global tracked

    if path in event_handler.directories:
        tracked[path].stop()
        tracked[path].join()
        del tracked[path]
        del event_handler.directories[path]

        logging.info(f"***** Le dossier {path} n'est plus sous surveillance *****")

# watchdog
tracked = {}
event_handler = CustomLoggingEventHandler()

###### Tkinter ######
###### Tkinter ######
###### Tkinter ######

def switch_monitor():
    welcome_frame.forget()
    manage_frame.forget()
    about_frame.forget()
    monitor_frame.tkraise()
    monitor_frame.pack(padx = 10, pady = 20,fill="both", expand=True)

def switch_manage():
    welcome_frame.forget()
    monitor_frame.forget()
    about_frame.forget()
    manage_frame.tkraise()
    manage_frame.pack(side = "left", padx = 10, pady = 20,fill="both", expand=True)

def switch_about():
    welcome_frame.forget()
    monitor_frame.forget()
    manage_frame.forget()
    about_frame.tkraise()
    about_frame.pack(padx = 10, pady = 20, fill="both", expand=True)

def get_path_to_add():
    path = path_to_add.get()
    if os.path.exists(path):
        path_list.append(path)
        path_tree.insert("", tk.END, text = path)
        path_tree.pack(padx = 10, pady = 20, fill="both", expand=True)
        path_entry.delete(0, tk.END)
        add_directory(path)

def del_all_path():
    for record in path_tree.get_children():
        path = str(path_tree.item(record)["text"])
        path_list.remove(path)
        path_tree.delete(record)
        remove_directory(path)

def del_one_path():
    selected = path_tree.selection()
    if str(selected) != "()":
        path = str(path_tree.item(selected)["text"])
        path_list.remove(path)
        path_tree.delete(selected)
        remove_directory(path)

def browse_dir():
    dir_path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, dir_path)

def browse_file_manage():
    file_path = filedialog.askopenfilename()
    manage_file_entry.delete(0, tk.END)
    manage_file_entry.insert(0, file_path)

def browse_dir_manage():
    file_path = filedialog.askdirectory()
    manage_file_entry.delete(0, tk.END)
    manage_file_entry.insert(0, file_path)

def get_perm_file():
    path = manage_file_path.get()
    if os.path.exists(path):
        path_file = path
        if get_permissions_bool(path, "user", "read"):
            user_read.set("checked")
        if get_permissions_bool(path, "user", "write"):
            user_write.set("checked")
        if get_permissions_bool(path, "user", "execute"):
            user_execute.set("checked")
        if get_permissions_bool(path, "user", "suid"):
            user_suid.set("checked")
        if get_permissions_bool(path, "group", "read"):
            group_read.set("checked")
        if get_permissions_bool(path, "group", "write"):
            group_write.set("checked")
        if get_permissions_bool(path, "group", "execute"):
            group_execute.set("checked")
        if get_permissions_bool(path, "group", "sgid"):
            group_sgid.set("checked")
        if get_permissions_bool(path, "other", "read"):
            other_read.set("checked")
        if get_permissions_bool(path, "other", "write"):
            other_write.set("checked")
        if get_permissions_bool(path, "other", "execute"):
            other_execute.set("checked")
        if get_permissions_bool(path, "other", "sticky"):
            other_sticky.set("checked")

def apply_permissions():
    path = manage_file_path.get()

    if os.path.exists(path):
        user_perm = 0
        group_perm = 0
        other_perm = 0
        special_perm = 0

        if user_read.get() == "checked":
            user_perm = user_perm + 4
        if user_write.get() == "checked":
            user_perm = user_perm + 2
        if user_execute.get() == "checked":
            user_perm = user_perm + 1
        
        if group_read.get() == "checked":
            group_perm = group_perm + 4
        if group_write.get() == "checked":
            group_perm = group_perm + 2
        if group_execute.get() == "checked":
            group_perm = group_perm + 1
        
        if other_read.get() == "checked":
            other_perm = other_perm + 4
        if other_write.get() == "checked":
            other_perm = other_perm + 2
        if other_execute.get() == "checked":
            other_perm = other_perm + 1
        
        if user_suid.get() == "checked":
            special_perm = special_perm + 4
        if group_sgid.get() == "checked":
            special_perm = special_perm + 2
        if other_sticky.get() == "checked":
            special_perm = special_perm + 1
        
        mask = str(f"{special_perm}{user_perm}{group_perm}{other_perm}")
        apply = os.popen(f"chmod {mask} {path}").read()
        user_read.set("unchecked")
        user_write.set("unchecked")
        user_execute.set("unchecked")
        user_suid.set("unchecked")
        group_read.set("unchecked")
        group_write.set("unchecked")
        group_execute.set("unchecked")
        group_sgid.set("unchecked")
        other_read.set("unchecked")
        other_write.set("unchecked")
        other_execute.set("unchecked")
        other_sticky.set("unchecked")
        manage_file_entry.delete(0, tk.END)

        if user_own_var.get() != "":
            chg_user = os.popen(f"chown {user_own_var.get()} {path}").read()
        
        if group_own_var.get() != "":
            chg_group = os.popen(f"chown :{group_own_var.get()} {path}").read()

        user_list = []
        group_list = []
        user_own_list = ttk.Combobox(master = manage_sub_frame_4, values = user_list, textvariable=user_own_var)
        user_own_list.set("")
        user_own_list.grid(column=0, row=1, padx=10, pady=10)
        group_own_list = ttk.Combobox(master = manage_sub_frame_4, values = group_list, textvariable=group_own_var)
        group_own_list.set("")
        group_own_list.grid(column=1, row=1, padx=10, pady=10)

def cancel_permissions():
    user_read.set("unchecked")
    user_write.set("unchecked")
    user_execute.set("unchecked")
    user_suid.set("unchecked")
    group_read.set("unchecked")
    group_write.set("unchecked")
    group_execute.set("unchecked")
    group_sgid.set("unchecked")
    other_read.set("unchecked")
    other_write.set("unchecked")
    other_execute.set("unchecked")
    other_sticky.set("unchecked")
    manage_file_entry.delete(0, tk.END)
    user_list = []
    group_list = []
    user_own_list = ttk.Combobox(master = manage_sub_frame_4, values = user_list, textvariable=user_own_var)
    user_own_list.set("")
    user_own_list.grid(column=0, row=1, padx=10, pady=10)
    group_own_list = ttk.Combobox(master = manage_sub_frame_4, values = group_list, textvariable=group_own_var)
    group_own_list.set("")
    group_own_list.grid(column=1, row=1, padx=10, pady=10)


def get_permissions_bool(path, who, which):
    mask = oct(os.stat(path).st_mode)[-4:]
    
    if who == "user":
        index = 1
    if who == "group":
        index = 2
    if who == "other":
        index = 3

    if which == "read":
        if mask[index] == "4":
            permission = True
        elif mask[index] == "5":
            permission = True
        elif mask[index] == "6":
            permission = True
        elif mask[index] == "7":
            permission = True
        else:
            permission = False
        
    if which == "write":
        if mask[index] == "2":
            permission = True
        elif mask[index] == "3":
            permission = True
        elif mask[index] == "6":
            permission = True
        elif mask[index] == "7":
            permission = True
        else:
            permission = False
    
    if which == "execute":
        if mask[index] == "1":
            permission = True
        elif mask[index] == "3":
            permission = True
        elif mask[index] == "5":
            permission = True
        elif mask[index] == "7":
            permission = True
        else:
            permission = False

    if which == "suid":
        if mask[0] == "4":
            permission = True
        elif mask[0] == "5":
            permission = True
        elif mask[0] == "6":
            permission = True
        elif mask[0] == "7":
            permission = True
        else:
            permission = False

    if which == "sgid":
        if mask[0] == "2":
            permission = True
        elif mask[0] == "3":
            permission = True
        elif mask[0] == "6":
            permission = True
        elif mask[0] == "7":
            permission = True
        else:
            permission = False
    
    if which == "sticky":
        if mask[0] == "1":
            permission = True
        elif mask[0] == "3":
            permission = True
        elif mask[0] == "5":
            permission = True
        elif mask[0] == "7":
            permission = True
        else:
            permission = False
    
    return permission

def get_own_file():
    path = manage_file_path.get()
    if os.path.exists(path):
        username = get_username(path)
        groupname = get_groupname(path)
        user_list = []
        group_list = []

        for p in pwd.getpwall():
            user_list.append(p[0])
            group_list.append(grp.getgrgid(p[3])[0])

        user_own_list = ttk.Combobox(master = manage_sub_frame_4, values = user_list, textvariable=user_own_var)
        user_own_list.set(username)
        user_own_list.grid(column=0, row=1, padx=10, pady=10)
        group_own_list = ttk.Combobox(master = manage_sub_frame_4, values = group_list, textvariable=group_own_var)
        group_own_list.set(groupname)
        group_own_list.grid(column=1, row=1, padx=10, pady=10)

def save_logs():
    os.system(f"cp {log_file} {script_dir}")

# window
window = tk.Tk()
window.title("FileFox")
window.geometry("1080x720")

# title
title_label = ttk.Label(master = window, 
                        text = "FileFox",
                        font = "Calibri 24 bold")
title_label.pack(padx = 10, pady = 20)

# horizontal separator
separator_1 = ttk.Separator(master = window, orient = "horizontal")
separator_1.pack(fill = "x")

# sidebar
sidebar_frame = ttk.Frame(master = window)
sidebar_frame.pack(side = "left", padx = 10, pady = 20)

sidebar_label = ttk.Label(master = sidebar_frame, 
                          text = "Menu",
                          font = "Calibri 18 bold")
sidebar_label.pack(padx = 10, pady = 20)

sidebar_btn_1 = ttk.Button(master = sidebar_frame,
                           text = "Surveiller un dossier",
                           command = switch_monitor)
sidebar_btn_1.pack(padx = 20, pady = 10, fill="both", expand=True)

sidebar_btn_2 = ttk.Button(master = sidebar_frame,
                           text = "Gerer les droits",
                           command = switch_manage)
sidebar_btn_2.pack(padx = 20, pady = 10, fill="both", expand=True)

sidebar_btn_3 = ttk.Button(master = sidebar_frame,
                           text = "A propos",
                           command = switch_about)
sidebar_btn_3.pack(padx = 20, pady = 10, fill="both", expand=True)

sidebar_blank = ttk.Frame(master = sidebar_frame)
sidebar_blank.pack(padx = 10, pady = 200)

# vertical separator
separator_2 = ttk.Separator(master = window, orient = "vertical")
separator_2.pack(fill = "y", side = "left")

# welcome menu
welcome_frame = ttk.Frame(master = window)
welcome_label = ttk.Label(master = welcome_frame,
                          text = "Bienvenue",
                          font = "Calibri 18 bold")
welcome_label.pack(padx = 10, pady = 20)
welcome_frame.pack(side = "left", padx = 10, pady = 20, fill="both", expand=True)

# about menu
about_frame = ttk.Frame(master = window)
about_frame.pack(padx = 10, pady = 20, fill="both", expand=True)

about_label = ttk.Label(master = about_frame,
                        text = "A propos",
                        font = "Calibri 18 bold")
about_label.pack(padx = 10, pady = 20)

about_text_labe = ttk.Label(master = about_frame,
                            text = " - Application developpee en Python Copyright 2001-2024, Python Software Foundation\n - Interfaces Utilisateur Graphiques avec \"Tk\" (Tkinter)\n - Fonctionnalites de journalisation avec \"logging\"\n - Surveillance de repertoire avec \"watchdog\" \n\nDevelopper par : \n - LASSOUED Hamza\n - DAIDOU Issam\n - GOMIS Kwency\n - KONTE Amara\n - MBEMBA MIAMISSA Yann",
                            font = "Calibri 12")
about_text_labe.pack(padx = 10, pady = 20)

about_frame.forget()

# monitor menu
monitor_frame = ttk.Frame(master = window)
monitor_frame.pack(padx = 10, pady = 20, fill="both", expand=True)

monitor_label = ttk.Label(master = monitor_frame,
                          text = "Surveiller un dossier",
                          font = "Calibri 18 bold")
monitor_label.pack(padx = 10, pady = 10)

add_path_label = ttk.Label(master = monitor_frame,
                           text = "Ajouter un dossier a surveiller",
                           font = "Calibri 14")
add_path_label.pack(padx = 10, pady = 10, expand = True)

monitor_sub_frame_1 = ttk.Frame(master = monitor_frame)
monitor_sub_frame_1.pack()

path_to_add = tk.StringVar()
path_entry = ttk.Entry(master = monitor_sub_frame_1, textvariable = path_to_add, width = 70)
path_entry.pack(side = "left", padx = 10, pady = 10)

browse_btn = ttk.Button(master=monitor_sub_frame_1, text = "Browse", command = browse_dir, width = 20)
browse_btn.pack(side = "left", padx = 10, pady = 10)

path_btn = ttk.Button(master = monitor_frame, text = "Ajouter", command = get_path_to_add, width = 90)
path_btn.pack(padx = 10, pady = 10)

var = tk.Variable(value = path_list)
path_tree = ttk.Treeview(monitor_frame)
path_tree.pack(padx = 10, pady = 20, fill="both", expand=True)

monitor_sub_frame_2 = ttk.Frame(master = monitor_frame)
monitor_sub_frame_2.pack()

del_all_btn = ttk.Button(master = monitor_sub_frame_2, text = "Tout supprimer", command = del_all_path, width = 50)
del_all_btn.pack(side = "left", padx = 10, pady = 20, fill = "both", expand = True)

del_one_btn = ttk.Button(master = monitor_sub_frame_2, text = "Supprimer l'element selectionne", command = del_one_path, width = 50)
del_one_btn.pack(side = "left", padx = 10, pady = 20, fill = "both", expand = True)

monitor_sub_frame_3 = ttk.Frame(master = monitor_frame)
monitor_sub_frame_3.pack()

save_logs_btn = ttk.Button(master = monitor_sub_frame_3, text = "Sauvegrader le fichier de logs", command = save_logs, width = 100)
save_logs_btn.pack(padx = 10, pady = 20, fill = "both", expand = True)

monitor_frame.forget()

# manage file menu
manage_frame = ttk.Frame(master = window)
manage_frame.pack(side = "left", padx = 10, pady = 20, fill="both", expand=True)

manage_label = ttk.Label(master = manage_frame,
                         text = "Gerer les droits",
                         font = "Calibri 18 bold")
manage_label.pack(padx = 10, pady = 20)

manage_label_file = ttk.Label(master=manage_frame,
                              text = "Selectionner un fichier ou un dossier",
                              font = "Calibri 14")
manage_label_file.pack()

manage_sub_frame_1 = ttk.Frame(master = manage_frame)
manage_sub_frame_1.pack()

manage_file_path = tk.StringVar()
manage_file_entry = ttk.Entry(master = manage_sub_frame_1, textvariable = manage_file_path, width = 70)
manage_file_entry.pack(side = "left", padx = 10, pady = 10)

manage_sub_frame_3 = ttk.Frame(master = manage_frame)
manage_sub_frame_3.pack()

browse_file_manage_btn = ttk.Button(master=manage_sub_frame_3, text = "Browse - Fichier", command = browse_file_manage, width = 30)
browse_file_manage_btn.pack(side = "left", padx = 10, pady = 10)

browse_dir_manage_btn = ttk.Button(master=manage_sub_frame_3, text = "Browse - Dossier", command = browse_dir_manage, width = 30)
browse_dir_manage_btn.pack(side = "left", padx = 10, pady = 10)

manage_file_btn = ttk.Button(master = manage_frame, text = "Gerer", command = lambda: [get_perm_file(), get_own_file()], width = 90)
manage_file_btn.pack(padx = 10, pady = 10)

manage_sub_frame_4 = ttk.Frame(master = manage_frame)
manage_sub_frame_4.pack()

manage_sub_frame_4.columnconfigure(0, weight = 1)
manage_sub_frame_4.columnconfigure(1, weight = 1)

user_own_label = ttk.Label(master = manage_sub_frame_4, text = "Utilisateur proprietaire", font = "Calibri 12 bold")
user_own_label.grid(column=0, row=0, padx=10, pady=10)

user_own_var = tk.StringVar()
user_own_list = ttk.Combobox(master = manage_sub_frame_4, values = user_list, textvariable=user_own_var)
user_own_list.grid(column=0, row=1, padx=10, pady=10)

group_own_label = ttk.Label(master = manage_sub_frame_4, text = "Groupe proprietaire", font = "Calibri 12 bold")
group_own_label.grid(column=1, row=0, padx=10, pady=10)

group_own_var = tk.StringVar()
group_own_list = ttk.Combobox(master = manage_sub_frame_4, values = group_list, textvariable=group_own_var)
group_own_list.grid(column=1, row=1, padx=10, pady=10)

manage_sub_frame_2 = ttk.Frame(master = manage_frame)
manage_sub_frame_2.pack()

manage_sub_frame_2.columnconfigure(0, weight = 1)
manage_sub_frame_2.columnconfigure(1, weight = 1)
manage_sub_frame_2.columnconfigure(2, weight = 1)

user_label = ttk.Label(master = manage_sub_frame_2, text = "Droit de l'utilisateur", font = "Calibri 12 bold")
user_label.grid(column=0, row=0, padx=10, pady=10)

user_read = tk.StringVar()
user_read_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Lecture", variable = user_read, onvalue = "checked", offvalue = "unchecked")
user_read_check.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

user_write = tk.StringVar()
user_write_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Ecriture", variable = user_write, onvalue = "checked", offvalue = "unchecked")
user_write_check.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

user_execute = tk.StringVar()
user_execute_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Execution", variable = user_execute, onvalue = "checked", offvalue = "unchecked")
user_execute_check.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)

user_suid = tk.StringVar()
user_suid_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "[SUID]", variable = user_suid, onvalue = "checked", offvalue = "unchecked")
user_suid_check.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

group_label = ttk.Label(master = manage_sub_frame_2, text = "Droit du groupe", font = "Calibri 12 bold")
group_label.grid(column=1, row=0, padx=10, pady=10)

group_read = tk.StringVar()
group_read_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Lecture", variable = group_read, onvalue = "checked", offvalue = "unchecked")
group_read_check.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

group_write = tk.StringVar()
group_write_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Ecriture", variable = group_write, onvalue = "checked", offvalue = "unchecked")
group_write_check.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

group_execute = tk.StringVar()
group_execute_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Execution", variable = group_execute, onvalue = "checked", offvalue = "unchecked")
group_execute_check.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)

group_sgid = tk.StringVar()
group_sgid_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "[SGID]", variable = group_sgid, onvalue = "checked", offvalue = "unchecked")
group_sgid_check.grid(column=1, row=4, padx=10, pady=10, sticky=tk.W)

other_label = ttk.Label(master = manage_sub_frame_2, text = "Droit des autres", font = "Calibri 12 bold")
other_label.grid(column=2, row=0, padx=10, pady=10)

other_read = tk.StringVar()
other_read_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Lecture", variable = other_read, onvalue = "checked", offvalue = "unchecked")
other_read_check.grid(column=2, row=1, padx=10, pady=10, sticky=tk.W)

other_write = tk.StringVar()
other_write_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Ecriture", variable = other_write, onvalue = "checked", offvalue = "unchecked")
other_write_check.grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)

other_execute = tk.StringVar()
other_execute_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "Execution", variable = other_execute, onvalue = "checked", offvalue = "unchecked")
other_execute_check.grid(column=2, row=3, padx=10, pady=10, sticky=tk.W)

other_sticky = tk.StringVar()
other_sticky_check = ttk.Checkbutton(master = manage_sub_frame_2, text = "[Sticky]", variable = other_sticky, onvalue = "checked", offvalue = "unchecked")
other_sticky_check.grid(column=2, row=4, padx=10, pady=10, sticky=tk.W)

manage_sub_frame_3 = ttk.Frame(master = manage_frame)
manage_sub_frame_3.pack()

cancel_btn = ttk.Button(master=manage_sub_frame_3, text = "Annuler", command = cancel_permissions, width = 40)
cancel_btn.pack(side = "left", padx = 10, pady = 10)

apply_btn = ttk.Button(master=manage_sub_frame_3, text = "Appliquer", command = apply_permissions, width = 40)
apply_btn.pack(side = "left", padx = 10, pady = 10)

manage_frame.forget()

# run
def tail():
    logging.info(f"Ouverture de la fenetre des logs")
    os.system(f"tail -f {log_file}")
def run():
    window.mainloop()
    logging.info(f"Arret de l'interface graphique ...")

if __name__ == "__main__":
    process_1 = Process(target=tail)
    process_1.start()
    process_2 = Process(target=run)
    process_2.start()
    process_1.join()
    process_2.join()

# EOF