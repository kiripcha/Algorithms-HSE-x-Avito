import pytest
from src.hash_table import HashTable

def test_put_get():
    '''вставка и получения значений'''
    ht = HashTable()
    ht.put("key1", 1)
    ht.put("key2", 2)
    assert ht.get("key1") == 1
    assert ht.get("key2") == 2
    assert ht.get("key3") == None

def test_update_value():
    '''обновление значения для существующего ключа'''
    ht = HashTable()
    ht.put("key1", 1)
    ht.put("key1", 10)
    assert ht.get("key1") == 10
    assert ht.count == 1

def test_remove():
    '''удаление элементов'''
    ht = HashTable()
    ht.put("key1", 1)
    ht.put("key2", 2)
    assert ht.remove("key1") == True
    assert ht.get("key1") == None
    assert ht.count == 1
    assert ht.remove("key3") == False

def test_collision_handling():
    '''обработка коллизий'''
    ht = HashTable(size=1)  # заставляем все ключи попадать в один бакет
    ht.put("key1", 1)
    ht.put("key2", 2)
    assert ht.get("key1") == 1
    assert ht.get("key2") == 2
    assert ht.count == 2

def test_resize():
    '''расширение таблицы'''
    ht = HashTable(size=2)
    ht.put("key1", 1)
    ht.put("key2", 2)
    ht.put("key3", 3)  # должно вызвать расширение
    assert ht.get("key1") == 1
    assert ht.get("key2") == 2
    assert ht.get("key3") == 3
    assert ht.count == 3
    assert len(ht.buckets) > 2

def test_empty_table():
    '''операции с пустой таблицей'''
    ht = HashTable()
    assert ht.get("key1") == None
    assert ht.remove("key1") == False
    assert ht.count == 0

def test_different_key_types():
    '''работа с разными типами ключей'''
    ht = HashTable()
    ht.put("string_key", 1)
    ht.put(123, 2)
    ht.put(3.14, 3)
    assert ht.get("string_key") == 1
    assert ht.get(123) == 2
    assert ht.get(3.14) == 3
    assert ht.count == 3