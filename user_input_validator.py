class UserInputValidator:
    def validate_positive_integers(self, items):
        valid_numbers = []
        for i in items:
            if i.isdigit() and int(i) > 0:
                valid_numbers.append(int(i))
        return valid_numbers
    def display_validation_message(self, items):
        print('Validating input:',items)