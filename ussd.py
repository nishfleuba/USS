
import json
def charger_produits():
   
        with open("produits.json", "r", encoding="utf-8") as f:
            return json.load(f)
    

data = charger_produits()
produits = data.get("produits", [])
ventes = data.get("ventes", [])


def sauvegarder_produits():
    with open("produits.json", "w", encoding="utf-8") as f:
        json.dump({"produits": produits, "ventes": ventes}, f, ensure_ascii=False, indent=4)


def kwemeza():
    code = input("shiramwo ikode yanyu:")
    if code =='*150#':

        return True
        
    else :
        print ("ikode yanyu ninkorabara")
        kwemeza()


def kurabaurutonde():
    urutonde = "\n       URUDANDAZA \n"
    urutonde += "1. Kuraba ibidandazwa\n"
    urutonde += "2. Gushiramwo ikidandazwa\n"
    urutonde += "3. Guhanagura ikidandazwa\n"
    urutonde += "4. Guhindura ibiranga ikidandazwa\n"
    urutonde += "5. Kudandaza\n"
    urutonde += "6. Kuraba ivyadandajwe\n"
    urutonde += "7. Kuraba raporo\n"
    urutonde += "0. Guhagarika"
    return urutonde




def guhitamwo(ibiharuro):
    if ibiharuro == "1":
        kurabaibidandazwa()
    elif ibiharuro == "2":
        gushiramwo()  
    elif ibiharuro == "3":
        gukuramwo() 
    elif ibiharuro == "4":    
        guhindura_ikidandazwa() 
             
    elif ibiharuro == "0":
        print(" Urakoze gukoresha serivisi yacu!")
    else:
        print(" ibiharuro mwashizemwo ntibibaho")



def kurabaibidandazwa():
    if not produits:
        print(" Nta bidandazwa bihari.")
    else:
        print("\n Ibidandazwa bihari:")
        print(f"DEBUG produits: {produits}")
        print(f"DEBUG type de chaque élément:")

        for produit in produits:
            print(f"- {produit['id']}. {produit['nom']} - {produit['prix']} FBu (Stock: {produit['stock']})")
    
    input("\n↩ Taper entrer pour daire un reto...")


    
    
def gushiramwo():
    print("Gushiramwo ibidandazwa")
    nom=input("Shiramwo izina ryikidandazwa :")
    try:
        prix=int(input("Shiramwo igiciro ryikidandazwa  :"))
        stock=int(input("Shiramwo  igitigiri ryikidandazwa  :"))
    except ValueError:
        print("Shiramwo igiciro canke igitigiri ryikidandazwa bigizwe nibiharuro ")
    id_shasha=max([p["id"] for p in produits],default=0)+1
    ikidandanzwagishasha={
        "id":id_shasha,
        "nom":nom,
        "prix":prix,
        "stock":stock
    }  
    produits.append(ikidandanzwagishasha)
    sauvegarder_produits()
    print(f"\n Ikidandazwa '{nom}' ciyongerewe neza!")


def gukuramwo():
    print("\n Gukuramwo ikidandazwa")

    if not produits:
        print(" Nta bidandazwa bihari.")
        return
    
    kurabaibidandazwa()

    try:
        id_supprimer = int(input("Tanga ID y'ikidandazwa ushaka gukuraho: "))
        produit = next((p for p in produits if p["id"] == id_supprimer), None)

        if produit:
            produits.remove(produit)
            sauvegarder_produits()

            print(f" Ikidandazwa '{produit['nom']}' cahanaguwe neza.")
        else:
            print(" ID ntibaho.")
    
    except ValueError:
        print(" Shiramwo ID yemewe (igiharuro).")


def guhindura_ikidandazwa():
    print("\n Guhindura ibiranga vy'ikidandazwa")
    
    if not produits:
        print(" Nta bidandazwa bihari.")
        return
    
    kurabaibidandazwa()

    try:
        id_modifier = int(input("Tanga ID y'ikidandazwa ushaka guhindura: "))
        produit = next((p for p in produits if p["id"] == id_modifier), None)

        if produit:
            print(f"\n Uri guhindura: {produit['nom']} - {produit['prix']} FBu (Stock: {produit['stock']})")

            nouveau_nom = input(f"Izina rishasha (Enter kugirango usigaze '{produit['nom']}'): ") or produit['nom']
            try:
                nouveau_prix_input = input(f"Igiciro gishasha (Enter kugirango usigaze {produit['prix']}): ")
                nouveau_prix = int(nouveau_prix_input) if nouveau_prix_input else produit['prix']
                
                nouveau_stock_input = input(f"Stock gishasha (Enter kugirango usigaze {produit['stock']}): ")
                nouveau_stock = int(nouveau_stock_input) if nouveau_stock_input else produit['stock']
            except ValueError:
                print("Igiciro na stock bigomba kuba ibiharuro.")
                return

            produit['nom'] = nouveau_nom
            produit['prix'] = nouveau_prix
            produit['stock'] = nouveau_stock

            sauvegarder_produits()
            print(f"\n Ikidandazwa '{produit['nom']}' cahinduwe neza.")
        else:
            print(" ID ntibaho.")
    except ValueError:
        print("Shiramwo ID yemewe (igiharuro).")

        


    


if __name__ == "__main__":
         
    if kwemeza():

    
        while True:
            
                print(kurabaurutonde())
                ibiharuro = input("\nHitamwo ibiharuro bir hagat (0-7): ")
                guhitamwo(ibiharuro)
                if ibiharuro == "0":
                    break
