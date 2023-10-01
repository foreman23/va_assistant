import speech_recognition as sr


# # obtain audio from the microphone
# r = sr.Recognizer()
#
# # Get microphones list
# mic_arr = sr.Microphone.list_microphone_names()
# # print(mic_arr[1])
# mic = sr.Microphone(device_index=1)
#
# with mic as source:
#     audio = r.listen(source)
#
# # recognize speech using Sphinx
# try:
#     print(r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))


def startApp(app):
    print("Welcome to the app")

    loop = True

    while loop:
        print("Please choose a command:")
        print("1: View current input device")
        print("2: Change input device")
        print("x: Exit application")
        command = input("::")

        if command == "1":
            print(app.getMicName())

        if command == "2":
            app.setMic(None)

        if command == "x":
            loop = False

        # app.setMic(None)


class ProgramLoop:

    def __init__(self):
        self.mic_name = sr.Microphone.list_microphone_names()[0]
        self.mic_obj = sr.Microphone()

    # Returns the name of the current mic
    def getMicName(self):
        return self.mic_name

    def getMicObj(self):
        return self.mic_obj

    # Sets the current mic from system list (optional index param)
    def setMic(self, index):
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


if __name__ == "__main__":
    loopFlag = True
    app = ProgramLoop()
    if loopFlag:
        startApp(app)
