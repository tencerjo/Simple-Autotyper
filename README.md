Instructions for simple autotyper:
1. Install the latest python distribution at https://www.python.org/downloads/ 
2. Open Python and install package requirements (built on Python 3.10, but it should work with the latest Python and packages).
      `pip install pyautogui`
       `pip install pynput`
    (time should be pre-installed in the Python distribution)
4. Create a new text file (.txt) using notepad or a similar program. Separate typed items by new lines.
5. Edit the python script's file path on line 62 with the file path of your text file:
   `text_file = 'C:\Users\[USER]\Documents.txt'`
6. Make a batch (.bat) file with the following text in the first line referencing your python executable file path  in quotes and the script file in quotes:
         "C:\Users\[user]\anaconda3\python.exe" "C:\Users\[user]\Documents\Python Scripts\Autotype_Script_HPLC_Down_v1_6_windows.py"
8. Use the autotyper at any time by running the script and press `Esc` to stop it if you made a mistake.
