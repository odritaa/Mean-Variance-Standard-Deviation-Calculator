import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(input_list).reshape(3, 3)
    
    calculations = {
        'Mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'Variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'Standard Deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'Max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'Min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'Sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    
    return calculations
