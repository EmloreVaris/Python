from Main_Tools import *





MonsterStats = {
    "Goblin": {
        "HP": [20, 30],
        "Weapons": {
            "Copper Shortsword": ["Broken", "Heavy", "Tiny", "Well-Made"],
            "Other": ["None"],
            "Flimsy Bow": ["Broken", "Heavy", "Tiny", "Well-Made"]
        },
        "Items": {
            "Small Health Potion": [0, 3],
            "Bomb": [0, 5],
            "Wooden Arrows" : [5, 20]
        }
        
    }
}





class Player:
    def __init__(self, MAX: tuple, HP, MP, DEF, SPEs: list, LUK, INV: dict):
        self.MAXHP = MAX[0]
        self.MAXMP = MAX[1]
        self.HP = HP
        self.MP = MP
        self.INV = INV
        self.DEF = DEF
        self.SPEs = SPEs
        self.LUK = LUK
        
    def getMAXHP(self):
        return self.MAXHP
    
    def getMAXMP(self):
        return self.MAXMP
    
    def getHP(self):
        return self.HP
    
    def getMP(self):
        return self.MP
    
    def getDEF(self):
        return self.DEF
    
    def getSPEs(self):
        return self.SPEs
    
    def getLUK(self):
        return self.LUK
    
    def getINV(self):
        return self.INV
    
    def getINVitem(self, keys):
        tempdict = self.INV
        item = tempdict
        for key in keys:
            item = item[key]
        return item
    
    def getALL(self):
        return [self.MAXHP, self.MAXMP, self.HP, self.MP, self.DEF, self.SPEs, self.LUK, self.INV]
    
    def setMAXHP(self, newMAXHP):
        self.MAXHP = newMAXHP
        
    def setMAXMP(self, newMAXMP):
        self.MAXMP = newMAXMP
        
    def setHP(self, newHP):
        self.HP = newHP
        
    def setMP(self, newMP):
        self.MP = newMP
        
    def setDEF(self, newDEF):
        self.DEF = newDEF
        
    def setSPEs(self, newSPEs):
        self.SPEs = newSPEs
        
    def setLUK(self, newLUK):
        self.LUK = newLUK
        
    def setINV(self, newINV):
        self.INV = newINV
        
    def setINVitem(self, keys, newValue):
        item = self.INV
        for key in keys[:-1]:
            item = item.setdefault(key, {})
        item[keys[-1]] = newValue
        
    def delINVitem(self, keys):
        item = self.INV
        for key in keys[:-1]:
            item = item[key]
        del item[keys[-1]]
    
    def useItem(self, item, keys, quantity):
        Item = self.INV
        for key in keys:
            Item = Item[key]
        if not Item[item] <= quantity-1:
            if Item[item] > quantity:
                item[item] -= quantity
            else:
                del Item[item]
    
    
    def statAction(self, stat: str, action: str, nV: str = "", keys: list = []):
        
        """
        stat: player stat
        action: get, set
        action for INV item: get item, set item, del item
        nV: for set only
        keys: for INV item only
        """
        
        stat = stat.upper()
        action = action.upper()
        functions = {
            "GET": {
                "MAX HP": [self.getMAXHP, []],
                "MAX MP": [self.getMAXMP, []],
                "HP": [self.getHP, []],
                "MP": [self.getMP, []],
                "DEF": [self.getDEF, []],
                "SPEs": [self.getSPEs, []],
                "LUK": [self.getLUK, []],
                "INV": [self.getINV, []],
                "ALL": [self.getALL, []]
            },
            
            "SET": {
                "MAX HP": [self.setMAXHP, [nV]],
                "MAX MP": [self.setMAXMP, [nV]],
                "HP": [self.setHP, [nV]],
                "MP": [self.setMP, [nV]],
                "DEF": [self.setDEF, [nV]],
                "SPEs": [self.setSPEs, [nV]],
                "LUK": [self.setLUK, [nV]],
                "INV": [self.setINV, [nV]]
            },
            
            "INV": {
                "GET ITEM": [self.getINVitem, [keys]],
                "SET ITEM": [self.setINVitem, [keys, nV]],
                "DEL ITEM": [self.delINVitem, [keys]],
            }
        }
        
        if stat == "INV" and "ITEM" in action:
            functions["INV"][action][0](*functions["INV"][action][1])
        else:
            if action == "GET":
                return functions[action][stat][0]()
            else:
                functions[action][stat][0](*functions[action][stat][1])
        
        
        
        


class Enemy():
    
    def __init__(self, name):
        self.NAME = name
        self.MAXHP = random.randint(MonsterStats[name]["HP"][0], MonsterStats[name]["HP"][1])
        self.HP = self.MAXHP



def setUpCharacter(New: bool, p):
    if not New:
        pass
    
def SetUpGame(saves, playerNum, ):
    pass



















p = Player((0, 0), 0, 0, 0, [], 0, {})

import os

onlyfiles = next(os.walk("C:\\Users\\Matt JR\\Desktop\\Coding\\Python\\Text Based Adventure Game\\Saves"))[2] #directory is your directory path as string
if len(onlyfiles) == 0:
    setUpCharacter(True, p)