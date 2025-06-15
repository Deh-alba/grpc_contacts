import random



#Class to generate pseudo randon name and phone numbers
class randon_info:


    def get_random_name(self):
        first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Judy"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        return f"{first_name} {last_name}"

    def get_randon_phone_number(self):
        area_code = random.randint(100, 999)
        central_office_code = random.randint(100, 999)
        line_number = random.randint(1000, 9999)
        
        return f"{area_code}{central_office_code}{line_number}"

    