print(f"multip name {__name__}")

from multiprocessing import Manager
_manager = None
def get_manager():
    global _manager
    if _manager is None:
        raise RuntimeError("manager nao inicializado")
    print("pegou o manager de boa")
    return _manager

def init_manager():
    global _manager
    if _manager is None:
        print("manager inicializado")
        _manager = Manager()