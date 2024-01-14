#Clave fija en código
kfija_desarrollador = 0xB1EF2ACFE2BAEEFF
#Parte dinámica que modifica el fichero de propiedades
kdinamica_fichero = 0xB98A15BA31AEBB3F
#Clave final (en memoria)
kfinal_memoria = 0x91BA13BA21AABB12



#XOR entre Clave fija y Clave final en memoria
k_en_properties = (hex(kfija_desarrollador^kfinal_memoria))
print("Clave en properties:", k_en_properties)



