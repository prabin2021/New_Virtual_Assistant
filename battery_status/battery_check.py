import psutil

# def battery_alert1():
#             battery = psutil.sensors_battery()
#             percent = int(battery.percent)

#             if percent < 50:
#                 .speak(f"Your battery is less than 30 percent,You have only {percent} percent sir.")

#             elif percent < 10:
#                 .speak(f"Your battery is less than 10 percent,You have only {percent} percent sir.")

#             elif percent == 100:
#                 .speak(f"Your battery is fully charged,You have {percent} percent sir.")
#             else:
#                 .speak(f"sir,your battery is in perfect battery level, you have {percent} percent sir.")

#     previous_state = None
# def check_plugin_status1():
#         global previous_state  # Use the global variable

#         battery = psutil.sensors_battery()

#         if battery.power_plugged != previous_state:
#             if battery.power_plugged:
#                 .speak("Charger is plugged in")
#             else:
#                 .speak("Charger is plugged out")
#             previous_state = battery.power_plugged
#         return None


def battey_persentage():
        from main import speak

        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        speak(f"the device is running on {percent}% battery power")
        secsleft = battery.secsleft
        if secsleft == psutil.POWER_TIME_UNLIMITED:
            speak("Battery is fully charged.")
        elif secsleft == psutil.POWER_TIME_UNKNOWN:
            speak("Battery time left is unknown.")
        else:
            hours, remainder = divmod(secsleft, 3600)
            minutes, _ = divmod(remainder, 60)
            time_left_message = f"if you normally use your device then you will be able to use about: {hours} hours and {minutes} minutes sir."
            speak(time_left_message)
        return f"You have percent{percent}in your device{time_left_message}"