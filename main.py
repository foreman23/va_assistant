import speech_recognition as sr


def startApp(app):
    print("Welcome to the app")

    loop = True

    while loop:
        print("Please choose a command:")
        print("1: View current input device")
        print("2: Change input device")
        print("3: Record voice")
        print("4: Get last voice prompt")
        print("x: Exit application")
        command = input("::")

        if command == "1":
            print(app.getMicName())

        if command == "2":
            app.setMic(None)

        if command == "3":
            app.recordPrompt()

        if command == "4":
            print(app.getPrompt())

        if command == "x":
            loop = False


class ProgramLoop:

    def __init__(self):
        self.mic_name = sr.Microphone.list_microphone_names()[1]
        self.mic_obj = sr.Microphone()
        self.prompt = None

    def getMicName(self):
        """
        Returns the NAME of the current mic
        """
        return self.mic_name

    def getMicObj(self):
        """
        Returns the current mic OBJECT
        """
        return self.mic_obj

    def getPrompt(self):
        """
        Returns the current prompt
        """
        return self.prompt

    def setMic(self, index):
        """
        Sets the current mic from system list (optional index param)
        """
        mic_arr = sr.Microphone.list_microphone_names()
        if index is not None:
            mic_obj = sr.Microphone(device_index=index)
            self.mic_name = mic_arr[index]
            self.mic_obj = mic_obj

        else:
            for i in range(len(mic_arr)):
                print(i, mic_arr[i])
            val = input("Select an input device from the list...")
            index = int(val)
            mic_obj = sr.Microphone(device_index=index)
            self.mic_name = mic_arr[index]
            self.mic_obj = mic_obj

    def recordPrompt(self):
        r = sr.Recognizer()

        with self.mic_obj as source:
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            speech = r.recognize_sphinx(audio)
            print(speech)
            self.prompt = speech
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


if __name__ == "__main__":
    loopFlag = True
    app = ProgramLoop()
    if loopFlag:
        startApp(app)
