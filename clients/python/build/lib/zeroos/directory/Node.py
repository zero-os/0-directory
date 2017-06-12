"""
Auto-generated class for Node
"""

from . import client_support


class Node(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(description, nr_cu, nr_su, nr_tu, remarks, uid):
        """
        :type description: str
        :type nr_cu: int
        :type nr_su: int
        :type nr_tu: int
        :type remarks: str
        :type uid: str
        :rtype: Node
        """

        return Node(
            description=description,
            nr_cu=nr_cu,
            nr_su=nr_su,
            nr_tu=nr_tu,
            remarks=remarks,
            uid=uid,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Node'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'description'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.description = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'nr_cu'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.nr_cu = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'nr_su'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.nr_su = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'nr_tu'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.nr_tu = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'remarks'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.remarks = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'uid'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.uid = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
