from rich.console import Console
from rich.rule import Rule
from rich.prompt import Prompt
from rich.panel import Panel
import webbrowser
import random

c = Console()
r = Rule()
p = Prompt()

c.print(r"""
 ____        _____ _                 
|  _ \ _   _|  ___| | __ _ _ __ ___  
| |_) | | | | |_  | |/ _` | '__/ _ \ 
|  __/| |_| |  _| | | (_| | | |  __/ 
|_|    \__, |_|   |_|\__,_|_|  \___| 
       |___/                         """, style="bold bright_green")

c.print("Welcome to Pyflare Terminal version 1.0 made by Aryan for fun, For help type /help/", style="bright_green bold")
c.rule(style="bright_green bold")

while True:
  cmd = p.ask("[bright_green bold]Enter command")
  if cmd.lower() == "/open_google/":
    c.print(f"Opening {cmd}", style="bright_green bold")
    webbrowser.open("https://www.google.com")
    print()
    continue
    
  elif cmd.lower() == "/exit/":
    c.print("Exiting...", style="bright_red bold")
    exit()
    
  elif cmd.lower() == "/help/":
    c.print("""
    COMMANDS
    1./love/
    2./cat/
    3./joke/
    4./magic/
    5./dance/
    6./help/
    7./exit/
    """, style="bright_red bold")
    
  elif cmd.lower() == "/love/":
    c.print("""
   (づ｡◕‿‿◕｡)づ
   Sending virtual hugs!
   """, style="bold bright_red")
    
  elif cmd.lower() == "/cat/":
    c.print("""
     /\\_/\\\\
    ( o.o )
     > ^ <
    Meow! Welcome to PyFlare!
    """, style="bold bright_magenta")
    continue

  elif cmd.lower() == "/coffee/":
   c.print("""
       ( (
        ) )
     .______.
     |      |]
     \\      /
      `----'
    Coffee.exe not found!
    Please imagine the coffee 😂
    """, style="bold bright_yellow")
   continue

  elif cmd.lower() == "/joke/":
    c.print("""
    Why do Python programmers wear glasses?

    Because they cannot C! 😂
    """, style="bold bright_cyan")
    continue

  elif cmd.lower() == "/magic/":
    c.print("""
       *  .  *
      . PYTHON .
       *  ✨  *
    You summoned the legendary
         Python Duck!
          <(o )___
           ( ._> /
            `---'
    """, style="bold bright_green")
    continue

  elif cmd.lower() == "/dance/":
    c.print("""
      \\o/
       |
      / \\

    PYTHON PARTY TIME!
    \\o/  \\o/  \\o/
     |    |    |
    / \\  / \\  / \\
    """, style="bold bright_magenta")
    continue
  
  else:
    c.print("Command Not Found!", style="bright_red bold")
    continue    