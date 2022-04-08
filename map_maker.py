from PIL import Image

WIDTH = 8
HEIGHT = 8


def concat_images_h(images: list, rowno=None, width=7000, height=1000):
    new_img = Image.new('RGB', (width, height))
    x_offset = 0
    for img in images:
        new_img.paste(img, (x_offset, 0))
        x_offset += img.size[0]

    if rowno is not None:
        outputfp = 'map2/created/row{}.png'.format(rowno)
        new_img.save(outputfp)
        print('Concatanated horizonataly: {}'.format(outputfp))
    return new_img


def concat_images_v(images: list, width=7000, height=7000):
    new_img = Image.new('RGB', (width, height))
    y_offset = 0
    for img in images:
        new_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

    return new_img


if __name__ == '__main__':
    images = []
    for n in range(1, 8):
        filepath = 'map2/1_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    firstrow = concat_images_h(images, 1)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/2_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    secondrow = concat_images_h(images, 2)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/3_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    thirdrow = concat_images_h(images, 3)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/4_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    fourthrow = concat_images_h(images, 4)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/5_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    fifthrow = concat_images_h(images, 5)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/6_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    sixthrow = concat_images_h(images, 6)

    images.clear()
    for n in range(1, 8):
        filepath = 'map2/7_{n}.png'.format(n=n)
        images.append(Image.open(filepath).resize((1000, 1000)))

    seventhrow = concat_images_h(images, 7)

    always_map_list = []
    for n in range(1, 8):
        filepath = 'map2/created/row{n}.png'.format(n=n)
        always_map_list.append(Image.open(filepath))

    am = concat_images_v(always_map_list)
    outputfp = 'map2/created/always_map.png'
    am.save(outputfp)
    print('Map 7000x7000 created (without edges): {}'.format(outputfp))

# 700 x 1000
    right_edge = []
    for n in range(1, 9):
        filepath = 'map2/{n}_8.png'.format(n=n)
        right_edge.append(Image.open(filepath).resize((700, 1000)))

    re = concat_images_v(right_edge, width=700, height=7700)
    outputfp = 'map2/created/right_edge.png'
    re.save(outputfp)
    print('Right edge created: {}'.format(outputfp))

# 1000 x 700
    bottom_edge = []
    for n in range(1, 9):
        filepath = 'map2/8_{n}.png'.format(n=n)
        bottom_edge.append(Image.open(filepath).resize((1000, 700)))

    be = concat_images_h(bottom_edge, width=7700, height=700)
    outputfp = 'map2/created/bottom_edge.png'
    be.save(outputfp)
    print('Bottom edge created: {}'.format(outputfp))

# Glue always map with right and bottom edge
    map = Image.new('RGB', (7700, 7700))
    map.paste(am, (0, 0))
    map.paste(re, (7000, 0))
    map.paste(be, (0, 7000))
    outputfp = 'map2/created/map.png'
    map.save(outputfp)
    print('Map created: {}'.format(outputfp))
