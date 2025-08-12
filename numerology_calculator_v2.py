# --- FINAL CORRECTED CALCULATOR (V2.3) ---
# Implements the user-provided, gender-based Kua calculation rules.

def reduce_to_single_digit(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def calculate_psychic_number(birth_date_str):
    day_str, _, _ = birth_date_str.split('/')
    return reduce_to_single_digit(int(day_str))

def calculate_destiny_number(birth_date_str):
    all_digits_str = birth_date_str.replace('/', '')
    all_digits_sum = sum(int(digit) for digit in all_digits_str)
    return reduce_to_single_digit(all_digits_sum)

# --- FINAL AND CORRECTED KUA NUMBER FUNCTION ---
def calculate_kua_number(birth_date_str, gender):
    _, _, year_str = birth_date_str.split('/')
    year_num = int(year_str)
    
    last_two_digits_sum = sum(int(digit) for digit in year_str[-2:])
    reduced_year_digits = reduce_to_single_digit(last_two_digits_sum)
    
    kua_number = 0
    
    if year_num < 2000:
        if gender.lower() == 'male':
            kua_number = 10 - reduced_year_digits
        else: # Female
            kua_number = 5 + reduced_year_digits
    else: # Born in or after 2000
        if gender.lower() == 'male':
            kua_number = 9 - reduced_year_digits
        else: # Female
            kua_number = 6 + reduced_year_digits
            
    # Apply the special case for Kua 5
    if kua_number == 5:
        if gender.lower() == 'male':
            kua_number = 2
        else: # Female
            kua_number = 8
            
    return reduce_to_single_digit(kua_number)

def get_birth_chart_digits(birth_date_str):
    all_digits_str = birth_date_str.replace('/', '')
    return [int(digit) for digit in all_digits_str if digit != '0']

def generate_complete_lo_shu_grid(birth_date_str, psychic_num, destiny_num, kua_num):
    dob_digits = get_birth_chart_digits(birth_date_str)
    all_digits = dob_digits + [psychic_num, destiny_num, kua_num]
    
    grid_positions = {
        4: (0, 0), 9: (0, 1), 2: (0, 2),
        3: (1, 0), 5: (1, 1), 7: (1, 2),
        8: (2, 0), 1: (2, 1), 6: (2, 2)
    }
    
    grid = [['', '', ''], ['', '', ''], ['', '', '']] # Use empty strings to avoid extra spaces
    for digit in all_digits:
        if digit in grid_positions:
            row, col = grid_positions[digit]
            grid[row][col] += str(digit)

    grid_str = ""
    grid_str += f" --- --- ---\n"
    grid_str += f"| {grid[0][0]:<2}| {grid[0][1]:<2}| {grid[0][2]:<2}|\n"
    grid_str += f" --- --- ---\n"
    grid_str += f"| {grid[1][0]:<2}| {grid[1][1]:<2}| {grid[1][2]:<2}|\n"
    grid_str += f" --- --- ---\n"
    grid_str += f"| {grid[2][0]:<2}| {grid[2][1]:<2}| {grid[2][2]:<2}|\n"
    grid_str += f" --- --- ---\n"
    
    return grid_str, all_digits