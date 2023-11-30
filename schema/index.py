from sqlalchemy import Float


# Define training table
table_training = {'x': Float}
table_training.update({f'y{i}': Float for i in range(1, 5)})

# Define test table
table_test = {
    'x': Float,
    'y1': Float,
    'delta_y': Float,
    'ideal_func': Text
}

# Define ideal table
table_ideal = {'x': Float}
table_ideal.update({f'y{i}': Float for i in range(1, 51)})

