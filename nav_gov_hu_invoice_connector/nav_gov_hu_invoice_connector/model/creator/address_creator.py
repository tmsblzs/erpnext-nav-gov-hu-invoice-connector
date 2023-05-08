from nav_gov_hu_invoice_connector.nav_gov_hu_invoice_connector.model.address import Address


class AddressCreator:
    @staticmethod
    def create_list_from_taxpayer_data(taxpayer_data):
        result = []
        address_list = taxpayer_data.taxpayerAddressList
        for address in address_list.taxpayerAddressItem:
            result.append(AddressCreator.create_item_from_taxpayer_address_item(address))
        return result

    @staticmethod
    def create_item_from_taxpayer_address_item(address_item):
        address_detail = address_item.taxpayerAddress
        address = Address()
        address.type = address_item.taxpayerAddressType
        address.country_code = address_detail.countryCode
        address.postal_code = address_detail.postalCode
        address.city = address_detail.city.capitalize()
        address.street_name = address_detail.streetName.capitalize()
        address.public_place_category = address_detail.publicPlaceCategory.lower()
        address.number = address_detail.number
        return address
