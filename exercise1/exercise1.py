#função str_to_bool
def str_to_bool(value):
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
    