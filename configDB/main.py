from configparser import ConfigParser
import os

class ConfigDB():
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
        last_sid=another_config.sections()
        last_sid=len(last_sid)
        return last_sid

    def create(self,section,dico):
        self.config=ConfigParser()
        self.config[section]=dico
        self.save()

    def save(self):
        with open(self.db_path,"a+") as f:
            self.config.write(f)
            f.close()

    def clear(self):
        with open(self.db_path,"a+") as f:
            f.truncate(0)
            f.close()
    
    def get(self,section):
        self.config.read(self.db_path)
        get_list=[]
        for k in self.config[section]:
            v=self.config[section][k]
            get_list.append(k)
            get_list.append(v)
        it = iter(get_list)
        the_dict=dict(zip(it,it))
        return the_dict
    
    def get_all(self):
        another_config=ConfigParser()
        another_config.read(self.db_path)
        sections_list=another_config.sections()
        the_list=[]
        for section in sections_list:
           the_list.append(self.get(section))
        return the_list

    def has(self,section):
        if sid <= self.len():
            return True
        else:
            return False

    def update(self,dico,sid ):
        another_config=ConfigParser()
        another_config.read(self.db_path)
        for k in another_config[str(sid)]:
            for ku in dico:
                if k==ku:
                    another_config[str(sid)][k]=dico[ku]
        self.clear()
        self.config=another_config
        self.save()

    def delete(self,sid):
        another_config=ConfigParser()
        _=another_config.read(self.db_path)
        another_config.remove_section(str(sid))
        sections_list=another_config.sections()
        self.clear()
        self.config=another_config
        self.save()
        data_list=[] 
        for i in range(self.len()):
            ids=int(sections_list[i])
            data=self.get(ids)
            data_list.append(data)
        self.clear()
        for item in data_list:
            self.create(item)

