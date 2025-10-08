class SimpleValidator:
    def is_valid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", " ")
            s = s.replace("{}", " ")
            s = s.replace("[]", " ")
        return s == " "

# Example usage
validator = SimpleValidator()
print(validator.is_valid("()"))          
print(validator.is_valid("(){}[]"))      
print(validator.is_valid("[)"))           
print(validator.is_valid("({{)]"))        
print(validator.is_valid("{{{"))          
