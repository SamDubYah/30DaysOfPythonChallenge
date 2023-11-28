import math

class Person:
    def __init__ (self, firstname='Samuel', lastname='Warner', age='27', country='Dallas', city='USA'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []
        
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    
    def add_skill(self, skill):
        self.skills.append(skill)

class Student(Person):
    def __init__ (self, firstname='Samuel', lastname='Warner', age='27', country='Dallas', city='USA', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
        
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}'

print()
print("Studen Info: ")
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

print()
print("Person Info: ")
p1 = Person()
print(p1.person_info())
p1.add_skill('Python')
p1.add_skill('C++')
p1.add_skill('Computer Hacking')
p2 = Person('John', 'Doe', '32', 'USA', 'Anytown')
print(p2.person_info())
print(p1.skills)
print(p2.skills)


############ EXERCISES ###############

#### Exercise 1

class Statistics:
    def __init__ (self, ages=[]):
        self.ages = ages
        #self.count = self.calc_Count()
        self.sum = self.calc_Sum()
        self.min = self.calc_Min()
        self.max = self.calc_Max()
        self.range = self.calc_Range()
        self.mean = self.calc_Mean()
        self.median = self.calc_Median()
        self.mode = self.calc_Mode()
        self.variance = self.calc_Variance()
        self.std_Deviation = self.calc_std_Deviation()
        self.freq_Distribution = self.calc_freq_Distribution()
    
    # Calculate count of supplied ages
    def count(self):
        return len(self.ages)
    
    # Calculate sum of all ages
    def calc_Sum(self):
        return sum(self.ages)

    # Calculate miniuman age value
    def calc_Min(self):
        return min(self.ages)
    
    # Calculate maximum age value
    def calc_Max(self):
        return max(self.ages)
    
    # Calculate range of age values
    def calc_Range(self):
        # Calculated by sorting the array, taking last element minus first
        return sorted(self.ages)[-1] - sorted(self.ages)[0]
    
    # Calculate mean of age values
    def calc_Mean(self):
        return (self.sum / self.count()) 
    
    # Calculate median of age values
    #   Calculated by sorting ages, and returning middle element [(array length / 2)]
    def calc_Median(self):
        # Typcasted to int to avoid floats from division
        return sorted(self.ages)[int((self.count() / 2 ))]
    
    # Calculate Mode of age values
    #   Iterate through array assinging counts to each found number
    def calc_Mode(self):
        ages_Dict = {}
        
        # Iterate through ages, add age key if DNE, increase count by 1
        for age in self.ages:
            if age in ages_Dict:
                ages_Dict[age] += 1
            else:
                ages_Dict[age] = 1
        
        # List/Dict comprehension on sorted dictionary using *.get for sorting on key
        #   [-1] to return last item in array ( Mode )
        return [(k, ages_Dict[k]) for k in sorted(ages_Dict, key=ages_Dict.get)][-1]
    
    
    # Calculate Variance of ages
    def calc_Variance(self):
        # Step 1: Find mean (self.mean)
        # Step 2: For each data point, find square of distance to mean
        # Step 3: Sum value from step 2
        # Step 4: Divide by number of data points (self.count)
        
        # Define & initialize summation prior to loop
        summation = 0
        
        #STEP 2-3
        for age in self.ages:
            summation += (age - self.mean) ** 2
            
        # STEP 4    
        # Return variance: Summation / # of elements
        return (summation / self.count())
    
    
    # Calculate Standard Deviation of ages
    def calc_std_Deviation(self):
        #~~~~~ self.variance
        # Step 1: Find mean (self.mean)
        # Step 2: For each data point, find square of distance to mean
        # Step 3: Sum value from step 2
        # Step 4: Divide by number of data points (self.count)
        #~~~~~ self.variance
        # Step 5: Take square root
     
        # Step 5
        # Calculate the squar root of ( summation of deviations / number of entitites )
        return math.sqrt(self.variance)
    
    # Caculate Relative Frequency distribution of ages
    def calc_freq_Distribution (self):
        # Step 1: Calculate frequency values
        # Step 2: Devide freq values by # of elements
        # Step 3: return in (value, element) format
        
        freq_dict = {}
        
        # Build dictionary with frequency counts
        for age in self.ages:
            if age in freq_dict:
                freq_dict[age] += 1
            else:
                freq_dict[age] = 1
                
        # Format (Freq Dist %, Data Point)
        #   Divide Freq Dist by self.count(elements in list) to get percent
        #   Multiply value by 100, to get normalized percentile
        #   Sorted freq_dict by values, and reversed order to put high value first
        return [((freq_dict[k]/self.count())*100, k) for k in sorted(freq_dict, key=freq_dict.get, reverse=True)]


    def describe(self):
        # std_Devation, Variance: formated to print 1 decimal point
        return f"""
            Count:\t\t\t {self.count()}
            Sum:\t\t\t {self.sum}
            Min:\t\t\t {self.min}
            Max:\t\t\t {self.max}
            Min:\t\t\t {self.min}
            Range:\t\t\t {self.range}
            Mean:\t\t\t {self.mean}
            Median:\t\t\t {self.median}
            Mode:\t\t\t {self.mode}
            Variance:\t\t\t {self.variance:.1f}
            Standard Deviation:\t\t {self.std_Deviation:.1f}
            Frequency Distribution:\t {self.freq_Distribution}
                """
                
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum) # 744
print('Min: ', data.min) # 24
print('Max: ', data.max) # 38
print('Range: ', data.range) # 14
print('Mean: ', data.mean) # 30
print('Median: ', data.median) # 29
print('Mode: ', data.mode) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std_Deviation) # 4.2
print('Variance: ', data.variance) # 17.5
print('Frequency Distribution: ', data.freq_Distribution) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

#### Exercise 2

class PersonAccount:
    def __init__ (self, Firstname, Lastname, Incomes={}, Expenses={}):
        self.firstname = Firstname
        self.lastname = Lastname
        self.incomes = Incomes
        self.expenses = Expenses
        self.account_balance = self.account_balance()
        self.total_income = self.total_income()
        self.total_expense = self.total_expense()
        
    
    def total_income(self):
        return sum([v for v in self.incomes.values()])
    
    def total_expense(self):
        return sum([v for v in self.expenses.values()])
    
    def add_income(self, income, description):
        self.incomes[description] = income
    
    def add_expense(self, expense, description):
        self.expenses[description] = expense
        
    def account_balance(self):
        return (self.total_income() - self.total_expense())
    
        
incomes = {"one": 1000, "two": 2000, "three": 3000}
expenses = {"one": 999, "two": 1999, "three": 2999}

p1 = PersonAccount("Samuel", "Warner", incomes, expenses)

print("Before income/expense add: ", p1.account_balance)
p1.add_expense(3999, "four")
p1.add_income(450000, "four")
print("After income/expense add: ", p1.account_balance) # Not printed updated balance
print(p1.incomes)
print(p1.expenses)
