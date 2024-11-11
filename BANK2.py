class Cuenta:  
    def __init__(self, bank_account, balance):
        """
        Inicializa la cuenta bancaria con un número de cuenta y un saldo inicial.
        """
        self.bank_account = bank_account  
        self.balance = balance  

    def operaciones(self):
        """
        Muestra el menú de operaciones al usuario y llama a los métodos según su elección.
        """
        while True:
            try:
                opcion = int(input('''
        ------------------------------------------
        POR FAVOR INDIQUE QUE OPERACIÓN DESEA REALIZAR..
        1. CONSULTAR BALANCE
        2. DEPÓSITO A CUENTA
        3. RETIRO DE EFECTIVO
        4. SALIR
        Opción: '''))
                
                if opcion == 1:
                    print(f"Su balance actual es de: {self.get_balance()}€")
                elif opcion == 2:
                    cantidad = int(input("Introduzca la cantidad a depositar: "))
                    self.deposito(cantidad)
                elif opcion == 3:
                    cantidad = int(input("Introduzca la cantidad a retirar: "))
                    self.retirar(cantidad)
                elif opcion == 4:
                    self.salir()
                    break
                else:
                    print("Lo sentimos, opción no válida. Intente de nuevo.")
            except ValueError:
                print("Por favor, introduzca un número válido para la opción.")
    
    def deposito(self, cantidad):
        """
        Realiza un depósito si la cantidad es positiva.
        """
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se han depositado {cantidad}€. Su balance actual es de: {self.balance}€")
        else:
            print("Por favor, introduzca una cantidad positiva para depositar.")
    
    def retirar(self, cantidad):
        """
        Realiza un retiro si la cantidad es positiva y hay suficiente saldo.
        """
        if cantidad > 0:
            if self.balance >= cantidad:
                self.balance -= cantidad  
                print(f"Se han retirado {cantidad}€. Su balance actual es de: {self.balance}€")
            else:
                print(f"Fondos insuficientes. Su balance actual es de: {self.balance}€")
        else:
            print("Por favor, introduzca una cantidad positiva para retirar.")

    def get_balance(self): 
        """
        Devuelve el balance actual de la cuenta.
        """
        return self.balance

    def salir(self):
        """
        Muestra un mensaje de despedida al usuario.
        """
        print("Gracias por su visita.")                                                                                                          

# Clase hija para cuenta de ahorros
class SavingsAccount(Cuenta):
    def __init__(self, bank_account, balance, interest_rate):
        super().__init__(bank_account, balance)
        self.interest_rate = interest_rate  # Tasa de interés anual

    def calculate_interest(self, years):
        """
        Calcula los intereses generados sobre el balance en un tiempo dado (años).
        """
        interest = self.balance * (self.interest_rate / 100) * years
        print(f"Interés generado en {years} años con una tasa del {self.interest_rate}%: {interest}€")
        return interest

# Clase hija para cuenta corriente
class CheckingAccount(Cuenta):
    def __init__(self, bank_account, balance, overdraft_limit):
        super().__init__(bank_account, balance)
        self.overdraft_limit = overdraft_limit  # Límite de sobregiro

    def retirar(self, cantidad):
        """
        Sobrescribe el método de retiro para permitir el uso de sobregiro hasta el límite.
        """
        if cantidad > 0:
            if self.balance + self.overdraft_limit >= cantidad:
                self.balance -= cantidad
                print(f"Se han retirado {cantidad}€. Su balance actual es de: {self.balance}€")
            else:
                print(f"Fondos insuficientes, incluso con sobregiro. Su balance actual es de: {self.balance}€ y su límite de sobregiro es de {self.overdraft_limit}€")
        else:
            print("Por favor, introduzca una cantidad positiva para retirar.")

# Ejemplo de uso
savings_account = SavingsAccount("12345", 1000, 3)  # Cuenta de ahorros con 3% de interés anual
checking_account = CheckingAccount("67890", 500, 200)  # Cuenta corriente con límite de sobregiro de 200€

# Interacciones con la cuenta de ahorros
savings_account.operaciones()
savings_account.calculate_interest(2)  # Calcula interés para 2 años

# Interacciones con la cuenta corriente
checking_account.operaciones()
