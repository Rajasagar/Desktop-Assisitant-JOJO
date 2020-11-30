# Desktop-Assistant-JOJO

#### Created and Tested on Linux with Python 2.7

An attempt to make a very simple, Personal Assistant that understands speech as well as text input and is capable of performing tasks other than conversing.
This project is based on AIML 1.0 and uses pyaiml for using the AIML interpreter in python. AIML, is based on pattern matching and this project does not implement any sort of machine learning or language processing.

Combined with a few python scripts, this assistant now performs quite a few tasks:

- ### Converses, barely.

    **Talk to JOJO :** hello<br>
    **JOJO  :** Well, hello sir 

    **Talk to JOJO :** What is your name?<br>
    **JOJO :** . My name is jojo 
    
    All conversation is only for the hardcoded patterns, which are quite few. Can be easily extended to add AIML scripts.

- ### Rhythmbox: Play, Pause, Open.

    Uses shell commands to play and pause rhythmbox music.

    **Talk to JOJO :** play music<br>
    **JOJO :** playing music <br>
    **Talk to JOJO :** stop music<br>
    **JOJO :** On it!<br>
    **Talk to JOJO :** please open youTube <br>
    **JOJO :** Opening youTube

- ### Tells time.
    
    **Talk to JOJO :** what time is it?<br>
    **JOJO:** The time is 4 43 am

- ### Gives a brief system status.

    **Talk to JOJO :** how are you? / System report / System Status<br>
    **JOJO :** I am fine, sir. All systems are at 100 percent. Battery percentage: 100%. Battery state: discharging. 265 processes are currently running. Current volume is 30 percent

- ### Suggests Googling for all unrecognized interrogative questions

    **Talk to JOJO :** What is IIT, Bombay?<br>
    **JOJO :** Do you want me to google that for you?<br>
    **Talk to JOJO :** yes<br>
    **JOJO:** Right away, sir!  Created new window in existing browser session.

- ### Plays any song, first search result in youtube

    **Talk to JOJO :** play me a song<br>
    **JOJO :** What song, sir?<br>
    **Talk to JOJO :** Alter Bridge Isolation<br>
    **JOJO :** On it!  Created new window in existing browser session.

    Uses youtube.py script to find the first search result for the last user input in above case, and opens it in chromium browser.

- ### Searches internet.

    **Talk to JOJO :** Google what is the answer to life?<br>
    **JOJO :** Right away, sir!  Created new window in existing browser session.<br>
    **Talk to JOJO :** Search youtube for Call of Duty<br>
    **JOJO :** On it!  Created new window in existing browser session.<br>
    **Talk to JOJO :** Search for Navi Mumbai on google maps<br>
    **JOJO :** On it!  Created new window in existing browser session.
    
    ## Requirements:

Make sure you install these packages before moving forward to other python libraries-

`sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools`

You can run `pip install -r requirements.txt` to install them all.

Individual packages listed as follows-

- ### webbrower (For searching on web)
    `import webbrowser`
- ### datetime (for giving the date and time)
    `import datetime`
    
- ### Speech Recognition
    `pip install SpeechRecognition`

- ### wikipedia is required for searching something on wikipedia
    `pip install wikipedia`

- ### smtplib ( For sending mail)
    `pip install smtplib`

- ### ttsx: (Offline Text to Speech Service)
    `pip install pyttsx`

- ### Optional for Google Text to Speech :
   + #### gTTS: (Google Text to Speech service)
      `pip install gTTS`

   + #### PyGame: (For audio playback with gTTS)
       `pip install pygame`

- ### wolframalpha (For different purpose such weather report,mathematical..etc)
    `pip install wolframalpha`

