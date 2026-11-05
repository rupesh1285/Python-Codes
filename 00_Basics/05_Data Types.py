def show_basic_data_types():
    integer_value = 5
    float_value = 3.14
    complex_value = 1 + 2j

    true_value = True
    false_value = False
    none_value = None
    string_value = "Hello, World!"
    list_value = [1, 2, 3, 4, 5]
    tuple_value = (1, 2, 3, 4, 5)
    set_value = {1, 2, 3, 4, 5}
    dictionary_value = {"name": "John", "age": 30, "city": "New York"}

    print(type(integer_value))  # <class 'int'>
    print(type(float_value))  # <class 'float'>
    print(type(complex_value))  # <class 'complex'>
    print(type(true_value))  # <class 'bool'>
    print(type(false_value))  # <class 'bool'>
    print(type(none_value))  # <class 'NoneType'>
    print(type(string_value))  # <class 'str'>
    print(type(list_value))  # <class 'list'>
    print(type(tuple_value))  # <class 'tuple'>
    print(type(set_value))  # <class 'set'>
    print(type(dictionary_value))  # <class 'dict'>


def show_integer_data_types():
    positive_integer = 1
    large_integer = 35656222554887711
    negative_integer = -3255522

    print(type(positive_integer))
    print(type(large_integer))
    print(type(negative_integer))


def show_float_data_types():
    scientific_float = 35e3
    uppercase_scientific_float = 12E4
    negative_scientific_float = -87.7e100

    print(type(scientific_float))
    print(type(uppercase_scientific_float))
    print(type(negative_scientific_float))


def show_complex_data_types():
    complex_number = 3 + 5j
    imaginary_number = 5j
    negative_imaginary_number = -5j

    print(type(complex_number))
    print(type(imaginary_number))
    print(type(negative_imaginary_number))


if __name__ == "__main__":
    show_basic_data_types()
    show_integer_data_types()
    show_float_data_types()
    show_complex_data_types()
