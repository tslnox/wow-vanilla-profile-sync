import os
import shutil

# Constants for internal exclusions
INTERNAL_EXCLUSIONS = ["TurtleRP.lua", "engbags.lua", "pfQuest.lua", "ModifiedPowerAuras.lua", "Outfitter.lua"]

# Helper function for case-insensitive path matching
def find_case_insensitive_path(base_path, target_name):
    for root, dirs, files in os.walk(base_path):
        for name in dirs + files:
            if name.lower() == target_name.lower():
                return os.path.join(root, name)
    return None

def list_subdirectories(path):
    try:
        return [entry.name for entry in os.scandir(path) if entry.is_dir()]
    except FileNotFoundError:
        return []

def prompt_for_choice(options, prompt_message):
    print(prompt_message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice. Please try again.")

def confirm_directory_is_wow(base_path):
    wow_exe_path = find_case_insensitive_path(base_path, "Wow.exe")
    if wow_exe_path:
        print(f"Detected World of Warcraft executable at: {wow_exe_path}")
        confirmation = input("Is this the correct WoW directory? (yes/no): ").strip().lower()
        return confirmation == "yes"
    return False

def copy_savedvariables(src_character_path, dest_characters, exclusions):
    savedvariables_path = find_case_insensitive_path(src_character_path, "SavedVariables")
    if not savedvariables_path:
        print(f"No 'SavedVariables' folder found for {src_character_path}.")
        return

    for dest_character in dest_characters:
        dest_savedvariables_path = os.path.join(dest_character, "SavedVariables")

        # Ensure the destination SavedVariables folder exists
        os.makedirs(dest_savedvariables_path, exist_ok=True)

        for filename in os.listdir(savedvariables_path):
            if filename.endswith(".lua") and not filename.endswith(".lua.bak") and filename not in exclusions:
                src_file = os.path.join(savedvariables_path, filename)
                dest_file = os.path.join(dest_savedvariables_path, filename)
                print(f"Copying {src_file} to {dest_file}")
                shutil.copy2(src_file, dest_file)

def main():
    base_path = os.getcwd()

    if not confirm_directory_is_wow(base_path):
        print("This does not appear to be a valid World of Warcraft directory.")
        return

    wtf_path = find_case_insensitive_path(base_path, "WTF")
    if not wtf_path:
        print("WTF directory not found. Make sure you are in the WoW parent directory.")
        return

    accounts_path = os.path.join(wtf_path, "Account")
    accounts = list_subdirectories(accounts_path)

    if not accounts:
        print("No accounts found in WTF/Account directory.")
        return

    selected_account = prompt_for_choice(accounts, "Select an account:")
    account_path = os.path.join(accounts_path, selected_account)

    realms = [realm for realm in os.listdir(account_path) \
              if os.path.isdir(os.path.join(account_path, realm)) and realm.lower() != "savedvariables"]
    if not realms:
        print("No realms found in the selected account.")
        return

    selected_realm = prompt_for_choice(realms, "Select a realm:")
    realm_path = os.path.join(account_path, selected_realm)

    characters = list_subdirectories(realm_path)
    if not characters:
        print("No characters found in the selected realm.")
        return

    source_character = prompt_for_choice(characters, "Select the source character to copy from:")
    src_character_path = os.path.join(realm_path, source_character)

    dest_characters = [os.path.join(realm_path, char) for char in characters if char != source_character]

    exclusions = INTERNAL_EXCLUSIONS[:]
    additional_exclusions = input("Enter additional exclusions (comma-separated), or press Enter to skip: ").split(",")
    exclusions.extend([item.strip() for item in additional_exclusions if item.strip()])

    copy_savedvariables(src_character_path, dest_characters, exclusions)

if __name__ == "__main__":
    main()

