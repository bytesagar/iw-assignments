def dic_update(*dicts):
    result = dict()

    for dic in dicts:
        result.update(dic)
    return result
