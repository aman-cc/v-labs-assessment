import os
import shutil


def segregate_image_and_text(input_folder: str, output_folder: str) -> None:
    """Method to separate image ad text files in input folder and write to output folder

    Args:
        input_folder (str): Directory where input images and text files are present
        output_folder (str): Directory to write separate image and text files
    """
    output_image_dir = os.path.join(output_folder, "image_files")
    output_text_dir = os.path.join(output_folder, "text_files")

    # Iterate through the input directory
    for (root, dirs, files) in os.walk(input_folder, topdown=True):
        for file in files:
            file_name, ext = os.path.splitext(file)
            file_path = os.path.abspath(os.path.join(root, file))

            # Copy image to output_image_dir
            if ext in [".jpg", ".jpeg", ".png", ".tiff"]:
                shutil.copyfile(file_path, os.path.join(output_image_dir, file))

            # Copy text to output_text_dir
            elif ext == ".txt":
                shutil.copyfile(file_path, os.path.join(output_text_dir, file))


if __name__ == "__main__":
    input_folder_path = "Assignment_1/input_folder/"
    output_folder_path = "Assignment_1/output_folder/"

    # Make output folder if not present
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)
    os.makedirs(os.path.join(output_folder_path, "image_files"), exist_ok=True)
    os.makedirs(os.path.join(output_folder_path, "text_files"), exist_ok=True)

    segregate_image_and_text(input_folder_path, output_folder_path)
