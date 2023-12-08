from datetime import datetime

class Logging:

    def __init__(self) -> None:
       self.log = open ('log.txt', 'a')
       self.logging()

    def logging (self):
        now = datetime.now()
        timestamp = now.strftime('%d.%m.%Y, %H:%M:%S')
        self.log.write(f'{timestamp}\n')

    def __del__(self):
        self.log.close()
        
