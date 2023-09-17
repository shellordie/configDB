import ini
import os

class Virvadb():
    def __init__(self,name):
        self.current_path=os.getcwd()
        self.db_folder_path=r"{}/db".format(self.current_path)
        self.db_path=r"{}/{}".format(self.db_folder_path,name)
        if not os.path.exists(self.db_folder_path):
            os.mkdir(self.db_folder_path)
        if not os.path.exists(self.db_path):
            with open(self.db_path+".ini","a+") as fp:
                pass


