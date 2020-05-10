import os


def create_txt(root):
    folders = os.listdir(root)
    for folder in folders:
        if folder.endswith('.DS_Store'):
            continue
        image_path = root + folder + '/images/'
        images = os.listdir(image_path)

        with open(root[:-1] + '_' + folder + '.txt', 'w') as f:
            for image in images:
                if image.endswith('.DS_Store'):
                    continue
                f.write(image_path + image + '\n')


def creat_txt_lr_sr(root, folder):
    image_path = root + 'images/'
    images = os.listdir(image_path)

    with open(root + folder + '.txt', 'w') as f:
        for image in images:
            if image.endswith('.DS_Store'):
                continue
            f.write(image_path + image + '\n')


if __name__ == '__main__':
    # create_txt('data/insulator/augmented/')
    # create_txt('data/insulator/original/')

    creat_txt_lr_sr('data/insulator-lr/', 'lr')
    creat_txt_lr_sr('data/insulator-sr/', 'sr')
    creat_txt_lr_sr('data/insulator-hr/', 'hr')
