from configparser import ConfigParser
import os

class Virvadb():
    def __init__(self,name):
        self.current_path=os.getcwd()
        self.db_folder_path=r"{}/db".format(self.current_path)
        self.db_path=r"{}/{}.ini".format(self.db_folder_path,name)
        if not os.path.exists(self.db_folder_path):
            os.mkdir(self.db_folder_path)
        if not os.path.exists(self.db_path):
            with open(self.db_path,"a+") as fp:
                pass

    def len(self):
        another_config=ConfigParser()
        another_config.read(self.db_path)
        last_sid=another_config.sections()[-1]
        return int(last_sid)

    def create(self,dico):
        self.config=ConfigParser()
        sid=0
        if os.path.getsize(self.db_path)==0:
            sid+=1
            self.config[sid]=dico
        else:
            last_sid=self.len()
            sid=last_sid+1
            self.config[sid]=dico

    def save(self):
        with open(self.db_path,"a+") as f:
            self.config.write(f)
            f.close()

    def clear(self):
        with open(self.db_path,"a+") as f:
            f.truncate(0)
            f.close()
    
    def get(self,sid):
        self.config.read(self.db_path)
        get_list=[]
        for k in self.config[str(sid)]:
            v=self.config[str(sid)][k]
            get_list.append(k)
            get_list.append(v)
        it = iter(get_list)
        the_dict=dict(zip(it,it))
        return the_dict
    
    def get_all(self):
        db_len=self.len()
        the_list=[]
        for i in range(db_len):
           the_list.append(self.get(i+1))
        return the_list

    def has(self,sid):
        if sid <= self.len():
            return True
        else:
            return False

        

