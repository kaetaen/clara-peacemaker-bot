import quantumrandom

def get_random_file(content_name: str, items: dict):
    content = items[content_name]
    index = int(quantumrandom.randint(0, 2))
    
    return content[index]
