from dundie.utils.log import get_logger

def load(filepath):
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
           
    except FileNotFoundError as e:
        get_logger.error(str(e)) 
        raise e

