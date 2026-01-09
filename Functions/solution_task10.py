# 🔥 Debugging
# Fix it
# def clean(data):
#     for x in data:
#         if x < 0:
#             data.remove(x)
#     return data

def clean(data):
    valid_data = []

    for x in data:
        if x > 0:
            valid_data.append(x)
    return valid_data
