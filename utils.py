from datetime import datetime

def log_start():
    print("="*60)
    print("Luxury Housing Sales Analysis")
    print(f" Analysis started at: {datetime.now()}")
    print("="*60)

def log_end():
    print("="*60)
    print(f" Analysis ended at: {datetime.now()}")
    print("="*60)