from os import system, path

def is_valid_api_key(key):
    """
    Validate if the provided key is a plausible API key.
    This checks for common patterns like length, alphanumeric characters, and special symbols.
    """
    if not key:
        return False

    if len(key) < 20:
        return False

    if not re.search(r"[A-Za-z]", key):
        return False
    if not re.search(r"[0-9]", key):  
        return False
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", key): 
        return False
    return True

def setup_rc(aapik):
    try:
        if system("zsh --version > /dev/null 2>&1") == 0:
            rc_path = path.expanduser("~/.zshrc")
        elif system("bash --version > /dev/null 2>&1") == 0:
            rc_path = path.expanduser("~/.bashrc")
        else:
            print("Unsupported shell environment.")
            return 2

        with open(rc_path, "r") as rc_file:
            rc_content = rc_file.read()

        api_key_exists = any(
            line.strip().startswith("export ANTHROPIC_API_KEY=")
            for line in rc_content.splitlines()
        )

        if not api_key_exists:
            with open(rc_path, "a") as rc_file:
                rc_file.write(f"\nexport ANTHROPIC_API_KEY={aapik}\n")
            return 0
        else:
            print("API key already exists in the configuration file.")
            return 1

    except Exception as e:
        raise RuntimeError(f"Unexpected exception: {e}")

if __name__ == "__main__":
    print("Hello There!, this tool Sets/Updates ANTHROPIC API Key in ANTHROPIC_API_KEY system variable so you can use our computer agent.")
    API = input("Enter your ANTHROPIC API Key: ")
    valid = is_valid_api_key(API)
    if valid:
        env = setup_rc(API)
        if env == 1:
            exit(0)
        print(f"\nUpdated your env variables.")
        print("\nAPI Key is ready to use!")
    else:
        print(f"The API Key ({API}) you have entered is not a valid Anthropic API Key.")
        exit(1)