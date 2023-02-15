with open("futbolPlayer.txt","r",encoding="utf-8") as file:
    galatasaray=list()
    fenerbahçe=list()
    beşiktaş=list()
    for fp in file:
        fp=fp[:-1]
        liste=fp.split(",")
        isim=liste[0]
        takim=liste[1]
        if(takim=="Galatasaray"):
            galatasaray.append(isim+"-----"+takim+"\n")
        elif(takim=="Fenerbahçe"):
            fenerbahçe.append(isim+"-------"+takim+"\n")
        else:
            beşiktaş.append(isim+"--------"+takim+"\n")
    
    with open("fenerbahce.txt","w",encoding="utf-8") as file:
        file.writelines(fenerbahçe)
    
    with open("galatasaray.txt","w",encoding="utf-8") as file:
        file.writelines(galatasaray)
    with open("besiktas.txt","w",encoding="utf-8") as file:
        file.writelines(beşiktaş)
    


