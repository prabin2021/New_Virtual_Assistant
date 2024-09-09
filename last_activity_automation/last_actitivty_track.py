
import re
import os
import json
import pygetwindow as gw
import time
import psutil

# File to store the last activity
LAST_ACTIVITY_FILE = "last_activities.json"

def save_last_activity(activities):
    """Save the last activity to a file."""
    with open(LAST_ACTIVITY_FILE, "w") as file:
        json.dump({"last_activities": activities}, file)

def load_last_activity():
    """Load the last activity from a file."""
    if os.path.exists(LAST_ACTIVITY_FILE):
        with open(LAST_ACTIVITY_FILE, "r") as file:
            data = json.load(file)
            return data.get("last_activities",[])
    return []

def remind_last_activity():
    from main import speak,take_user_input
    """Remind the user of the last activity."""
    last_activities = load_last_activity()
    if last_activities:
        speak("Sir, last time we were working on the following activities:")
        for i, activity in enumerate(last_activities):
            speak(f"{i + 1}: {activity}")
        speak(f"Would you like to continue any of them?")
        user_input = take_user_input()
        if user_input:
            if "yes" in user_input.lower() or "continue" in user_input.lower() or "ok" in user_input.lower():
                while True:
                    number = extract_number_from_command(user_input)
                    if number is not None:
                        chosen_index = number - 1
                        if 0 <= chosen_index < len(last_activities):
                            chosen_activity = last_activities[chosen_index]
                            switch_to_activity(chosen_activity)
                            speak(f"Continuing with {chosen_activity}")
                            break
                        else:
                            speak("Invalid number. Please try again.")
                            user_input = take_user_input()
                    else:
                        speak("I didn't understand. Please say the number of the activity.")
                        
                        user_input = take_user_input()
            

def get_active_window():
    """Get the title of the currently active window."""
    window = gw.getActiveWindow()
    if window:
        window_title = window.title
        parts = window_title.split(" - ")
        if len(parts) == 3:
            file_name = parts[0]
            folder_name = parts[1]
            window_name = parts[2]
            return f"In {window_name}, you were engaged in {folder_name} folder, and you were working in {file_name} file"
        elif len(parts) == 2:
            file_name = parts[0]
            folder_name = parts[1]
            return f"In {folder_name} folder, and you were working in {file_name} file"
        else:
            return window_title
    return None
def monitor_activities(interval=5):
    """Monitor the active window and log activities."""
    last_window = None
    last_activities = load_last_activity()
    while True:
        current_window = get_active_window()
        if current_window != last_window:
            last_window = current_window
            if current_window:
                if current_window not in last_activities:
                    if len(last_activities) >= 3:
                        last_activities.pop(0)
                    last_activities.append(current_window)
                    save_last_activity(last_activities)
                    print(f"Current active window: {current_window}")
        time.sleep(interval)

def extract_window_info(activity):
    """Extract window title, folder, and file name from a variety of activity string formats."""
    window_info = {}
    
    # Common patterns
    folder_pattern = re.compile(r'(?:engaged in|working in|folder|directory|dir)\s+(\S+)', re.IGNORECASE)
    file_pattern = re.compile(r'(?:working in|file|document|doc)\s+(\S+)', re.IGNORECASE)
    window_pattern = re.compile(r'(?:in|on|window|app)\s+(.+?)(?:,|$)', re.IGNORECASE)
    print(folder_pattern,file_pattern,window_pattern)
    # Try to find folder name
    folder_match = folder_pattern.search(activity)
    if folder_match:
        window_info['folder'] = folder_match.group(1)
    
    # Try to find file name
    file_match = file_pattern.search(activity)
    if file_match:
        window_info['file'] = file_match.group(1)
    
    # Try to find window title
    window_match = window_pattern.search(activity)
    if window_match:
        window_info['title'] = window_match.group(1).strip()
    
    # Fallback if title not found
    if 'title' not in window_info:
        window_info['title'] = activity.strip()
    
    return window_info
def switch_to_activity(activity):
    """Switch to the specified activity."""
    window_info = extract_window_info(activity)
    if not window_info:
        print(f"No matching window found for activity: {activity}")
        return

    print(f"Looking for a window with the title: '{window_info.get('title', '')}'")
    windows = gw.getWindowsWithTitle('')  # Get all open windows

    for window in windows:
        title_match = window_info.get("title", "").lower() in window.title.lower()
        folder_match = window_info.get("folder", "").lower() in window.title.lower() if "folder" in window_info else True
        file_match = window_info.get("file", "").lower() in window.title.lower() if "file" in window_info else True

        if title_match and folder_match and file_match:
            window.activate()
            print(f"Switched to activity: {window.title}")
            return

    print(f"No matching window found for activity: {activity}")
def extract_number_from_command(command):
    number_words = {
    "zero": 0, "one": 1, "two": 2, "three": 3
    }
    command = command.lower()
    match = re.search(r'\d+', command)
    if match:
        return int(match.group())
    words = command.split()
    for word in words:
        if word in number_words:
            return number_words[word]
    return None


# commandd = input("Enter you commands:")
# extract_number_from_command(commandd)
# print(f"Extracted number: {extract_number_from_command(commandd)}")
