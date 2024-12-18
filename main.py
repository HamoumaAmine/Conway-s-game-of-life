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

