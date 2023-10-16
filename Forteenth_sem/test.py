import pytest
from main import Person, Employee, InvalidNameError, InvalidAgeError, InvalidIdError


@pytest.fixture
def valid_person_data():
    return "Ivanov", "Ivan", "Ivanovich", 30


@pytest.fixture
def valid_employee_data():
    return "Ivanov", "Ivan", "Ivanovich", 30, 123456


def test_person_initialization(valid_person_data):
    last_name, first_name, patronymic, age = valid_person_data
    person = Person(last_name, first_name, patronymic, age)
    assert person.full_name() == "Ivanov Ivan Ivanovich"
    assert person.get_age() == 30


def test_employee_initialization(valid_employee_data):
    last_name, first_name, patronymic, age, id_ = valid_employee_data
    employee = Employee(last_name, first_name, patronymic, age, id_)
    assert employee.full_name() == "Ivanov Ivan Ivanovich"
    assert employee.get_age() == 30
    assert employee.id == 123456


def test_invalid_person_name(valid_person_data):
    last_name, first_name, patronymic, age = valid_person_data
    with pytest.raises(InvalidNameError):
        Person("", first_name, patronymic, age)


def test_invalid_person_age(valid_person_data):
    last_name, first_name, patronymic, age = valid_person_data
    with pytest.raises(InvalidAgeError):
        Person(last_name, first_name, patronymic, -1)


def test_invalid_employee_id(valid_employee_data):
    last_name, first_name, patronymic, age, id_ = valid_employee_data
    with pytest.raises(InvalidIdError):
        Employee(last_name, first_name, patronymic, age, -1)


def test_employee_level(valid_employee_data):
    last_name, first_name, patronymic, age, id_ = valid_employee_data
    employee = Employee(last_name, first_name, patronymic, age, id_)
    assert employee.get_level() == sum(int(num) for num in str(id_)) % Employee.MAX_LEVEL
