from ftplib import FTP, all_errors
from datetime import datetime

class FTP_Handler:
    def __init__(self, cred_file='credentials'):
        with open(cred_file) as file:
            self.host = file.readline().strip()
            self.user = file.readline().strip()
            self.passwd = file.readline().strip()
        self.ftp = None
        self.connected = False
        self.directory = {}

    def connect(self):
        try:
            self.ftp = FTP(host=self.host, user=self.user, passwd=self.passwd)
            self.build_directory()
            self.connected = True
        except all_errors:
            print("Error")  #TODO: Build Error Handling here

    def change_dir(self, new_dir):
        if self.connected:
            self.ftp.cwd(new_dir)
            # TODO: Add error handling here
            self.build_directory()


    def build_directory(self):
        # TODO: investigate MLSD support?
        directory = []
        self.ftp.dir(directory.append)
        directory = [line.split() for line in directory]

        # Parse directory to filename and date
        filenames = [line[-1] for line in directory]
        date_string = ["{} {} {} {}".format('2018', line[5], line[6], line[7]) for line in directory]
        date_dt = [datetime.strptime(dt, '%Y %b %d %I:%M') for dt in date_string]
        self.directory = dict(zip(date_dt, filenames))

    def find_latest(self):
        filename = self.directory[max(self.directory)]
        with open(filename, 'wb') as file:
            self.ftp.retrbinary('RETR {}'.format(filename), file.write)

    def close(self):
        self.ftp.quit()


test = FTP_Handler()
test.connect()
test.change_dir('data')
test.find_latest()
test.close()
