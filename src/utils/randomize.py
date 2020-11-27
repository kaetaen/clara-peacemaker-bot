import quantumrandom

def get_random_file(content_name: str, items: dict) -> str:
    content: list = items[content_name]
    index = int(quantumrandom.randint(0, len(content) - 1))
    
    return content[index]
