from project.custom_list import CustomList
from unittest import TestCase, main


class CustomListTest(TestCase):

    def setUp(self) -> None:
        self.custom_list = CustomList()

    def test_append_method_adds_element_at_the_end_of_the_list(self):
        custom_list = CustomList()
        self.assertEqual([], custom_list._CustomList__values)

        custom_list.append(5)

        self.assertEqual([5], custom_list._CustomList__values)

    def test_remove_method_when_received_invalid_index_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(IndexError) as er:
            self.custom_list.remove(0)

        self.assertEqual("Invalid index", str(er.exception))

    def test_remove_method_when_received_index_not_integer_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.remove('0')

        self.assertEqual("Index is not a valid integer", str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.custom_list.remove(1.2)

        self.assertEqual("Index is not a valid integer", str(er.exception))

    def test_remove_method_removes_element_and_return_its_value(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        returned_element = self.custom_list.remove(0)

        self.assertEqual([], self.custom_list._CustomList__values)
        self.assertEqual(5, returned_element)

    def test_get_method_when_invalid_index_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        # Pass invalid index left border
        with self.assertRaises(IndexError) as er:
            self.custom_list.get(-2)

        self.assertEqual("Invalid index", str(er.exception))

        # Pass invalid index right border
        with self.assertRaises(IndexError) as er:
            self.custom_list.get(1)

        self.assertEqual("Invalid index", str(er.exception))

    def test_get_method_when_index_not_integer(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.get('0')

        self.assertEqual("Index is not a valid integer", str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.custom_list.get(1.5)

        self.assertEqual("Index is not a valid integer", str(er.exception))

    def test_get_method_returns_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        returned_element = self.custom_list.get(0)

        self.assertEqual(5, returned_element)
        self.assertEqual([5], self.custom_list._CustomList__values)

    def test_extend_method_with_non_iterable_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.extend(15)

        self.assertEqual("Object not an iterable", str(er.exception))

    def test_extend_method_append_received_list_and_return_new_list(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        new_list = self.custom_list.extend(['a'])

        self.assertEqual([5, 'a'], self.custom_list._CustomList__values)
        self.assertEqual([5, 'a'], new_list)
        self.assertNotEqual(id(self.custom_list), id(new_list))

    def test_insert_method_when_received_index_not_integer(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.insert(1.2, 'a')

        self.assertEqual("Index is not a valid integer", str(er.exception))

    def test_index_method_when_index_not_valid_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.insert(-1, 'a')

        self.assertEqual("Invalid index", str(er.exception))

        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.insert(1, 6)

        self.assertEqual("Invalid index", str(er.exception))

    def test_insert_method_adds_element_at_index_and_returns_list(self):
        self.custom_list.append('b')
        self.custom_list.append('c')
        self.assertEqual(['b', "c"], self.custom_list._CustomList__values)

        lst = self.custom_list.insert(0, 'a')

        self.assertEqual(['a', 'b', 'c'], self.custom_list._CustomList__values)
        self.assertEqual(id(self.custom_list._CustomList__values), id(lst))

    def test_pop_method_when_list_is_empty_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.pop()

        self.assertEqual("Can not pop element form empty list!", str(er.exception))

    def test_pop_method_returns_last_element(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        popped_element = self.custom_list.pop()

        self.assertEqual(5, popped_element)
        self.assertEqual([], self.custom_list._CustomList__values)

    def test_clear_method(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.assertEqual([5, 'a'], self.custom_list._CustomList__values)

        self.custom_list.clear()

        self.assertEqual([], self.custom_list._CustomList__values)

    def test_index_method_when_value_not_exists_raises(self):
        self.custom_list.append('a')
        self.assertEqual(['a'], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.index('b')

        self.assertEqual("The value not exists in the list!", str(er.exception))

    def test_index_method_returns_value_of_received_index(self):
        self.custom_list.append('a')
        self.assertEqual(['a'], self.custom_list._CustomList__values)

        index = self.custom_list.index('a')

        self.assertEqual(0, index)

    def test_count_method_when_value_not_exist_raises(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.custom_list.append(25)
        self.assertEqual([5, 15, 25], self.custom_list._CustomList__values)

        with self.assertRaises(ValueError) as er:
            self.custom_list.count(35)

        self.assertEqual("Not such value in the list", str(er.exception))

    def test_count_method_returns_count_of_value(self):
        self.custom_list.append(5)
        self.custom_list.append(15)
        self.custom_list.append(5)
        self.assertEqual([5, 15, 5], self.custom_list._CustomList__values)

        value_count = self.custom_list.count(5)

        self.assertEqual(2, value_count)

    def test_reverse_method_returns_reversed_list(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        self.custom_list.reverse()

        self.assertEqual([], self.custom_list._CustomList__values)

        self.custom_list.append('a')
        self.custom_list.append(1)
        self.custom_list.append('c')
        self.assertEqual(['a', 1, 'c'], self.custom_list._CustomList__values)

        reversed_lst = self.custom_list.reverse()

        self.assertEqual(['a', 1, 'c'], self.custom_list._CustomList__values)
        self.assertEqual(['c', 1, 'a'], reversed_lst)

    def test_copy_method_returns_same_elements_in_different_list(self):
        self.custom_list.append('a')
        self.custom_list.append(1)
        self.custom_list.append('c')
        self.assertEqual(['a', 1, 'c'], self.custom_list._CustomList__values)

        copied_lst = self.custom_list.copy()

        self.assertEqual(self.custom_list._CustomList__values, copied_lst)
        self.assertNotEqual(id(self.custom_list._CustomList__values), id(copied_lst))

    def test_size_method_returns_size_of_the_list(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        lst_size = self.custom_list.size()

        self.assertEqual(0, lst_size)

        self.custom_list.append(5)
        self.custom_list.append('a')

        lst_size = self.custom_list.size()

        self.assertEqual(2, lst_size)

    def test_add_first_method_adds_element_at_the_begging(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.assertEqual([5, 'a'], self.custom_list._CustomList__values)

        self.custom_list.add_first('z')

        self.assertEqual(['z', 5, 'a'], self.custom_list._CustomList__values)

    def test_dictionize_method_when_size_of_list_is_even(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.assertEqual([5, 'a'], self.custom_list._CustomList__values)

        lst_to_dict = self.custom_list.dictionize()

        self.assertEqual({5: 'a'}, lst_to_dict)

    def test_dictionize_method_when_size_of_list_is_odd(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.custom_list.append(2)
        self.assertEqual([5, 'a', 2], self.custom_list._CustomList__values)

        lst_to_dict = self.custom_list.dictionize()

        self.assertEqual({5: 'a', 2: ' '}, lst_to_dict)

    def test_move_method_when_received_amount_bigger_than_list_size_raises(self):
        self.custom_list.append(5)
        self.assertEqual([5], self.custom_list._CustomList__values)

        with self.assertRaises(Exception) as ex:
            self.custom_list.move(2)

        self.assertEqual("Elements amount is bigger than size of the list", str(ex.exception))

    def test_move_method(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.assertEqual([5, 'a'], self.custom_list._CustomList__values)

        lst = self.custom_list.move(2)

        self.assertEqual([5, 'a'], lst)
        self.assertEqual(id(self.custom_list._CustomList__values), id(lst))

        self.custom_list.append(3)
        self.assertEqual([5, 'a', 3], self.custom_list._CustomList__values)

        lst = self.custom_list.move(2)

        self.assertEqual([3, 5, 'a'], lst)
        self.assertEqual(id(self.custom_list._CustomList__values), id(lst))

    def test_sum_method_return_sum_of_elements(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        elements_sum = self.custom_list.sum()

        self.assertEqual(0, elements_sum)

        self.custom_list.append(5)
        self.custom_list.append('a')
        self.custom_list.append(1.2)
        self.custom_list.append('xyz')
        self.assertEqual([5, 'a', 1.2, 'xyz'], self.custom_list._CustomList__values)

        elements_sum = self.custom_list.sum()

        self.assertEqual(10.2, elements_sum)

    def test_overbound_method_when_list_is_empty_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(Exception) as ex:
            self.custom_list.overbound()

        self.assertEqual("The list is empty", str(ex.exception))

    def test_overbound_method_returns_biggest_value(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.custom_list.append(1.2)
        self.custom_list.append('xyzaaa')
        self.assertEqual([5, 'a', 1.2, 'xyzaaa'], self.custom_list._CustomList__values)

        index = self.custom_list.overbound()

        self.assertEqual(3, index)

    def test_underbound_method_when_list_is_empty_raises(self):
        self.assertEqual([], self.custom_list._CustomList__values)

        with self.assertRaises(Exception) as ex:
            self.custom_list.underbound()

        self.assertEqual("The list is empty", str(ex.exception))

    def test_underbound_method_returns_biggest_value(self):
        self.custom_list.append(5)
        self.custom_list.append('a')
        self.custom_list.append(1)
        self.custom_list.append('xyzaaa')
        self.assertEqual([5, 'a', 1, 'xyzaaa'], self.custom_list._CustomList__values)

        index = self.custom_list.underbound()

        self.assertEqual(1, index)


if __name__ == '__main__':
    main()
