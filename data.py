__author__ = 'troy'

import sys
import csv
import pickle


class Attribute:
    attribute_id = -1
    name = ''
    entity_type = -1
    backend_type = ''
    frontend_type = ''

    def __init__(self, values):
        self.attribute_id = int(values[0])
        self.name = values[2]
        self.entity_type = int(values[1])
        self.backend_type = values[5]
        self.frontend_type = values[8]

    @staticmethod
    def read_attribute_list(filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            reader.next()   # skip header row
            return [Attribute(row) for row in reader]

    @staticmethod
    def useful_attributes(filename):
        with open(filename, 'r') as r:
            lines = r.readlines()
            return dict((int(line[:-1].split(',')[0]), line[:-1].split(',')[1]) for line in lines)


class ValueRow:
    value_id = -1
    entity_type_id = -1
    attribute_id = -1
    entity_id = -1
    value = ""
    store_id = -1

    def __init__(self, values):
        if len(values) == 6:
            self.value_id = int(values[0])
            self.entity_type_id = int(values[1])
            self.attribute_id = int(values[2])
            self.store_id = int(values[3])
            self.entity_id = int(values[4])
            if not values[5] == 'NULL':
                self.value = values[5].replace('\r\n', ' ')
                self.value = self.value.replace('\n', ' ')
                self.value = self.value.replace(',', ' ')
            else:
                self.value = ''
        else:
            print len(values)
            print values
            sys.exit(0)

    @staticmethod
    def read_value_table(filename):
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            reader.next()   # skip header row
            return [ValueRow(row) for row in reader]


class Shoe:
    id = -1
    attributes = {}

    def __init__(self, num):
        self.id = num
        self.attributes = {}


def processing():
    #attribute_list = Attribute.read_attribute_list('eav_attribute.csv')
    attributes = Attribute.useful_attributes('useful_attributes.txt')

    value_rows = ValueRow.read_value_table('catalog_product_entity_decimal.csv') \
        + ValueRow.read_value_table('catalog_product_entity_int.csv') \
        + ValueRow.read_value_table('catalog_product_entity_text.csv') \
        + ValueRow.read_value_table('catalog_product_entity_varchar.csv')
    all_shoes = {}
    for row in value_rows:
        if not row.entity_type_id == 4 or not row.store_id == 0 or not row.attribute_id in attributes:
            continue
        shoe = all_shoes.get(row.entity_id, Shoe(row.entity_id))
        shoe.attributes[row.attribute_id] = row.value
        all_shoes[shoe.id] = shoe
    #shoe_attribute_list = filter(lambda attribute: attribute.entity_type == 4, attribute_list)
    filtered_shoes = filter(lambda shoe: 85 in shoe.attributes and shoe.attributes[85] != 'no_selection' and
                                         shoe.attributes[85] != '', all_shoes.values())
    filtered_shoes = filter(lambda shoe: 71 in shoe.attributes and shoe.attributes[71] != '', filtered_shoes)
    filtered_shoes = filtered_shoes[1:]
    #output_value(filtered_shoes, attributes, 'all.csv')
    #serialization(filtered_shoes, attributes, 'shoes.p', 'attributes.p')


def serialization(shoes, attributes, shoe_file, attri_file):
    pickle.dump(shoes, open(shoe_file, 'wb'))
    pickle.dump(attributes, open(attri_file, 'wb'))


def deserialization(shoe_file, attri_file):
    return pickle.load(open(shoe_file, 'rb')), pickle.load(open(attri_file, 'rb'))


def output_value(all_shoes, attributes, filename):
    w = open(filename, 'w')
    for attribute in attributes.keys():
        w.write(attributes[attribute] + ',')
    w.write('last\n')
    for shoe in all_shoes:
        for attribute in attributes.keys():
            w.write(shoe.attributes.get(attribute, '') + ',')
        w.write('last\n')
    w.close()


if __name__ == '__main__':
    #processing()
    #shoes, attributes = deserialization('shoes.p', 'attributes.p')
    #output_value(shoes, attributes, 'test.csv')

















