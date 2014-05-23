import operator

class Item:
    sku = None
    attribute_set = None
    category = None
    created_at = None
    updated_at = None
    url_path = None
    weight = None
    ws_location = None
    _media_image = None
    _links_related_sku = None
    _links_upsell_sku = None
    _super_products_sku = None


r = open('2.csv', 'r')
lines = r.readlines()
titles = lines[0].split(',')
vals = [line.split(',') for line in lines[1:]]
cared_key = {"sku":1, "_attribute_set":1, "_category":1, "created_at":1, "updated_at":1, "url_path":1, "weight":1, "ws_location":1, "_links_related_sku":1, "_links_upsell_sku":1, "_media_image":1, "_super_products_sku":1}

for i in range(len(titles)):
    if titles[i] in cared_key:
        cared_key[titles[i]] = i

w = open('clean.csv', 'w')

pairs = cared_key.items()

for pair in pairs[:-1]:
    w.write(pair[0] + ",")
w.write(pairs[-1][0] + "\n")

for val in vals:
    for pair in pairs[:-1]:
        w.write(val[pair[1]] + ",")
    w.write(val[pairs[-1][1]] + "\n")
w.close()


