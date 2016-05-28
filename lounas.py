from errbot import BotPlugin, botcmd
import requests, json

class Lounas(BotPlugin):
    """Errbot plugin for getting the lunch menu for today at a certain  hardcoded restaurant. The restaurant is Amica Oulu VTT."""

    @botcmd
    def lounas(self, msg, args):
        """Get webpage, parse and return"""
        
        try:

            url = "http://www.amica.fi/modules/json/json/Index?costNumber=3587&language=fi"
            menu = requests.get(url)
            parsedMenu = json.loads(menu.text)
            menulist = []
            
            #in case different amount of items, will create an exception
            for i in range(0,5):
                menulist.append(str(parsedMenu['MenusForDays'][0]['SetMenus'][i]['Components']))
        except:
            pass        
        output =''.join(menulist)
        
        return output
