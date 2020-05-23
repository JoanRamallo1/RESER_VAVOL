class User:

    def __init__(self):
        self.DNI = 0
        self.Nombre = ' '
        self.Apellido1 = ' '
        self.Apellido2 = ' '
        self.Telf = 0
        self.Email = ' '
        self.Sexo = ' '
        self.Nacionalidad = ' '
        self.FechaNacimiento = [0,0,0] 
        """dia, mes, año"""
    
    def Insert_User_Data(self, DNI, name, a1, a2, phone, email, sex, nacionality, birthdate):
        self.DNI = DNI
        self.Nombre = name
        self.Apellido1 = a1
        self.Apellido2 = a2
        self.Telf = phone
        self.Email = email
        self.Sexo = sex
        self.Nacionalidad = nacionality
        self.FechaNacimiento = birthdate
        

