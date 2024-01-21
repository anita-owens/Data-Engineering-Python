json_data = {'results': [
        {'id': 987, 'departmentId': '123abc', 'managerId': '1a2b', 'contributionIds': [
                1,
                2
            ], 'status': 'ACTIVE',  'country': 'SE', 'replaces': 18,  'price': 'v3', 'validFrom': '2022-11-01', 'validTo': '2023-01-01', 'createdAt': '2022-10-25T13: 02: 38.542Z',  'owner': None
        },
        {'id': 21, 'departmentId': '456def', 'managerId': '3c4d', 'contributionIds': [
                1
            ], 'status': 'ACTIVE',  'country': None, 'replaces': None,  'price': 'v2', 'validFrom': '2022-07-01', 'validTo': '2023-01-01', 'createdAt': '2022-03-26T07: 16: 25.703Z',  'owner': None
        },
        {'id': 123, 'departmentId': '789ghi', 'managerId': '5d6e', 'contributionIds': [
                1,
                2
            ], 'status': 'INVALID', 'country': 'DK', 'replaces': None, 'price': 'v2', 'validFrom': '2022-08-01', 'validTo': '2023-01-01', 'createdAt': '2022-07-02T10: 01: 29.297Z',  'owner': None
        }
    ], 'limit': 3, 'currentPage': 1, 'total': 400, 'totalPages': 150
}


def flatten_json(json_data):
    flattened_list = []
    for result in json_data['results']:
        flat_dict = {
            'row_id': result['id'],
            'department_id': result['departmentId'],
            'manager_id': result['managerId'],
            'status': result['status'],
            'country': result['country'],
            'replaces': result['replaces'],
            'price': result['price'],
            'valid_from': result['validFrom'],
            'valid_to': result['validTo'],
            'created_at': result['createdAt'],
            'owner': result['owner']
            }
        for contribution_id in result['contributionIds']:
            flat_dict['contribution_id'] = contribution_id
            flattened_list.append(flat_dict.copy())
    return flattened_list

data_to_insert = flatten_json(json_data)
data_to_insert


## METHOD 2: If there is a key error use the get method.
def flatten_json(json_data):
    flattened_list = []
    for result in json_data['results']:
        flat_dict = {
            'id': result.get('id'),
            'departmentId': result.get('departmentId'),
            'managerId': result.get('managerId'),
            'contributionId': None,
            'status': result.get('status'),
            'country': result.get('country'),
            'replaces': result.get('replaces'),
            'price': result.get('price'),
            'validFrom': result.get('validFrom'),
            'validTo': result.get('validTo'),
            'createdAt': result.get('createdAt'),
            'owner': result.get('owner')
        }
        for contribution_id in result['contributionIds']:
            flat_dict['contributionId'] = contribution_id
            flattened_list.append(flat_dict.copy())
    return flattened_list

data_to_insert = flatten_json(json_data)
data_to_insert