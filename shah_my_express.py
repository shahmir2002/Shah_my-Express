from graphsearch import bfs, dfs
from routes_to_routes import hu_metro
from landmarks_nearby_routes import hu_landmarks
from Habib_landmarks import landmark_choices
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("700x700")

landmark_string = ""
not_accessible = ["Mehfil"]
for letter,landmark in landmark_choices.items():
    landmark_string += "{} - {}\n".format(letter, landmark)

def greet():
    global landmarks_label
    global show_table_btn
    global show_exit_button
    global logo_image
    global image
    for widget in root.winfo_children():
        widget.destroy()

    image_file_bg = "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/logo.png"
    
    image = tk.PhotoImage(file=image_file_bg)
    canvas = tk.Canvas(root, width=3*image.width(), height=3*image.height())
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(1, 1, image=image, anchor=tk.NW)

    root.title("Start Menu")

    name = tk.Label(root, text= "Habib Route", font=("Tkdefault", 16, "italic", "bold"))
    name.place(relx=0.05, rely=0.05, anchor="nw")

    greeting = "Hi there and welcome to Shah_My Express!\nWe'll help you find the shortest wheelchair accessible routes between the Habib landmarks"
    landmarks_label = tk.Label(root, text=greeting, justify ="left", font=("Tkdefault", 13))
    landmarks_label.place(relx=0.05, rely=0.1, anchor="nw")

    show_table_btn = tk.Button(root, text="Show Landmarks Table", relief=tk.RAISED, bg="purple",fg="white",font=("Arial", 11, "italic"), command=landmarks_display)
    show_table_btn.place(relx=0.05, rely=0.2, relwidth=0.3,anchor = "nw")

    show_exit_button = tk.Button(root, text="Exit", relief=tk.RAISED, bg="purple", fg="white", font=('Arial', 11, "italic"), command=goodbye)
    show_exit_button.place(relx=0.05, rely=0.25, relwidth=0.3, anchor = "nw")

    catch_phrase=tk.Label(root, text = "Making campus more accessible", font=("Times New Roman", 14))
    catch_phrase.place(relx=0.95, rely=0.95, anchor="se")

def landmarks_display():
    global label
    global next_button
    global logo_image
    global image

    for widget in root.winfo_children():
        widget.destroy()
    

    image_file_bg= "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/bg_5.png"
    image = tk.PhotoImage(file=image_file_bg)
    canvas = tk.Canvas(root, width=image.width(), height=image.height())
    canvas.pack(fill=tk.BOTH, expand=False, side="left")
    canvas.create_image(0, 0, image=image, anchor=tk.NW)
    
    
    image_file_logo = "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/logo.png"
    logo_image = tk.PhotoImage(file=image_file_logo)
    logo_image = logo_image.subsample(25)
    label = tk.Label(root, image=logo_image)
    label.place(relx=0.5, rely=0.9,anchor="center")
    label.lift(aboveThis=canvas)

    logo = tk.Label(root, text="HabibRoute", fg="black",font=("Times New Roman", 11, "italic", "bold"))
    logo.place(relx=0.5, rely=0.98, anchor="center")
    logo.lift(aboveThis=canvas)

    root.title("Landmarks")
    landmarks_title = tk.Label(root, text="LANDMARKS", fg="black",font=("Times New Roman", 13,"bold"))
    landmarks_title.place(relx=0.5, rely=0.05, anchor="n")

    next_button = tk.Button(root, text="Next", relief= tk.RAISED, font=('Arial', 10, "italic"),command = new_route,bg="grey", fg="black")
    next_button.place(relx=1, rely=1, relwidth=0.2, anchor='se')

    landmarks = tk.Label(root, justify="left", text = landmark_string, font=("Times New Roman", 11), bg="black", fg="white")
    landmarks.place(relx=0.5, rely=0.45, anchor="center")

    go_back_btn = tk.Button(root, text="Go back", relief=tk.RAISED, font=('Arial', 10, "italic"),command=greet, bg="grey", fg="black")
    go_back_btn.place(relx=0, rely=1, relwidth=0.2, anchor="sw")

def goodbye():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Exit")
    global image
    global logo_image
    global goodbye_text

    goodbye_text=tk.Label(root, text="Thankyou for using Shah_My Express!", fg="black", font=("Times New Roman", 13))
    goodbye_text.place(relx=0.5, rely=0.5, anchor="center")

    image_file_logo = "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/logo.png"
    image = tk.PhotoImage(file=image_file_logo)
    logo_image = tk.PhotoImage(file=image_file_logo)
    logo_image = logo_image.subsample(20)
    label = tk.Label(root, image=logo_image)
    label.place(relx=0.5, rely=0.3,anchor="n")
    label.lift(aboveThis=goodbye_text)

