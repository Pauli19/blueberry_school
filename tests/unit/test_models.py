"""This module contains tests for models."""
import datetime
from decimal import Decimal

import pytest

from app.models import (
    Class,
    Cycle,
    Level,
    Mode,
    Month,
    Payment,
    Representative,
    Student,
    SubLevel,
    User,
    load_user,
)
from factories import (
    ClassFactory,
    CycleFactory,
    PaymentFactory,
    RepresentativeFactory,
    StudentFactory,
    UserFactory,
)


def test_user_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN a User instance is created
    THEN User is created properly
        - data is stored in the database
        - information is set properly
    """
    first_name = "John"
    first_surname = "Smith"
    email = "user@example.com"
    user = UserFactory(first_name=first_name, first_surname=first_surname, email=email)

    assert user.id is not None
    assert user.first_name == first_name
    assert user.first_surname == first_surname
    assert user.email == email


def test_user_str():
    """
    GIVEN a User instance which
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN converted to a string
    THEN the string is
        "John Smith - user@example.com"
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    assert str(user) == "John Smith - user@example.com"


def test_user_representation():
    """
    GIVEN
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN calling repr
    THEN the returned string is
        'User(first_name="John", first_surname="Smith", email="user@example.com")'
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    expected_repr = (
        'User(first_name="John", first_surname="Smith", email="user@example.com")'
    )
    assert repr(user) == expected_repr


@pytest.mark.parametrize(
    "user,expected_full_name",
    [
        pytest.param(
            User(
                first_name="John",
                second_name="James",
                first_surname="Smith",
                second_surname="Black",
            ),
            "John James Smith Black",
            id="all-names",
        ),
        pytest.param(
            User(
                first_name="John",
                second_name="James",
                first_surname="Smith",
            ),
            "John James Smith",
            id="two-names-first-surname",
        ),
        pytest.param(
            User(
                first_name="John",
                first_surname="Smith",
                second_surname="Black",
            ),
            "John Smith Black",
            id="first-name-two-surnames",
        ),
        pytest.param(
            User(first_name="John", first_surname="Smith"),
            "John Smith",
            id="first-name-first-surname",
        ),
    ],
)
def test_user_full_name(user, expected_full_name):
    """
    GIVEN a User instance
    WHEN getting its property full_name
    THEN property is equal to expected_full_name
    """
    assert user.full_name == expected_full_name


def test_user_password_not_readable():
    """
    GIVEN a User instance which
        first_name is "John"
        last_name is "Smith"
        and email is "user@example.com"
    WHEN trying to access password
    THEN verify that
        - an AttributeError exception is raised
        - exception message is "password is not a readable attribute"
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    message = "password is not a readable attribute"
    with pytest.raises(AttributeError, match=message):
        user.password  # pylint: disable=pointless-statement


def test_user_password_is_hashed():
    """
    GIVEN a User instance
    WHEN user's password is set
    THEN user's password_hash is not None
    """
    user = User()
    user.password = "this-is-a-password"
    assert user.password_hash is not None


def test_load_user(app):  # pylint: disable=unused-argument
    """
    GIVEN a User instance
    WHEN calling load_user with User instance's id
    THEN User instance is the same as loaded User instance
    """
    first_name = "John"
    first_surname = "Smith"
    email = "user@example.com"
    user = UserFactory(first_name=first_name, first_surname=first_surname, email=email)
    loaded_user = load_user(user.id)

    assert user == loaded_user


def test_user_verify_password():
    """
    GIVEN a User instance with password
    WHEN verifying password
    THEN User's verify_password method returns
        - True when the password is verified
        - False when the password is not verified
    """
    password = "this-is-a-password"
    user = User(password=password)

    assert user.verify_password(password)
    assert not user.verify_password("this-is-another-password")


def test_student_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
        email is "benhazlewood@example.com"
        birth_date is "1995-01-01"
    WHEN a Student instance is created
    THEN Student is created properly
        - data is stored in the database
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Ben"
    first_surname = "Hazlewood"
    email = "benhazlewood@example.com"
    birth_date = datetime.date(1995, 1, 1)
    student = StudentFactory(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        email=email,
        birth_date=birth_date,
    )

    assert student.id is not None
    assert student.identity_document == identity_document
    assert student.first_name == first_name
    assert student.first_surname == first_surname
    assert student.email == email
    assert student.birth_date == birth_date


