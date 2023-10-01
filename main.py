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


class ProgramLoop:
    def __init__(self):
        self.mic = None

    # Returns the current mic
    def getMic(self):
        # # Get microphones list
        # mic_arr = sr.Microphone.list_microphone_names()
        # # print(mic_arr[1])
        # mic = sr.Microphone(device_index=1)
        print('getting mic..')

    # Sets the current mic from system list
    def setMic(self):
        mic_arr = sr.Microphone.list_microphone_names()
        for mic in mic_arr:
            print(mic)
        mic = sr.Microphone(device_index=1)





loop = ProgramLoop()
loop.getMic()
loop.setMic()
