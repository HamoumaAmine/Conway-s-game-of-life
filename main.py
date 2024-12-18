import numpy as np

frame=np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])


def compute_number_neighbors(pad_frame, row_index, column_index):
    neighbors = pad_frame[row_index-1:row_index+2, column_index-1:column_index+2]
    number_of_neighbors = neighbors.sum() - neighbors[1, 1]#la cellule du centre ne peux pas etre voisine d'elle meme
    return number_of_neighbors

def compute_next_frame(frame):
    padded_frame=np.pad(frame, pad_width=1, mode="constant") 
    for row_index in range(1,len(padded_frame)-1):#lignes
        for column_index in range(1, len(padded_frame[row_index]) - 1):#colonnes
            
            number_neighbors=compute_number_neighbors(padded_frame, row_index, column_index)
            result=padded_frame[row_index, column_index] #etat de la cellule actuelle
            
            if result==1:#Regles du jeu:
                if number_neighbors<2 or number_neighbors>3:
                    frame[row_index-1,column_index-1]=0#la celule actuellemeurt
                    
            elif number_neighbors==3:
                frame[row_index-1,column_index-1]=1#la celule actuelle revit     
    return frame