def new_route(start_point=None, end_point=None):

    global start_entry, end_entry
    root.title("Finding Route")
    next_button.place_forget()
    start_label = tk.Label(root, text="Where are you coming from?\nType in the corresponding letter:", font=("TkdefaultFont", 11, "italic"))
    start_label.place(relx=0.25, rely=0.85, anchor="center")
    start_entry = tk.Entry(root, bg="grey")
    start_entry.place(relx=0.25, rely=0.9, anchor="center")

    end_label = tk.Label(root, text="Where are you headed?\nType in the corresponding letter:", font=("TkDefaultFont", 11, "italic"))
    end_label.place(relx=0.75, rely=0.85, anchor="center")
    end_entry = tk.Entry(root, bg="grey")
    end_entry.place(relx=0.75, rely=0.9, anchor="center")

    find_button = tk.Button(root, text="Find Route",relief=tk.RAISED, font=('Arial', 10, "italic"),command=find_route,bg="grey", fg="black")
    find_button.place(relx=1, rely=1, relwidth=0.2, anchor='se')


def get_start():
    start_point_letter = start_entry.get().lower()
    if start_point_letter in landmark_choices.keys():
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        tk.messagebox.showerror("Error", "Sorry, that's not a landmark we have data on. Please try again.")
        start_entry.delete(0, tk.END)
        return "Try again"

def get_end():
    end_point_letter = end_entry.get().lower()
    if end_point_letter in landmark_choices.keys():
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        tk.messagebox.showerror("Error", "Sorry, that's not a landmark we have data on. Please try again.")
        end_entry.delete(0, tk.END)
        return "Try again"

def find_route():
    root.title("Routes")
    start_point = get_start()
    end_point = get_end()
    print(start_point, end_point)
    if start_point=="Try again":
        start_point = get_start()
    elif end_point=="Try again":
        end_point = get_end()  
    else:
        for widget in root.winfo_children():
            widget.destroy()
        all_routes = []
        routes = get_route(start_point, end_point)
        if len(routes) > 0:
            for route in routes:
                route_string = '\n'.join(route)
                print("Route option: \n{}\n".format(route_string))
                all_routes.append(route)
            display(all_routes)
        else:
            print("Unfortunately, there is currently no wheelchair accessible path between" ,{0} ,'and', {1} ,"due to accessibility issues.".format(start_point, end_point))
            
            error_message = tk.Label(root, text="Unfortunately, there is currently no wheelchair accessible path between" + str({0}) + ' and ' + str({1})+ " due to accessibility issues.", font=("TkdefaultFont", 11, "italic"))
            error_message.place(relx=0.5, rely=0.85, anchor='s')


        label = tk.Label(root, text="Would you like to see another route? Enter yes/no:", font=("TkdefaultFont", 11, "italic"))
        label.place(relx=0.5, rely=0.95, anchor='s')
        yes_btn = tk.Button(root, text="Yes", relief=tk.SUNKEN, font=('Arial', 10, "italic"), command = landmarks_display,bg="grey", fg="black" )
        yes_btn.place(relx=0.4, rely=0.9, anchor ="s")
        no_btn=tk.Button(root, text="No", relief=tk.SUNKEN, font=('Arial', 10, "italic"), command=goodbye, bg="grey", fg="black")
        no_btn.place(relx=0.6, rely=0.9, anchor ="s")

        image_file_logo = "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/logo.png"
        logo_image = tk.PhotoImage(file=image_file_logo)
        logo_image = logo_image.subsample(25)
        label = tk.Label(root, image=logo_image)
        label.place(relx=0.5, rely=0.08,anchor="center")
        label.lift(aboveThis=logo_image)

        logo = tk.Label(root, text="HabibRoute", fg="black",font=("Times New Roman", 11, "italic", "bold"))
        logo.place(relx=0.5, rely=0.98, anchor="center")


def display(all_routes):
    global logo_image
 
    image_file_logo = "/Users/shahm/Desktop/DSA LAB/DSA FINAL PROJECT SPRING 2023/DSA FINAL PROJECT SPRING 2023/shamy.png"
    logo_image = tk.PhotoImage(file=image_file_logo)
    logo_image = logo_image.subsample(5)
    logo = tk.Label(root, image=logo_image)
    logo.place(relx=0.5, rely=0.5,anchor="center")

    for i, route in enumerate(all_routes):
        route_string = '\n'.join(route)
        label = tk.Label(root, text=f"Route option {i+1}:\n{route_string}", font=("Times New Roman",))
        label.grid(row=0, column=i, padx=10, pady=10)
        label.lift(aboveThis=logo)

    num_columns = len(all_routes)
    root.grid_columnconfigure(0, weight=1)
    for j in range(num_columns):
        root.grid_columnconfigure(j, weight=1)
    root.grid_rowconfigure(0, weight=1)
    

def get_route(start_point,end_point):
    start_stations = hu_landmarks[start_point]
    end_stations = hu_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if not_accessible else hu_metro
            if len(not_accessible)>0:
                possible_route = dfs(metro_system,start_station,end_station)
            if possible_route is None:
                return None
            route = bfs(metro_system,start_station,end_station)
            if route is not None:
                routes.append(route)
    return routes

def get_active_stations():
    updated_metro = hu_metro
    for station_under_construction in not_accessible:
        for current_station,neighboring_stations in hu_metro.items():
            if current_station != station_under_construction:
                updated_metro[current_station] -= set(not_accessible)
            else:
                updated_metro[current_station] = set([])
    return updated_metro
greet()
root.mainloop()