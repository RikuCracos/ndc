import pyxel as p
import random as r

#///////////////////////////
# CLASS APP
#///////////////////////////

class App:
    def __init__(self):
        p.init(256, 256, title = 'NDC', fps = 60, quit_key = p.KEY_ESCAPE)
        p.load('sprite.pyxres')
        self.vie = 100
        self.argent = 250
        self.tile_achat = [(0,8),(1,8),(0,9),(1,9)]
        self.tile_button_achat = [(i,y) for i in range(8) for y in range(16,20)]
        self.tile_tourelle = [(i,y) for i in range(2) for y in range(10,12)]
        print(self.tile_tourelle)
        self.pret = False
        self.round = 1
        self.add_e = 0
        self.ennemies = []
        self.achat= False
        self.att = False
        p.run(self.update, self.draw)
        
        
    def mvt_e(self):
        for ennemie in self.ennemies:
            ennemie.avancer()

    def debut(self):
        # if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) in self.btn_pret:
        #     if p.btnp(p.MOUSE_BUTTON_LEFT):    
        for i in range(10+self.add_e):
            self.ennemies.append(Mob(100, 10, 2, i))
        self.app = True
        self.pret = True

    def labirynthe(self):
        pass
    
    
    def ouvrir_menu_achat(self):
        if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) in self.tile_achat:
            if p.btnp(p.MOUSE_BUTTON_LEFT):
                return True
    
   
    def fermer_menu(self):
        if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) not in self.tile_achat:
            if p.btnp(p.MOUSE_BUTTON_LEFT):
                return True
        
    
    def ouvrir_menu_ameliorer(self):
        if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) in self.tile_tourelle:
            if p.btnp(p.MOUSE_BUTTON_LEFT):
                return True
    
    
    def acheter_tourelle(self):
        if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) in self.tile_button_achat:
            if p.btnp(p.MOUSE_BUTTON_LEFT):
                pass

    
    def ameliorer_tourelle(self):
        if p.tilemap(0).pget(p.mouse_x//8,p.mouse_y//8) in self.button_ameliorer:
            if p.btnp(p.MOUSE_BUTTON_LEFT):
                pass

    
    def update(self):
        if not self.att:
            self.debut()
        if self.pret:
            if self.vie > 0:
                if len(self.ennemies) == 0:
                    self.round += 1
                    self.add_e += r.randint(10*self.round-5,10*self.round)
                    self.att =  False
                    self.pret = False
                else:
                    self.mvt_e()
            else:
                p.rect(0,0,256,256,0)

    
    def draw(self):
        p.cls(0)
        p.mouse(visible=True)
        p.bltm(0,0,0,0,0,256,256,0)
        if self.ouvrir_menu_achat():
            self.achat = True
        # if self.fermer_menu():
        #     self.achat = False
        if self.achat:
            p.blt(192,224,0,0,128,64,32,0)
            p.rect(50,224,141,32,4)
            p.blt(60,230,0,0,80,16,16,0,scale=2)
            p.text(62,250,'150',0)
        if self.pret:
            for ennemie in self.ennemies:
                p.blt(ennemie.x,ennemie.y,0,0,16,8,8,colkey=0,scale=1.5)




#////////////////////////////
# CLASS MOB
#////////////////////////////


class Mob:
    def __init__(self, vie, degat, vitesse, co_y):
        self.vie = vie
        self.degat = degat
        self.vitesse = vitesse
        self.x,self.y = 12,-10-14*co_y
    
    def avancer(self):
        pass


#///////////////////////////
# CLASS TOURELLE
#///////////////////////////

class Tourelle:
    def __init__(self, vitesse_attaque, distance, degat):
        pass



#///////////////////////////
# LANCEMENT DE L'APP
#///////////////////////////

App()