import glob
import io
import os
import random
import re

import allure

from projekt_tests.data.entities import Antrag
from projekt_tests.utils import path_dir
from resources import xml_pattern


def get_last():
    files = glob.iglob(os.path.join(path_dir.download(), '*'))
    last_downloaded_file = max(files, key=os.path.getmtime)
    print(f'last_downloaded_file:  {last_downloaded_file}')
    return last_downloaded_file


def create_tar_file(dir, name):
    # return os.path.join(dir, f'{name}.tar')
    return os.path.join(dir, f'{name}')


def get_name(file_path: str):
    return os.path.basename(file_path)[:-4]


def create_output_dir(bv_number, processing_time): # TODO subrepo
    output_dir = os.path.join(path_dir.output(),
                              f'bvCli_{bv_number}_{processing_time.strftime("%Y%m%d%H%M%S")}.{random.randint(111111, 999999)}')
    os.makedirs(output_dir)
    print(f'\n\n- Create output_dir :    {output_dir}')
    return output_dir


def create_antrag_xml(file_name, antrag: Antrag): # TODO subrepo
    with allure.step(f' Create antrag.xml {file_name}  antrag {antrag} '):
        print(f'- Create antrag :    {antrag}')
        antrag_xml = path_dir.testdata('EBEF', file_name)
        text_antrag = xml_pattern.create_text(antrag)

    # print(f'\n    ***  Check antrag is ASCII')
    # assert text_antrag.isascii(), 'Error Antrag is not ASCII'

    with io.open(antrag_xml, 'a', encoding='utf8') as f:
        f.write(text_antrag)
    print(f'- Antrag.xml created successfully :    {antrag_xml}')

    return antrag_xml


def clear_folder(folder_path):
    # Check if the folder exists
    with allure.step(f' Create folder {folder_path}  '):
        if not os.path.exists(folder_path):
            print(f"Folder {folder_path} does not exist.")
            return

        files = os.listdir(folder_path)

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path) and file_name != "__init__.py":
                    os.remove(file_path)
                    print(f"File {file_path} removed successfully.")
                elif os.path.isdir(file_path) and file_name.startswith("bvCli"):
                    shutil.rmtree(file_path)
                    print(f"Directory {file_path} removed successfully.")
            except Exception as e:
                print(f"Error while removing file {file_path}: {e}")


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


import shutil


def copy_file(source_path, destination_path):
    with allure.step(f' Copy file source_path  {source_path}  destination_path  {destination_path} '):
        try:
            # Copy the file from source_path to destination_path
            shutil.copy2(source_path, destination_path)
            print(f"File copied from {source_path} to {destination_path} successfully.")
        except FileNotFoundError:
            print(f"File {source_path} not found.")
        except PermissionError:
            print(f"Permission denied to copy file {source_path}.")
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")


import xml.etree.ElementTree as ET


def update_xml_attr(xml_file_path, attr, value):
    #try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for elem in root.iter("Testcase"):
        elem.set(attr, value)

    tree.write(xml_file_path)
    with allure.step(f"The value of the 'Verfahrensmerkmal' attribute has been successfully set to 'AGBVB_v05' in the file {xml_file_path}."):
        print(
            f"The value of the 'Verfahrensmerkmal' attribute has been successfully set to 'AGBVB_v05' in the file {xml_file_path}.")
    # except Exception as e:
    #     with allure.step(f"An error occurred while updating the XML file: {e}"):
    #         print(f"An error occurred while updating the XML file: {e}")


# def replace_attribute(xml_file_path, attribute, value):
#     # Convert the XML string to an ElementTree object
#     tree = ET.parse(xml_file_path)
#     root = tree.getroot()
#
#     # Find all elements <DBMI></DBMI>
#     dbmi_elements = root.findall((".//DSBE/DBMI[@KE='RONG']"))
#
#     # Replace each element
#     for dbmi_element in dbmi_elements:
#         dbmi_element.attrib = {attribute: value}
#         dbmi_element.text = None  # Clear the element's text
#
#     tree.write(xml_file_path)


# !!!!!!!!!
def add_DBMI_element(xml_file_path, tag, attribute, value):
    # Convert the XML string to an ElementTree object
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Create a new DBMI element with the specified attributes
    # DBMI_element = ET.Element("DBMI", attributes)

    # Find the DSBE element where the DBMI should be added
    # DSBE_element = root.find(".//DSBE/DBMI")
    DSBE_element = root.find(f".//{tag}")
    # Append the new DBMI element inside the DSBE element
    # DSBE_element.append(DBMI_element)
    DSBE_element.set(attribute, value)

    # Convert the updated ElementTree back to a string
    tree.write(xml_file_path)


def replace_attribute_dsbe(xml_file_path, attribute, value):
    # Convert the XML string to an ElementTree object
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all elements <DBMI></DBMI>
    dbmi_elements = root.findall((".//DSBE/DBMI[@KE='RONG']"))

    # Replace each element
    for elem in root.iter("DSBE"):
        if elem.get("VF") == "DEUEV":
            elem.set("MNRBV", "9046/0146086/0075")
            elem.attrib.pop("VF")

    # Convert the modified XML back to string
    modified_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")

    tree.write(xml_file_path)


