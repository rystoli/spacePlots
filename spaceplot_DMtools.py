from importer import *
sys.dont_write_bytecode = True

def check_symmetric(DM, tol=1e-8):
    '''
    Checks if DM numpy array is symmetric
    ---
    ARGUMENTS:
    ---
    DM: 2x2 numpy array, distance matrix
    ---
    Returns: boolean, True if symmetric, False if asymmetric
    '''
    return np.allclose(DM, DM.T, atol=tol)

def read_DM( dm_csvpath ):
    '''
    Reads distance matrix (DM) csv, returns labels and DM
    ---
    ARGUMENTS:
    ---
    dm_csvpath: str, path to DM csv file
        * csv should be symmetric distance matrix (i.e., 0 along diagnoal)
        * csv first row & column should be variable names, with the column of variable names
        ..named 'variables', e.g., text file as:
        
            variables, v1_name, v2_name, v3_name
            v1_name,   0,       .1,      .2
            v2_name,   .1,      0,       .3
            v3_name,   .2,      .3,      0
    ---
    Returns: 2 elements, [0]=labels, [1]=DM, where:
    ... labels: list of strings, each element a variable name
    ... DM: numpy array, symmetric 2x2 distance matrix 
    '''
    
    DM = pd.read_csv(dm_csvpath)
    labels = list(DM['variables'])
    DM = DM.drop('variables',1).as_matrix()
    assert check_symmetric(DM),'Input csv DM is not symmetric'
    
    return labels,DM

def reorder_labels_DM( new_index_order, labels, DM ):
    '''
    Reorders labels and DM based on specified new order of columns/rows
    ---
    ARGUMENTS:
    ---
    new_index_order: list of ints, new index per each original index
    ...for example, [0,2,1] switches places of the second two columns/rows
    labels: list of strings, each element a variable name
    DM: 2x2 numpy array, symmetric DM
    ---
    Returns: 2 elements, [0]=labels, [1]=DM, where:
    ... reordered_labels: list of strings, reordered, each element a variable name
    ... reordered_DM: numpy array, reordered symmetric 2x2 distance matrix 
    '''
    # reorder labels
    reordered_labels = [labels[i] for i in new_index_order]        
    
    # reorder the rows based on clustering
    reordered_DM = [DM[i] for i in new_index_order]        

    # reorder columns based on clustering
    for count,row in enumerate(reordered_DM):
        new_row = [row[col] for col in new_index_order]            
        reordered_DM[count] = new_row

    return reordered_labels, np.array(reordered_DM)