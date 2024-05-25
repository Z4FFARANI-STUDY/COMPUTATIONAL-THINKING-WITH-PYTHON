from faker import Faker

fake = Faker("pt_BR")
print(fake.name(), fake.address(), fake.cpf())