def replace_attribute_verfahren(xml_file_path, value):  # TODO replace_tag_value
    # Convert the XML string to an ElementTree object
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all elements <DBMI></DBMI>

    verfahren_element = root.find('.//Verfahren')
    verfahren_element.text = value
    tree.write(xml_file_path)


def replace_attribute_bnag(xml_file_path, value):  # TODO replace_tag_value
    # Convert the XML string to an ElementTree object
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all elements <DBMI></DBMI>

    verfahren_element = root.find('.//BNAG')
    verfahren_element.text = value
    tree.write(xml_file_path)


def replace_tag_value(xml_file_path, tag, value):
    # Convert the XML string to an ElementTree object
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find all elements <DBMI></DBMI>

    verfahren_element = root.find(f'.//{tag}')
    verfahren_element.text = value
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
    # tree.write(xml_file_path)


def get_files_without_extension(folder_path):
    with allure.step(f'Get rueckmeldungen that the data has been received and from  SV in {folder_path}'):
        files = os.listdir(folder_path)
        files_without_extension = [file for file in files if
                                   os.path.isfile(os.path.join(folder_path, file)) and '.' not in file]

        print("Files without extension:")
        for file in files_without_extension:
            print(file)

        assert files_without_extension, f"no rueckmeldungen files in {folder_path} "
        return files_without_extension

def get_file_path_with_id(folder_path, id):
    with allure.step(f'Get rueckmeldungen file with id {id} in {folder_path}'):
        files = os.listdir(folder_path)
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))
                 and '.' not in file and id in file]
        assert files, f"no rueckmeldungen files in {folder_path} "
        file = os.path.join(folder_path, files[0])
        with allure.step(f' Search file  {file}'):
            print(f' Search file  {file}\n')
        return file


def find_phrase_in_file(file_path, target_phrase, versions=[]):
    with allure.step(f"Find '{target_phrase}' and phrases from 'versions' in file, and check no 'Fehlercode'"):
        with allure.step("Open the file in read mode with UTF-8 encoding"):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                with allure.step(f"File content: {content}"):

                    # Check if target_phrase is in the content
                    with allure.step(f"Check if '{target_phrase}' is in the file content"):
                        assert target_phrase in content, f"The phrase '{target_phrase}' was not found in the file {file_path}."

                    # Check if all phrases from versions are in the content
                    with allure.step(f"Check {versions} in rückmeldung"):
                        missing_phrases = [phrase for phrase in versions if phrase not in content]
                        assert not missing_phrases, f"The following phrases from 'versions' were not found in the file {file_path}: {missing_phrases}"

                    # Check if "Fehlercode" is in the content
                    with allure.step("Check if 'Fehlercode' is in the file content"):
                        assert "Fehlercode" not in content, f"The 'Fehlercode' was found in the file {file_path}."
        return True


def find_no_phrase_in_file(file_path, target_phrase):
    with allure.step(f"Do not find  '{target_phrase}'  in file"):
        with allure.step("Open the file in read mode with UTF-8 encoding"):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                with allure.step(f"File content: {content}"):

                    # Check if target_phrase is in the content
                    with allure.step(f"Check if '{target_phrase}' is in the file content"):
                        assert not target_phrase in content, f"The phrase '{target_phrase}' was not found in the file {file_path}."




def get_character_in_4_ln_66_col(file_path):
    with open(file_path, 'r') as file:
        # Read all lines into a list of strings
        lines = file.readlines()

        # Check if there are enough lines in the file
    if len(lines) >= 4:
        # Check if there are enough characters in the fourth line
        if len(lines[3]) >= 66:
            # Check if the character at position 66 in the fourth line is '3'
            print(f" lines[4][66]  = {lines[3][65]}")
            return lines[3][65]
        else:
            print("Not enough characters in the fourth line.")
    else:
        print("Not enough lines in the file.")


def get_character_in_4_ln_62_col(file_path):
    with open(file_path, 'r') as file:
        # Read all lines into a list of strings
        lines = file.readlines()

        # Check if there are enough lines in the file
    if len(lines) >= 4:
        # Check if there are enough characters in the fourth line
        if len(lines[3]) >= 62:
            # Check if the character at position 66 in the fourth line is '3'
            print(f" lines[4][62]  = {lines[3][61]}")
            return lines[3][61]
        else:
            print("Not enough characters in the fourth line.")
    else:
        print("Not enough lines in the file.")


def replace_file_content(file_path, old_content, new_content):
    with open(file_path, 'r') as file:
        file_content = file.read()
    file_content = file_content.replace(old_content, new_content, 1)
    with open(file_path, 'w') as file:
        file.write(file_content)


def replace_file_content_index(file_path, old_content, new_content):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Find the index of the second occurrence of old_content
    index = file_content.find(old_content, file_content.find(old_content) + 1)

    # Replace only the second occurrence
    if index != -1:
        file_content = file_content[:index] + new_content + file_content[index + len(old_content):]

    with open(file_path, 'w') as file:
        file.write(file_content)
