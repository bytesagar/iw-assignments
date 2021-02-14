def add_tags(tag, textContent):
    element = "<{tag}>{content}</{tag}>".format(tag=tag, content=textContent)
    return element

print(add_tags("i", "sagar"))