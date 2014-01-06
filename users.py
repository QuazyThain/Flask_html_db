# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:38:51 2014

@author: quazythain
"""

from wrapper import HeyheyDB


class Users(HeyheyDB):
    def get_user(self, id):
        return self.select("*", "users", "user_id="+str(id))

if __name__ == "__main__":
    u = Users()
    u.get_user(2)
