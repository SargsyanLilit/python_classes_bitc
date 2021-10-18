class WebStore(object):
    addresses_dict = {}

    def __init__(self, address):
        self.address = address
        if self.address not in WebStore.addresses_dict:
            WebStore.addresses_dict[self.address] = 0
        WebStore.addresses_dict[self.address] += 1

    @classmethod
    def get_address_number(cls):
        return len(WebStore.addresses_dict)

    @classmethod
    def get_order_number(cls, address):
        return f"There were {WebStore.addresses_dict[address]} orders from {address}."

    @classmethod
    def top_addresses(cls, top_number):
        sorted_dict_values_list = sorted(WebStore.addresses_dict.values(), reverse=True)
        top_addresses = []
        for i in range(top_number):
            for key in WebStore.addresses_dict:
                if WebStore.addresses_dict[key] == sorted_dict_values_list[i] and key not in top_addresses:
                    top_addresses.append(key)
        return top_addresses
