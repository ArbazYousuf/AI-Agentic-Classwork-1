from utils.logger import logger

def nameCheck(name):
    if name == "":
        print("Invalid name")
        logger.warning("Invalid name entered")
        return False
    return True

def validation(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        logger.warning(f"Invalid marks entered: {marks}")
        return False
    return True