def test_student_creation_with_representative(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
        email is "benhazlewood@example.com"
        birth_date is "1995-01-01"
        and an associated representative
    WHEN a Student instance is created
    THEN Student is created properly
        - data is stored in the databse
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Ben"
    first_surname = "Hazlewood"
    email = "benhazlewood@example.com"
    birth_date = datetime.date(1995, 1, 1)
    representative = RepresentativeFactory()
    student: Student = StudentFactory(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        email=email,
        birth_date=birth_date,
        representative=representative,
    )

    assert student.id is not None
    assert student.identity_document == identity_document
    assert student.first_name == first_name
    assert student.first_surname == first_surname
    assert student.email == email
    assert student.birth_date == birth_date
    assert student.representative == representative


def test_student_str():
    """
    GIVEN a Student instance which
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
    WHEN converted to a string
    THEN the string is
        "1020304050 - Ben Hazlewood"
    """
    student = Student(
        identity_document="1020304050",
        first_name="Ben",
        first_surname="Hazlewood",
    )
    assert str(student) == "1020304050 - Ben Hazlewood"


def test_student_representation():
    """
    GIVEN a Student instance which
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
    WHEN calling repr
    THEN the returned string is
        'Student(
            identity_document="1020304050",
            first_name="Ben",
            first_surname="Hazlewood")'
    """
    student = Student(
        identity_document="1020304050",
        first_name="Ben",
        first_surname="Hazlewood",
    )
    expected_repr = (
        'Student(identity_document="1020304050", '
        'first_name="Ben", first_surname="Hazlewood")'
    )
    assert repr(student) == expected_repr


def test_representative_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
        phone_number is "+593987654321"
    WHEN a Representative instance is created
    THEN Representative is created properly
        - data is stored in the database
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Katy"
    first_surname = "Perry"
    phone_number = "+593987654321"
    representative = RepresentativeFactory(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        phone_number=phone_number,
    )

    assert representative.id is not None
    assert representative.identity_document == identity_document
    assert representative.first_name == first_name
    assert representative.first_surname == first_surname
    assert representative.phone_number.e164 == phone_number


def test_representative_str():
    """
    GIVEN a Representative instance which
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
    WHEN when converted to a string
    THEN the string is
        "1020304050 - Katy Perry"
    """
    representative = Representative(
        identity_document="1020304050",
        first_name="Katy",
        first_surname="Perry",
    )
    assert str(representative) == "1020304050 - Katy Perry"


def test_representative_representation():
    """
    GIVEN a Representative instance which
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
    WHEN calling repr
    THEN the returned string is
        'Representative(
            identity_document="1020304050",
            first_name="Katy",
            first_surname="Perry")'
    """
    representative = Representative(
        identity_document="1020304050", first_name="Katy", first_surname="Perry"
    )
    expected_repr = (
        'Representative(identity_document="1020304050", '
        'first_name="Katy", first_surname="Perry")'
    )
    assert repr(representative) == expected_repr


def test_cycle_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        month is "NOVEMBER"
        year is 2022
        start_date is "2022-11-01"
        end_date is "2022-11-30"
    WHEN a Cycle instance is created
    THEN Cycle is created properly
        - data is stored in the database
        - information is set properly
    """
    month = Month.NOVEMBER
    year = 2022
    start_date = datetime.date(2022, 11, 1)
    end_date = datetime.date(2022, 11, 30)

    cycle = CycleFactory(
        month=month,
        year=year,
        start_date=start_date,
        end_date=end_date,
    )

    assert cycle.id is not None
    assert cycle.month == month
    assert cycle.year == year
    assert cycle.start_date == start_date
    assert cycle.end_date == end_date


def test_cycle_str():
    """
    GIVEN a Cycle instance which
        month is "NOVEMBER"
        year is 2022
    WHEN converted to a string
    THEN the string is
        "November - 2022"
    """
    cycle = Cycle(month=Month.NOVEMBER, year=2022)

    assert str(cycle) == "November - 2022"


def test_cycle_representation():
    """
    GIVEN a Cycle instance which
        month is "NOVEMBER"
        year is 2022
    WHEN calling repr
    THEN the returned string is
        'Cycle(month="November", year=2022)'
    """
    cycle = Cycle(month=Month.NOVEMBER, year=2022)
    expected_repr = 'Cycle(month="November", year=2022)'

    assert repr(cycle) == expected_repr


def test_class_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        mode = "Normal"
        start_at = "20:00"
        end_at = "21:00"
        level = "L1"
        sub_level = "P1"
        and an associated cycle
    WHEN a Class instance is created
    THEN Class is created properly
        - data is stored in the databse
        - information is set properly
    """
    mode = Mode.NORMAL
    start_at = datetime.time(20, 0)
    end_at = datetime.time(21, 0)
    level = Level.L1
    sub_level = SubLevel.P1
    cycle = CycleFactory()
    class_: Class = ClassFactory(
        mode=mode,
        start_at=start_at,
        end_at=end_at,
        level=level,
        sub_level=sub_level,
        cycle=cycle,
    )

    assert class_.id is not None
    assert class_.mode == mode
    assert class_.start_at == start_at
    assert class_.end_at == end_at
    assert class_.level == level
    assert class_.sub_level == sub_level
    assert class_.cycle == cycle


def test_class_str():
    """
    GIVEN a class instance which
        mode = "Normal"
        level = "L1"
        sub_level = "P1"
    WHEN converted to a string
    THEN the string is
        "L1P1 Normal"
    """
    class_ = Class(
        mode=Mode.NORMAL,
        level=Level.L1,
        sub_level=SubLevel.P1,
    )
    assert str(class_) == "L1P1 Normal"


def test_class_repr():
    """
    GIVEN a class instance which
        mode = "Normal"
        level = "L1"
        sub_level = "P1"
    WHEN calling repr
    THEN the returned string is
        'Class(level="L1", sub_level="P1", mode="Normal")'
    """
    class_ = Class(
        mode=Mode.NORMAL,
        level=Level.L1,
        sub_level=SubLevel.P1,
    )
    expected_repr = 'Class(level="L1", sub_level="P1", mode="Normal")'
    assert repr(class_) == expected_repr


def test_payment_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        amount is 99.99
        an associated student
        and an associated cycle
    WHEN a Payment instance is created
    THEN Payment is created properly
        - data is stored in the database
        - information is set properly
    """
    amount = Decimal("99.99")
    student = StudentFactory()
    cycle = CycleFactory()
    payment: Payment = PaymentFactory(
        amount=amount,
        student=student,
        cycle=cycle,
    )

    assert payment.id is not None
    assert payment.amount == amount
    assert payment.student == student
    assert payment.cycle == cycle


def test_payment_str():
    """
    GIVEN a Payment instance which
        amount is 99.99
    WHEN converted to a string
    THEN the string is "$99.99"
    """
    payment = Payment(amount=Decimal("99.99"))
    assert str(payment) == "$99.99"


def test_payment_representation():
    """
    GIVEN a Payment instance which
        amount is 99.99
    WHEN calling repr
    THEN the returned string is
        'Payment(amount="$99.99")'
    """
    payment = Payment(amount=Decimal("99.99"))
    assert repr(payment) == 'Payment(amount="$99.99")'


@pytest.mark.parametrize(
    "payment,expected_payment_str",
    [
        pytest.param(
            Payment(amount=Decimal("99.99")),
            "$99.99",
            id="just-payment",
        ),
        pytest.param(
            Payment(amount=Decimal("99.99"), discount=Decimal("10.00")),
            "$89.99 = $99.99 - $10.00",
            id="payment-with-discount",
        ),
    ],
)
def test_payment_str_options(payment, expected_payment_str):
    """
    GIVEN a payment instance
    WHEN getting its property payment_options_str
    THEN property is equal to expected_payment_str
    """
    assert payment.payment_options_str == expected_payment_str


@pytest.mark.parametrize(
    "payment,expected_payment_repr",
    [
        pytest.param(
            Payment(amount=Decimal("99.99")),
            'Payment(amount="$99.99")',
            id="just-payment",
        ),
        pytest.param(
            Payment(amount=Decimal("99.99"), discount=Decimal("10.00")),
            'Payment(amount="$99.99", discount="$10.00")',
            id="payment-with-discount",
        ),
    ],
)
def test_payment_repr_options(payment, expected_payment_repr):
    """
    GIVEN a payment instance
    WHEN getting its property payment_options_repr
    THEN property is equal to expected_payment_repr
    """
    assert payment.payment_options_repr == expected_payment_repr
