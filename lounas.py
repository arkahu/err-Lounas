# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:10:11 2016

Author: Arttu H., Oulu, Finland.

Version 0.2 2016.9.6
Optional restaurants added.
"""

from errbot import BotPlugin, botcmd
import requests, json


class Lounas(BotPlugin):
    """Errbot plugin for getting the lunch menu for today at a certain  hardcoded restaurant."""

    @botcmd
    def lounas(self, msg, args):
        """Get webpage, parse and return"""
        
        #defaults to Amica VTT Oulu.
        url = "http://www.amica.fi/modules/json/json/Index?costNumber=3587&language=fi"
        
        #optional restaurants
        if args == 'garden':
            url = "http://www.amica.fi/modules/json/json/Index?costNumber=3497&language=fi"
        elif args == 'smart':
            url = "http://www.amica.fi/modules/json/json/Index?costNumber=3498&language=fi"
            
        
        try:

            menu = requests.get(url)
            parsedMenu = json.loads(menu.text)
            menulist = []
            
            #in case different amount of items, will create an exception
            for i in range(0,6):
                menulist.append(parsedMenu['MenusForDays'][0]['SetMenus'][i]['Components'])
        except:
            pass       
        
        #remove useless stuff and format nicely
        out_list_menu = []
        for counter, item in enumerate(menulist):
            out_list_food = []
            for counter2, item2 in enumerate(item):
                food = menulist[counter][counter2]
                #Remove the extra info in parenthesis                
                cutlimit = food.find('(')  
                if cutlimit != -1:
                    food = food[:cutlimit-1]
                out_list_food.append(food)                                

            out_list_menu.append(', '.join(out_list_food))

        output = '-' + '\n-'.join(out_list_menu)

        return output
        
