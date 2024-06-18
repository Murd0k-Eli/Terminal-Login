import curses
import time

def boot_system():
    stdscr.clear()
    print("Starting system boot...")
    time.sleep(0.3)
    print("Analyzing processor speed...")
    time.sleep(0.3)
    print("Checking memory modules...")
    time.sleep(0.3)
    print("Loading system resources...")
    time.sleep(0.3)
    print("Initializing peripherals...")
    time.sleep(0.3)
    print("Establishing network connection...")
    time.sleep(0.3)
    print("Booting operating system...")
    time.sleep(0.3)
    print("Configuring system settings...")
    time.sleep(0.3)
    print("Performing system diagnostics...")
    time.sleep(0.3)
    print("Running startup scripts...")
    time.sleep(0.3)
    print("Checking disk drives...")
    time.sleep(0.3)
    print("Initializing graphics subsystem...")
    time.sleep(0.3)
    print("Loading user profiles...")
    time.sleep(0.3)
    print("Mounting file systems...")
    time.sleep(0.3)
    print("Starting system services...")
    time.sleep(0.3)
    print("Launching user interface...")
    time.sleep(0.3)
    print("System boot complete!")
    print("Press any Key to Continue...")
    key = stdscr.getch()
    stdscr.clear()

def animate_login_screen(stdscr):
    stdscr.clear()						# Clear the Screen
    height, width = stdscr.getmaxyx()				# Get Screen Dimension
    login_text = "Termux Login"					# Setup Text
    username_text = "Username: "
    password_text = "Password: "
    username = "termux"						# Pre-defined UserName and Password
    password = ""
    login_x = width // 2 - len(login_text) // 2			# Calculate the Position of Elements
    username_x = width // 2 - len(username_text) // 2
    password_x = width // 2 - len(password_text) // 2
    text_y = height // 2
    while True:							# Animation Loop
        stdscr.clear()									# Clear Screen
        stdscr.addstr(text_y - 2, login_x, login_text)					# Print Login Text
        stdscr.addstr(text_y, username_x, username_text + username)			# Print UserName Text
        stdscr.addstr(text_y + 1, password_x, password_text + "*" * len(password))	# Print Password Text
        stdscr.refresh()								# Refresh Screen
        key = stdscr.getch()								# Wait for user Input
        if key == ord('\n'):								# Check if Enter key is pressed
            stdscr.clear()									# Clear the Screen
            success_message = "Login successful!"						# Print Login Screen Success
            success_x = width // 2 - len(success_message) // 2
            stdscr.addstr(text_y, success_x, success_message)
            stdscr.refresh()									# Refresh the Screen
            time.sleep(2)									# Pause for a Short Duration
            break
        elif key == curses.KEY_BACKSPACE or key == 127:					# Check if Backspace key is Pressed
            password = password[:-1]  								# Remove the last character
        else:
            password += chr(key)  							# Append the typed character to the password
 
curses.wrapper(animate_login_screen)				# Initialize curses and run the animation
curses.wrapper(boot_system)                                      # Call the function to start the system boot

