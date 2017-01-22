import struct

# packed = struct.pack('>2d2i', *(123.456, 987.765, 123, 456))
# for b in packed:
#     print(b)

# unpacked = struct.unpack('2d2i', packed) # 튜플 형식으로 반환
# print (unpacked)

# struct_fmt = '=16s2fi' # char[16], float[2], int
# city_info = [
#     ('서울'.encode(encoding='utf-8'), 37.566535, 126.977969, 9820000),
#     ('뉴욕'.encode(encoding='utf-8'), 40.712784, -74.005941, 8400000),
#     ('파리'.encode(encoding='utf-8'), 48.856614, 2.352222, 2210000),
#     ('런던'.encode(encoding='utf-8'), 51.507351, -0.127758, 8300000)
# ]

# with open('cities.dat', 'wb') as file:
#     for city in city_info:
#         file.write(struct.pack(struct_fmt, *city))

struct_fmt = '16s2fi' # char[16], float[2], int
struct_len = struct.calcsize(struct_fmt)

cities = []
with open('cities.dat', "rb") as file:
    while True:
        buffer = file.read(struct_len)
        if not buffer: break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)
    
    for city in cities:
        name = city[0].decode(encoding='utf-8').replace('\x00', '')
        print('City:{0}, Lat/Long:{1}/{2}, Population:{3}'.format(
            name,
            city[1],
            city[2],
            city[3]
        ))