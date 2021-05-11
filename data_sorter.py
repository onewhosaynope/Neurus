import os

train_dir = "Data/cats_dogs_dataset/train"
valid_dir = "Data/cats_dogs_dataset/valid"


def main(root_dir):
    count = 0
    all_files = os.listdir(root_dir)
    for filename in all_files:
        if filename.endswith(".txt"):
            with open("{}/{}".format(root_dir, filename), "r") as f:
                class_label = f.readline().split()[0]
                if class_label == "1":
                    class_label = "cats"
                elif class_label == "2":
                    class_label = "dogs"
                else:
                    class_label = "other"
                picture_name = filename.replace(".txt", ".jpg")
                try:
                    os.replace("{}/{}".format(root_dir, picture_name),
                               "{}/{}/{}".format(root_dir, class_label, picture_name))
                    count += 1
                except OSError:
                    os.mkdir(root_dir + "/" + class_label)
                    os.replace("{}/{}".format(root_dir, picture_name),
                               "{}/{}/{}".format(root_dir, class_label, picture_name))
                    count += 1
                    f.close()
    print("Moved {} files in folder {}".format(count, root_dir))


if __name__ == "__main__":
    main(train_dir)
    main(valid_dir)
