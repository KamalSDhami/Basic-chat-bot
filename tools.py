import pyfiglet
from datetime import datetime
from rich.console import Console
from rich import box

# Create a rich console
console = Console()

def print_response(message, style=None, width=60):
    with console:
        if style:
            console.print(f":robot_face: [bold {style}]{message}[/bold {style}]", width=width)
        else:
            console.print(f":robot_face: {message}", width=width)



def pifi(text):
    print(pyfiglet.figlet_format(text, font="slant"))

def get_time_period():
    current_time = datetime.now().time()
    
    if current_time >= datetime.strptime("00:00", "%H:%M").time() and current_time < datetime.strptime("12:00", "%H:%M").time():
        return "morning"
    elif current_time >= datetime.strptime("12:00", "%H:%M").time() and current_time < datetime.strptime("17:00", "%H:%M").time():
        return "afternoon"
    elif current_time >= datetime.strptime("17:00", "%H:%M").time() and current_time < datetime.strptime("20:00", "%H:%M").time():
        return "evening"
    else:
        return "night"

