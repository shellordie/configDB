from configparser import ConfigParser
import os

class ConfigDB():
    def __init__(self,name:str):
        self.current_path=os.getcwd()
        self.db_folder_path=r"{}/configs".format(self.current_path)
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

    def create(self,section:str,dico:dict):
        self.config=ConfigParser()
        self.config[section]=dico
        self.__save()

    def __save(self):
        with open(self.db_path,"a+") as f:
            self.config.write(f)
            f.close()

    def clear(self):
        with open(self.db_path,"a+") as f:
            f.truncate(0)
            f.close()
    
    def get(self,section:str):
        self.config.read(self.db_path)
        get_list=[]
        for k in self.config[section]:
            v=self.config[section][k]
            get_list.append(k)
            get_list.append(v)
        it = iter(get_list)
        the_dict=dict(zip(it,it))
        return the_dict
    
    def get_sections(self):
        self.config.read(self.db_path)
        sections_list=self.config.sections()
        return sections_list

    def get_all(self):
        sections_list=self.get_sections()
        the_list=[]
        for section in sections_list:
           the_list.append(self.get(section))
        return the_list

    def iter(self):
        self.config.read(self.db_path)
        return self.config

    def has(self,section:str):
        sections_list=self.get_sections()
        if section in sections_list:
            return True
        else:
            return False

    def update(self,section:str,dico:dict):
        another_config=ConfigParser()
        another_config.read(self.db_path)
        another_config.read_dict({section:dico})
        self.clear()
        self.config=another_config
        self.__save()

    def delete(self,section:str):
        another_config=ConfigParser()
        _=another_config.read(self.db_path)
        another_config.remove_section(section)
        self.clear()
        self.config=another_config
        self.__save()
        
