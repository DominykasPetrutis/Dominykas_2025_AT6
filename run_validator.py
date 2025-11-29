from user_input_validator import UserInputValidator

validator1 = UserInputValidator()
validator2 = UserInputValidator()

data1 = ['12', '25', 'abc', '-3']
data2 = ['7', '0', 'hello', '99']

validator1.display_validation_message(data1)
result1 = validator1.validate_positive_integers(data1)
print('Validated numbers (validator1):', result1)

validator2.display_validation_message(data2)
result2 = validator2.validate_positive_integers(data2)
print('Validated numbers (validator2):', result2)