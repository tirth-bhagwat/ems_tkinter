from emsdb import *


class Employee:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        email: str,
        designation: str,
        doj: datetime.date,
        gender: str,
        contact: str,
        address: str,
    ):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.designation = designation
        self.doj = doj
        self.gender = gender
        self.contact = contact
        self.address = address

    @classmethod
    def create_new(
        self,
        name: str,
        age: int,
        email: str,
        designation: str,
        doj: datetime.date,
        gender: str,
        contact: str,
        address: str,
    ):
        return Employee(
            id=None,
            name=name,
            age=age,
            email=email,
            designation=designation,
            doj=doj,
            gender=gender,
            contact=contact,
            address=address,
        )

    def to_tuple(self):
        return (
            str(self.name),
            str(self.age),
            str(self.email),
            str(self.designation),
            str(self.doj),
            str(self.gender),
            str(self.contact),
            str(self.address),
        )

    def __str__(self):
        return str(
            {
                "name": str(self.name),
                "age": str(self.age),
                "email": str(self.email),
                "designation": str(self.designation),
                "doj": str(self.doj),
                "gender": str(self.gender),
                "contact": str(self.contact),
                "address": str(self.address),
            }
        )


db = Database("employee.db")

# create 4 employees

emp1 = Employee.create_new(
    name="Rahul",
    age=25,
    email="rahul22@gmail.com",
    designation="Operator",
    doj="01/12/2019",
    gender="Male",
    contact="9876543210",
    address="23-Abc flats, Mumbai, Maharashtra - 400001",
)

emp2 = Employee.create_new(
    name="Riya",
    age=22,
    email="riya@gmail.com",
    designation="Manager",
    doj="01/12/2019",
    gender="Female",
    contact="9876543211",
    address="23-Abc flats, Vadodara, Gujarat - 390001",
)

emp3 = Employee.create_new(
    name="Raj",
    age=44,
    email="raj@gmail.com",
    designation="Senior Engineer",
    doj="01/12/2019",
    gender="Male",
    contact="9876543212",
    address="29-Pqr residency, Rajkot, Gujarat - 360001",
)

emp4 = Employee.create_new(
    name="Karan",
    age=30,
    email="karan@gmail.com",
    designation="Operator",
    doj="01/12/2019",
    gender="Male",
    contact="9876543213",
    address="02-Xyz flats, Vadodara, Gujarat - 390001",
)


# db.insert(*emp1.to_tuple())
# db.insert(*emp2.to_tuple())
# db.insert(*emp3.to_tuple())
# db.insert(*emp4.to_tuple())


# print(db.fetch_002(1))
# print(db.fetch_all_002())

# print(db.fetch_by_contact_002("9876543210"))
print(db.fetch_by_contact_002("9876500000"))
