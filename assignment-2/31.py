def dict_iterator(dict):
    for k,v in dict.items():
        print(str(k)+ ":" + str(v))

sample_dict = {"name":"sagar"}

dict_iterator(sample_dict)